"""
Why: compute writing-style metrics (title, abstract moves, headings, voice, figures, captions,
     tables, results sentences, hedging, gap sentences, references) from parsed/*.json so the
     guidance for a SWMM-calibration master's thesis paper is grounded in real Q1 papers.
Rerun: C:\\Users\\SGJEONG99\\anaconda3\\envs\\pyswmm\\python.exe -X utf8 s06_metrics.py
Output: metrics_per_paper.csv, figures_per_caption.csv, tables_per_caption.csv,
        examples.json (real sentences with DOI), summary.json
All classifiers are keyword heuristics; see README notes in the report.
"""
import os, re, json, glob, statistics as st
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
PARSED = os.path.join(HERE, "parsed")
OUT_CSV = os.path.join(HERE, "metrics_per_paper.csv")
OUT_FIG = os.path.join(HERE, "figures_per_caption.csv")
OUT_TAB = os.path.join(HERE, "tables_per_caption.csv")
OUT_EX = os.path.join(HERE, "examples.json")
OUT_SUM = os.path.join(HERE, "summary.json")

ABBR = ["et al.", "e.g.", "i.e.", "Fig.", "Figs.", "Eq.", "Eqs.", "vs.", "cf.", "approx.", "resp.", "Sect.", "No.", "Ref.", "ca."]


def sents(text):
    t = text
    for a in ABBR:
        t = t.replace(a, a.replace(".", "<DOT>"))
    t = re.sub(r"(\d)\.(\d)", r"\1<DOT>\2", t)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(\[])", t)
    return [p.replace("<DOT>", ".").strip() for p in parts if len(p.split()) >= 4]


def wc(t):
    return len(re.findall(r"[A-Za-z][A-Za-z'-]*", t))


def per_k(n, words):
    return round(1000 * n / words, 2) if words else None


def count(pat, text, flags=re.I):
    return len(re.findall(pat, text, flags))


# ---------- heading classification ----------
def head_class(h):
    h0 = re.sub(r"^(\d+(\.\d+)*\.?|[A-Z](\.\d+)*\.)\s+", "", h.strip()).lower().strip()
    if re.search(r"introduc", h0): return "Introduction"
    if re.search(r"results? and discussion|results & discussion|results and discussions", h0): return "Results and Discussion"
    if re.search(r"summary and conclu|conclu|concluding|summary", h0): return "Conclusions"
    if re.search(r"^discussion|discussion", h0): return "Discussion"
    if re.search(r"^results?|results", h0): return "Results"
    if re.search(r"study (area|site)|case stud|data|catchment|site descri|materials", h0) and not re.search(r"method", h0): return "Study area/Data"
    if re.search(r"method|approach|framework|model(l)?ing|design of|theory|background|calibration|setup|set-up|experiment|materials", h0): return "Methods"
    if re.search(r"limitation|outlook|future", h0): return "Limitations/Outlook"
    return "Other"


# ---------- figure classification ----------
FIG_RULES = [
    ("map/site", r"^(\S+\s){0,6}(study area|study site|research area|location|map of the stud|study catchment|overview of the study|site map|study domain)|^(the )?map of (the )?(\d+ )?(selected|studied|study|catchment|basin)"),
    ("spatial map of results", r"spatial (distribution|pattern|variab)|maps? of (the )?(simulated|maximum|flood|inundation|difference|error|change|performance|sensitivity|optimal|estimated)|inundation|flood extent|flooded area|flood depth"),
    ("boxplot/performance comparison", r"taylor diagram|cumulative distribution|cdf|flow duration|model efficiency|difference in (the )?(median )?model efficiency"),
    ("framework/flowchart/schematic", r"flow ?chart|framework|workflow|schematic|scheme|procedure|conceptual|structure of|algorithm|steps of|description of the|diagram|overview of the (proposed|method|approach|model)|pseudocode|pseudo-code|sketch|illustration|depiction|linkage|layers and|implementation|definition of|cross-section|method applied|membership function"),
    ("convergence", r"converge|iteration|iterative|number of (model |expensive )?(objective function )?(evaluations|runs|simulations)|generations|evolution of the (objective|best)|sample sizes?"),
    ("parameter/posterior/sensitivity", r"posterior|prior|sensitivity|sobol|morris|dotty|marginal|identifiab|parameter|first-order|total-order|\(st\)|correlation matrix|importance|histogram|probability distribution"),
    ("scatter obs-vs-sim", r"scatter|observed (vs\.?|versus|against) (simulated|modelled|predicted)|(simulated|modelled|predicted) (vs\.?|versus|against) observed|1\s?:\s?1|one-to-one"),
    ("rainfall/input data", r"idf|intensity[–-]duration|depth[–-]duration|daily precipitation|rainfall (data|series|intensity|input|field|product)|precipitation (data|series|product)|design storm|radar (rainfall|image)"),
    ("hydrograph/time series", r"hydrograph|time series|time-series|hyetograph|(observed|measured) and (simulated|modelled|predicted)|(simulated|modelled) and (observed|measured)|rainfall event|flow at|discharge at|water level|water depth|runoff (volume|response)|storm event|bounds for|prediction bound|confidence interval|temporal evolution"),
    ("boxplot/performance comparison", r"box ?plot|box-and-whisker|performance|nse|kge|rmse|efficiency|pbias|bias|error|comparison|compar|pareto|trade-off|tradeoff|taylor|metric|skill|score|cdf|cumulative (distribution|frequency)|optimi[sz]ation results|optimal (solutions|objectives)|ens|m-nse"),
    ("spatial map of results", r"spatial (distribution|pattern|variab)|maps? of (the )?(simulated|maximum|flood|inundation|difference|error|change|performance|sensitivity|optimal|estimated)|inundation|flood extent|flooded area|flood depth"),
    ("map/site", r"catchment|map|layout|network|land use|land cover|topograph|elevation|gauge|station|drainage system|sewer system|watershed|spatial representation|underlying surface"),
]


def fig_type(cap):
    c = re.sub(r"^(figure|fig\.?)\s*\d+\s*[.:|]?\s*", "", cap, flags=re.I).lower()
    for name, pat in FIG_RULES:
        if re.search(pat, c):
            return name
    return "other"


FINITE = r"\b(is|are|was|were|shows?|showed|indicates?|increases?|decreases?|outperforms?|improves?|reduces?|leads?|results? in|yields?|exhibits?|depends?|has|have|can|differs?|remains?|varies|becomes?)\b"


def cap_first_sentence(cap):
    c = re.sub(r"^(figure|fig\.?|table)\s*[A-Z]?\d+\s*[.:|]?\s*", "", cap, flags=re.I)
    s = sents(c)
    return s[0] if s else c


def cap_style(cap):
    fs = cap_first_sentence(cap)
    return {
        "first_is_finding": bool(re.search(FINITE, fs, re.I)),
        "panels": bool(re.search(r"\(a\)|\(b\)|\ba\)\s|\bpanel|\(left\)|\(right\)|\btop\b|\bbottom\b|upper|lower (panel|row)", cap, re.I)),
        "symbols_colors": bool(re.search(r"\b(red|blue|black|gr[ae]y|green|orange|purple|dashed|dotted|solid|shaded|shading|markers?|circles?|dots?|triangles?|crosses|symbols?|colou?r|legend|line[s]? (represent|indicate|show|denote)|bars? (represent|indicate|show))\b", cap, re.I)),
        "units": bool(re.search(r"(\bmm\b|\bm3|m\^3|m³|\bm s|\bl s|\bL s|\bkm|\bha\b|%|\bh−1|h-1|\bmin\b|\bhours?\b|\bmm h|\bm\)|\(m\b|s−1|s-1|°)", cap)),
        "n_words": wc(cap),
        "n_sentences": len(sents(cap)) or 1,
    }


# ---------- table classification ----------
TAB_RULES = [
    ("performance metrics", r"performance|nse|kge|rmse|efficiency|pbias|error|goodness|metric|statistic|evaluation|validation result|calibration result|skill"),
    ("model parameters/ranges", r"parameter|range|prior|bound|value used|calibrated value|optimal value"),
    ("event characteristics", r"event|storm|rainfall|precipitation|hyetograph"),
    ("method comparison", r"comparison|compar|algorithm|method|approach|strateg|scenario|configuration|setting"),
    ("study site/data characteristics", r"characteristic|catchment|site|data|station|gauge|land|area|properties|description|summary of"),
]


def tab_type(cap):
    c = cap.lower()
    for name, pat in TAB_RULES:
        if re.search(pat, c):
            return name
    return "other"


# ---------- title ----------
TITLE_FINDING = r"\b(improves?|reduces?|enhances?|increases?|decreases?|matters?|outperforms?|leads? to|affects?|controls?|drives?|is|are|does|do|can|reveals?|shows?|yields?|requires?)\b"

GAP_PAT = re.compile(r"^(However|Nevertheless|Nonetheless|Yet|Despite|Although)\b|to (the best of )?our knowledge|"
                     r"(remains?|is still|are still) (unclear|unknown|limited|a (major |key )?challenge|poorly|largely|an open)|"
                     r"(few|limited|little) (studies|research|attention|work)|has not been|have not been|"
                     r"(the )?(main |primary |overall )?(objective|aim|purpose|goal)s? of this (study|paper|work|research)|"
                     r"^(Here|In this (study|paper|work)|This (study|paper|work))[, ]+(we )?", re.I)
RES_METRIC = re.compile(r"\b(NSE|KGE|RMSE|PBIAS|NRMSE|MAE|ENS|E_NS|R\s?2|R²|coefficient of determination|Nash[–-]Sutcliffe|relative error|peak error|volume error|percent bias|correlation coefficient)\b")
NUM = re.compile(r"\d+(\.\d+)?\s?%|\b0\.\d+|\b\d+\.\d+")

rows, figrows, tabrows = [], [], []
ex_results, ex_gap, ex_caps, ex_abstract_open, ex_limit = [], [], [], [], []

files = sorted(glob.glob(os.path.join(PARSED, "*.json")))
assert len(files) >= 15, len(files)
for fp in files:
    d = json.load(open(fp, encoding="utf-8"))
    doi, year = d["doi"], d["year"]
    main_text = " ".join(s["text"] for s in d["sections"])
    W = wc(main_text)
    # --- title
    title = d["title"]
    # --- abstract
    ab = d["abstract"]
    ab_s = sents(ab)
    ab_nums = [m.group() for m in NUM.finditer(ab)]
    moves = {
        "context": bool(ab_s) and not re.search(r"\b(we|this study|this paper|here)\b", ab_s[0], re.I),
        "gap": bool(re.search(r"\bhowever\b|remain|lack|limited|challeng|few studies|not been|unclear|difficult|rarely|seldom|insufficient|yet to", ab, re.I)),
        "aim": bool(re.search(r"this (study|paper|work|research)|we (propose|present|develop|investigate|introduce|evaluate|assess|explore|compare|test|apply|analy[sz]e|quantif)|here,? we|aims? (to|at)|objective|purpose", ab, re.I)),
        "method": bool(re.search(r"\busing\b|\bapplied\b|\bmethod|\bframework|based on|calibrat|algorithm|approach|simulat", ab, re.I)),
        "numeric_result": len([n for n in ab_nums]) > 0,
        "implication": bool(re.search(r"suggest|implication|can be used|could be used|useful|recommend|help|provide[s]? (a |an )?(basis|guidance|insight)|practitioner|decision|benefit|valuable|support", ab_s[-1] if ab_s else "", re.I) or
                            re.search(r"implication|recommend|practitioner|guidance", ab, re.I)),
    }
    ex_abstract_open.append({"doi": doi, "first": ab_s[0] if ab_s else "", "last": ab_s[-1] if ab_s else ""})
    # --- headings
    l1 = [s["heading"] for s in d["sections"] if s["level"] == 1]
    cls = [head_class(h) for h in l1]
    back_heads = " | ".join(b["heading"] for b in d["back"])
    all_heads = " | ".join(l1) + " | " + back_heads
    has_disc = "Discussion" in cls
    has_rd = "Results and Discussion" in cls
    # conclusions length: level-1 conclusion + its subsections
    concl_words, inside = 0, False
    for s in d["sections"]:
        if s["level"] == 1:
            inside = head_class(s["heading"]) == "Conclusions"
        if inside:
            concl_words += wc(s["text"])
    data_av = bool(re.search(r"data availab|code availab|code and data|data and code|open research|data accessibility", all_heads, re.I))
    # --- voice
    n_we = count(r"\bwe\b", main_text); n_our = count(r"\bour\b", main_text)
    n_this = count(r"\b(this|the present|the current) (study|paper|work|research|article)\b", main_text)
    n_pass = count(r"\b(is|are|was|were|been|be|being)\s+(\w+ly\s+)?(\w+ed|built|made|set|run|found|shown|given|done|chosen|taken|seen|known|drawn|written|held|kept|split|put|fit|laid)\b", main_text)
    n_itwas = count(r"\bit (was|is|has been|can be) (found|observed|noted|seen|shown|concluded) that\b", main_text)
    # --- hedging
    hedge = {k: count(p, main_text) for k, p in {
        "may": r"\bmay\b", "might": r"\bmight\b", "could": r"\bcould\b", "suggest": r"\bsuggest(s|ed|ing)?\b",
        "indicate": r"\bindicat(e|es|ed|ing)\b", "demonstrate": r"\bdemonstrat(e|es|ed|ing)\b",
        "show": r"\bshow(s|ed|n|ing)?\b", "reveal": r"\breveal(s|ed|ing)?\b", "likely": r"\blikely\b",
        "possibly": r"\bpossibl[ey]\b", "appear": r"\bappear(s|ed)?\b"}.items()}
    lim_sents = [s for s in sents(main_text) if re.search(r"\blimitation", s, re.I)]
    lim_head = bool(re.search(r"limitation", all_heads, re.I))
    if lim_sents:
        ex_limit.append({"doi": doi, "sentence": lim_sents[0]})
    # --- figures
    ftypes = []
    for i, c in enumerate(d["figures"], 1):
        ft = fig_type(c); cs = cap_style(c); ftypes.append(ft)
        figrows.append({"doi": doi, "fig_no": i, "n_figs": len(d["figures"]), "rel_pos": round(i / len(d["figures"]), 2),
                        "type": ft, **cs, "caption": c[:400]})
    # --- tables
    perf_decimals, perf_bold = [], []
    for i, tb in enumerate(d["tables"], 1):
        tt = tab_type(tb["caption"])
        decs = []
        for cell in tb["cells"]:
            for m in re.finditer(r"(?<![\d.])-?\d+\.(\d+)(?![\d.])", cell):
                decs.append(len(m.group(1)))
        mode_dec = st.mode(decs) if decs else None
        tabrows.append({"doi": doi, "tab_no": i, "type": tt, "n_bold": tb["n_bold"], "mode_decimals": mode_dec,
                        "n_words_caption": wc(tb["caption"]), "caption": tb["caption"][:300]})
        if tt == "performance metrics":
            if mode_dec is not None: perf_decimals.append(mode_dec)
            perf_bold.append(tb["n_bold"] > 0)
    # --- results sentences with metrics
    res_cands = []
    for s in d["sections"]:
        hc = head_class(s["heading"]) if s["level"] == 1 else None
        for se in sents(s["text"]):
            if RES_METRIC.search(se) and NUM.search(se) and 12 <= len(se.split()) <= 70:
                res_cands.append(se)
    n_res = len(res_cands)
    comp = sum(1 for s in res_cands if re.search(r"\bthan\b|compared|outperform|improv|from [\d.]+ to [\d.]+|higher|lower|better|worse|increase|decrease|reduc", s, re.I))
    interp = sum(1 for s in res_cands if re.search(r"indicat|suggest|mean(s|ing)|demonstrat|show(s|ing)|reflect|confirm|imply|due to|because|owing", s, re.I))
    for s in res_cands[:3]:
        ex_results.append({"doi": doi, "sentence": s})
    # --- intro gap/aim sentences
    intro_txt = ""
    inside = False
    for s in d["sections"]:
        if s["level"] == 1:
            inside = head_class(s["heading"]) == "Introduction"
        if inside:
            intro_txt += " " + s["text"]
    gaps = [s for s in sents(intro_txt) if GAP_PAT.search(s)]
    for s in gaps:
        ex_gap.append({"doi": doi, "sentence": s})
    intro_words = wc(intro_txt)
    # --- references
    ys = [r["year"] for r in d["refs"] if r["year"]]
    recent = sum(1 for y in ys if year - 4 <= y <= year + 1)
    rows.append({
        "doi": doi, "journal": d["journal"], "year": year, "group": d["group"],
        "title": title, "title_words": wc(title), "title_colon": ":" in title,
        "title_finding_auto": bool(re.search(TITLE_FINDING, title, re.I)),
        "abs_words": wc(ab), "abs_sentences": len(ab_s), "abs_has_numbers": len(ab_nums) > 0, "abs_n_numbers": len(ab_nums),
        "abs_we": count(r"\bwe\b", ab), "abs_here_we": bool(re.search(r"\bhere,? we\b", ab, re.I)),
        "abs_this_study": count(r"\bthis (study|paper|work)\b", ab),
        **{f"move_{k}": v for k, v in moves.items()},
        "n_l1_sections": len(l1), "l1_headings": " | ".join(l1), "l1_classes": " > ".join(cls),
        "back_headings": back_heads,
        "sep_discussion": has_disc, "results_and_discussion": has_rd, "conclusions_words": concl_words,
        "data_code_availability": data_av, "intro_words": intro_words, "main_words": W,
        "we_per_k": per_k(n_we, W), "our_per_k": per_k(n_our, W), "thisstudy_per_k": per_k(n_this, W),
        "passive_per_k": per_k(n_pass, W), "it_was_found_n": n_itwas,
        **{f"h_{k}_per_k": per_k(v, W) for k, v in hedge.items()},
        "limitation_sentences": len(lim_sents), "limitation_heading": lim_head,
        "n_figs": len(d["figures"]), "fig_types_seq": " > ".join(ftypes), "first_fig_type": ftypes[0] if ftypes else None,
        "cap_words_median": st.median([wc(c) for c in d["figures"]]) if d["figures"] else None,
        "n_tables": len(d["tables"]),
        "perf_table_decimals_mode": st.mode(perf_decimals) if perf_decimals else None,
        "perf_table_bold": any(perf_bold) if perf_bold else None,
        "n_metric_sentences": n_res, "metric_sent_with_comparison": comp, "metric_sent_with_interpretation": interp,
        "n_gap_sentences": len(gaps),
        "n_refs": len(d["refs"]), "refs_with_year": len(ys), "refs_recent5_share": round(recent / len(ys), 3) if ys else None,
    })
    print(f"{doi:32s} W={W:6d} figs={len(d['figures']):2d} first={ftypes[0] if ftypes else None:30s} metricsent={n_res:3d} gaps={len(gaps):2d}")

df = pd.DataFrame(rows); df.to_csv(OUT_CSV, index=False, encoding="utf-8-sig")
fdf = pd.DataFrame(figrows); fdf.to_csv(OUT_FIG, index=False, encoding="utf-8-sig")
tdf = pd.DataFrame(tabrows); tdf.to_csv(OUT_TAB, index=False, encoding="utf-8-sig")
assert len(df) >= 15 and len(fdf) > 100 and len(tdf) > 40, (len(df), len(fdf), len(tdf))

# figure-type position profile: mean relative position & share of papers using each type
prof = fdf.groupby("type").agg(n=("type", "size"), papers=("doi", "nunique"), mean_pos=("rel_pos", "mean"),
                               median_pos=("rel_pos", "median")).sort_values("median_pos")
json.dump({"ex_results": ex_results, "ex_gap": ex_gap, "ex_abstract": ex_abstract_open, "ex_limit": ex_limit},
          open(OUT_EX, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def desc(s):
    s = pd.to_numeric(s, errors="coerce").dropna()
    return {"median": float(s.median()), "min": float(s.min()), "max": float(s.max()), "n": int(len(s))}


num_cols = ["title_words", "abs_words", "abs_sentences", "abs_n_numbers", "n_l1_sections", "conclusions_words", "intro_words",
            "main_words", "we_per_k", "our_per_k", "thisstudy_per_k", "passive_per_k", "n_figs", "cap_words_median",
            "n_tables", "n_refs", "refs_recent5_share", "n_metric_sentences", "n_gap_sentences"] + \
           [c for c in df.columns if c.startswith("h_")]
bool_cols = ["title_colon", "title_finding_auto", "abs_has_numbers", "abs_here_we", "sep_discussion", "results_and_discussion",
             "data_code_availability", "limitation_heading"] + [c for c in df.columns if c.startswith("move_")]
summary = {"n_papers": len(df), "by_group": df.group.value_counts().to_dict(), "by_journal": df.journal.value_counts().to_dict(),
           "numeric": {c: desc(df[c]) for c in num_cols},
           "share_true": {c: round(float(df[c].mean()), 3) for c in bool_cols},
           "numeric_by_group": {g: {c: desc(sub[c]) for c in ["n_figs", "abs_words", "we_per_k", "passive_per_k", "n_refs"]} for g, sub in df.groupby("group")},
           "abs_we_any_share": round(float((df.abs_we > 0).mean()), 3),
           "limitation_sentence_share": round(float((df.limitation_sentences > 0).mean()), 3),
           "first_fig_type": df.first_fig_type.value_counts().to_dict(),
           "fig_type_profile": prof.round(3).reset_index().to_dict(orient="records"),
           "fig_type_counts": fdf.type.value_counts().to_dict(),
           "caption_style_share": {c: round(float(fdf[c].mean()), 3) for c in ["first_is_finding", "panels", "symbols_colors", "units"]},
           "caption_words": desc(fdf.n_words), "caption_sentences": desc(fdf.n_sentences),
           "tab_type_counts": tdf.type.value_counts().to_dict(),
           "perf_table_decimals_mode": df.perf_table_decimals_mode.value_counts(dropna=True).to_dict(),
           "perf_table_bold": df.perf_table_bold.value_counts(dropna=True).to_dict(),
           "metric_sent_total": int(df.n_metric_sentences.sum()),
           "metric_sent_comparison_share": round(df.metric_sent_with_comparison.sum() / max(df.n_metric_sentences.sum(), 1), 3),
           "metric_sent_interpretation_share": round(df.metric_sent_with_interpretation.sum() / max(df.n_metric_sentences.sum(), 1), 3),
           "it_was_found_total": int(df.it_was_found_n.sum()),
           "heading_class_seq": df.l1_classes.tolist()}
json.dump(summary, open(OUT_SUM, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
print(json.dumps({k: summary[k] for k in ["share_true", "first_fig_type", "caption_style_share", "caption_words", "tab_type_counts",
                                          "perf_table_decimals_mode", "perf_table_bold", "metric_sent_total",
                                          "metric_sent_comparison_share", "metric_sent_interpretation_share", "it_was_found_total",
                                          "abs_we_any_share", "limitation_sentence_share", "fig_type_counts"]}, indent=1, default=str))
print(prof.round(2))
for c in num_cols:
    print(c, summary["numeric"][c])
