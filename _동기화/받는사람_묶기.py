r"""지인에게 줄 Prompt 사본을 만든다. 원본 Prompt 폴더와 이 PC 의 설정은 건드리지 않는다.

왜 있나
  폴더를 통째로 넘기면 git 이력 · 브라우저 캡처 · 임시 폴더까지 딸려 가고, 받는 사람 PC 의
  클로드가 무엇을 해야 할지 모른다. 반대로 설치 안내 CLAUDE.md 를 원본 폴더 맨 위에 두면
  원작자가 이 폴더에서 일할 때마다 그 안내가 원작자 세션에도 읽힌다(원작자 작업에 영향).
  그래서 받는 사람용 파일은 _동기화\recipient\ 에만 두고, 사본을 만들 때만 사본 맨 위에 놓는다.

무엇을 하나
  1. 바탕화면에 Prompt_전달_YYYYMMDD\ 를 만든다(있으면 _v2, _v3). 원본을 복사하되
     .git · .playwright-mcp · _workspace · __pycache__ · *.pyc · *.bak · ~$* 와
     원작자 전용 도구(apply.bat · _sync.py) 는 뺀다
  2. 시작하기.md(파일 하나만으로 설치하는 문서)를 새로 만들고, 사본 맨 위에
     CLAUDE.md(설치 안내) · 설치하기.bat · 설치안내.md · 시작하기.md 를 놓는다
  3. 같은 이름의 zip 을 만든다
  4. 개인 식별 정보(이름 · 계정 · 이메일)가 남은 곳을 세어 알린다. 고치지는 않는다

실행
  C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe -X utf8 _동기화\받는사람_묶기.py
"""
import datetime
import fnmatch
import os
import re
import shutil
import zipfile

여기 = os.path.dirname(os.path.abspath(__file__))
뿌리 = os.path.dirname(여기)
받는사람 = os.path.join(여기, "recipient")
바탕화면 = os.path.join(os.path.expanduser("~"), "Desktop")
기본이름 = "Prompt_전달_" + datetime.date.today().strftime("%Y%m%d")

뺄폴더 = {".git", ".playwright-mcp", "_workspace", "__pycache__",
       "claude_memory"}          # author's Claude memory, synced between his own PCs only
뺄파일 = ["*.pyc", "*.bak", "*.bak.*", "~$*",
       "apply.bat", "_sync.py",   # author-only tools; they call the author's Python and fail elsewhere
       "깃동기화.py", "노트북_붙여넣기.md", "친구판_올리기.py"]   # author's two-PC sync and publishing
# name in the bundle root <- file in _동기화\recipient
맨위 = {"CLAUDE.md": "recipient_CLAUDE.md", "설치하기.bat": "설치하기.bat",
      "설치안내.md": "설치안내.md", "시작하기.md": "시작하기.md"}
# things a recipient may not expect to receive; reported, not changed
개인정보 = {"작성자 이름": r"정상곤|Sanggon Jeong|Jeong, S\.", "GitHub 계정": r"sheahe0220",
         "이메일": r"[A-Za-z0-9._%+-]+@(gmail|naver|daum|skku)\.[a-z.]+", "PC 사용자 이름": r"SGJEONG99"}


def 새이름():
    d, k = os.path.join(바탕화면, 기본이름), 1
    while os.path.exists(d) or os.path.exists(d + ".zip"):
        k += 1
        d = os.path.join(바탕화면, "%s_v%d" % (기본이름, k))
    return d


def 무시(폴더, 이름들):
    return [n for n in 이름들 if n in 뺄폴더 or any(fnmatch.fnmatch(n, p) for p in 뺄파일)]


def main():
    import runpy
    # dist 를 먼저 새로 만든다. 2026-09-23 에 반쯤 지워진 dist 로 사본을 만들어
    # 스킬 참고 문서가 통째로 빠진 적이 있다(파일 152 -> 113). 아래 검사로도 막는다
    for 스크립트 in ("내보내기.py", "받는사람_한파일.py"):
        try:
            runpy.run_path(os.path.join(여기, 스크립트), run_name="__main__")
        except SystemExit as e:      # 내보내기.py 는 sys.exit 로 끝난다. 그것이 여기까지 끝내지 않게 한다
            assert not e.code, "%s 가 실패했다(종료코드 %s)" % (스크립트, e.code)
    for 원본 in 맨위.values():
        assert os.path.isfile(os.path.join(받는사람, 원본)), "받는 사람용 파일이 없다: %s" % 원본
    assert os.path.isfile(os.path.join(받는사람, "install.ps1"))
    dst = 새이름()
    shutil.copytree(뿌리, dst, ignore=무시)
    for 이름, 원본 in 맨위.items():
        shutil.copy2(os.path.join(받는사람, 원본), os.path.join(dst, 이름))

    파일 = [os.path.join(d, f) for d, _, fs in os.walk(dst) for f in fs]
    assert len(파일) > 100, "사본 파일이 너무 적다: %d" % len(파일)
    스킬 = os.path.join(dst, "dist", "skills")
    이름들 = sorted(os.listdir(스킬)) if os.path.isdir(스킬) else []
    assert len(이름들) == 9, "스킬이 9 개가 아니다: %s" % 이름들
    for n in 이름들:
        assert os.path.isfile(os.path.join(스킬, n, "SKILL.md")), "SKILL.md 가 없다: %s" % n
        if n.startswith("std-"):
            r = os.path.join(스킬, n, "references")
            assert os.path.isdir(r) and os.listdir(r), "참고 문서가 비었다: %s" % n
    for n in 뺄폴더:
        assert not any(os.sep + n + os.sep in p for p in 파일), "빠져야 할 폴더가 남았다: %s" % n
    첫줄 = open(os.path.join(dst, "CLAUDE.md"), encoding="utf-8").readline().strip()
    assert 첫줄.startswith("# 이 폴더를 받은 PC"), 첫줄

    zp = dst + ".zip"
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for p in 파일:
            z.write(p, os.path.join(os.path.basename(dst), os.path.relpath(p, dst)))
    크기 = sum(os.path.getsize(p) for p in 파일)
    print("사본  %s  (파일 %d 개, %.1f MB)" % (dst, len(파일), 크기 / 1e6))
    print("zip   %s  (%.1f MB)" % (zp, os.path.getsize(zp) / 1e6))

    print("\n개인 식별 정보가 남은 곳 (고치지 않았다. 넘기기 전에 판단한다)")
    for 무엇, 식 in 개인정보.items():
        걸린 = []
        for p in 파일:
            if os.path.splitext(p)[1].lower() not in (".md", ".py", ".json", ".txt", ".bat", ".ps1"):
                continue
            t = open(p, encoding="utf-8", errors="ignore").read()
            n = len(re.findall(식, t))
            if n:
                걸린.append((n, os.path.relpath(p, dst)))
        print("  %-10s %d 파일" % (무엇, len(걸린)) + (": " + ", ".join(f for _, f in 걸린[:6]) +
                                                   (" ..." if len(걸린) > 6 else "") if 걸린 else ""))


if __name__ == "__main__":
    main()
