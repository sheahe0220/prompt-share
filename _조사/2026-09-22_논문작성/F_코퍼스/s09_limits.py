"""
Why: the plain 'limitation' count also hits intro sentences about other methods' limitations.
     This script counts only statements in Discussion / Results-and-Discussion / Conclusions
     sections (own-study limitations and future work), and saves example sentences.
Rerun: C:\\Users\\SGJEONG99\\anaconda3\\envs\\pyswmm\\python.exe -X utf8 s09_limits.py
"""
import os, re, json, glob

HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, "s06_metrics.py"), encoding="utf-8").read().split("rows, figrows, tabrows")[0])
LIM = re.compile(r"\blimitations?\b|shortcoming|caveat|should be (noted|acknowledged)|it is worth noting|is beyond the scope|not considered in this|was not considered|were not considered", re.I)
FUT = re.compile(r"future (work|research|stud)|further (research|work|stud|investigation)", re.I)
out, n_lim, n_fut = [], 0, 0
files = sorted(glob.glob(os.path.join(HERE, "parsed", "*.json"))); assert len(files) == 26
for fp in files:
    d = json.load(open(fp, encoding="utf-8"))
    txt, keep = "", False
    for s in d["sections"]:
        if s["level"] == 1:
            keep = head_class(s["heading"]) in ("Discussion", "Results and Discussion", "Conclusions", "Limitations/Outlook")
        if keep:
            txt += " " + s["text"]
    ls = [x for x in sents(txt) if LIM.search(x)]
    fs = [x for x in sents(txt) if FUT.search(x)]
    n_lim += bool(ls); n_fut += bool(fs)
    out.append({"doi": d["doi"], "n_lim": len(ls), "n_future": len(fs), "lim_ex": ls[:2], "fut_ex": fs[:1]})
print("papers with own-limitation statement in Disc/Concl:", n_lim, "/ 26; with future-work statement:", n_fut, "/ 26")
json.dump(out, open(os.path.join(HERE, "limits.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for o in out:
    if o["lim_ex"]:
        print("-", o["doi"], "|", o["lim_ex"][0][:260])
