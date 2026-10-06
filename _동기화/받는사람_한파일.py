r"""지인에게 파일 하나만 주면 되는 설치 문서(시작하기.md)를 만든다.

왜 있나
  폴더를 통째로 받는 것보다, md 파일 하나를 클로드에게 주고 "이대로 해줘" 하는 편이 쉽다.
  그래서 전역 지침 원문을 파일 안에 그대로 넣고, 앞에 사람이 할 일(링크 포함)과 클로드가
  할 일을 나눠 적는다. 원작자 PC 에 깔린 플러그인 · 확장 · MCP 목록도 함께 싣는다.
  목록은 손으로 적으면 어긋나므로 만들 때마다 이 PC 에서 읽어 넣는다.

지침 본문에 ``` 코드 블록이 있어 문서를 코드 블록으로 감쌀 수 없다. 경계 표시(<<<...>>>)로
감싸고 클로드에게 그 사이를 그대로 옮기라고 지시한다.

실행
  C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe -X utf8 _동기화\받는사람_한파일.py
  --빠르게   환경 목록을 다시 읽지 않고 직전에 저장해 둔 것을 쓴다
결과
  _동기화\recipient\시작하기.md   (묶기 스크립트가 사본 맨 위에도 넣는다)
  _동기화\recipient\환경목록.json  (마지막으로 읽은 목록)
"""
import json
import os
import re
import subprocess
import sys

여기 = os.path.dirname(os.path.abspath(__file__))
뿌리 = os.path.dirname(여기)
받는사람 = os.path.join(여기, "recipient")
머리말 = os.path.join(받는사람, "recipient_preface.md")
규칙 = os.path.join(뿌리, "_전역", "CLAUDE.md")
결과 = os.path.join(받는사람, "시작하기.md")
환경파일 = os.path.join(받는사람, "환경목록.json")

작성자뿌리 = r"C:\Users\SGJEONG99\Desktop\Prompt"
작성자파이썬 = r"C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe"
작성자집 = r"C:\Users\SGJEONG99"

시작표시 = "<<<지침시작>>>"
끝표시 = "<<<지침끝>>>"

# 지인(토목 설계 실무)에게 실제로 쓸모가 있을 것만 고른다. 나머지는 목록으로만 싣는다
권장확장 = {
    "ms-ceintl.vscode-language-pack-ko": "VS Code 한국어",
    "mjyoo2.hwpx-editor": "한글 hwpx 보기 · 편집",
    "edwardkim.rhwp-vscode": "한글 hwp 보기",
    "shahilkumar.docxreader": "Word docx 보기",
    "tomoki1207.pdf": "PDF 보기",
    "mechatroner.rainbow-csv": "CSV 를 색으로 구분",
    "davidanson.vscode-markdownlint": "마크다운 점검",
    "vscode-icons-team.vscode-icons": "파일 아이콘",
    "eamodio.gitlens": "git 이력 보기",
    "mhutchie.git-graph": "git 그래프",
    "ms-python.python": "Python (Python 을 깔았을 때)",
    "ms-toolsai.jupyter": "Jupyter 노트북 (선택)",
}
권장플러그인 = {
    "claude-code-setup": "설정 도우미",
    "claude-md-management": "지침(CLAUDE.md) 관리",
    "context7": "라이브러리 공식 문서 조회",
    "pdf-viewer": "PDF 읽기",
}


def 실행(명령, 초=180):
    try:
        r = subprocess.run(명령, capture_output=True, text=True, encoding="utf-8",
                           errors="ignore", timeout=초, shell=True)
        return r.stdout or ""
    except Exception as ex:
        print("  [건너뜀] %s (%s)" % (명령, type(ex).__name__))
        return ""


def 환경읽기():
    print("이 PC 의 구성을 읽는다(플러그인 · 확장 · MCP)")
    플러그인 = []
    t = 실행("claude plugin list")
    이름 = None
    for 줄 in t.splitlines():
        m = re.match(r"\s*❯\s*(\S+)", 줄)
        if m:
            이름 = m.group(1)
        elif 이름 and "Status:" in 줄:
            상태 = "켜짐" if "enabled" in 줄 or "loaded" in 줄 else "꺼짐"
            플러그인.append([이름, 상태])
            이름 = None
    장터 = re.findall(r"❯\s*(\S+)\n\s*Source:\s*(.+)", 실행("claude plugin marketplace list"))
    확장 = [x for x in 실행("code --list-extensions --show-versions").splitlines() if "@" in x]
    mcp = []
    for 줄 in 실행("claude mcp list", 300).splitlines():
        m = re.match(r"([^:]+):\s*(\S+)\s*(?:\((\w+)\))?\s*-\s*(.+)", 줄.strip())
        if m and not 줄.startswith("Checking"):
            mcp.append([m.group(1).strip(), m.group(2), m.group(4).strip()])
    환경 = {"플러그인": 플러그인, "장터": 장터, "확장": 확장, "mcp": mcp}
    for k, v in 환경.items():
        print("  %s %d 개" % (k, len(v)))
    return 환경


def 환경(다시읽기=True):
    if 다시읽기:
        새것 = 환경읽기()
        if all(새것.values()):
            json.dump(새것, open(환경파일, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            return 새것
        print("  일부를 읽지 못했다. 저장해 둔 목록을 쓴다")
    assert os.path.exists(환경파일), "환경목록.json 이 없다. 다시 읽어야 한다"
    return json.load(open(환경파일, encoding="utf-8"))


def 표(항목들):
    return "\n".join("    " + x for x in 항목들)



도구설명파일 = os.path.join(받는사람, "도구설명.json")
도구목록파일 = os.path.join(받는사람, "도구목록.md")
등급순서 = ["기본", "물어봄", "권하지않음"]
종류순서 = ["확장", "플러그인", "장터", "MCP"]


def 도구읽기(env):
    """Every extension / plugin / marketplace / MCP on the author's PC must have a description.
    Stops when one is missing, so a newly installed tool is never shipped without one."""
    목록 = json.load(open(도구설명파일, encoding="utf-8"))
    ids = {d["id"] for d in 목록}
    assert len(ids) == len(목록), "도구설명.json 에 같은 id 가 둘 있다"
    필요 = [x.split("@")[0] for x in env["확장"]] + [n for n, _ in env["플러그인"]] + [n for n, _ in env["장터"]]
    빠짐 = [x for x in 필요 if x not in ids]
    assert not 빠짐, "도구설명.json 에 설명이 없다(새로 깐 것?): %s" % 빠짐
    n_mcp = sum(1 for d in 목록 if d["종류"] == "MCP")
    assert n_mcp >= len(env["mcp"]), "MCP 설명 %d 개 < 목록 %d 개" % (n_mcp, len(env["mcp"]))
    for d in 목록:
        assert d["등급"] in 등급순서 and d["종류"] in 종류순서, d["id"]
        for k in ("이름", "무엇", "비유", "설치"):
            assert d.get(k, "").strip(), "%s 의 %s 가 비었다" % (d["id"], k)
    return 목록


def 도구그리기(목록):
    """(기본 묶음 block, full catalog text). The catalog also goes to 도구목록.md."""
    기본 = []
    for 종류 in 종류순서:
        for d in (x for x in 목록 if x["종류"] == 종류 and x["등급"] == "기본"):
            기본.append("    [%s] %s  (%s)" % (종류, d["이름"], d["무엇"]))
            기본.append("        %s" % d["설치"])
    assert 기본, "기본 등급 도구가 0 개다"
    줄 = []
    for 등급 in 등급순서:
        묶음 = [x for x in 목록 if x["등급"] == 등급]
        줄.append("### %s (%d 개)%s" % (등급, len(묶음), "  2-4 에서 깔았다" if 등급 == "기본" else ""))
        줄.append("")
        for 종류 in 종류순서:
            for d in (x for x in 묶음 if x["종류"] == 종류):
                줄.append("    [%s] %s   %s" % (종류, d["이름"], d["id"]))
                줄.append("        무엇  %s" % d["무엇"])
                줄.append("        예    %s" % d["비유"])
                if d.get("조건"):
                    줄.append("        조건  %s" % d["조건"])
                줄.append("        설치  %s" % d["설치"])
                줄.append("")
    본문 = "\n".join(줄).rstrip()
    with open(도구목록파일, "w", encoding="utf-8", newline="\n") as f:
        f.write("<!-- 점검예외: _동기화\\받는사람_한파일.py 가 도구설명.json 으로 만든다. 직접 고치지 않는다. -->\n"
                "# 도구 목록 (원작자 PC 에 깔린 것 전부)\n\n"
                "클로드가 이 PC 사용자의 일에 빗대어 하나씩 묻는 데 쓴다. 쓰는 법은 시작하기.md 3 부.\n\n"
                + 본문 + "\n")
    return "\n".join(기본), 본문


def 안내글(env):
    플러그인 = env["플러그인"]
    확장 = env["확장"]
    확장이름 = [x.split("@")[0] for x in 확장]
    켜진플러그인 = [n for n, s in 플러그인 if s == "켜짐"]
    권장확장목록 = [("code --install-extension %-42s # %s" % (k, v))
                for k, v in 권장확장.items() if k in 확장이름]
    나머지확장 = sorted(x for x in 확장이름 if x not in 권장확장)
    mcp켜짐 = [f"{n:<45} {s}" for n, _, s in env["mcp"] if "Connected" in s]
    mcp인증 = [n for n, _, s in env["mcp"] if "authentication" in s or "Failed" in s]

    기본묶음, 도구목록 = 도구그리기(도구읽기(env))
    블록1 = 표([
 "$env:USERPROFILE                                사용자 폴더",
 "where.exe claude                                Claude Code",
 "where.exe code                                  VS Code",
 "where.exe git                                   Git",
 "where.exe python ; py -0p                       Python (WindowsApps 안의 것은 스토어 바로가기다)",
 "winget --version                                winget",
 "New-Object -ComObject PowerPoint.Application    MS Office (되면 바로 .Quit())",
 "New-Object -ComObject HWPFrame.HwpObject        한글 (되면 바로 .Quit())",
])
    블록2 = 표([
 "꼭 필요      없음. 2-3 의 전역 지침만 있어도 모든 새 대화에 규칙이 걸린다",
 "필요         Git (새 지침 자동 받기, Bash 도구)",
 "선택         VS Code + Claude Code 확장 (원작자와 같은 환경)",
 "선택         Python (점검 도구 · 그림 · 문서 자동화에 필요)",
 "권하지 않음   MS Office · 한글은 유료다. 없으면 그 자동화만 못 쓴다고 알린다",
])
    블록3 = 표([
 "Claude Code   winget install -e --id Anthropic.ClaudeCode",
 "VS Code       winget install -e --id Microsoft.VisualStudioCode",
 "확장          code --install-extension anthropic.claude-code",
 "              (VS Code 를 방금 깔아 code 를 못 찾으면 전체 경로로 부른다. VS Code 를 켤 필요는 없다)",
 "              & \"$env:LOCALAPPDATA\\Programs\\Microsoft VS Code\\bin\\code.cmd\" --install-extension <이름>",
 "Git           winget install -e --id Git.Git",
 "Python        winget install -e --id Python.Python.3.12 --scope user",
])
    블록4 = 표(["claude --version    claude doctor", "code --version      git --version      py --version"])
    블록5 = 표([", ".join(나머지확장[i:i + 4]) for i in range(0, len(나머지확장), 4)])
    블록6 = 표([
 "claude plugin marketplace add anthropics/claude-plugins-official",
 "claude plugin install <이름>@claude-plugins-official",
 "목록 보기   claude plugin list          장터 보기   claude plugin marketplace list",
])
    블록7 = 표(["claude plugin install %-24s # %s" % (k, v) for k, v in 권장플러그인.items()])
    블록8 = 표([", ".join(켜진플러그인[i:i + 3]) for i in range(0, len(켜진플러그인), 3)])
    블록9 = 표(["%-26s %s" % (n, s) for n, s in env["장터"]])
    블록10 = 표([
 "Claude 앱      https://claude.com/download",
 "Claude Code    https://code.claude.com/docs/en/setup",
 "VS Code        https://code.visualstudio.com/download",
 "VS Code 확장   https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code",
 "Git            https://git-scm.com/download/win",
 "Python         https://www.python.org/downloads/windows/   (설치 때 Add python.exe to PATH 체크)",
 "winget 없으면  https://aka.ms/getwinget  (또는 Microsoft Store 에서 App Installer)",
 "앱 사용법      https://code.claude.com/docs/en/desktop-quickstart",
 "VS Code 사용법 https://code.claude.com/docs/en/vs-code",
])
    블록11 = 표([
 "winget 이 없다         Microsoft Store 에서 App Installer 를 깔거나 4 부 링크로 받는다",
 "PowerShell 이 막는다   powershell -NoProfile -ExecutionPolicy Bypass -File <파일> 로 실행한다",
 "설치했는데 명령이 없다  새 PowerShell 창을 연다. 경로는 새 창부터 적용된다",
 "로그인 창이 안 뜬다     화면의 주소를 복사해 브라우저에 붙여 넣고, 받은 코드를 터미널에 붙인다",
 "회사 PC 라 설치가 막힌다 관리자에게 요청한다. 설치 없이도 2-3 의 전역 지침만으로 쓸 수 있다",
 "지침이 안 먹는 것 같다  새 대화를 연다. 열려 있던 대화에는 적용되지 않는다",
 "되돌리고 싶다          %USERPROFILE%\\.claude\\CLAUDE.md.bak.<시각> 을 CLAUDE.md 로 되돌린다",
])

    return f"""<!-- 점검예외: 이 문서는 표기 규칙(금지 문자 예시)을 그대로 싣고 있다. -->
# 클로드 작업 지침 설치 안내 (이 파일 하나면 된다)

이 파일 하나를 클로드에게 주고 **"이 파일대로 해줘"** 라고 쓰면 된다. 나머지는 클로드가 한다.
아래 1 부(사람이 하는 것)만 직접 하고, 2 부부터는 읽지 않아도 된다.

---

# 0 부. AI 를 처음 써 본다면 (2 분만 읽으면 된다)

**클로드 코드가 무엇인가.** 사람 대신 컴퓨터 일을 해 주는 프로그램이다. 채팅처럼 한국어로
시키면 된다. 다른 챗봇과 다른 점은 **내 컴퓨터의 파일을 직접 읽고 고칠 수 있다**는 것이다.
예를 들면 이런 일을 시킬 수 있다.

    엑셀에 흩어진 수량을 정리해서 한글 보고서 표로 만들어줘
    이 폴더 보고서에서 숫자가 본문과 표가 다른 곳을 찾아줘
    작년 과업 보고서 양식 그대로, 올해 자료로 초안을 만들어줘
    이 PDF 과업지시서에서 우리가 내야 할 산출물 목록만 뽑아줘
    발표자료 20 장을 만들고 글이 넘치는 쪽이 없는지 확인해줘

**폴더를 고르는 이유.** 클로드는 고른 폴더 안만 본다. 그 바깥 파일은 건드리지 않는다.
과업 폴더를 고르면 그 과업만, 이 설치 파일이 있는 폴더를 고르면 그것만 본다.

**"허용" 이 무슨 뜻인가.** 클로드가 파일을 고치거나 프로그램을 실행하기 전에 물어본다.
내용을 보고 허용을 누르면 실행한다. 이상하면 거절하면 된다. 처음에는 하나씩 확인하는 편이
좋다.

**못 하는 것도 있다.** AutoCAD 로 도면을 직접 그리거나, 설치된 구조해석 프로그램을 대신
조작하지는 못한다. 대신 그 프로그램이 뱉은 결과 파일(엑셀 · 텍스트 · PDF)을 정리하고
계산 · 표 · 보고서로 만드는 일은 잘한다.

**조심할 것.** 발주처 자료나 미공개 자료를 아무 데나 올리지 않는다. 클로드에게 시킨 일은
Anthropic 서버를 거친다. 회사 규정이 있으면 먼저 확인한다. 이 지침에도 "과업 자료를 공개
URL 에 올리지 않는다" 는 규칙이 들어 있다.

**지침(이 파일)이 왜 필요한가.** 매번 "말투는 이렇게, 보고서는 이렇게, 숫자는 출처를 적고"
를 설명하지 않아도 되게, 미리 규칙을 적어 두는 것이다. 한 번 설치하면 앞으로 여는 모든
대화에 자동으로 걸린다.

---

# 1 부. 사람이 직접 하는 것 (약 10 분)

## 1-1. Claude 계정과 요금제

Claude Code 는 유료 요금제(Pro · Max · Team · Enterprise) 또는 Claude Console 계정이 있어야
쓸 수 있다. 계정이 없으면 먼저 만든다.

    가입 · 로그인    https://claude.ai
    요금제           https://claude.com/pricing

## 1-2. Claude 데스크톱 앱을 깐다 (앱 하나만 깔면 된다)

    받는 곳    https://claude.com/download   (claude.ai/download 도 같은 곳으로 간다)
    설치       받은 파일을 두 번 눌러 설치한다. 다른 앱 깔 때와 같다
    로그인     앱을 켜고 1-1 의 계정으로 로그인한다
    확인       왼쪽 위에 "Code" 단추가 보이면 된다

VS Code · 한국어 메뉴 · 한글 보기 · Git · Python 은 직접 깔지 않는다. 1-4 를 하면 클로드가
하나씩 무엇인지 설명하고, 깔지 물어본 뒤 대신 깔아 준다. "예" 나 "아니오" 만 고르면 된다.

## 1-3. 이 파일을 PC 에 저장

**문서** 폴더 안에 `클로드` 라는 새 폴더를 만들고(빈 곳에서 오른쪽 단추 > 새로 만들기 > 폴더),
카톡 등으로 받은 이 파일(`시작하기.md`)을 거기에 저장한다. 문서 폴더에 바로 두지 않는 까닭은
클로드가 고른 폴더 안의 파일을 전부 볼 수 있어서다. 이 새 폴더에는 이 파일만 둔다.

## 1-4. 클로드에게 시키기

1. 앱 왼쪽 위의 **Code** 를 누른다.
2. 입력창 위에서 **로컬** 을 고른다.
3. **폴더** 를 눌러 1-3 에서 만든 `문서\클로드` 폴더를 고른다.
4. 입력창에 아래 한 줄을 쓰고 Enter 를 누른다.

    이 파일대로 해줘

명령을 실행해도 되는지 묻는 창이 뜨면 **허용** 을 누른다. 그 뒤로는 클로드가 점검 · 설치 ·
질문을 알아서 한다. 모르는 말이 나오면 입력창에 "쉽게 다시 설명해줘" 라고 쓰면 된다.

이미 VS Code 를 쓰고 있다면 앱 대신 VS Code 에서 해도 된다. Ctrl+Shift+X 로 확장 창을 열어
"Claude Code"(Anthropic) 를 설치하고, **파일 > 폴더 열기** 로 이 파일이 있는 폴더를 연 뒤 이 파일을
눌러 연다. 편집 창 오른쪽 위의 불꽃 모양(Spark) 아이콘을 누르고 **Sign in** 으로 로그인한 뒤
같은 문장을 쓴다.

터미널을 쓰는 경우에는 PowerShell 에서 아래를 먼저 실행해 Claude Code 를 깔고, 이 파일이 있는
폴더에서 `claude` 를 실행한 뒤 같은 문장을 쓴다.

    winget install -e --id Anthropic.ClaudeCode
    (winget 이 없으면)  irm https://claude.ai/install.ps1 | iex

---

# 2 부. 클로드가 하는 것 (사람은 읽지 않아도 된다)

이 파일을 읽은 시점부터 너는 설치를 돕는 역할이다. 사용자는 컴퓨터 설정에 익숙하지 않을 수
있다. 쉬운 말로 짧게 말하고 단계마다 한 줄로 알린다. **프로그램 설치는 반드시 사용자 동의를
받고 한다.** 관리자 권한이 필요하면 멈추고 알린다.

## 2-0. 이미 있는 것부터 본다 (있는 것은 건너뛴다)

**이 PC 는 일부가 미리 깔려 있을 수 있다.** 원작자가 넘겨주기 전에 VS Code, 확장, Git,
Python, 플러그인 등을 먼저 깔아 두기도 했다(완벽하지는 않다). 그래서 무엇이든 깔기 전에 이
PC 에 이미 있는 것을 먼저 조사하고, **이미 있는 것은 다시 깔거나 덮어쓰지 않고 건너뛴다.**
빠진 것만 채운다. 판이 낮아 문제가 되는 것만 사용자에게 알리고 갱신할지 묻는다.

    지침          %USERPROFILE%\\.claude\\CLAUDE.md 첫 줄이 "# 이 PC 에서 이 지침을 쓰는 법" 이면 설치됨
    자동 갱신      C:\\claude-prompt\\update.ps1 과 settings.json SessionStart 의 prompt-share-update
    프로그램       2-1 의 표 (Claude Code 명령줄, VS Code, Git, Python, winget, Office, 한글)
    확장          code --list-extensions   (code 를 못 찾으면 2-4 의 전체 경로로)
    플러그인 · 장터 claude plugin list ; claude plugin marketplace list
    Python 패키지  py -m pip list   (requirements.txt 와 대조)
    연결(MCP)     claude mcp list

조사 결과를 **"이미 있음 / 새로 깔 것 / 판 확인 필요"** 세 칸 표로 보여 주고, 새로 깔 것만
진행한다. 2-3 에서 2-4 까지 각 단계도 같은 원칙이다: 있으면 "이미 있어 건너뜀" 으로 한 줄
적고 넘어간다. 지침과 자동 갱신이 둘 다 이미 있으면 다시 설치하길 원하는지 묻고, 원하지
않으면 2-5(면담)부터 한다. 이미 있던 `CLAUDE.md` 가 이 지침이 아닌 다른 내용이면 지우지 말고
`.bak.<날짜시각>` 으로 백업한 뒤 설치하고, 그 안에 사용자 메모가 있었으면 새 `## 이 PC 메모` 로
옮겨 적는다.

**PC 를 두 대 쓰는 사람이면** 두 PC 에서 각각 이 파일대로 설치한다. "이 PC 메모" 는 PC 마다
따로 저장되므로, 다른 PC 에서 이미 면담(2-5)을 했다면 "다른 PC 의 이 PC 메모를 붙여 넣어
주시면 면담을 줄이겠습니다" 라고 안내한다. 사용자가 그 PC 의 `%USERPROFILE%\\.claude\\CLAUDE.md`
맨 끝 `## 이 PC 메모` 절을 복사해 붙여 주면 그대로 옮겨 적고, 이 PC 에서 다른 점(깔린
프로그램, 과업 폴더 위치)만 묻는다.

## 2-1. 이 PC 를 점검해 표로 보여 준다 (PowerShell)

{블록1}

## 2-2. 무엇이 필요한지 설명하고 동의를 받는다

{블록2}

## 2-3. 지침을 설치하고 자동 갱신을 건다 (핵심)

원작자는 지침을 자주 고친다. 그래서 파일 하나로 끝내지 않고, 원작자의 공개 저장소
(https://github.com/sheahe0220/prompt-share, 지침만 들어 있다)를 이 PC 에 받아 두고, 클로드를
열 때마다 새 판을 받아 다시 설치하게 한다. 사용자에게 "원작자가 지침을 고치면 이 PC 에도
자동으로 들어옵니다. 이 PC 의 파일이나 대화는 어디에도 올라가지 않습니다" 라고 설명하고
동의를 받는다.

1. **Git 이 없으면 깐다.** 저장소를 받는 데 꼭 필요하다. 동의를 받고
   `winget install -e --id Git.Git` 을 실행한다. 설치 뒤 새 PowerShell 창에서 `git --version` 을
   본다. GitHub 가입이나 로그인은 필요 없다(공개 저장소라 받기만 한다).
2. **저장소를 받는다.** 자리는 `C:\\claude-prompt` 로 한다. 사용자 이름이 한글이어도 훅 명령이
   깨지지 않게 영문 경로를 쓴다. 이미 있으면 받지 않고 3 으로 간다.

       git clone https://github.com/sheahe0220/prompt-share.git C:\\claude-prompt

3. **설치하고 훅을 건다.** 먼저 확인 모드를 보여 준 뒤 실행한다.

       powershell -NoProfile -ExecutionPolicy Bypass -File C:\\claude-prompt\\_동기화\\recipient\\install.ps1 -Check
       powershell -NoProfile -ExecutionPolicy Bypass -File C:\\claude-prompt\\update.ps1 -Install

   두 번째 줄이 전역 지침(`%USERPROFILE%\\.claude\\CLAUDE.md`)과 스킬 9 개를 설치하고(기존 것은
   백업), `%USERPROFILE%\\.claude\\settings.json` 의 SessionStart 에 자동 갱신 훅을 넣는다. 끝에
   `hook added` 가 나와야 한다. settings.json 을 다시 읽어 JSON 이 깨지지 않았는지 확인한다.
4. **Git 설치나 받기가 끝내 안 되면** 자동 갱신 없이 이 파일만으로 설치한다.
   - `%USERPROFILE%\\.claude` 폴더가 없으면 만들고, `CLAUDE.md` 가 이미 있으면
     `CLAUDE.md.bak.<날짜시각>` 으로 복사한다. 지우지 않는다.
   - 이 문서 끝의 `{시작표시}` 와 `{끝표시}` 사이 글을 **그대로** `%USERPROFILE%\\.claude\\CLAUDE.md`
     에 UTF-8 로 쓴다. 표시줄 자체는 넣지 않는다.
   - 쓰기 전에 `{{{{PYTHON}}}}` 은 2-1 에서 찾은 Python 경로(없으면 `python`)로,
     `{{{{원본폴더}}}}` 는 `(없음. 이 파일 하나로 설치했다)` 로 채운다.
   - 맨 끝에 `## 이 PC 메모` 절이 없으면 만든다(내용은 "아직 없음.").
   - 사용자에게 "나중에 Git 을 깔면 자동 갱신을 걸 수 있다" 고 알린다.

## 2-4. 기본 묶음을 한 번에 깐다

2-3 을 마쳤으면 누구에게나 쓸모 있는 **기본 묶음을 한 번에** 권한다. 하나씩 묻지 않는다.
무엇인지 쉬운 말로 한 번에 설명하고("한글 · PDF · 워드 파일을 VS Code 안에서 바로 열어 보고,
엑셀 계산서를 제가 직접 읽고 고칠 수 있게 하는 기본 도구들입니다. 모두 무료이고 10-20 분쯤
걸립니다. 한 번에 깔까요?"), **한 번 동의를 받은 뒤 차례로 깐다.** 사용자가 빼 달라는 것만
뺀다. 관리자 권한이 필요하면 멈추고 알린다. **2-0 에서 이미 있다고 나온 것은 건너뛴다**
(설명할 때도 "이미 깔려 있는 것 n 개는 건너뛰고, 빠진 m 개만 깝니다" 라고 말한다).

프로그램

    Claude Code 명령줄   winget install -e --id Anthropic.ClaudeCode     플러그인을 깔고 관리하는 데 쓴다
    VS Code              winget install -e --id Microsoft.VisualStudioCode
    Python               winget install -e --id Python.Python.3.12 --scope user
    Python 패키지         (새 창에서) py -m pip install -r C:\\claude-prompt\\_동기화\\recipient\\requirements.txt
                         엑셀 · 워드 · 발표자료 · PDF 를 읽고 만들고, 표를 계산하고 그래프를 그리는 도구들

VS Code 를 막 깔아 `code` 를 못 찾으면 전체 경로로 부른다. VS Code 를 켤 필요는 없다.

    & "$env:LOCALAPPDATA\\Programs\\Microsoft VS Code\\bin\\code.cmd" --install-extension <이름>

확장 · 플러그인 · 연결 (도구 목록에서 "기본" 인 것 전부)

{기본묶음}

설치 뒤 **새 PowerShell 창** 에서 확인한다(경로가 새 창부터 적용된다).

{블록4}
    code --list-extensions      claude plugin list

깐 것과 실패한 것을 **개수로** 보고한다(예: "확장 8 개 중 8 개, 플러그인 3 개 중 3 개, 실패 0").
실패한 것은 이유를 한 줄로 적고 넘어간다. Claude Code 명령줄을 처음 실행하면 브라우저 로그인이
열린다. 사용자 계정으로 로그인하게 안내한다. 브라우저가 안 열리면 화면의 주소를 복사해 직접
열고 코드를 붙여 넣게 한다. 연결(MCP)은 사용자 계정으로 claude.ai 설정에서 켜는 것이라, 켜는
화면까지 안내하고 사용자가 직접 누르게 한다.

## 2-5. 무슨 일을 하는지 아주 자세히 묻는다 (가장 중요하다)

이 단계가 설치의 핵심이다. 무엇을 더 권할지, 앞으로 어떻게 도울지가 여기서 정해진다.
**서두르지 않는다.** 사용자는 AI 를 처음 써 볼 수 있다. 전문 용어(스킬, MCP, 토큰, 컨텍스트)를
쓰지 않고, 한 번에 한두 가지만 묻고, 보기를 함께 준다.

- 답이 짧거나 막연하면 한 번 더 파고든다. "예를 들면요?", "지난주에 실제로 한 것 하나만
  말씀해 주세요", "그건 무슨 프로그램으로 하세요?", "그다음엔 누구에게 넘기세요?"
- 모른다고 하면 넘어가고 메모의 "알아볼 것" 에 적는다.
- 한 번에 다 못 들으면 다음 대화에서 이어서 묻는다(지침 머리말의 "이 사용자를 계속 알아 간다").
- 단계마다 들은 것을 한 줄로 되짚어 확인한 뒤 다음으로 넘어간다.

차례

    1  큰 그림         분야(도로 · 하천 · 상하수도 · 단지 · 구조 · 지반 · 교통 · 환경 · 조경 · 측량),
                       소속(설계사 · 발주처 · 감리 · 시공사), 경력, 팀에서 맡은 역할
    2  지금 과업       지금 하고 있는 과업 하나를 골라 달라고 한다. 이름, 발주처, 기간, 지금 단계
    3  과업의 흐름     그 과업을 착수부터 납품까지 따라가며 묻는다
                       착수(과업지시서 · 착수보고) -> 현황 조사 · 자료 수집 -> 계산 · 해석 ->
                       설계 · 도면 -> 수량 · 공사비 -> 보고서 · 계산서 -> 보고회 · 심의 -> 수정 · 납품
                       단계마다: 무엇을 받나(형식), 무엇을 만드나(형식 · 양식), 무엇으로 하나(프로그램),
                       얼마나 걸리나, 누구에게 넘기나
    4  산출물 하나씩    3 에서 나온 산출물마다: 양식이 정해져 있나, 매번 새로 쓰나 고쳐 쓰나,
                       표 · 그림 · 계산은 어디서 오나, 검토에서 자주 지적받는 것은 무엇인가
    5  프로그램        CAD(AutoCAD · Civil3D), 해석(MIDAS · HEC-RAS · SWMM · EPANET 등), 적산,
                       한글 · 엑셀 버전. 결과를 어떤 파일로 뽑나(엑셀 · txt · PDF · 그림)
    6  번거로운 일      가장 시간이 아까운 일 세 가지. 실제로 지난주에 한 일로 묻는다
                       예: 해석 결과를 보고서 표로 옮기기, 단위 환산, 수량 집계, 양식 맞추기,
                       오탈자 · 숫자 불일치 찾기, 도면 목록, 회의록, 검토의견 회신 표
    7  함께 일하는 사람  발주처 · 협력사 · 팀장과 무엇을 어떤 방법으로 주고받나
                       (메일 · 구글 드라이브 · 메신저 · 회사 서버 · 공문)
    8  자료와 폴더      과업 자료가 어디 있나(이 PC · 회사 서버 · 드라이브), 폴더를 어떻게 나누나
    9  보안 · 규정      발주처 자료를 외부 서비스에 올리면 안 되는 규정, 회사 PC 설치 제한
    10 바라는 것        클로드가 해 주면 가장 좋을 일, 답변 말투(짧게 · 자세히)

다 들은 뒤 사용자의 말로 **"제가 이해한 일은 이렇습니다"** 를 5-10 줄로 보여 주고, 틀리거나
빠진 곳을 고쳐 달라고 한다. 고칠 것이 없다고 할 때까지 되풀이한다.

### 메모로 남긴다

확인받은 내용을 `%USERPROFILE%\\.claude\\CLAUDE.md` 맨 끝 `## 이 PC 메모` 절에만 적는다. 지침
본문은 건드리지 않는다. 네 칸으로 나누고, 줄마다 날짜를 붙인다. 앞으로 대화할 때마다 이 메모를
갱신한다.

    ### 업무
    2026-09-29  하천 설계, 설계사 5 년차. 발주처는 지자체 · 유역환경청 (예)
    2026-09-29  지금 과업: ○○천 재해예방사업 실시설계. 중간보고 준비 중 (예)
    2026-09-29  흐름: 과업지시서(hwp) -> 현황조사 -> HEC-RAS 해석 -> 수리계산서(엑셀) -> 보고서(hwp) (예)
    ### 자료와 도구
    2026-09-29  한글 2022, 엑셀, AutoCAD, HEC-RAS. 과업 폴더 D:\\과업\\2026_○○천 (예)
    2026-09-29  보안: 발주처 원본 자료는 외부 업로드 금지 (예)
    ### 도구 결정
    2026-09-29  기본 묶음 설치. 거절: 구글 드라이브 연결(회사 규정). 나중에: 발표자료 도구 (예)
    ### 알아볼 것
    2026-09-29  검토의견 회신을 어떤 양식으로 하는지 (예)

### 첫 일감을 같이 해 본다

메모를 적은 뒤, **작고 확실한 일 하나**를 함께 해 보자고 제안한다. 2-5 의 "번거로운 일" 중
하나를 고른다. 예를 들어 사용자가 가진 엑셀 표 하나를 한글 · 워드 표로 정리하거나, 보고서 한
절의 오탈자와 숫자 불일치를 찾아 준다. 처음 쓰는 사람에게는 설명보다 한 번 해 보는 것이
빠르다. 이때도 파일을 고치기 전에 무엇을 할지 먼저 말하고 허락을 받는다.

## 2-6. 끝을 알린다

설치한 것(개수), 백업 위치, 안 된 것을 적고 **새 대화를 열어야 지침이 적용된다**고 알린다.
그리고 "앞으로 대화할 때마다 하시는 일을 조금씩 더 여쭤보고 메모를 고쳐 가겠습니다. 새로운
일이 생기면 거기에 맞는 도구도 그때 여쭤보겠습니다" 라고 알린다. 3 부는 2-5 가 끝난 뒤 바로
이어서 해도 되고, 사용자가 지쳐 보이면 다음 대화로 미룬다(메모의 "알아볼 것" 에 적는다).

## 2-7. 갱신 · 되돌리기

2-3 의 1-3 으로 설치했으면 할 일이 없다. 상황별 지침 20 여 개, 스킬 9 개, 점검 도구, 도구 목록이
모두 `C:\\claude-prompt` 에 있고, 클로드를 열 때마다 새 판을 받는다. 받았으면 "[지침 갱신]
원작자가 고친 지침 n건을 받아 설치했습니다" 라고 한 줄 뜬다. 이 PC 메모는 보존된다.

    지금 바로 받기     powershell -NoProfile -ExecutionPolicy Bypass -File C:\\claude-prompt\\update.ps1
    자동 갱신 끄기     ... update.ps1 -Uninstall      (지침은 설치된 채 남는다)
    지침 되돌리기      %USERPROFILE%\\.claude\\CLAUDE.md.bak.<시각> 을 CLAUDE.md 로 되돌린다

`C:\\claude-prompt` 안의 파일은 고치지 않는다. 고치면 새 판을 받을 때 막힌다. 이 PC 에만
맞출 것은 `CLAUDE.md` 맨 끝 `## 이 PC 메모` 에 적는다.

---

# 3 부. 더 깔 것을 하나씩 묻는다 (이 사람의 일에 빗대어)

원작자 PC 에 깔린 확장 {len(확장)} 개, 플러그인 {len(플러그인)} 개, 장터 {len(env["장터"])} 개, 연결(MCP)
{len(env["mcp"])} 개를 **전부** 아래 도구 목록에 실었다. 같은 목록이
`C:\\claude-prompt\\_동기화\\recipient\\도구목록.md` 에도 있다. "기본" 은 2-4 에서 이미 깔았다.
**"물어봄" 을 하나씩, 2-5 에서 들은 이 사람의 실제 일에 빗대어 설명하고 필요한지 묻는다.**

- 한 번에 한 가지씩 묻는다. 메모의 "번거로운 일" 에 닿는 것부터 묻는다.
- 목록의 "예" 는 일반 예시다. 그대로 읽지 말고 **이 사람의 과업 · 산출물 이름으로 바꿔** 말한다.
- 비용 · 계정이 필요하면 먼저 말한다. 메일 · 드라이브처럼 자료를 읽는 연결은 메모의 보안
  규정을 먼저 확인한다.
- 이 사람 일과 전혀 닿지 않는 것은 묻지 않고 넘어가되, 메모 "도구 결정" 에 "해당 없음" 으로 남긴다.
- "권하지않음" 은 사용자가 먼저 묻거나 "원작자와 똑같이 해 달라" 고 할 때만 설명한다.
- 다른 사람이 만든 장터 · 플러그인은 설치 전에 무엇을 설치 · 실행하는지 확인한다.
- 답은 모두 메모 "도구 결정" 에 적는다(깐 것 · 거절한 것 · 나중에). 거절한 것은 다시 권하지 않는다.
- 나중에 새 일이 생기면(메모에 없던 산출물 · 프로그램) 이 목록을 다시 보고 그 일에 맞는 것을 묻는다.

    나쁨   "Rainbow CSV 는 CSV 열을 색으로 구분하는 확장입니다. 깔까요?"
    좋음   "HEC-RAS 결과를 CSV 로 뽑으신다고 하셨죠. 그 파일을 열면 열마다 색이 달라서 어느
            숫자가 수위이고 어느 것이 유속인지 바로 보입니다. 무료입니다. 깔까요?"

## 도구 목록

{도구목록}

---

# 4 부. 손으로 깔 때 (winget 이 없거나 회사 PC 라 막힐 때)

{블록10}

# 5 부. 잘 안 될 때

{블록11}

---

# 6 부. 전역 지침 원문 (2-3 에서 쓸 글)

{시작표시}
"""


def 본문():
    a = open(머리말, encoding="utf-8").read().rstrip()
    b = re.sub(r"^<!--.*?-->\s*", "", open(규칙, encoding="utf-8").read(), flags=re.S)
    t = a + "\n\n" + b
    t = t.replace(작성자파이썬, "{{PYTHON}}").replace(작성자뿌리, "{{원본폴더}}")
    t = t.replace(작성자집 + "\\", "%USERPROFILE%\\").replace(작성자집, "%USERPROFILE%")
    assert "SGJEONG99" not in t, "작성자 경로가 남았다"
    assert "{{PYTHON}}" in t and "{{원본폴더}}" in t
    return t.rstrip()


def main():
    env = 환경(다시읽기="--빠르게" not in sys.argv)
    글 = 안내글(env) + 본문() + "\n" + 끝표시 + "\n"
    assert 글.count(시작표시) == 2 and 글.count(끝표시) == 2, "표시가 짝이 맞지 않는다"
    assert "{{PYTHON}}" in 글 and "{{{" not in 글, "자리표시가 깨졌다"
    assert "SGJEONG99" not in 글.replace(작성자뿌리, ""), "작성자 경로가 남았다"
    open(결과, "w", encoding="utf-8").write(글)
    print("만듦 %s  (%d 줄, %.1f KB)" % (결과, 글.count("\n") + 1, len(글.encode("utf-8")) / 1024))


if __name__ == "__main__":
    main()
