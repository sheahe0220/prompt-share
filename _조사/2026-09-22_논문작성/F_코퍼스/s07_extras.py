"""
Why: extra corpus counts needed for the guidance note (roadmap paragraph, numbered objectives,
     'However' density in introductions, abstract opening/closing sentences, limitation sentences,
     sample captions, performance-table details, data-availability wording).
Rerun: C:\\Users\\SGJEONG99\\anaconda3\\envs\\pyswmm\\python.exe -X utf8 s07_extras.py
Output: extras.json
"""
import os, re, json, glob
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
PARSED = os.path.join(HERE, "parsed")
OUT = os.path.join(HERE, "extras.json")
exec(open(os.path.join(HERE, "s06_metrics.py"), encoding="utf-8").read().split("rows, figrows, tabrows")[0])  # reuse helpers

res = {"roadmap": [], "numbered_obj": [], "however_per_k_intro": {}, "abs_first": [], "abs_last": [], "limit": [],
       "caps_long": [], "caps_short": [], "perf_tables": [], "data_av_text": [], "abs_here_we": [], "concl_style": []}
files = sorted(glob.glob(os.path.join(PARSED, "*.json")))
assert len(files) == 26, len(files)
for fp in files:
    d = json.load(open(fp, encoding="utf-8")); doi = d["doi"]
    intro, inside = "", False
    for s in d["sections"]:
        if s["level"] == 1:
            inside = head_class(s["heading"]) == "Introduction"
        if inside:
            intro += " " + s["text"]
    if re.search(r"(organi[sz]ed|structured) as follows|remainder of (this|the) paper|rest of (this|the) paper", intro, re.I):
        res["roadmap"].append(doi)
    if re.search(r"\((1|i)\)[^.]{5,}\((2|ii)\)", intro):
        res["numbered_obj"].append(doi)
    res["however_per_k_intro"][doi] = round(1000 * len(re.findall(r"\bHowever\b", intro)) / max(wc(intro), 1), 2)
    ab = sents(d["abstract"])
    res["abs_first"].append({"doi": doi, "s": ab[0] if ab else ""})
    res["abs_last"].append({"doi": doi, "s": ab[-1] if ab else ""})
    if re.search(r"\bhere,? we\b", d["abstract"], re.I):
        res["abs_here_we"].append({"doi": doi, "s": [x for x in ab if re.search(r"\bhere,? we\b", x, re.I)][0]})
    main = " ".join(s["text"] for s in d["sections"])
    lim = [x for x in sents(main) if re.search(r"\blimitations?\b", x, re.I)]
    if lim:
        res["limit"].append({"doi": doi, "n": len(lim), "s": lim[0]})
    for c in d["figures"]:
        n = wc(c)
        if 30 <= n <= 70 and re.search(r"\(a\)", c) and len(res["caps_long"]) < 40:
            res["caps_long"].append({"doi": doi, "c": c})
        if n <= 8 and len(res["caps_short"]) < 40:
            res["caps_short"].append({"doi": doi, "c": c})
    for t in d["tables"]:
        if tab_type(t["caption"]) == "performance metrics":
            res["perf_tables"].append({"doi": doi, "cap": t["caption"][:200], "n_bold": t["n_bold"],
                                       "sample_cells": [x for x in t["cells"] if re.search(r"\d\.\d", x)][:8]})
    for b in d["back"]:
        if re.search(r"data|code", b["heading"], re.I) and b["text"]:
            res["data_av_text"].append({"doi": doi, "h": b["heading"], "t": b["text"][:250]})
    # conclusions: numbered list or prose?
    concl, inside = "", False
    for s in d["sections"]:
        if s["level"] == 1:
            inside = head_class(s["heading"]) == "Conclusions"
        if inside:
            concl += " " + s["text"]
    res["concl_style"].append({"doi": doi, "numbered": bool(re.search(r"\((1|i)\)|\b1\)\s|First(ly)?,", concl)),
                               "has_future": bool(re.search(r"future (work|research|stud)|further (research|work|stud)", concl, re.I)),
                               "has_limit": bool(re.search(r"limitation", concl, re.I)),
                               "has_number": bool(re.search(r"\d+(\.\d+)?\s?%|\b0\.\d+", concl))})
cs = pd.DataFrame(res["concl_style"])
res["concl_share"] = cs[["numbered", "has_future", "has_limit", "has_number"]].mean().round(3).to_dict()
res["however_median"] = float(pd.Series(res["however_per_k_intro"]).median())
print("roadmap", len(res["roadmap"]), "numbered_obj", len(res["numbered_obj"]), "however/k intro median", res["however_median"])
print("concl", res["concl_share"], "limit papers", len(res["limit"]))
print("perf tables", len(res["perf_tables"]))
json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
