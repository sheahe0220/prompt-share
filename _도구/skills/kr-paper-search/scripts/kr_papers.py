r"""국내 학술 논문 검색. KCI 와 DBpia 의 공식 Open API 만 부른다.

무엇을 왜 만들었나
  남이 만든 국내 논문 MCP(korea-academic-mcp)는 별 0 개에 라이선스가 없고, 거기에
  API 키를 넘기는 구조였다. 공식 API 를 직접 부르는 짧은 도구가 더 안전하다.
  KCI 원고의 선행연구 조사와 20_자료조사.md 의 근거 찾기에 쓴다.

확인한 것 (2026-09-20)
  KCI    https://open.kci.go.kr/po/openapi/openApiSearch.kci   apiCode=articleSearch
         인자와 응답 필드는 KCI Open API 명세서(openDataView.kci?dtstSeqNo=21)에서 옮겼다
         키 없이 부르면 <resultMsg>등록되지 않은 key 입니다.</resultMsg> 를 돌려준다(실측)
  DBpia  https://api.dbpia.co.kr/v2/search/search.xml   target=se
         http 로 부르면 https 로 301 옮긴다(실측). 시험용 키는 이제 E0001 을 돌려준다
  RISS   공식 명세를 확인하지 못해 넣지 않았다. [판정보류]

키
  환경변수 KCI_API_KEY · DBPIA_API_KEY, 없으면 아래 파일에서 읽는다 (git 에 올리지 않는다)
    %USERPROFILE%\.claude\keys\kr_papers.env
      KCI_API_KEY=...
      DBPIA_API_KEY=...
  발급  KCI    https://www.kci.go.kr  > Open API 신청
        DBpia  https://api.dbpia.co.kr > 키 발급

실행
  python.exe -X utf8 kr_papers.py "초기 우수 비점오염" --src kci dbpia --n 20 --out 결과.csv
  --from 2015 --to 2026   발행 연도 범위 (KCI 만)
"""
import argparse
import csv
import os
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

KCI_URL = "https://open.kci.go.kr/po/openapi/openApiSearch.kci"
DBPIA_URL = "https://api.dbpia.co.kr/v2/search/search.xml"
KEYFILE = os.path.join(os.path.expanduser("~"), ".claude", "keys", "kr_papers.env")
열 = ["출처", "제목", "저자", "학술지", "연도", "권호", "DOI", "URL"]


def 키(name):
    v = os.environ.get(name, "").strip()
    if v:
        return v
    if os.path.exists(KEYFILE):
        for line in open(KEYFILE, encoding="utf-8"):
            if line.strip().startswith(name + "="):
                return line.split("=", 1)[1].strip()
    return ""


def 받기(url, params):
    q = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    req = urllib.request.Request(url + "?" + q, headers={"User-Agent": "kr-paper-search"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def 글(el, path):
    x = el.find(path) if el is not None else None
    return " ".join((x.text or "").split()) if x is not None and x.text else ""


def parse_kci(raw):
    """KCI 응답을 행으로 바꾼다. 오류면 (None, 메시지)."""
    root = ET.fromstring(raw)
    msg = 글(root, "outputData/result/resultMsg")
    recs = root.findall(".//record")
    if not recs and msg:
        return None, msg
    rows = []
    for r in recs:
        j, a = r.find("journalInfo"), r.find("articleInfo")
        titles = [" ".join((t.text or "").split())
                  for t in (a.findall("title-group/article-title") if a is not None else [])
                  if t.text]
        authors = [" ".join((t.text or "").split())
                   for t in (a.findall("author-group/author") if a is not None else [])
                   if t.text]
        vol, iss = 글(j, "volume"), 글(j, "issue")
        rows.append({
            "출처": "KCI",
            "제목": titles[0] if titles else 글(a, ".//article-title"),
            "저자": "; ".join(authors),
            "학술지": 글(j, "journal-name"),
            "연도": 글(j, "pub-year"),
            "권호": ("%s(%s)" % (vol, iss)) if vol or iss else "",
            "DOI": 글(a, "doi"),
            "URL": 글(a, "url"),
        })
    return rows, msg


def parse_dbpia(raw):
    root = ET.fromstring(raw)
    code = 글(root, ".//error/Code") or 글(root, "error/Code")
    items = root.findall(".//item")
    if not items and code:
        return None, "DBpia 오류 코드 %s (키가 없거나 잘못됨)" % code
    rows = []
    for it in items:
        authors = [" ".join((x.text or "").split()) for x in it.findall("authors/author")
                   if x.text]
        rows.append({
            "출처": "DBpia",
            "제목": 글(it, "title"),
            "저자": "; ".join(authors),
            "학술지": 글(it, "publication/name"),
            # 공식 안내의 필드는 issue/name 뿐이다. 거기서 네 자리 연도만 뽑는다
            "연도": (re.search(r"(19|20)\d{2}", 글(it, "issue/name")) or [""])[0],
            "권호": 글(it, "issue/name"),
            "DOI": "",
            "URL": 글(it, "link_url"),
        })
    return rows, ""


def 검색_kci(q, n, y0, y1):
    k = 키("KCI_API_KEY")
    if not k:
        return None, "KCI_API_KEY 가 없다. 키 파일: %s" % KEYFILE
    p = {"apiCode": "articleSearch", "key": k, "title": q, "displayCount": min(n, 100)}
    if y0:
        p["dateFrom"] = "%s01" % y0
    if y1:
        p["dateTo"] = "%s12" % y1
    return parse_kci(받기(KCI_URL, p))


def 검색_dbpia(q, n):
    k = 키("DBPIA_API_KEY")
    if not k:
        return None, "DBPIA_API_KEY 가 없다. 키 파일: %s" % KEYFILE
    return parse_dbpia(받기(DBPIA_URL, {"key": k, "target": "se", "searchall": q,
                                       "pagecount": min(n, 100)}))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--src", nargs="+", default=["kci", "dbpia"], choices=["kci", "dbpia"])
    ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--from", dest="y0")
    ap.add_argument("--to", dest="y1")
    ap.add_argument("--out")
    a = ap.parse_args()

    모두, 실패 = [], []
    for s in a.src:
        try:
            rows, msg = (검색_kci(a.query, a.n, a.y0, a.y1) if s == "kci"
                         else 검색_dbpia(a.query, a.n))
        except Exception as e:                     # 네트워크 · XML 오류
            rows, msg = None, "%s: %s" % (type(e).__name__, e)
        if rows is None:
            실패.append((s, msg))
            print("[%s 실패] %s" % (s.upper(), msg))
            continue
        print("[%s] %d 건" % (s.upper(), len(rows)))
        모두 += rows

    for r in 모두[:a.n * 2]:
        print("  %s  %s  %s  %s" % (r["연도"] or "----", r["출처"], r["제목"][:60], r["저자"][:30]))
    if a.out:
        with open(a.out, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=열)
            w.writeheader()
            w.writerows(모두)
        print("[저장] %s  %d 건" % (a.out, len(모두)))

    # 0 건을 조용히 넘기지 않는다
    if not 모두:
        print("[결과] 0 건. 위의 실패 이유를 본다")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
