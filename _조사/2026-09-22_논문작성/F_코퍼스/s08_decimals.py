"""
Why: count how many decimals authors use when stating NSE/KGE/R2 values in running text
     (all metric sentences in all 26 papers), to recommend a reporting precision.
Rerun: C:\\Users\\SGJEONG99\\anaconda3\\envs\\pyswmm\\python.exe -X utf8 s08_decimals.py
"""
import os, re, json, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, "s06_metrics.py"), encoding="utf-8").read().split("rows, figrows, tabrows")[0])
pat = re.compile(r"\b(NSE|KGE'?|R2|R²|ENS|M-NSE|CE|Nash[–-]Sutcliffe (efficiency|coefficient))\b[^.;]{0,40}?(-?0\.\d+|1\.0+)")
dec = collections.Counter(); per_paper = collections.defaultdict(collections.Counter); n = 0
for fp in sorted(glob.glob(os.path.join(HERE, "parsed", "*.json"))):
    d = json.load(open(fp, encoding="utf-8"))
    txt = " ".join(s["text"] for s in d["sections"]) + " " + d["abstract"]
    for m in pat.finditer(txt):
        k = len(m.group(3).split(".")[1]); dec[k] += 1; per_paper[d["doi"]][k] += 1; n += 1
assert n > 20, n
print("values", n, "decimals", dict(sorted(dec.items())))
modes = collections.Counter(max(c, key=c.get) for c in per_paper.values())
print("papers", len(per_paper), "per-paper mode decimals", dict(modes))
json.dump({"n_values": n, "decimals": dict(dec), "papers": len(per_paper), "paper_mode": dict(modes)},
          open(os.path.join(HERE, "decimals.json"), "w"), indent=1)
