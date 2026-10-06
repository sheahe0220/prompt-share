r"""오늘 작업 폴더를 만든다. 04_날짜작업.md 의 규칙을 도구로 옮긴 것이다.

무엇을 왜 만들었나
  그날 한 일이 주제 폴더 여기저기에 서로 다른 이름과 날짜 형식으로 흩어져,
  오늘 무엇을 했는지 찾으려면 다섯 곳을 뒤져야 했다(FABLE, 2026-09-21).
  날짜 폴더와 작업 폴더의 이름을 사람이 매번 짓지 않게 도구가 만든다.

만드는 것
  <root>\_작업\00_색인.md                    없으면 만들고, 오늘 줄이 없으면 넣는다
  <root>\_작업\YYYYMMDD\00_일지.md            없으면 틀로 만든다
  --작업 이름 을 주면
  <root>\_작업\YYYYMMDD\HHMM_이름\00_실행.md
                                 \그림\00_그림목록.md
                                 \결과\

지키는 것
  이미 있는 파일은 절대 덮어쓰지 않는다. 같은 날 여러 번 돌려도 안전하다
  root 는 과업 폴더여야 한다. 과업_산출 이 없으면 확인을 요구하고 멈춘다

실행
  C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe -X utf8 today.py --root <과업 폴더>
  ... --작업 648검토
  ... --날짜 2026-09-21      다른 날짜로 (지난 작업을 정리할 때)
  ... --그래도              과업_산출 이 없는 폴더에서도 만든다
"""
import argparse
import datetime as dt
import os
import re
import sys

일지틀 = """# {날짜} 일지

## 오늘의 목표


## 한 일


## 안 된 것
(무엇이 실패했고 실패인 줄 어떻게 알았나. 없으면 "없음")

## 과업_산출 로 올린 것
(무엇을 어디로. 없으면 "없음")

## 내일

"""

색인머리 = """# 작업 색인

하루에 한 줄. 04_날짜작업.md 를 본다.

| 날짜 | 한 줄 | 주요 작업 폴더 | 올린 것 |
|---|---|---|---|
"""

실행틀 = """# {이름}

시작 {날짜} {시각}

## 무엇을 왜


## 입력
(절대경로)

## 돌린 명령
```text

```

## 결과
(결과\\ 와 그림\\ 의 파일, 핵심 수치)
"""

그림목록틀 = """# 그림 목록 · {이름}

그림마다 무엇을 보라는 한 줄.

| 파일 | 무엇을 보나 |
|---|---|
"""


def 쓰기(path, text, 만든것):
    if os.path.exists(path):
        return
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    만든것.append(path)


def 이름다듬기(s):
    s = re.sub(r"[\\/:*?\"<>|\s]+", "_", s.strip())
    return s.strip("_")[:40]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.getcwd())
    ap.add_argument("--작업")
    ap.add_argument("--날짜", help="YYYY-MM-DD. 없으면 오늘")
    ap.add_argument("--그래도", action="store_true")
    a = ap.parse_args()

    root = os.path.abspath(a.root)
    assert os.path.isdir(root), "root 가 없다: %s" % root
    if not a.그래도 and not os.path.isdir(os.path.join(root, "과업_산출")) \
            and not os.path.isdir(os.path.join(root, "_작업")):
        print("[멈춤] %s 에 과업_산출 도 _작업 도 없다. 과업 폴더가 맞나?" % root)
        print("       맞으면 --그래도 를 붙인다")
        return 1

    now = dt.datetime.now()
    d = dt.datetime.strptime(a.날짜, "%Y-%m-%d") if a.날짜 else now
    날짜 = d.strftime("%Y-%m-%d")
    작업뿌리 = os.path.join(root, "_작업")
    오늘 = os.path.join(작업뿌리, d.strftime("%Y%m%d"))
    os.makedirs(오늘, exist_ok=True)
    만든것 = []

    쓰기(os.path.join(오늘, "00_일지.md"), 일지틀.format(날짜=날짜), 만든것)

    색인 = os.path.join(작업뿌리, "00_색인.md")
    쓰기(색인, 색인머리, 만든것)
    t = open(색인, encoding="utf-8").read()
    if ("| %s |" % 날짜) not in t:
        # 날짜 줄을 넣고 날짜 순으로 다시 세운다. 다른 줄과 채워 둔 내용은 그대로다
        # 첫 표(머리 구분선 바로 뒤의 날짜 줄들) 안에서만 정렬한다. 표 밖의 절은 건드리지 않는다
        lines = t.rstrip("\n").split("\n")
        날짜줄 = re.compile(r"^\| \d{4}-\d{2}-\d{2} \|")
        s = next(i for i, l in enumerate(lines) if l.startswith("|---")) + 1
        e = s
        while e < len(lines) and 날짜줄.match(lines[e]):
            e += 1
        행 = sorted(lines[s:e] + ["| %s |  |  |  |" % 날짜])
        with open(색인, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines[:s] + 행 + lines[e:]) + "\n")
        만든것.append(색인 + "  (%s 줄)" % 날짜)

    작업폴더 = None
    if a.작업:
        이름 = 이름다듬기(a.작업)
        assert 이름, "작업 이름이 비었다"
        있는 = [n for n in os.listdir(오늘) if re.match(r"^\d{4}_" + re.escape(이름) + "$", n)]
        작업폴더 = os.path.join(오늘, 있는[0] if 있는 else "%s_%s" % (now.strftime("%H%M"), 이름))
        for sub in ("그림", "결과"):
            os.makedirs(os.path.join(작업폴더, sub), exist_ok=True)
        쓰기(os.path.join(작업폴더, "00_실행.md"),
             실행틀.format(이름=이름, 날짜=날짜, 시각=now.strftime("%H:%M")), 만든것)
        쓰기(os.path.join(작업폴더, "그림", "00_그림목록.md"),
             그림목록틀.format(이름=이름), 만든것)

    print("[오늘] %s" % 오늘)
    if 작업폴더:
        print("[작업] %s" % 작업폴더)
    print("[새로 만든 것] %d 개" % len(만든것))
    for p in 만든것:
        print("   ", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
