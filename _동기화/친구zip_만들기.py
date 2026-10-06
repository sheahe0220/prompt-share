r"""지인에게 카톡으로 보낼 zip 을 바탕화면에 만든다(시작하기.md + 먼저 읽기).

왜 있나
  지인은 앱 설치까지만 할 수 있다(2026-09-29 사용자). 파일 하나를 받아 Claude 에게 주면
  Git 설치 · 공개 저장소 받기 · 자동 갱신까지 Claude 가 한다. zip 에는 그 파일과, 사람이
  읽을 네 단계 안내만 넣는다. 전체 지침은 zip 이 아니라 공개 저장소에서 받는다.

실행
  C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe -X utf8 _동기화\친구zip_만들기.py
  결과는 바탕화면\공유\ 에 둔다. 판은 _v2, _v3 로 올린다(덮어쓰지 않는다).
"""
import datetime
import os
import runpy
import zipfile

여기 = os.path.dirname(os.path.abspath(__file__))
시작하기 = os.path.join(여기, "recipient", "시작하기.md")
바탕화면 = os.path.join(os.path.expanduser("~"), "Desktop")
기본이름 = "클로드_시작하기_" + datetime.date.today().strftime("%Y%m%d")

먼저읽기 = """클로드 작업 지침 설치 (먼저 읽어 주세요)

할 일은 네 가지입니다. 10 분쯤 걸립니다.

1. Claude 유료 요금제에 가입합니다.            https://claude.ai
2. Claude 데스크톱 앱을 깔고 로그인합니다.     https://claude.com/download
   (앱 왼쪽 위에 "Code" 단추가 보이면 됩니다)
3. "문서" 폴더 안에 "클로드" 라는 새 폴더를 만들고,
   이 압축 파일 안의 "시작하기.md" 를 그 폴더에 넣습니다.
4. 앱에서 Code > 로컬 > 폴더 에서 "문서\\클로드" 를 고르고, 입력창에

       이 파일대로 해줘

   라고 쓰고 Enter 를 누릅니다.

VS Code 와 클로드 확장이 이미 깔린 PC 라면 앱 대신 VS Code 에서 해도 됩니다.
   파일 > 폴더 열기 로 "문서\\클로드" 를 열고, 시작하기.md 를 눌러 연 뒤,
   편집 창 오른쪽 위의 불꽃 아이콘을 눌러 같은 문장을 쓰면 됩니다.

이미 깔려 있는 프로그램이 있어도 괜찮습니다. 클로드가 이 PC 에 있는 것부터 확인하고,
있는 것은 건너뛰고 빠진 것만 채웁니다. PC 가 두 대면 두 PC 에서 각각 이렇게 하면 됩니다.

그다음은 클로드가 하나씩 설명하고 물어봅니다. 허락을 물으면 "허용" 을 누르면 됩니다.
Git 같은 프로그램도 클로드가 물어보고 대신 깔아 줍니다.
한 번 설치하면, 보낸 사람이 지침을 고칠 때마다 클로드를 열면 자동으로 새 판이 들어옵니다.
여러분의 파일이나 대화는 어디에도 올라가지 않습니다.

함께 든 문서 (설치한 뒤 읽으세요)
  VS Code 에서 클로드 코드 쓰기 (사용설명서) .pdf / .docx
      폴더 열기, 세션, 경로 복사해서 시키기, 모델 · 권한, 세션 이어서 하기, 지침 저장,
      에이전트, 휴대폰에서 이어 보기, 토목 실무 예시
  클로드 코드 명령 총정리 .pdf / .docx   (있을 때)
      모든 명령 · 단축키와 인터넷의 좋은 정리 자료 모음
"""
설명서폴더 = os.path.join(여기, "설명서", "산출")
# (prefix of the versioned file, name inside the zip, required?)
문서들 = [("VSCode_클로드코드_사용설명서", "VS Code 에서 클로드 코드 쓰기 (사용설명서)", True),
        ("클로드코드_명령총정리", "클로드 코드 명령 총정리", False)]


def 최신판(접두):
    """Highest _vN of a versioned output that has both pdf and docx, as {ext: path}."""
    import re
    판 = {}
    for f in os.listdir(설명서폴더) if os.path.isdir(설명서폴더) else []:
        m = re.fullmatch(re.escape(접두) + r"_v(\d+)\.(pdf|docx)", f)
        if m:
            판.setdefault(int(m.group(1)), {})[m.group(2)] = os.path.join(설명서폴더, f)
    완전 = [k for k, v in 판.items() if set(v) == {"pdf", "docx"}]
    return 판[max(완전)] if 완전 else {}


공유폴더 = os.path.join(바탕화면, "공유")   # 2026-09-29 user: zips for friends go in Desktop\공유


def 새경로():
    """Next version after the highest one in Desktop\\공유, the Desktop itself, or either _폐기 (a retired _v1
    must not free the bare name again: 2026-09-29 that put the newest zip under the oldest-looking name)."""
    import glob
    import re
    판 = [0]
    for 곳 in (공유폴더, 바탕화면):
        for f in glob.glob(os.path.join(곳, 기본이름 + "*.zip")) + \
                glob.glob(os.path.join(곳, "_폐기", "*", 기본이름 + "*.zip")):
            m = re.fullmatch(re.escape(기본이름) + r"(?:_v(\d+))?\.zip", os.path.basename(f))
            if m:
                판.append(int(m.group(1) or 1))
    os.makedirs(공유폴더, exist_ok=True)
    return os.path.join(공유폴더, "%s_v%d.zip" % (기본이름, max(판) + 1))


def main():
    # regenerate the guide from the current environment list so the zip is never stale
    runpy.run_path(os.path.join(여기, "받는사람_한파일.py"), run_name="__main__")
    글 = open(시작하기, encoding="utf-8").read()
    assert "claude-prompt" in 글 and "update.ps1 -Install" in 글, "시작하기.md 에 자동 갱신 절이 없다"
    zp = 새경로()
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(시작하기, "시작하기.md")
        z.writestr("먼저 읽어 주세요.txt", 먼저읽기.replace("\n", "\r\n").encode("utf-8-sig"))
        기대 = ["시작하기.md", "먼저 읽어 주세요.txt"]
        for 접두, 이름, 필수 in 문서들:
            판 = 최신판(접두)
            assert 판 or not 필수, "%s 의 pdf · docx 가 없다. 설명서\\02_워드.py 를 먼저 돌린다" % 접두
            for ext, src in sorted(판.items()):
                z.write(src, "%s.%s" % (이름, ext))
                기대.append("%s.%s" % (이름, ext))
                print("  넣음 %s" % os.path.basename(src))
    with zipfile.ZipFile(zp) as z:
        이름들 = z.namelist()
        assert 이름들 == 기대, 이름들
        assert z.read("시작하기.md") == open(시작하기, "rb").read()
    print("zip  %s  (%.1f KB, 파일 %d 개: %s)" % (zp, os.path.getsize(zp) / 1024, len(이름들), ", ".join(이름들)))


if __name__ == "__main__":
    main()
