r"""클로드 코드 명령 총정리의 본문(명령총정리.txt)을 조사 자료 두 개로 만든다. Word · PDF 는 02_워드.py 가 만든다.

왜 있나
  2026-09-29 사용자 요청: "다른 명령들도 엄청 많을 텐데 다 파악해서 정리", "인터넷에 명령어 정리된 사이트
  들도 확인해서 정리 분석", "나도 확인해 볼 거니까 아주 깔끔하게". 지인 zip 에도 넣는다.
  자료\cmd_official.json   공식 문서 16 쪽과 이 PC 의 claude --help 로 만든 명령 · 옵션 · 단축키 · 기호 목록
  자료\web_guides.json     인터넷 정리 자료(국내외) 조사와 공식 문서 대조
  두 자료는 서브에이전트가 만들었고, 슬래시 명령 115 개는 원작자 세션이 공식 표와 대조했다(일치).

실행
  C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe -X utf8 _동기화\설명서\03_명령총정리.py
  C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe -X utf8 _동기화\설명서\02_워드.py --본문 명령총정리.txt --이름 클로드코드_명령총정리
"""
import json
import os

여기 = os.path.dirname(os.path.abspath(__file__))
자료 = os.path.join(여기, "자료")
공식 = json.load(open(os.path.join(자료, "cmd_official.json"), encoding="utf-8"))
웹경로 = os.path.join(자료, "web_guides.json")
웹 = json.load(open(웹경로, encoding="utf-8")) if os.path.exists(웹경로) else None
결과 = os.path.join(여기, "명령총정리.txt")

분류순서 = ["대화·세션", "모델·속도", "지침·기억", "권한·안전", "상태·사용량", "원격·예약", "도구·확장", "계정·설정", "기타"]
자주 = ["/model", "/usage", "/compact", "/clear", "/resume", "/rewind", "/rename", "/plan", "/memory", "/init",
      "/btw", "/export", "/remote-control", "/effort", "/context", "/skills", "/plugin", "/mcp", "/status", "/help"]


def 칸(x):
    """Cell text: no column separator, no forbidden characters, no line breaks."""
    s = " ".join(str(x or "").split())
    return s.replace(" | ", " / ").replace("|", "/").replace("\u2014", ", ").replace("\u2212", "-").replace("~", "홈")


def 표(머리, 행들):
    줄 = ["@표", " | ".join(머리)]
    for r in 행들:
        줄.append(" | ".join(칸(c) or "-" for c in r))
    줄.append("@끝")
    return 줄


def 슬래시행(c):
    이름 = c["name"] + ((" (" + c["aliases"] + ")") if c.get("aliases") else "")
    if c.get("args"):
        이름 += " " + c["args"]
    return [이름, c["하는일"], c.get("쓰는때", ""), c["VSCode"]]


def main():
    s = 공식["slash"]
    이름표 = {c["name"]: c for c in s}
    빠짐 = [n for n in 자주 if n not in 이름표]
    assert not 빠짐, "자주 쓰는 명령이 공식 목록에 없다: %s" % 빠짐
    assert sorted({c["분류"] for c in s}) == sorted(분류순서), {c["분류"] for c in s}

    L = ["#표지 클로드 코드 명령 총정리",
         "@부제 공식 문서 기준 명령 · 단축키 · 실행 옵션 전부와 인터넷 정리 자료 분석",
         "@상자 기준 | 2026-09-29 에 공식 문서(code.claude.com/docs) 16 쪽과 이 PC 의 claude --help (2.1.283) 로 확인했습니다.",
         "슬래시 명령 %d 개, 실행 명령 · 옵션 %d 개, 단축키 %d 개, 입력 기호 %d 개." % (len(s), len(공식["cli"]), len(공식["keys"]), len(공식["symbols"])),
         "",
         "@상자 보는 법 | 처음이면 1 장(입력 기호)과 2 장(자주 쓰는 20 개)만 보면 됩니다.",
         "3 장은 모든 슬래시 명령을 분류별로, 4 장은 단축키를, 5 장은 터미널에서 쓰는 실행 명령을 모았습니다.",
         "6 장은 인터넷의 정리 자료를 공식 문서와 대조해 평가한 것입니다.",
         "",
         "@상자 VS Code 칸 | 됨: VS Code 확장 문서가 쓸 수 있다고 적은 것. 안 됨: 문서가 안 된다고 적은 것.",
         "확인 못 함: 문서에 적혀 있지 않은 것입니다. VS Code 입력창에 / 를 쳐서 목록에 보이면 쓸 수 있습니다.",
         "",
         "@작게 명령은 판(버전)마다 늘고 바뀝니다. 헷갈리면 입력창에 /help 를 치거나 공식 목록(code.claude.com/docs/en/commands)을 보세요.",
         "@쪽나눔", "", "# 1. 입력 기호", "",
         "입력창 맨 앞에 쓰는 기호에 따라 하는 일이 달라집니다.", ""]
    L += 표(["기호", "뜻", "되는 곳"], [[x["기호"], x["뜻"], x["되는곳"]] for x in 공식["symbols"]])
    L += ["", "@쪽나눔", "", "# 2. 자주 쓰는 명령 20", "",
          "처음에는 이것만 알아도 충분합니다. 쓰는 때의 예는 토목 설계 사무실 기준입니다.", ""]
    L += 표(["명령", "하는 일", "쓰는 때", "VS Code"], [슬래시행(이름표[n]) for n in 자주])
    L += ["", "@쪽나눔", "", "# 3. 슬래시 명령 전체 (%d 개, 분류별)" % len(s), "",
          "[번들 스킬] 은 Claude Code 에 함께 들어 있는 스킬, [번들 워크플로] 는 함께 들어 있는 여러 단계 작업입니다. "
          "삭제되었다고 적힌 명령은 옛 글에서 보이면 무시하세요.", ""]
    for i, 분류 in enumerate(분류순서, 1):
        묶음 = sorted((c for c in s if c["분류"] == 분류), key=lambda c: c["name"])
        L += ["## 3-%d. %s (%d 개)" % (i, 분류, len(묶음)), ""]
        L += 표(["명령", "하는 일", "쓰는 때", "VS Code"], [슬래시행(c) for c in 묶음])
        L.append("")
    L += ["@쪽나눔", "", "# 4. 단축키", ""]
    for i, 곳 in enumerate(["VS Code 확장", "터미널 CLI", "데스크톱 앱"], 1):
        묶음 = [k for k in 공식["keys"] if k["곳"] == 곳]
        assert 묶음, 곳
        L += ["## 4-%d. %s (%d 개)" % (i, 곳, len(묶음)), ""]
        L += 표(["키", "하는 일"], [[k["키"], k["하는일"]] for k in 묶음])
        L.append("")
    L += ["@작게 데스크톱 앱 단축키는 문서의 Mac 키(Cmd)를 Windows 키(Ctrl)로 옮긴 것이라 앱에서 한 번 확인하세요.",
          "@쪽나눔", "", "# 5. 터미널 실행 명령과 옵션 (%d 개)" % len(공식["cli"]), "",
          "VS Code 창만 쓰면 몰라도 됩니다. 터미널(Ctrl+`)에서 claude 로 시작하는 명령을 칠 때 씁니다. "
          "터미널에서 쓰려면 Claude Code 명령줄을 따로 설치해야 합니다.", ""]
    L += 표(["명령 · 옵션", "하는 일", "예"], [[c["syntax"], c["하는일"], c.get("예", "")] for c in 공식["cli"]])
    L.append("")
    if 웹:
        L += 웹부분(웹)
    L += ["@쪽나눔", "", "# 7. 확인하지 못한 것", "",
          "아래는 공식 문서와 이 PC 에서 확인하지 못한 것입니다. 추측으로 채우지 않았습니다.", ""]
    for k, x in enumerate(공식["unverified"], 1):
        L.append("%d. %s" % (k, 칸(x if isinstance(x, str) else json.dumps(x, ensure_ascii=False))))
    if 웹 and 웹.get("unverified"):
        for x in 웹["unverified"]:
            k += 1
            L.append("%d. %s" % (k, 칸(x if isinstance(x, str) else json.dumps(x, ensure_ascii=False))))
    글 = "\n".join(L) + "\n"
    for c in ("\u2014", "\u2212", "~"):
        assert c not in 글, "금지 문자 %r" % c
    open(결과, "w", encoding="utf-8", newline="\n").write(글)
    print("만듦 %s (%d 줄, 웹 자료 %s)" % (결과, len(L), "있음" if 웹 else "없음"))


def 웹부분(w):
    L = ["@쪽나눔", "", "# 6. 인터넷 정리 자료 분석", "",
         "국내외 정리 글 %d 개를 열어 보고, 권하는 명령과 요령을 공식 문서와 대조했습니다. "
         "남의 글은 옛 판 기준인 경우가 많으니 공식 문서와 다르면 공식 문서를 따르세요." % len(w["sources"]), ""]
    순 = {"상": 0, "중": 1, "하": 2}
    src = sorted(w["sources"], key=lambda x: (순.get(x["rating"][:1], 3), x["lang"] != "ko", x["id"]))
    이름 = {x["id"]: "%s %s" % (x["id"], x["title"]) for x in w["sources"]}
    assert len(src) >= 10, "자료가 너무 적다: %d" % len(src)
    L += ["자료 번호의 K 는 한국어, E 는 영어 자료입니다. 추천도는 상 · 중 · 하입니다.", "",
          "## 6-1. 자료 목록과 평가", ""]
    L += 표(["자료", "무엇이 들어 있나", "좋은 점 / 주의", "추천"],
           [["%s %s (%s, %s) %s" % (x["id"], x["title"], x["operator"], x["date"][:30], x["url"]),
             x["contents"], "좋음: %s  주의: %s" % (x["strengths"], x["limits"]),
             "%s. %s" % (x["rating"], x["rating_reason"])] for x in src])
    L += ["", "## 6-2. 여러 자료가 공통으로 권하는 것 (%d 개)" % len(w["practices"]), ""]
    L += 표(["권하는 것", "말한 자료", "공식 문서"],
           [[p["practice"], ", ".join(p["sources"]), p["official"]] for p in sorted(w["practices"], key=lambda p: p["rank"])])
    L += ["", "## 6-3. 잘못 알려졌거나 옛날 정보 (%d 개)" % len(w["misconceptions"]), ""]
    L += 표(["퍼진 말", "나온 곳", "지금 공식 문서"],
           [[m["claim"], ", ".join(m["where"]), m["fact"]] for m in w["misconceptions"]])
    L += ["", "## 6-4. 남이 만든 명령 · 스킬 · 훅을 들일 때 (%d 개)" % len(w["cautions"]), ""]
    L += 표(["점검", "무엇을 보나", "근거"],
           [[c["item"], c["detail"], ", ".join(c["sources"])] for c in w["cautions"]])
    팁 = [(x["id"], t) for x in src for t in x["tips"]]
    L += ["", "## 6-5. 자료별 요령과 공식 대조 (%d 개)" % len(팁), "",
          "일치: 지금 공식 문서와 맞음. 옛 정보: 예전엔 맞았으나 지금은 다름. 공식 문서에 없음: 공식에서 찾지 못함.", ""]
    L += 표(["자료", "요령", "공식 대조"],
           [[i, t["tip"], (t["check"] + (" (" + t["note"] + ")" if t.get("note") else ""))] for i, t in 팁])
    L.append("")
    return L


if __name__ == "__main__":
    main()
