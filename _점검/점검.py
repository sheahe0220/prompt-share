r"""내놓기 전 점검. 사람 눈 대신 돌린다.

무엇을 왜 만들었나
  90_점검표.md 는 읽는 표였다. "프로그램으로 확인한다" 고 적어 놓고 정작
  돌릴 것이 없어서, 바쁠 때는 아무도 점검하지 않았다.

왜 오류와 권고를 갈랐나
  처음에는 금지어 목록 하나를 모든 파일에 똑같이 적용하고 걸리면 막았다.
  그런데 "포착" 은 보고서에서는 틀리지만 코드 주석에서는 아무 문제가 없고,
  인용 원문에 있는 "물량" 은 고칠 수 없는 것이다. 판단이 필요한 것을 기계로
  막으니 오탐이 나고, 오탐이 나면 무시하게 되고, 무시하면 검사가 없는 것과
  같아진다. 그래서 기계로 확실한 것만 막고 나머지는 보고만 한다.

  목록 방식의 더 큰 한계는 오탐이 아니라 목록에 없는 것을 못 잡는다는 것이다.
  번역투와 이중피동은 도메인과 무관하게 나쁘므로 규칙으로 함께 본다.

오류 (막는다. 종료코드 1)
  em dash · U+2212        표기 규칙. 기계로 확실하다
  빈 파일 · 훑은 파일 0 개   조용한 실패를 막는다

권고 (보고만 한다. 막지 않는다)
  구어 · 일상어            보고서 문맥에서만 본다
  번역투 · 이중피동         어느 문서에서든 본다

잣대
  엄격  보고서 · 논문 · 발표대본 · docx · hwpx   학술 용어를 써야 하는 곳
  느슨  세션기록 · 코드 · 안내문                뜻만 통하면 된다
  면제  원문 · 발췌 · 09_원자료                남의 글은 손대지 않는다

실행
  python.exe -X utf8 _점검\점검.py <폴더> [...]
  폴더를 안 주면 이 파일이 있는 폴더의 위를 검사한다
  --조용   권고를 찍지 않는다
"""
import os
import re
import sys
import zipfile

# ------------------------------------------------------------------ 규칙

EM_DASH = chr(8212)      # —
MINUS = chr(8722)        # −

# 보고서 문맥에서 학술 용어로 바꿀 것. 절대 금지가 아니라 그 자리의 권고다.
구어 = {
    "물량": "체적 · 방류량 · 유입량",
    "넘치는": "초과분 · 월류",
    "넘침": "초과분 · 월류",
    "잡다": "차집 · 저류",
    "붙잡다": "차집 · 저류",
    "가두다": "저류",
    "포착": "차집",
    "잡아먹": "잠식",
    "빼내다": "배제",
    "퍼내다": "배제",
    "들어오는 물": "유입수",
    "나가는 물": "방류수",
    "나중물": "후기 유출",
    "앞쪽 물": "초기 유출",
    "더럽다": "농도가 높다",
    "깨끗하게": "수질 개선",
    "쓸모가 있": "활용될 수 있",
    "마른 날": "선행 건기",
    "길바닥": "도로 노면",
    "쌓이다": "축적되다",
    "씻기다": "세척되다",
    "숫자로 보이": "정량적으로 제시하",
    "행방": "배분",
}

# 도메인과 무관하게 나쁜 것. 어느 문서에서든 본다.
번역투 = {
    "되어지": "이중피동. -되다 로 충분하다",
    "보여지": "이중피동. 보이다",
    "쓰여지": "이중피동. 쓰이다",
    "나뉘어지": "이중피동. 나뉘다",
    "불리워": "이중피동. 불리다",
    "모아지": "이중피동. 모이다",
    "잊혀지": "이중피동. 잊히다",
    "짜여지": "이중피동. 짜이다",
    "에 있어서": "일본어투. -에서 · -의 경우",
    "에 다름 아니": "일본어투. -과 같다",
    "을 필요로 하": "영어 직역. -이 필요하다",
    "를 필요로 하": "영어 직역. -가 필요하다",
    "가지고 있": "영어 직역. 있다 · 지닌다",
    "아무리 강조해도 지나치지 않": "영어 관용구 직역",
    "에 값하": "번역투",
}

# 규칙 자체를 싣고 있는 파일
SKIP_NAMES = {"01_공통.md", "90_점검표.md", "점검.py"}

# 남의 글을 그대로 옮겨 둔 곳. 우리 용어 규칙을 적용하지 않는다.
SKIP_DIRS = ("근거_발췌", "원문발췌", "09_원자료", "_폐기",
             "__pycache__", ".git", "_workspace",
             os.sep + "dist")         # 배포_만들기.py 가 만든 사본. 원본을 이미 본다

# 이름이 이렇게 끝나면 인용 원문으로 본다
SKIP_SUFFIX = ("_원문", "_발췌", "_전사")

# 파일 안에 이 말이 있으면 건너뛴다
OPT_OUT = "점검예외"

# 구어 검사를 적용할 곳. 이름이나 경로에 이 말이 들어가면 엄격으로 본다.
엄격표시 = ("보고", "논문", "발표", "대본", "원고", "초록", "요약본")
엄격확장 = (".docx", ".hwpx")

TEXT_EXT = (".md", ".txt", ".py")


# ------------------------------------------------------------------ 읽기

def 읽기_글자(p):
    return open(p, encoding="utf-8", errors="ignore").read()


def 읽기_docx(p):
    try:
        import docx
    except ImportError:
        return None
    d = docx.Document(p)
    조각 = [x.text for x in d.paragraphs]
    for tb in d.tables:                       # 표 칸을 빼먹으면 놓친다
        for r in tb.rows:
            for c in r.cells:
                조각.append(c.text)
    return "\n".join(조각)


def 읽기_hwpx(p):
    z = zipfile.ZipFile(p)
    조각 = []
    for nm in z.namelist():
        if re.match(r"Contents/section\d+\.xml$", nm):
            s = z.read(nm).decode("utf-8", errors="ignore")
            조각 += re.findall(r"<hp:t>(.*?)</hp:t>", s, re.S)
    return "\n".join(조각)


def 본문(p):
    e = os.path.splitext(p)[1].lower()
    try:
        if e in TEXT_EXT:
            return 읽기_글자(p)
        if e == ".docx":
            return 읽기_docx(p)
        if e == ".hwpx":
            return 읽기_hwpx(p)
    except Exception as ex:
        return "\x00읽기실패:%s: %s" % (type(ex).__name__, ex)
    return None


def 엄격한가(p):
    """학술 용어를 써야 하는 문서인가. 이름과 확장자로 가린다.

    코드는 언제나 느슨하다. 06_코드 폴더가 보고서 폴더 아래 있다고 해서
    주석까지 학술 용어를 쓸 이유는 없다.
    """
    확장 = os.path.splitext(p)[1].lower()
    if 확장 == ".py":
        return False
    if 확장 in 엄격확장:
        return True
    return any(x in p for x in 엄격표시)


# ------------------------------------------------------------------ 검사

def 검사_오류(t):
    """막을 것. 기계로 확실한 것만."""
    난것 = []
    if t.startswith("\x00"):
        return [t[1:]]
    if EM_DASH in t:
        난것.append("em dash %d 개" % t.count(EM_DASH))
    if MINUS in t:
        난것.append("U+2212 %d 개" % t.count(MINUS))
    return 난것


def 검사_권고(t, 엄격):
    """보고만 할 것. 판단이 필요하므로 막지 않는다."""
    난것 = []
    for w, 대신 in 번역투.items():
        n = t.count(w)
        if n:
            난것.append("%s (%d) -> %s" % (w, n, 대신))
    if 엄격:
        for w, 대신 in 구어.items():
            n = t.count(w)
            if n:
                난것.append("%s (%d) -> %s" % (w, n, 대신))
    return 난것


# 아래 두 이름은 훅에서 부른다. 60_하네스.md 를 본다.
검사_글 = 검사_오류


def 모으기(뿌리들):
    파일 = []
    for 뿌리 in 뿌리들:
        if os.path.isfile(뿌리):
            파일.append(뿌리)
            continue
        건너뛸 = []
        for d, _, fs in os.walk(뿌리):
            if any(x in d for x in SKIP_DIRS):
                continue
            # 폴더 안에 .점검예외 파일이 있으면 그 아래를 통째로 뺀다. 옛 기록 보관용
            if ".점검예외" in fs:
                건너뛸.append(d)
            if any(d == s or d.startswith(s + os.sep) for s in 건너뛸):
                continue
            for f in fs:
                if f.startswith("~$"):        # Word 락 파일
                    continue
                if os.path.splitext(f)[1].lower() in TEXT_EXT + 엄격확장:
                    파일.append(os.path.join(d, f))
    return 파일


def main(뿌리들, 조용=False):
    파일 = 모으기(뿌리들)
    print("검사 대상 %d 개" % len(파일))
    print()

    오류수 = 0
    권고수 = 0
    권고파일 = 0
    빈파일 = []
    본적 = 0
    건너뜀 = 0

    for p in 파일:
        이름 = os.path.basename(p)
        if os.path.getsize(p) == 0:
            빈파일.append(p)
            continue
        if 이름 in SKIP_NAMES:
            continue
        if os.path.splitext(이름)[0].endswith(SKIP_SUFFIX):   # 인용 원문
            건너뜀 += 1
            continue
        t = 본문(p)
        if t is None:
            continue
        if OPT_OUT in t:
            건너뜀 += 1
            continue
        본적 += 1

        난것 = 검사_오류(t)
        if 난것:
            오류수 += len(난것)
            print("[오류] %s" % p)
            for x in 난것:
                print("        %s" % x)

        권고 = 검사_권고(t, 엄격한가(p))
        if 권고 and not 조용:
            권고수 += len(권고)
            권고파일 += 1
            print("[권고] %s%s" % (p, "  (엄격)" if 엄격한가(p) else ""))
            for x in 권고:
                print("        %s" % x)
        elif 권고:
            권고수 += len(권고)
            권고파일 += 1

    print()
    print("훑은 파일 %d 개" % 본적, end="")
    print(" (점검예외 %d 개)" % 건너뜀 if 건너뜀 else "")
    if 빈파일:
        print("[빈 파일] %d 개" % len(빈파일))
        for p in 빈파일[:10]:
            print("        %s" % p)
    if 권고수:
        print("[권고] %d 건 · %d 파일. 막지 않는다. 문맥을 보고 판단해라"
              % (권고수, 권고파일))
    if 본적 == 0:
        print("[경고] 훑은 파일이 0 개다. 경로가 맞는지 본다")
        return 1
    if 오류수 or 빈파일:
        print("[결과] 오류 %d 건. 고치고 다시 돌린다" % (오류수 + len(빈파일)))
        return 1
    print("[결과] 오류 없음")
    return 0


if __name__ == "__main__":
    인자 = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not 인자:
        인자 = [os.path.dirname(os.path.dirname(os.path.abspath(__file__)))]
    sys.exit(main(인자, 조용="--조용" in sys.argv))
