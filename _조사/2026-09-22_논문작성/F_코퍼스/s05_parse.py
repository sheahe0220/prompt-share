"""
Why: turn four publisher formats (Copernicus JATS XML, Wiley HTML, ScienceDirect HTML,
     IWA/Silverchair HTML) into one JSON schema so style metrics are computed identically.
Rerun: C:\\Users\\SGJEONG99\\anaconda3\\envs\\pyswmm\\python.exe -X utf8 s05_parse.py
Input : raw/*, corpus_list.csv      Output: parsed/<file>.json
Schema: title, abstract, sections[{level, heading, text}], back[{heading, text}],
        figures[caption], tables[{caption, cells, n_bold}], refs[{text, year}]
"""
import os, re, json, csv
import lxml.html, lxml.etree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw"); OUT = os.path.join(HERE, "parsed")
os.makedirs(OUT, exist_ok=True)
LIST = os.path.join(HERE, "corpus_list.csv")
HTMLP = lxml.html.HTMLParser(encoding="utf-8")  # browser-saved pages are UTF-8

BACK_PAT = re.compile(r"acknowledg|conflict|competing|declaration|credit author|author contribution|"
                      r"data availab|code availab|code and data|data and code|funding|financial support|"
                      r"review statement|supporting information|supplement|nomenclature|list of acronyms|"
                      r"statements and declarations|appendix|open research|abbreviation", re.I)


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()


def ref_year(txt, pubyear):
    for m in re.finditer(r"(?<![\d./-])(19[0-9]{2}|20[0-3][0-9])[a-z]?(?![\d])", txt):
        y = int(m.group(1))
        if 1900 <= y <= pubyear + 1:
            return y
    return None


def walk(container, heads, paras):
    """Collect sections in document order. heads: dict element->level; paras: set of elements."""
    secs = []
    cur = {"level": 0, "heading": "(pre)", "text": ""}
    for el in container.iter():
        if el in heads:
            secs.append(cur)
            cur = {"level": heads[el], "heading": norm(el.text_content() if hasattr(el, "text_content") else "".join(el.itertext())), "text": ""}
        elif el in paras:
            t = el.text_content() if hasattr(el, "text_content") else "".join(el.itertext())
            cur["text"] += " " + norm(t)
    secs.append(cur)
    return [s for s in secs if s["heading"] != "(pre)" or s["text"].strip()]


def split_back(secs):
    main, back = [], []
    in_back = False
    for s in secs:
        if s["level"] <= 1 and BACK_PAT.search(s["heading"]):
            in_back = True
        elif s["level"] <= 1:
            in_back = False
        (back if in_back else main).append(s)
    return main, back


def parse_jats(fp, year):
    x = ET.parse(fp)
    title = norm("".join(x.find(".//article-title").itertext()))
    ab = x.find(".//abstract")
    abstract = norm(" ".join("".join(p.itertext()) for p in ab.iter("p"))) if ab is not None else ""
    body = x.find(".//body")
    heads = {}
    for t in body.iter("title"):
        par = t.getparent()
        if par.tag == "sec":
            heads[t] = len([a for a in par.iterancestors("sec")]) + 1
    paras = set(p for p in body.iter("p") if not any(a.tag in ("caption", "table-wrap", "fig") for a in p.iterancestors()))
    secs = walk(body, heads, paras)
    back = []
    for n in x.find(".//back") if x.find(".//back") is not None else []:
        if n.tag in ("notes", "ack", "sec"):
            back.append({"level": 1, "heading": norm(n.findtext("title") or n.get("notes-type") or n.tag),
                         "text": norm(" ".join("".join(p.itertext()) for p in n.iter("p")))})
    # sections that look like back matter inside body
    secs, extra = split_back(secs); back += extra
    figs = [norm("".join(f.find("caption").itertext())) for f in body.iter("fig") if f.find("caption") is not None]
    tabs = []
    for tw in x.iter("table-wrap"):
        cap = norm("".join(tw.find("caption").itertext())) if tw.find("caption") is not None else ""
        cells = [norm("".join(e.itertext())) for e in tw.iter() if isinstance(e.tag, str) and e.tag.endswith("entry")]
        nb = sum(1 for e in tw.iter("bold") if not any(isinstance(a.tag, str) and a.tag.endswith("thead") for a in e.iterancestors()))
        tabs.append({"caption": cap, "cells": cells, "n_bold": nb})
    refs = []
    for r in x.iter("ref"):
        txt = norm("".join(r.itertext()))
        y = r.findtext(".//year")
        yy = int(re.match(r"\d{4}", y).group()) if y and re.match(r"\d{4}", y) else ref_year(txt, year)
        refs.append({"text": txt[:300], "year": yy})
    return dict(title=title, abstract=abstract, sections=secs, back=back, figures=figs, tables=tabs, refs=refs)


def html_cells(tab):
    cells = [norm(td.text_content()) for td in tab.xpath(".//td|.//th")]
    nb = len(tab.xpath(".//tbody//*[self::b or self::strong or contains(@class,'bold')]"))
    return cells, nb


def parse_wiley(fp, year):
    t = lxml.html.parse(fp, parser=HTMLP).getroot()
    title = norm(t.xpath('//h1[contains(@class,"citation__title")]')[0].text_content())
    ab = t.xpath('//section[contains(@class,"article-section__abstract")][.//h2[contains(@class,"main")]]')
    abstract = norm(" ".join(p.text_content() for p in ab[0].xpath('.//p'))) if ab else ""
    body = t.xpath('//div[contains(@class,"article__body")]')[0]
    heads = {h: 1 for h in body.xpath('.//h2[contains(@class,"article-section__title")]')}
    heads.update({h: 2 for h in body.xpath('.//h3[contains(@class,"section2")]')})
    heads.update({h: 3 for h in body.xpath('.//h4[contains(@class,"section3")]|.//h3[contains(@class,"section3")]')})
    paras = set(body.xpath('.//section[contains(@class,"article-section__full")]//p[not(ancestor::figure) and not(ancestor::div[contains(@class,"article-table-content")]) and not(ancestor::section[contains(@class,"article-section__abstract")])]'))
    secs = walk(body, heads, paras)
    secs, back = split_back(secs)
    figs = [norm(c.text_content()) for c in body.xpath('.//figure[contains(@class,"figure")]//div[contains(@class,"figure__caption-text")]')]
    tabs = []
    for tw in body.xpath('.//div[contains(@class,"article-table-content") and not(contains(@class,"wrapper"))]'):
        cap = tw.xpath('.//header[contains(@class,"article-table-caption")]')
        tb = tw.xpath('.//table')
        cells, nb = html_cells(tb[0]) if tb else ([], 0)
        tabs.append({"caption": norm(cap[0].text_content()) if cap else "", "cells": cells, "n_bold": nb})
    refs = [{"text": norm(li.text_content())[:300], "year": ref_year(norm(li.text_content()), year)}
            for li in t.xpath('//section[@id="references-section"]//ul/li|//div[contains(@class,"article-section__references")]//ul/li')]
    if not refs:
        refs = [{"text": norm(li.text_content())[:300], "year": ref_year(norm(li.text_content()), year)}
                for li in t.xpath('//ul[contains(@class,"rlist separator")]/li')]
    return dict(title=title, abstract=abstract, sections=secs, back=back, figures=figs, tables=tabs, refs=refs)


def parse_sd(fp, year):
    t = lxml.html.parse(fp, parser=HTMLP).getroot()
    title = norm(t.xpath('//span[contains(@class,"title-text")]')[0].text_content())
    ab = t.xpath('//div[contains(@class,"abstract author") and not(contains(@class,"highlights"))][./h2[normalize-space()="Abstract"]]')
    abstract = norm(" ".join(p.text_content() for p in ab[0].xpath('.//div[contains(@class,"u-margin-s-bottom")]|.//p'))) if ab else ""
    if ab and not abstract:
        abstract = norm(ab[0].text_content()).removeprefix("Abstract").strip()
    body = t.xpath('//div[@id="body"]')[0]
    heads = {}
    for h in body.xpath('.//h2|.//h3|.//h4'):
        heads[h] = {"h2": 1, "h3": 2, "h4": 3}[h.tag]
    paras = set(body.xpath('.//div[contains(@class,"u-margin-s-bottom")][not(ancestor::figure) and not(ancestor::div[contains(@class,"tables")]) and not(ancestor::div[contains(@class,"u-margin-s-bottom")])]|.//p[not(ancestor::figure) and not(ancestor::div[contains(@class,"tables")]) and not(ancestor::div[contains(@class,"u-margin-s-bottom")])]'))
    secs = walk(body, heads, paras)
    secs, back = split_back(secs)
    # back matter outside #body (CRediT, declarations, data availability)
    for s in t.xpath('//section[.//h2][not(ancestor::div[@id="body"])][contains(@id,"sec") or contains(@id,"ack") or contains(@id,"coi") or contains(@id,"da")]'):
        h = s.xpath('.//h2')[0]
        if BACK_PAT.search(h.text_content()):
            back.append({"level": 1, "heading": norm(h.text_content()), "text": norm(s.text_content())[:3000]})
    figs = []
    for f in body.xpath('.//figure'):
        cap = f.xpath('.//span[contains(@class,"captions")]')
        c = norm(cap[0].text_content()) if cap else ""
        if c and c not in figs:
            figs.append(c)
    tabs = []
    for tw in body.xpath('.//div[contains(@class,"tables")]'):
        cap = tw.xpath('.//span[contains(@class,"captions")]')
        tb = tw.xpath('.//table')
        cells, nb = html_cells(tb[0]) if tb else ([], 0)
        tabs.append({"caption": norm(cap[0].text_content()) if cap else "", "cells": cells, "n_bold": nb})
    refs = [{"text": norm(r.text_content())[:300], "year": ref_year(norm(r.text_content()), year)}
            for r in t.xpath('//ol[contains(@class,"references")]/li')]
    return dict(title=title, abstract=abstract, sections=secs, back=back, figures=figs, tables=tabs, refs=refs)


def parse_iwa(fp, year):
    t = lxml.html.parse(fp, parser=HTMLP).getroot()
    title = re.sub(r"\s*Open Access\s*$", "", norm(t.xpath('//h1[contains(@class,"article-title-main")]|//h1')[0].text_content()))
    ab = t.xpath('//section[contains(@class,"abstract")]')
    abstract = norm(" ".join(p.text_content() for p in ab[0].xpath('.//p'))) if ab else ""
    cont = t.xpath('//div[contains(@class,"widget-ArticleFulltext")]')
    cont = cont[0] if cont else t
    heads = {}
    for h in cont.xpath('.//h2[contains(@class,"section-title") or contains(@class,"backsection-title") or contains(@class,"backacknowledgements-title") or contains(@class,"backreferences-title")]'):
        heads[h] = 1
    for h in cont.xpath('.//h3[contains(@class,"section-title")]'):
        heads[h] = 2
    for h in cont.xpath('.//h4[contains(@class,"section-title")]'):
        heads[h] = 3
    paras = set(cont.xpath('.//p[contains(@class,"chapter-para")][not(ancestor::div[contains(@class,"fig")]) and not(ancestor::div[contains(@class,"table-wrap")]) and not(ancestor::section[contains(@class,"abstract")])]'))
    if not paras:
        paras = set(cont.xpath('.//p[not(ancestor::div[contains(@class,"fig")]) and not(ancestor::div[contains(@class,"table")]) and not(ancestor::section[contains(@class,"abstract")])]'))
    secs = walk(cont, heads, paras)
    secs = [s for s in secs if not re.match(r"references", s["heading"], re.I)]
    secs, back = split_back(secs)
    figs, seen = [], set()
    for f in cont.xpath('.//div[contains(@class,"fig-section")]'):
        did = f.get("data-id")
        cap = f.xpath('.//div[contains(@class,"fig-caption")]')
        c = norm(cap[0].text_content()) if cap else ""
        if did in seen or not c:
            continue
        seen.add(did); figs.append(c)
    tabs, seen = [], set()
    for tw in cont.xpath('.//div[contains(@class,"table-wrap ")][not(ancestor::div[contains(@class,"table-modal")])]'):
        cap = tw.xpath('.//div[contains(@class,"caption")]')
        c = norm(cap[0].text_content()) if cap else ""
        if c in seen:
            continue
        seen.add(c)
        tb = tw.xpath('.//table')
        cells, nb = html_cells(tb[0]) if tb else ([], 0)
        tabs.append({"caption": c, "cells": cells, "n_bold": nb})
    refs = [{"text": norm(r.text_content())[:300], "year": ref_year(norm(r.text_content()), year)}
            for r in cont.xpath('.//div[contains(@class,"citation mixed-citation")]')]
    return dict(title=title, abstract=abstract, sections=secs, back=back, figures=figs, tables=tabs, refs=refs)


rows = list(csv.DictReader(open(LIST, encoding="utf-8")))
assert rows
n_ok = 0
for r in rows:
    fn, year = r["file"], int(r["year"])
    fp = os.path.join(RAW, fn)
    if fn.endswith(".xml"):
        d = parse_jats(fp, year)
    elif fn.startswith(("wrr", "hyp")):
        d = parse_wiley(fp, year)
    elif fn.startswith("jhi"):
        d = parse_iwa(fp, year)
    else:
        d = parse_sd(fp, year)
    d.update(doi=r["doi"], journal=r["journal"].replace("&amp;", "&"), year=year, group=r["group"], file=fn)
    words = sum(len(s["text"].split()) for s in d["sections"])
    print(f"{fn:26s} abs={len(d['abstract'].split()):4d} secs={len(d['sections']):3d} words={words:6d} "
          f"back={len(d['back']):2d} figs={len(d['figures']):3d} tabs={len(d['tables']):2d} refs={len(d['refs']):3d} "
          f"refyr_none={sum(1 for x in d['refs'] if x['year'] is None)}")
    json.dump(d, open(os.path.join(OUT, fn + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if words > 2000 and d["abstract"] and d["figures"] and d["refs"]:
        n_ok += 1
print("parsed with full text:", n_ok, "/", len(rows))
assert n_ok >= 15
