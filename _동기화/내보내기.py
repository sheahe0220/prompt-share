r"""Prompt 모음을 ~/.claude 로 내보낸다. 모든 프로젝트 · 모든 세션에 걸린다.

무엇을 왜 만들었나
  새 세션이나 새 프로젝트를 열 때마다 규칙을 다시 설명하는 일이 반복됐다.
  ~/.claude 에 두면 자동으로 걸린다. 다만 그냥 복사하면 Prompt 와 두 벌이
  되어 갈리므로, 원본은 Prompt 에 두고 이 스크립트로 내보낸다.

무엇을 내보내나
  _전역\CLAUDE.md            ->  ~/.claude/CLAUDE.md          매 세션 자동
  상황별 md 를 묶어 스킬로     ->  ~/.claude/skills/std-*/      해당할 때만
  _점검\점검.py               ->  std-check/scripts/

스킬 하나는 짧은 안내문(SKILL.md)과 전문(references/*.md)으로 나눈다.
매 세션 읽히는 것은 description 뿐이므로 그것만 짧게 유지하면 된다.

실행
  C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe -X utf8 _동기화\내보내기.py
  --확인   무엇이 바뀌는지만 보고 쓰지 않는다
"""
import os
import shutil
import subprocess
import sys

여기 = os.path.dirname(os.path.abspath(__file__))
뿌리 = os.path.dirname(여기)
집 = os.path.join(os.path.expanduser("~"), ".claude")
스킬뿌리 = os.path.join(집, "skills")

확인만 = "--확인" in sys.argv


# 스킬 이름, 담을 파일, description
# description 이 스킬이 걸릴지 말지를 정한다. 사용자가 실제로 쓸 말을 넣는다.
스킬 = [
    (
        "std-project",
        ["02_폴더.md", "03_새과업.md", "04_날짜작업.md", "40_세션관리.md"],
        "과업 폴더 구조 · 새 과업 시작 절차 · 날짜별 작업 폴더(_작업\\YYYYMMDD) · "
        "세션 기록과 인수인계 규칙. "
        "\"오늘 작업\", \"날짜 폴더\", \"일지\", \"오늘 한 일\", "
        "다음 상황에서 사용할 것: \"새 과업\", \"새 프로젝트\", \"폴더 정리\", "
        "\"폴더 구조\", \"어디에 둬야 하나\", \"파일이 어디 있나\", "
        "\"작업 재개\", \"세션 기록\", \"이어서 하자\", \"지금 어디까지\", "
        "\"CLAUDE.md 만들어\", \"README 써줘\", \"인수인계\". "
        "폴더를 새로 만들거나 파일을 옮기기 전에 먼저 읽어라. "
        "번호 규칙과 _폐기 처리를 어기면 나중에 무엇이 최신인지 알 수 없게 된다.",
    ),
    (
        "std-figures",
        ["10_그림.md"],
        "matplotlib 그림 작성 규격. 인쇄 크기 그대로 그리기, 한글 폰트, "
        "범례 겹침 처리 사다리와 자동 검사, 배치기 선택, 흑백 인쇄 대비. "
        "다음 상황에서 사용할 것: \"그림\", \"그래프\", \"플롯\", \"도표\", "
        "\"figure\", \"matplotlib\", \"범례\", \"legend\", \"범례가 겹친다\", "
        "\"글자가 작다\", \"한글이 깨진다\", \"축 바꿔\", \"색 바꿔\", "
        "\"그림 50장\", \"재생성\", \"잘린다\". "
        "그림을 1장이라도 만들거나 고칠 때는 코드를 쓰기 전에 먼저 읽어라. "
        "크게 그려 줄여 넣으면 글자가 같이 줄어들고, 범례는 배치기를 안 부르면 잘린다.",
    ),
    (
        "std-docs",
        ["11_보고서.md", "12_발표대본.md", "13_논문.md", "14_HWPX.md", "15_발표자료.md"],
        "보고서 · 발표대본 · 발표자료(PPT) · 학술논문 조판과 서술 규칙. python-docx, "
        "한글 HWPX, python-pptx 와 PowerPoint COM 을 다룬다. 판형, 목차와 쪽번호, 그림, "
        "표, 캡션, 계보, 슬라이드 구성과 점검, 남의 양식을 해치지 않고 고치기. "
        "다음 상황에서 사용할 것: \"보고서\", \"docx\", \"워드\", \"한글\", "
        "\"hwp\", \"hwpx\", \"발표대본\", \"발표자료\", \"PPT\", \"pptx\", \"파워포인트\", "
        "\"슬라이드\", \"장표\", \"양식\", \"템플릿\", \"대본\", \"논문\", "
        "\"학술지\", \"KCI\", \"심사 대응\", \"조판\", \"목차\", \"쪽번호\", "
        "\"캡션\", \"PDF로\". "
        "문서를 만들거나 고치기 전에 먼저 읽어라. 양식이 있으면 틀은 두고 내용만 바꾸고 "
        "양식대조.py 로 맞대야 한다. HWPX 는 양식을 열어 값만 바꾼다.",
    ),
    (
        "std-data",
        ["20_자료조사.md", "21_자료분석.md", "22_문서분석.md", "23_문헌탐색.md"],
        "원자료 조사와 분석, 문헌(논문) 탐색. PDF 더미에서 근거 찾기, 계측 시계열 분석, "
        "남의 보고서를 읽고 판정하기. 핵심어 묶기, 태그 해독, 사상 잡기, 품질 검사. "
        "다음 상황에서 사용할 것: \"자료 조사\", \"원자료\", \"PDF 찾아\", "
        "\"근거 찾아\", \"계측\", \"시계열\", \"SCADA\", \"사상\", \"결측\", "
        "\"이상치\", \"보고서 읽고\", \"정리해줘\", \"대조표\", \"상충\", "
        "\"설계값과 현행\", \"논문 찾아\", \"선행연구\", \"관련 논문\", \"랩미팅 논문\", "
        "\"Q1\", \"DOI\", \"정독 노트\", \"논문 정리\". "
        "자료를 열기 전에 먼저 읽어라. 시트 이름과 폴더 이름을 믿으면 안 되고, "
        "사상 ID 를 숫자로 읽으면 지수 표기로 조용히 깨진다.",
    ),
    (
        "std-code",
        ["05_진행보고.md", "30_코드.md", "31_에이전트.md", "32_깃.md", "33_루프.md",
         "34_이해와설명.md"],
        "작업 진행 보고(시작 선언 · 보고 간격 · 끝 보고), 스크립트 작성 규칙, 서브에이전트에 일 나누기, git 이력 관리, "
        "루프 엔지니어링(종료 조건을 코드로 만들어 반복시키기), "
        "낯선 코드와 개념을 그림으로 파악하고 설명하기(eli5 · understand-anything · "
        "pr-walkthrough 를 언제 어떻게 쓰나, 남의 스킬을 들이는 순서). "
        "다음 상황에서도 사용할 것: \"설명해줘\", \"쉽게\", \"eli5\", \"그림으로\", "
        "\"코드 구조\", \"코드 지도\", \"무엇이 무엇을 부르나\", \"스킬 설치\", "
        "\"플러그인 깔아줘\". "
        "다음 상황에서 사용할 것: \"스크립트\", \"코드 짜줘\", \"파이썬\", "
        "\"에이전트\", \"병렬로\", \"나눠서\", \"서브에이전트\", \"git\", "
        "\"커밋\", \"gitignore\", \"GitHub\", \"루프\", \"반복\", "
        "\"될 때까지\", \"캘리브레이션\", \"보정\", \"자동으로 돌려\". "
        "코드를 쓰거나 일을 나누기 전에 먼저 읽어라. 되풀이시킬 때는 "
        "verify 스크립트를 먼저 만들어 종료 조건을 밖에서 재게 해야 한다.",
    ),
    (
        "std-check",
        ["90_점검표.md", "50_외부위임.md"],
        "내놓기 전 점검과 외부 위임. 금지어 · em dash · 빈 파일을 훑는 점검.py, "
        "발표자료의 넘침 · 잘림 · 글꼴을 PowerPoint 로 그려 보는 ppt점검.py, "
        "고친 문서가 양식(마스터 · 스타일 · 머리글 · 여백)을 해쳤는지 원본과 맞대는 "
        "양식대조.py, 논문 원고의 인용 · 참고문헌 · 그림표 번호 · 약어를 맞대고 참고문헌이 "
        "실재하는지 Crossref 로 묻는 원고점검.py 가 들어 있다. 남에게 일을 넘길 때의 지시서 "
        "형식과, 받은 것을 검증하는 순서도 담는다. "
        "다음 상황에서 사용할 것: \"점검\", \"검수\", \"확인해줘\", \"내놓기 전\", "
        "\"금지어\", \"오탈자\", \"제출\", \"납품\", \"지시서\", \"위임\", "
        "\"외주\", \"넘길 건데\", \"받은 결과\". "
        "산출물을 내놓기 전에 반드시 돌려라. 눈으로 훑지 말고 종료코드를 봐라.",
    ),
]

머리말 = """---
name: %s
description: |
%s
---

<!-- 출처: %s
     이 파일은 _동기화\\내보내기.py 가 만든다. 직접 고치지 마라.
     고칠 것이 있으면 위 원본을 고치고 다시 내보낸다. -->

# %s

이 스킬의 규칙 원본은 `%s` 에 있다.

아래 파일을 **읽고 그대로 따른다.** 요약해서 기억하지 말고 필요할 때 연다.

%s

각 파일 끝의 `함정` 절을 반드시 본다. 실제로 한 번 틀려 본 것만 적혀 있다.
"""


def 들여쓰기(s, n=2):
    return "\n".join(" " * n + x for x in s.split("\n"))


def 정션대상(경로):
    """정션이면 가리키는 곳을, 아니면 None 을 돌려준다."""
    try:
        t = os.readlink(경로)
    except (OSError, ValueError):
        return None
    if t.startswith("\\\\?\\"):          # \\?\C:\... 형태로 나온다
        t = t[4:]
    return os.path.normcase(os.path.normpath(t.rstrip("\\")))


def 정션(링크, 대상):
    """링크를 대상 폴더로 잇는다. 관리자 권한이 필요 없는 junction 을 쓴다.

    이미 맞게 이어져 있으면 아무것도 하지 않는다.
    옛 사본 폴더가 있으면 지우고 잇는다. references 는 우리가 만든 사본이라 안전하다.
    """
    대상n = os.path.normcase(os.path.normpath(대상))
    현재 = 정션대상(링크) if os.path.exists(링크) else None

    if 현재 == 대상n:
        if 확인만:
            print("  이미이음 %s" % 링크)
        return False

    if 확인만:
        print("  %s %s -> %s"
              % ("다시이음" if 현재 else "새로이음", 링크, 대상))
        return True

    if os.path.exists(링크):
        if 현재 is not None:
            os.rmdir(링크)                # 정션은 rmdir 로 끊는다
        else:
            shutil.rmtree(링크)           # 옛 사본 폴더
    os.makedirs(os.path.dirname(링크), exist_ok=True)
    # text=True 로 받으면 mklink 의 cp949 출력을 utf-8 로 읽어 예외가 난다.
    # 바이트로 받아 직접 푼다.
    r = subprocess.run(["cmd", "/c", "mklink", "/J", 링크, 대상],
                       capture_output=True)
    if r.returncode != 0:
        말 = (r.stdout + r.stderr).decode("cp949", errors="replace")
        raise AssertionError("mklink 실패: %s" % 말.strip())
    확인 = 정션대상(링크)
    assert 확인 == 대상n, "이었는데 가리키는 곳이 다르다: %s" % 확인
    return True


def 쓰기(경로, 내용):
    if 확인만:
        옛 = ""
        if os.path.exists(경로):
            옛 = open(경로, encoding="utf-8", errors="ignore").read()
        print("  %s %s" % ("바뀜" if 옛 != 내용 else "같음", 경로))
        return 옛 != 내용
    os.makedirs(os.path.dirname(경로), exist_ok=True)
    with open(경로, "w", encoding="utf-8", newline="\n") as f:
        f.write(내용)
    return True


# 일부러 스킬로 내보내지 않는 것. 이유를 함께 적는다.
# 여기에도 없고 스킬표에도 없는 md 가 있으면 새로 만들고 표에 안 넣은 것이다.
비대상 = {
    "00_읽기.md": "색인. 전역 CLAUDE.md 의 마지막 절이 이 파일을 가리킨다",
    "01_공통.md": "_전역\\CLAUDE.md 로 대체된다",
    "60_하네스.md": "하네스를 짤 때만 본다. 원본에서 직접 읽는다",
    "61_참고.md": "링크 모음. 필요할 때 원본에서 직접 읽는다",
    "README.md": "GitHub 저장소 첫 화면. 사람이 읽는 소개문이다",
}


def 매핑점검():
    """원본에 있는데 어디에도 안 실린 md 를 찾는다. 조용히 빠지는 것을 막는다."""
    실린것 = set(비대상)
    for _, 파일들, _ in 스킬:
        실린것.update(파일들)
    있는것 = {f for f in os.listdir(뿌리) if f.endswith(".md")}
    안실림 = sorted(있는것 - 실린것)
    사라짐 = sorted(실린것 - 있는것 - set(비대상))
    return 안실림, 사라짐


def 겹침점검():
    """claude.ai 에서 내려온 스킬(~/.claude/skills/synced/)과 로컬 스킬의 이름 겹침.

    겹치면 매 세션 목록에 두 번 실린다(2026-09-22 확인). 막지는 않고 알린다.
    """
    동기 = os.path.join(스킬뿌리, "synced")
    if not os.path.isdir(동기):
        return []
    내려온것 = set()
    for d in os.listdir(동기):
        p = os.path.join(동기, d)
        if os.path.isdir(p) and not d.startswith("."):
            내려온것.update(n for n in os.listdir(p)
                         if os.path.isfile(os.path.join(p, n, "SKILL.md")))
    로컬 = {n for n in os.listdir(스킬뿌리)
          if n != "synced" and os.path.isfile(os.path.join(스킬뿌리, n, "SKILL.md"))}
    return sorted(내려온것 & 로컬)


def main():
    print("원본 %s" % 뿌리)
    겹침 = 겹침점검()
    if 겹침:
        print("[알림] claude.ai 에서 내려온 스킬과 이름이 겹친다: %s" % ", ".join(겹침))
        print("       매 세션 목록에 두 번 실린다. 옛 쪽을 ~/.claude/_폐기_skills/날짜/ 로 옮긴다")
        print("       우리 스킬이면 claude.ai 에서 끈다. 60_하네스.md 함정 절")
    print("대상 %s" % 집)
    print("확인만 돌립니다. 쓰지 않습니다.\n" if 확인만 else "")

    안실림, 사라짐 = 매핑점검()
    if 사라짐:
        print("[멈춤] 표에 있는데 원본이 없다: %s" % ", ".join(사라짐))
        print("       파일 이름을 바꿨으면 이 스크립트의 스킬표도 고쳐라.")
        return 1
    if 안실림:
        print("[멈춤] 새 파일이 어느 스킬에도 안 실렸다:")
        for f in 안실림:
            print("         %s" % f)
        print("       내보내기.py 의 스킬표에 넣거나, 안 내보낼 것이면")
        print("       비대상 에 이유와 함께 적어라.")
        print("       그냥 두면 이 파일은 전역에 반영되지 않는다.")
        return 1

    # 1. 전역 CLAUDE.md
    print("[1] 전역 CLAUDE.md")
    원 = os.path.join(뿌리, "_전역", "CLAUDE.md")
    assert os.path.exists(원), "원본이 없다: %s" % 원
    전역본문 = open(원, encoding="utf-8").read()
    쓰기(os.path.join(집, "CLAUDE.md"), 전역본문)

    # 1-2. Codex 용 AGENTS.md. 같은 원본에서 만든다. 두 벌을 손으로 고치면 갈린다
    #      (2026-09-21 확인: 손으로 만든 AGENTS.md 가 09-09 판에 멈춰 있었다)
    print("[1-2] Codex AGENTS.md")
    코덱스 = 전역본문.replace("~/.claude", "~/.codex").replace(
        "각 과업 폴더의\n`CLAUDE.md`", "각 과업 폴더의\n`AGENTS.md`")
    # claude.ai skills only ever sync into Claude Code's folder, never Codex's
    # (2026-09-22: the blanket replace above turned it into ~/.codex/skills/synced/)
    동기경로 = "~/.claude/skills/synced/"
    코덱스 = 코덱스.replace("~/.codex/skills/synced/", 동기경로)
    assert (동기경로 in 전역본문) == (동기경로 in 코덱스), "synced 경로 복원 실패"
    for p in (os.path.join(os.path.expanduser("~"), ".codex", "AGENTS.md"),
              os.path.join(os.path.expanduser("~"), "AGENTS.md")):
        if os.path.isdir(os.path.dirname(p)):
            쓰기(p, 코덱스)

    # 2. 스킬
    print("\n[2] 스킬 %d 개" % len(스킬))
    쓴파일 = 0
    for 이름, 파일들, 설명 in 스킬:
        d = os.path.join(스킬뿌리, 이름)
        목록 = "\n".join(
            "- `references/%s`  %s" % (f, 한줄설명(f)) for f in 파일들)
        원본목록 = " · ".join(os.path.join(뿌리, f) for f in 파일들[:1])
        본문 = 머리말 % (이름, 들여쓰기(설명.strip()), 원본목록,
                      이름, os.path.join(뿌리, "00_읽기.md"), 목록)
        쓰기(os.path.join(d, "SKILL.md"), 본문)
        쓴파일 += 1

    # 3. references 와 scripts 를 원본 폴더로 잇는다 (사본을 두지 않는다)
    print("\n[3] 원본으로 잇기 (junction)")
    for 이름, _, _ in 스킬:
        정션(os.path.join(스킬뿌리, 이름, "references"), 뿌리)
    정션(os.path.join(스킬뿌리, "std-check", "scripts"),
        os.path.join(뿌리, "_점검"))

    # 우리가 만든 도구 스킬. 폴더째 정션으로 잇는다 (kr-paper-search · kr-hydro-data 등)
    도구 = os.path.join(뿌리, "_도구", "skills")
    if os.path.isdir(도구):
        for n in sorted(os.listdir(도구)):
            if os.path.isfile(os.path.join(도구, n, "SKILL.md")):
                정션(os.path.join(스킬뿌리, n), os.path.join(도구, n))

    print("\n[결과] 스킬 %d 개, SKILL.md %d 개%s"
          % (len(스킬), 쓴파일, " (확인만)" if 확인만 else " 내보냄"))
    if not 확인만:
        # 실제로 원본이 보이는지 확인한다. 정션이 끊기면 여기서 걸린다
        본 = os.path.join(스킬뿌리, "std-figures", "references", "10_그림.md")
        assert os.path.exists(본), "정션이 끊겼다: %s" % 본
        점 = os.path.join(스킬뿌리, "std-check", "scripts", "점검.py")
        assert os.path.exists(점), "정션이 끊겼다: %s" % 점
        print("       원본 직결 확인. Prompt 를 고치면 그대로 반영된다")

        # 4. PC 밖으로 내보낼 사본 (GitHub · claude.ai 웹). dist\ 를 다시 만든다
        print("\n[4] 배포 사본 (dist)")
        import runpy
        옛 = sys.argv
        sys.argv = [os.path.join(여기, "배포_만들기.py")]
        try:
            runpy.run_path(sys.argv[0], run_name="__main__")
        except SystemExit as e:
            assert not e.code, "배포_만들기.py 가 실패했다"
        finally:
            sys.argv = 옛
    return 0


설명표 = {
    "02_폴더.md": "폴더 구조와 이름 규칙",
    "03_새과업.md": "새 과업 시작 절차와 붙여 쓸 틀",
    "04_날짜작업.md": "날짜별 작업 폴더 · 일지 · 색인 · 승격",
    "40_세션관리.md": "세션 기록과 인수인계",
    "10_그림.md": "matplotlib 규격",
    "11_보고서.md": "docx 조판",
    "12_발표대본.md": "발표대본",
    "13_논문.md": "SCI · KCI · 학위논문 작성 · 교정 · 심사 대응 · Q1 실측",
    "14_HWPX.md": "한글 HWPX",
    "15_발표자료.md": "발표자료 pptx 만들기 · 고치기 · 양식 지키기 · 점검",
    "20_자료조사.md": "원자료 조사",
    "21_자료분석.md": "계측 시계열 분석",
    "22_문서분석.md": "남의 문서 읽고 판정",
    "23_문헌탐색.md": "논문 찾기 · Crossref 실재 확인 · 쓰임별 추천 · 정리 노트",
    "30_코드.md": "스크립트 작성",
    "31_에이전트.md": "에이전트에 나눠 시키기",
    "32_깃.md": "git",
    "33_루프.md": "루프 엔지니어링",
    "34_이해와설명.md": "eli5 · understand-anything · pr-walkthrough",
    "05_진행보고.md": "시작 선언 · 보고 간격 · 중간 · 끝 보고",
    "90_점검표.md": "내놓기 전 점검",
    "50_외부위임.md": "지시서와 결과 검증",
}


def 한줄설명(f):
    return 설명표.get(f, "")


if __name__ == "__main__":
    sys.exit(main())
