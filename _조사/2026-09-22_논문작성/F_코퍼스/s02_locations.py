"""
Why: for non-Copernicus candidate DOIs, list every OA location (repository PDFs etc.)
     from OpenAlex single-work lookups, since publisher sites (Elsevier/Wiley/IWA) block scripts.
Rerun: C:\\Users\\SGJEONG99\\anaconda3\\envs\\pyswmm\\python.exe -X utf8 s02_locations.py
Output: locations.json
"""
import os, json, time, requests

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "locations.json")
DOIS = [
    "10.1016/j.jhydrol.2019.124436", "10.1029/2022wr032440", "10.2166/hydro.2024.282",
    "10.2166/hydro.2026.064", "10.1016/j.envsoft.2024.106122", "10.1016/j.jhydrol.2015.05.057",
    "10.1016/j.jhydrol.2018.11.005", "10.1016/j.jhydrol.2021.126525", "10.1080/1573062x.2016.1254255",
    "10.1016/j.jhydrol.2023.129757", "10.1016/j.jhydrol.2024.131546", "10.1016/j.envsoft.2018.07.016",
    "10.1029/2024wr039525", "10.1002/2015wr018230", "10.1016/j.jhydrol.2016.11.051",
    "10.1016/j.envsoft.2022.105341", "10.1029/2021wr030928", "10.1002/hyp.13319",
    "10.1016/j.watres.2018.06.011", "10.1016/j.jenvman.2024.121244",
]
out = {}
for d in DOIS:
    for a in range(4):
        r = requests.get(f"https://api.openalex.org/works/doi:{d}",
                         params={**({"mailto": __import__("os").environ["OPENALEX_MAILTO"]} if __import__("os").environ.get("OPENALEX_MAILTO") else {}), "select": "doi,title,locations"}, timeout=60)
        if r.status_code == 429:
            time.sleep(15); continue
        break
    if r.status_code != 200:
        print("FAIL", d, r.status_code); continue
    w = r.json()
    locs = [(l.get("pdf_url"), l.get("landing_page_url"), (l.get("source") or {}).get("display_name"))
            for l in w.get("locations", []) if l.get("is_oa")]
    out[d] = {"title": w.get("title"), "locs": locs}
    print(d, len(locs)); [print("   ", x) for x in locs]
    time.sleep(1.5)
assert out
json.dump(out, open(OUT, "w", encoding="utf-8"), indent=1)
