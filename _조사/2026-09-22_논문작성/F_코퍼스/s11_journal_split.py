r"""Split the 26-paper Q1 corpus metrics by journal, so no finding is read as "all SCI".

Why: HESS is 12 of 26 papers (46 %). A pooled median can simply be the HESS habit.
The guideline (13_논문.md) must say which journal a number comes from.

Rerun:
  C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe -X utf8 s11_journal_split.py
Output: journal_split.csv next to this file, and a printed table.
"""
import os

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "metrics_per_paper.csv")
OUT = os.path.join(HERE, "journal_split.csv")

m = pd.read_csv(SRC)
assert len(m) == 26, "expected 26 papers, got %d" % len(m)

short = {
    "Hydrology and Earth System Sciences": "HESS",
    "Water Resources Research": "WRR",
    "Journal of Hydrology": "J. Hydrol.",
    "Journal of Hydroinformatics": "J. Hydroinform.",
    "Environmental Modelling & Software": "EMS",
    "Hydrological Processes": "Hydrol. Process.",
    "Journal of Environmental Management": "J. Environ. Manage.",
}
m["j"] = m["journal"].map(short).fillna(m["journal"])
assert m["j"].isin(short.values()).all(), m.loc[~m["j"].isin(short.values()), "journal"].unique()
m["hess"] = m["j"].eq("HESS").map({True: "HESS", False: "HESS 외"})

cols = {
    "we_per_k": "median", "thisstudy_per_k": "median", "passive_per_k": "median",
    "abs_words": "median", "n_figs": "median", "cap_words_median": "median",
    "n_tables": "median", "n_refs": "median",
    "abs_has_numbers": "mean", "abs_we": lambda s: (s > 0).mean(),
    "abs_this_study": lambda s: (s > 0).mean(),
    "data_code_availability": "mean", "results_and_discussion": "mean",
}


def table(by):
    g = m.groupby(by).agg(n=("doi", "size"), **{k: (k, f) for k, f in cols.items()})
    return g.round(2)


parts = [table("hess"), table("j"), table("group")]
res = pd.concat(parts, keys=["HESS 여부", "학술지", "주제군(U 도시배수 · R 인접)"])
res.to_csv(OUT, encoding="utf-8-sig")
pd.set_option("display.width", 220)
pd.set_option("display.max_columns", 30)
print(res)
assert res.loc["HESS 여부", "n"].sum() == 26
print("saved", OUT)
