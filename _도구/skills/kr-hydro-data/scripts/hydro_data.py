r"""강수 · 수위 관측 자료를 공식 Open API 로 받아 CSV 로 쌓는다.

무엇을 왜 만들었나
  사상마다 강우 · 수위 자료를 누리집에서 손으로 내려받아 붙이는 일이 반복됐다.
  공식 API 를 직접 부르면 사상 목록 하나로 한 번에 받고, 무엇을 언제 어디서
  받았는지가 기록으로 남는다. 관련 MCP 는 1 년째 멈췄거나 규모가 작아 쓰지 않았다.

출처와 확인한 것 (2026-09-20)
  WAMIS   http://www.wamis.go.kr:8080/wamis/openapi/wkw/   키가 필요 없다 (실측)
          rf_dubrfobs  강수 관측소 검색  basin · keynm      공식 안내 + 실호출
          wl_dubwlobs  수위 관측소 검색  basin               공식 안내 + 실호출
          rf_hrdata    강수 시자료  obscd · startdt · enddt  공식 안내 + 실호출. ymdh · rf
          rf_dtdata    강수 일자료  obscd · startdt · enddt  공식 안내.          ymd · rf
          wl_hrdata    수위 시자료  obscd · startdt · enddt  실호출 성공.         ymdh · wl
          공지: 연계 문제로 WAMIS 의 기상청 강수 자료가 정상 표출되지 않는다.
                기상청 관측소는 아래 ASOS 로 받는다.
  ASOS    https://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList
          공공데이터포털 명세 확인. serviceKey 필요. tm · stnNm · rn
          키가 틀리면 SERVICE_KEY_IS_NOT_REGISTERED_ERROR (실측)

실행
  관측소 찾기
    python.exe -X utf8 hydro_data.py 찾기 --kind rf --name 구로
    python.exe -X utf8 hydro_data.py 찾기 --kind wl --name 오금
  한 기간 받기
    python.exe -X utf8 hydro_data.py 받기 --src wamis-rf --obs 10184080 ^
        --from 2022-08-08 --to 2022-08-09 --out <폴더>
  사상 목록으로 받기  (CSV 열: 사상,시작,끝   예: 2022E40,2022-08-08,2022-08-10)
    python.exe -X utf8 hydro_data.py 사상 --list 사상목록.csv --src wamis-wl ^
        --obs 1018697 --out <폴더>

  ASOS 키   환경변수 DATA_GO_KR_KEY 또는 %USERPROFILE%\.claude\keys\kr_hydro.env

지키는 것
  없는 값은 비워 둔다. 0 으로 채우지 않는다. 없는 것과 0 은 다르다 (21_자료분석.md)
  서버가 연속 요청을 끊는다(실측 두 번). 요청 사이를 쉬고, 끊기면 다시 받는다
  응답의 count 와 실제 행 수가 다르면 잘린 것으로 보고 다시 받는다
  받은 기록을 _받기기록.csv 에 남긴다. 02_폴더.md 의 계보
"""
import argparse
import csv
import datetime as dt
import json
import os
import sys
import time
import urllib.parse
import urllib.request

WAMIS = "http://www.wamis.go.kr:8080/wamis/openapi/wkw/"
ASOS = "https://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList"
KEYFILE = os.path.join(os.path.expanduser("~"), ".claude", "keys", "kr_hydro.env")
쉼 = 3.0          # 요청 사이 초. 서버가 연속 요청을 끊는다
조각일수 = 31     # 긴 기간은 이만큼씩 나눠 부른다. 한도는 명세에 없다 [추정]


def 키(name):
    v = os.environ.get(name, "").strip()
    if v:
        return v
    if os.path.exists(KEYFILE):
        for line in open(KEYFILE, encoding="utf-8"):
            if line.strip().startswith(name + "="):
                return line.split("=", 1)[1].strip()
    return ""


def 부르기(url, params, 시도=4):
    """JSON 을 받는다. 끊기거나 잘리면 쉬었다 다시 받는다."""
    q = urllib.parse.urlencode(params)
    마지막 = None
    for n in range(시도):
        try:
            req = urllib.request.Request(url + "?" + q, headers={"User-Agent": "kr-hydro-data"})
            with urllib.request.urlopen(req, timeout=60) as r:
                d = json.loads(r.read().decode("utf-8"))
            return d
        except Exception as e:                       # 끊김 · 잘린 JSON
            마지막 = e
            time.sleep(쉼 * (n + 2))
    raise RuntimeError("%d 번 시도했으나 실패: %s: %s" % (시도, type(마지막).__name__, 마지막))


def wamis(name, params):
    params = dict(params, output="json")
    for n in range(3):
        d = 부르기(WAMIS + name, params)
        res = d.get("result", {})
        if res.get("code") != "success":
            raise RuntimeError("WAMIS %s: %s" % (name, res))
        rows = d.get("list", []) or []
        if int(d.get("count", len(rows))) == len(rows):
            return rows
        time.sleep(쉼 * (n + 2))                    # count 와 행 수가 다르면 잘린 것
    raise RuntimeError("WAMIS %s: 응답이 계속 잘린다 (count %s, 행 %d)"
                       % (name, d.get("count"), len(rows)))


def 수(s):
    """'.87' 같은 값도 읽는다. 빈 값 · '-' 는 None. 0 으로 바꾸지 않는다."""
    s = (s or "").strip()
    if s in ("", "-", "null", "None"):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def 조각(a, b):
    cur = a
    while cur <= b:
        end = min(b, cur + dt.timedelta(days=조각일수 - 1))
        yield cur, end
        cur = end + dt.timedelta(days=1)


def 받기_wamis(kind, obs, a, b):
    """kind: rf(시강수) · rfd(일강수) · wl(시수위)"""
    name, tkey, vkey = {"rf": ("rf_hrdata", "ymdh", "rf"),
                        "rfd": ("rf_dtdata", "ymd", "rf"),
                        "wl": ("wl_hrdata", "ymdh", "wl")}[kind]
    out = []
    for s, e in 조각(a, b):
        rows = wamis(name, {"obscd": obs, "startdt": s.strftime("%Y%m%d"),
                            "enddt": e.strftime("%Y%m%d")})
        for r in rows:
            out.append((r.get(tkey, ""), 수(r.get(vkey))))
        time.sleep(쉼)
    return out


def 받기_asos(stn, a, b):
    k = 키("DATA_GO_KR_KEY")
    if not k:
        raise RuntimeError("DATA_GO_KR_KEY 가 없다. 키 파일: %s" % KEYFILE)
    out = []
    for s, e in 조각(a, b):
        page = 1
        while True:
            d = 부르기(ASOS, {"serviceKey": k, "pageNo": page, "numOfRows": 999,
                              "dataType": "JSON", "dataCd": "ASOS", "dateCd": "HR",
                              "startDt": s.strftime("%Y%m%d"), "startHh": "00",
                              "endDt": e.strftime("%Y%m%d"), "endHh": "23",
                              "stnIds": stn})
            hdr = d.get("OpenAPI_ServiceResponse", {}).get("cmmMsgHeader")
            if hdr:
                raise RuntimeError("ASOS: %s" % hdr.get("returnAuthMsg") or hdr)
            body = d["response"]["body"]
            items = body.get("items", {}).get("item", []) or []
            out += [(it.get("tm", ""), 수(it.get("rn"))) for it in items]
            if page * 999 >= int(body.get("totalCount", 0)):
                break
            page += 1
            time.sleep(쉼)
        time.sleep(쉼)
    return out


def 받기(src, obs, a, b):
    if src == "asos":
        return 받기_asos(obs, a, b)
    return 받기_wamis({"wamis-rf": "rf", "wamis-rfd": "rfd", "wamis-wl": "wl"}[src], obs, a, b)


def 쓰기(rows, path, src, obs):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["시각", "값", "출처", "관측소"])
        for t, v in rows:
            w.writerow([t, "" if v is None else v, src, obs])


def 기록(out, 줄):
    p = os.path.join(out, "_받기기록.csv")
    새 = not os.path.exists(p)
    with open(p, "a", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        if 새:
            w.writerow(["받은시각", "출처", "관측소", "시작", "끝", "행수", "결측수", "파일"])
        w.writerow(줄)


def 날짜(s):
    return dt.datetime.strptime(s, "%Y-%m-%d").date()


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("찾기")
    f.add_argument("--kind", choices=["rf", "wl"], required=True)
    f.add_argument("--name", default="")
    f.add_argument("--basin", default="1", help="1 한강 · 2 낙동강 · 3 금강 · 4 섬진강 · 5 영산강 [추정]")
    g = sub.add_parser("받기")
    g.add_argument("--src", choices=["wamis-rf", "wamis-rfd", "wamis-wl", "asos"], required=True)
    g.add_argument("--obs", required=True)
    g.add_argument("--from", dest="a", required=True)
    g.add_argument("--to", dest="b", required=True)
    g.add_argument("--out", required=True)
    e = sub.add_parser("사상")
    e.add_argument("--list", required=True)
    e.add_argument("--src", choices=["wamis-rf", "wamis-rfd", "wamis-wl", "asos"], required=True)
    e.add_argument("--obs", required=True)
    e.add_argument("--out", required=True)
    a = ap.parse_args()

    if a.cmd == "찾기":
        name = "rf_dubrfobs" if a.kind == "rf" else "wl_dubwlobs"
        rows = wamis(name, {"basin": a.basin})
        hit = [r for r in rows if a.name in r.get("obsnm", "")]
        print("[찾기] %s 관측소 %d 개 중 '%s' %d 개" % (a.kind, len(rows), a.name, len(hit)))
        for r in hit:
            print("  %-10s %-24s %s  %s  %s" % (r.get("obscd"), r.get("obsnm"), r.get("clsyn"),
                                                 r.get("obsknd"), r.get("mngorg")))
        return 0 if hit else 1

    os.makedirs(a.out, exist_ok=True)
    일감 = ([("기간", 날짜(a.a), 날짜(a.b))] if a.cmd == "받기" else
          [(r[0], 날짜(r[1]), 날짜(r[2])) for r in
           list(csv.reader(open(a.list, encoding="utf-8-sig")))[1:] if r])
    assert 일감, "받을 기간이 없다"
    총 = 0
    for 이름, s, e_ in 일감:
        rows = 받기(a.src, a.obs, s, e_)
        결측 = sum(1 for _, v in rows if v is None)
        p = os.path.join(a.out, "%s_%s_%s.csv" % (이름, a.src, a.obs))
        쓰기(rows, p, a.src, a.obs)
        기록(a.out, [dt.datetime.now().strftime("%Y-%m-%d %H:%M"), a.src, a.obs,
                    s, e_, len(rows), 결측, os.path.basename(p)])
        vals = [v for _, v in rows if v is not None]
        요약 = ("합 %.1f" % sum(vals)) if a.src != "wamis-wl" else \
               ("최소 %.2f 최대 %.2f" % (min(vals), max(vals)) if vals else "-")
        print("[%s] %d 행 · 결측 %d · %s -> %s" % (이름, len(rows), 결측, 요약, p))
        총 += len(rows)
        time.sleep(쉼)
    assert 총 > 0, "받은 자료가 0 행이다. 관측소 코드와 기간을 본다"
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RuntimeError as e:                 # 키 없음 · 서버 오류는 안내만 하고 멈춘다
        print("[멈춤] %s" % e)
        sys.exit(1)
