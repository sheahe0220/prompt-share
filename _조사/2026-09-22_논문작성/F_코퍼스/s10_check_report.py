"""
Why: before handing over, verify (1) the report has no em dash, U+2212 or tilde, and
     (2) every quoted English sentence (in double quotes, followed by a DOI) occurs verbatim
     in the parsed full text of that DOI. Exits non-zero on any failure.
Rerun: C:\\Users\\SGJEONG99\\anaconda3\\envs\\pyswmm\\python.exe -X utf8 s10_check_report.py
"""
import os, re, json, glob, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPORT = os.path.join(os.path.dirname(HERE), "paper_F_Q1코퍼스.md")
txt = open(REPORT, encoding="utf-8").read()
bad = {"em dash": "\u2014", "U+2212": "\u2212", "tilde": "~"}
fail = 0
for k, ch in bad.items():
    n = txt.count(ch)
    print(k, n)
    fail += n

corp = {}
for fp in glob.glob(os.path.join(HERE, "parsed", "*.json")):
    d = json.load(open(fp, encoding="utf-8"))
    full = " ".join([d["title"], d["abstract"]] + [s["text"] for s in d["sections"]] + d["figures"])
    corp[d["doi"]] = re.sub(r"\s+", " ", full)

quotes = re.findall(r'"([^"]{25,}?)"\s*\((10\.[^,)\s]+)', txt)
assert len(quotes) >= 30, len(quotes)
nf = 0
for q, doi in quotes:
    body = corp.get(doi.lower()) or corp.get(doi)
    q2 = q.replace(" ...", "").strip()
    parts = [p.strip() for p in q2.split("...") if p.strip()]
    ok = body is not None and all(p in body for p in parts)
    if not ok:
        nf += 1
        print("NOT FOUND:", doi, "|", q[:120])
print("quotes checked", len(quotes), "not found", nf)
sys.exit(1 if (fail or nf) else 0)
