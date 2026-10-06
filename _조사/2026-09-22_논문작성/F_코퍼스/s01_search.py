"""
Why: find candidate OA articles (2015-2026) in Q1 hydrology journals via OpenAlex
     for a writing-style corpus on SWMM calibration / surrogate / BO papers.
Rerun: C:\\Users\\SGJEONG99\\anaconda3\\envs\\pyswmm\\python.exe -X utf8 s01_search.py
Output: candidates.csv (one row per hit, with query tag)
"""
import time, csv, requests, os, json

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "candidates.csv")
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qcache"); os.makedirs(CACHE, exist_ok=True)
import os as _os
MAILTO = _os.environ.get("OPENALEX_MAILTO", "")  # never hard-code a personal e-mail

JOURNALS = ["hydrology and earth system sciences", "water resources research",
            "journal of hydrology", "environmental modelling", "water research",
            "journal of hydroinformatics", "urban water journal", "water science and technology",
            "geoscientific model development", "journal of environmental management",
            "hydrological processes", "journal of water resources planning"]

QUERIES = [
    "SWMM calibration", "SWMM parameter uncertainty", "storm water management model calibration",
    "urban drainage model calibration", "urban drainage model uncertainty Bayesian",
    "sewer model calibration", "SWMM sensitivity analysis", "urban drainage rainfall uncertainty",
    "urban drainage surrogate model", "SWMM surrogate", "satellite rainfall urban flood model",
    "hydrological model calibration Bayesian optimization", "surrogate-based calibration hydrological model",
    "Gaussian process emulator hydrological model calibration", "rainfall input uncertainty hydrological model",
    "radar rainfall urban drainage", "automatic calibration hydrological model",
]

rows = []
for q in QUERIES:
    url = "https://api.openalex.org/works"
    params = {"search": q, "filter": "is_oa:true,from_publication_date:2015-01-01,type:article",
              "per-page": 50, "mailto": MAILTO,
              "select": "id,doi,title,publication_year,primary_location,open_access,cited_by_count,best_oa_location"}
    cf = os.path.join(CACHE, q.replace(" ", "_") + ".json")
    if os.path.exists(cf):
        res = json.load(open(cf, encoding="utf-8"))
    else:
        for attempt in range(4):
            r = requests.get(url, params=params, timeout=60)
            if r.status_code == 429:
                print("429, remaining:", r.headers.get("X-RateLimit-Remaining"), "retry-after:", r.headers.get("Retry-After"))
                time.sleep(15 * (attempt + 1)); continue
            break
        if r.status_code != 200:
            print("SKIP", q, r.status_code); continue
        res = r.json()["results"]
        json.dump(res, open(cf, "w", encoding="utf-8"))
        time.sleep(5)
    n = 0
    for w in res:
        src = ((w.get("primary_location") or {}).get("source") or {})
        jn = (src.get("display_name") or "")
        if not any(j in jn.lower() for j in JOURNALS):
            continue
        boa = w.get("best_oa_location") or {}
        rows.append({"query": q, "doi": w.get("doi"), "title": w.get("title"),
                     "year": w.get("publication_year"), "journal": jn,
                     "cites": w.get("cited_by_count"),
                     "oa_url": (w.get("open_access") or {}).get("oa_url"),
                     "pdf_url": boa.get("pdf_url")})
        n += 1
    print(f"{q}: {len(res)} hits, {n} in target journals")

assert rows, "no candidates"
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print("rows", len(rows), "->", OUT)
