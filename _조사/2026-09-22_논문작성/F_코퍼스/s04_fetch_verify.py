"""
Why: (1) download HESS JATS XML full texts, (2) verify every corpus DOI against Crossref
     (title, journal, year) so no paper is invented, (3) write corpus_list.csv.
Rerun: C:\\Users\\SGJEONG99\\anaconda3\\envs\\pyswmm\\python.exe -X utf8 s04_fetch_verify.py
Browser-fetched publisher HTML files are expected already in raw/ (see s03_receiver.py).
"""
import os, csv, time, requests, re

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
OUT = os.path.join(HERE, "corpus_list.csv")
UA = {"User-Agent": "Mozilla/5.0 (corpus study)"}

# Excluded 2026-09-22: hess-19-691-2015 and hess-19-2409-2015, their Copernicus XML has no body (abstract-only stub).
# (file, doi, group)  group: U = SWMM/urban drainage, R = related hydrological calibration
HESS = [("24-869-2020", "U"), ("22-2615-2018", "U"), ("21-1559-2017", "U"), ("25-5839-2021", "U"),
        ("25-5493-2021", "U"), ("19-4001-2015", "U"), ("23-4293-2019", "U"), ("21-4895-2017", "R"),
        ("24-4641-2020", "R"), ("22-5021-2018", "R"), ("21-393-2017", "R"), ("21-6219-2017", "R")]
OTHERS = [
    ("wrr_2022_032440.html", "10.1029/2022wr032440", "U"),
    ("wrr_2024_039525.html", "10.1029/2024wr039525", "R"),
    ("wrr_2015_018230.html", "10.1002/2015wr018230", "R"),
    ("wrr_2021_030928.html", "10.1029/2021wr030928", "U"),
    ("hyp_2018_13319.html", "10.1002/hyp.13319", "R"),
    ("jh_2019_124436.html", "10.1016/j.jhydrol.2019.124436", "U"),
    ("ems_2024_106122.html", "10.1016/j.envsoft.2024.106122", "U"),
    ("jh_2021_126525.html", "10.1016/j.jhydrol.2021.126525", "U"),
    ("jh_2023_129757.html", "10.1016/j.jhydrol.2023.129757", "U"),
    ("jh_2024_131546.html", "10.1016/j.jhydrol.2024.131546", "U"),
    ("ems_2022_105341.html", "10.1016/j.envsoft.2022.105341", "R"),
    ("jenv_2024_121244.html", "10.1016/j.jenvman.2024.121244", "U"),
    ("jhi_2024_282.html", "10.2166/hydro.2024.282", "U"),
    ("jhi_2026_064.html", "10.2166/hydro.2026.064", "U"),
]

items = []
for key, g in HESS:
    vol, page, yr = key.split("-")
    fn = f"hess-{key}.xml"
    fp = os.path.join(RAW, fn)
    if not os.path.exists(fp):
        url = f"https://hess.copernicus.org/articles/{vol}/{page}/{yr}/hess-{key}.xml"
        r = requests.get(url, headers=UA, timeout=60)
        assert r.status_code == 200 and b"<article" in r.content[:5000], (url, r.status_code)
        open(fp, "wb").write(r.content)
        time.sleep(1)
    items.append((fn, f"10.5194/hess-{key}", g))
items += OTHERS

rows = []
for fn, doi, g in items:
    fp = os.path.join(RAW, fn)
    assert os.path.exists(fp), fp
    r = requests.get(f"https://api.crossref.org/works/{doi}", headers=UA, timeout=60)
    assert r.status_code == 200, (doi, r.status_code)
    m = r.json()["message"]
    title = re.sub(r"<[^>]+>", "", (m.get("title") or [""])[0])
    journal = (m.get("container-title") or [""])[0]
    year = (m.get("published") or m.get("issued"))["date-parts"][0][0]
    # check that the downloaded file contains the Crossref title (first 6 words)
    txt = open(fp, encoding="utf-8", errors="ignore").read()
    words = re.findall(r"[A-Za-z]{4,}", title)[:5]
    match = all(w.lower() in txt.lower() for w in words)
    rows.append({"file": fn, "doi": doi, "group": g, "title": title, "journal": journal,
                 "year": year, "ref_count_crossref": m.get("reference-count"),
                 "oa_url": f"https://doi.org/{doi}", "title_in_file": match, "bytes": len(txt)})
    print(doi, year, journal[:30], "match" if match else "NO MATCH", "|", title[:70])
    time.sleep(0.5)

assert len(rows) >= 15
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("n =", len(rows), "matches =", sum(r["title_in_file"] for r in rows))
