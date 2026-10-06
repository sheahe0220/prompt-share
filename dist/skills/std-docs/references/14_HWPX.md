# HWPX 보고서

`01_공통.md` 뒤에 붙인다. 한글 문서로 보고서를 만들거나 고칠 때 쓴다.
docx 로 만들 때는 `11_보고서.md` 를 본다. 조판 원칙(판형·캡션·표·서술)은 그
문서와 같으므로 여기서는 **HWPX 에서만 다른 것**만 적는다.

여기 적힌 코드와 값은 표시가 없는 한 이 컴퓨터에서 실제로 돌려 확인한 것이다.
확인 환경은 한글 Office 2024 (HOffice130, Version 13,0,0,564), `pyswmm` env
python 3.11.14, pywin32. 남의 기록을 옮긴 것은 `[남의 기록]` 으로 표시했다.

---

## 가장 중요한 것

**한글로 양식을 한 번 만들어 두고, 그다음부터는 값만 채워라.**
**HWPX 를 처음부터 만들어 내지 마라.**

이것이 이 문서에서 가장 값어치 있는 두 줄이다. 근거가 셋이다.

**첫째, 고쳐 쓰는 것은 된다.** 한글이 저장한 실제 보고서를 풀어 `section0.xml`
의 글자를 바꾸고 다시 압축한 파일을 한글로 열어 확인했다. 정상으로 열리고
글자가 바뀌어 있었다.

**둘째, 처음부터 만드는 것은 깨진다.** `[남의 기록]` `pypandoc-hwpx` 로 md 에서
HWPX 를 직접 만든 기록이 있다.

```text
검증기 hwpx-validate-package    ERROR 0 통과
실제 한글에서 열기               열리기도 하고 한글이 죽기도 한다. 시도마다 다르다
크래시                          com_error(-2147023170, 원격 프로시저를 호출하지 못했습니다)
원인                            파일 크기 · 특수문자 · 문법 요소로 좁혀지지 않았다
결론                            재현이 불안정해 정상이라고 보증할 수 없다
```

**셋째, 나도 같은 불안정을 겪었다.** 양식을 만들고 치환하고 여는 시험을 되풀이
하는 동안, 같은 파일이 어떤 때는 열리고 어떤 때는 안 열렸다. 나중에는 한글
COM 자체가 죽어 `Run("FileNew")` 조차 `com_error(-2147417851)` 를 냈다.

여기서 나오는 규칙 셋이다.

**검증기 통과는 열린다는 뜻이 아니다.** 최종 확인은 반드시 한글에서 실제로
열어 보는 것이어야 한다.

**한 번 열렸다고 믿지 마라.** 되풀이해 확인한다. 대량으로 만들 때는 만든 것을
전부 열어 본다.

**자동 변환한 문서는 원본과 글자 수를 대조하라.** `[남의 기록]`
`pypandoc-hwpx` 가 인용문(`>` 블록)과 큰따옴표로 감싼 구간을 **오류도 경고도
없이 통째로** 지웠다. 한글 보존율이 78~97 퍼센트였는데 대조하지 않았으면
못 잡았다.

---

## 어느 길로 갈 것인가

```text
1  한글 COM         한글을 띄워 부린다.  양식 만들기 · 조판 · PDF · 최종 확인
                    한글이 깔려 있어야 한다. 느리고 가끔 불안정하다

2  python-hwpx      순수 파이썬. 한글 없이 hwpx 를 읽고 고친다
                    양식의 표에 값 넣기. 안 건드린 바이트는 그대로 둔다
                    ★ 값 채우기의 주력으로 삼는다

3  직접 XML         zip 을 풀어 고치고 다시 압축한다. 의존성이 없다
                    글자 바꾸기와 글자 뽑기까지. 원리를 알아야 할 때 쓴다
```

**양식은 1 로 만들고, 값은 2 로 채우고, 확인은 다시 1 로 한다.**
3 은 라이브러리를 못 쓸 때의 최후 수단이다.

---

## 도구

이 컴퓨터에는 **아무것도 설치되어 있지 않다.** 쓰려면 먼저 깔아야 한다.

```text
python-hwpx      한글 불필요.  pip install python-hwpx   (python 3.10+)
                 읽기 · 고치기 · 만들기 · 검증. 라벨로 표 칸을 찾아 채운다
                 안 건드린 부분은 바이트 그대로 둔다
                 https://github.com/airmang/python-hwpx

hwpx-plugin      Claude Code 플러그인. 위 라이브러리와 MCP 를 함께 붙인다
                   claude plugin marketplace add airmang/hwpx-plugins
                   claude plugin install hwpx-plugin@hwpx
                 상태는 알파다. 보고서 본편에 바로 쓰지 마라
                 https://github.com/airmang/hwpx-skill

hwpx-mcp-server  MCP 서버. 한글 없이 문서 생성 · 편집 · 탐색
                 https://github.com/airmang/hwpx-mcp-server

treesoop/hwp-mcp MCP. HWP 바이너리까지 읽는다. 도구 34개
                 https://github.com/treesoop/hwp-mcp

pyhwpx           한글 필요. COM 을 감싼 것. 표를 DataFrame 으로 주고받고
                 put_field_text 로 누름틀에 값을 넣는다
                 https://github.com/martiniifun/pyhwpx

pypandoc-hwpx    md -> hwpx 직접 변환. 위에 적은 이유로 보고서에 쓰지 마라

한컴 공식         https://developer.hancom.com/opensources   dvc 검증기 등
                 https://tech.hancom.com/hwpxformat/         HWPX 구조 해설
```

**성숙도를 기능보다 앞에 둔다.** 보고서는 틀렸을 때 값이 크다. 알파 딱지가
붙은 것은 시험용으로만 쓰고, 산출에 쓰기 전에 열어 보는 절차를 반드시 둔다.

### 안 되는 길

```text
LibreOffice 로 hwp 열기      안 된다. HWP 97 만 열고 5.x 는 못 연다
Pandoc 으로 hwpx 만들기       안 된다. pandoc 은 hwpx 를 지원하지 않는다
```

### 되는 우회로

자동 생성이 미덥지 않으면 이 길이 확실하다.

```text
md  --pandoc-->  docx  --사람이 한글로 열어 저장-->  hwpx
```

중간에 사람 손이 한 번 들어가지만 깨지지 않는다.

```bash
pandoc 보고서.md -o 보고서.docx --reference-doc=서식.docx --toc --toc-depth=3
```

`[남의 기록]` **python-docx 로 서식을 만들 때 `font.name` 만 지정하면 한글에는
안 걸린다.** `w:rFonts` 의 `w:eastAsia` 속성을 함께 지정해야 한다.
`11_보고서.md` 에도 해당하는 함정이다.

---

## 양식을 만들고 값을 채우는 법

이것이 주력 방식이다. **양식은 한 번만 만들고 계속 쓴다.**

### 1단계. 양식을 만든다

한글에서 손으로 만들어도 되고 COM 으로 만들어도 된다. **손으로 만드는 편이
안전하다.** 조판을 눈으로 확인하며 만들 수 있기 때문이다.

값이 들어갈 자리를 어떻게 표시할지 두 가지다.

```text
표식 문자열   {{사상명}} 처럼 본문에 적어 둔다
              장점  라이브러리 없이도 바꿀 수 있다. 눈에 보인다
              단점  실수로 지워지면 모른다

누름틀        한글의 누름틀(필드)을 넣는다
              장점  이름으로 찾는다. 서식이 유지된다
              단점  한글이나 pyhwpx 가 있어야 한다
```

**표식은 한 줄에 하나씩, 앞뒤에 다른 글자를 붙이지 마라.** 한글이 글자를 여러
`<hp:t>` 토막으로 쪼개면 표식이 갈라져 찾지 못한다. 채우기 전에 몇 곳이
잡혔는지 반드시 세어 본다.

누름틀은 COM 으로 이렇게 넣는다. 넣고 나서 목록에 잡히는 것을 확인했다.

```python
hwp.HAction.GetDefault("InsertFieldTemplate",
                       hwp.HParameterSet.HInsertFieldTemplate.HSet)
ft = hwp.HParameterSet.HInsertFieldTemplate
ft.TemplateName      = "작성자"
ft.TemplateDirection = "작성자를 적는 곳"      # 비어 있을 때 보이는 안내
hwp.HAction.Execute("InsertFieldTemplate", ft.HSet)

hwp.GetFieldList(1, 0)      # -> '작성자{{0}}'   목록에 잡힌다
```

### 2단계. 값을 채운다

**python-hwpx 로 채우는 것이 가장 안전하다.** 안 건드린 부분을 바이트 그대로
두기 때문이다. 만든 쪽 설명으로는 실제 한컴오피스에서 120건 중 120건이 정상으로
열렸다고 한다. `[남의 기록]`

```python
from hwpx.document import HwpxDocument     # pip install python-hwpx

doc = HwpxDocument.open("양식.hwpx")
doc.fill_by_path({                          # 표 칸을 라벨로 찾아 채운다
    "사상명 > right": "2021-1",
    "총강수량 > right": "66.0",
})
doc.save_to_path("과업1_사상별요약_v2.hwpx")
```

한글이 있으면 누름틀에 바로 넣을 수 있다. COM 으로 확인했다.

```python
hwp.Open(양식, "HWPX", "forceopen:true")
hwp.PutFieldText("작성자", "정상곤")
hwp.SaveAs(산출, "HWPX", "")
```

### 3단계. 열어서 확인한다

**빼먹지 마라.** 이 단계가 이 문서의 존재 이유다.

```python
hwp.Open(산출, "HWPX", "forceopen:true")     # 예외가 나면 깨진 것이다
t = hwp.GetTextFile("TEXT", "")
assert "2021-1" in t,  "값이 안 들어갔다"
assert "{{" not in t,  "안 채운 표식이 남았다"
```

대량으로 만들었으면 **전부 열어 본다.** 하나가 열린다고 나머지가 열리는 것이
아니다.

---

## 1부. 한글 COM 자동화

### 준비

```python
import win32com.client as win32

hwp = win32.Dispatch("HWPFrame.HwpObject")
hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")
hwp.Run("FileNew")                              # 열기 전에 문서를 하나 연다
hwp.XHwpWindows.Item(0).Visible = False
```

**`gencache.EnsureDispatch` 를 첫 실행에 쓰지 마라.** 타입 라이브러리를 만드느라
2분이 넘게 걸려 멈춘 것처럼 보인다. 실제로 120초 시간초과로 죽었다. 캐시가
만들어진 뒤에는 즉시 뜬다. **`win32.Dispatch` 를 써라.** 속성 이름을 들여다볼
때만 `EnsureDispatch` 를 쓴다.

**`RegisterModule` 이 `False` 를 돌려줘도 그냥 진행하라.** 이 컴퓨터에서는 보안
모듈이 등록되어 있지 않아 `False` 가 나오는데, 그래도 열기와 저장이 정상으로
됐다. `False` 를 보고 멈추지 마라.

**`Open` 전에 `Run("FileNew")` 를 부른다.** 문서가 하나도 없는 상태에서 바로
`Open` 하면 `com_error` 가 나는 경우가 있었다.

**반드시 `Quit()` 한다.** 안 하면 `Hwp.exe` 가 보이지 않는 채로 남는다.

```python
try:
    ...
finally:
    try:
        hwp.Quit()
    except Exception:
        pass
```

```bash
tasklist //FI "IMAGENAME eq Hwp.exe"        # 남았는지 확인
```

**COM 인스턴스를 되풀이해 만들고 죽이지 마라.** 시험 중에 그렇게 했더니 한글이
불안정해져서 `Run("FileNew")` 조차 실패하기 시작했다. **하나를 만들어 끝까지
쓰고 마지막에 한 번만 `Quit` 한다.** 이미 불안정해졌으면 `Hwp.exe` 를 모두 죽이고
다시 시작한다.

### 단위

**HWPUNIT 은 1/7200 인치다.** 실제 파일에서 재어 확인했다. A4 폭 210 mm 가
`59528` 로 적혀 있고 `59528 / 210 = 283.47` 이다.

```text
1 인치  = 7200 HWPUNIT
1 mm    =  283.465 HWPUNIT
1 cm    = 2834.65  HWPUNIT
```

**직접 곱하지 말고 변환 함수를 써라.** 둘 다 확인했다.

```python
hwp.MiliToHwpUnit(170.0)     # -> 48189   길이
hwp.PointToHwpUnit(11.0)     # -> 1100    글자 크기
```

글자 크기는 **1/100 pt** 로 들어간다. 11 pt 가 `1100` 이다.

### 판형

`11_보고서.md` 와 같이 A4 세로, 본문 폭 17 cm 를 기본으로 한다.

```python
hwp.HAction.GetDefault("PageSetup", hwp.HParameterSet.HSecDef.HSet)
sec = hwp.HParameterSet.HSecDef
sec.PageDef.PaperWidth   = hwp.MiliToHwpUnit(210.0)
sec.PageDef.PaperHeight  = hwp.MiliToHwpUnit(297.0)
sec.PageDef.LeftMargin   = hwp.MiliToHwpUnit(20.0)
sec.PageDef.RightMargin  = hwp.MiliToHwpUnit(20.0)
sec.PageDef.TopMargin    = hwp.MiliToHwpUnit(20.0)
sec.PageDef.BottomMargin = hwp.MiliToHwpUnit(15.0)
hwp.HAction.Execute("PageSetup", sec.HSet)
```

여백을 좌우 20 mm 로 두면 본문 폭이 170 mm 다. **그림을 17 cm 로 그려 1:1 로
넣으면 딱 맞는다.** `10_그림.md` 의 `PRINT_W_CM = 17.0` 과 짝이다.

### 글자 넣기

```python
def 글(hwp, t):
    hwp.HAction.GetDefault("InsertText", hwp.HParameterSet.HInsertText.HSet)
    hwp.HParameterSet.HInsertText.Text = t
    hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)

글(hwp, "1. 서론")
hwp.Run("BreakPara")            # 문단 나눔
```

**`InsertText` 는 줄바꿈을 넣지 않는다.** 문단을 나누려면 `BreakPara` 를 따로
부른다. 문자열에 `\n` 을 넣어 해결하려 하지 마라.

### 글자모양과 문단모양

```python
hwp.HAction.GetDefault("CharShape", hwp.HParameterSet.HCharShape.HSet)
cs = hwp.HParameterSet.HCharShape
cs.Height         = hwp.PointToHwpUnit(11.0)
cs.FaceNameHangul = "함초롬바탕"
cs.FaceNameLatin  = "Times New Roman"
hwp.HAction.Execute("CharShape", cs.HSet)

hwp.HAction.GetDefault("ParagraphShape", hwp.HParameterSet.HParaShape.HSet)
ps = hwp.HParameterSet.HParaShape
ps.AlignType   = 3        # 양쪽 정렬
ps.LineSpacing = 160      # 줄간격 160 %
hwp.HAction.Execute("ParagraphShape", ps.HSet)
```

**한글 글꼴과 라틴 글꼴을 따로 지정한다.** 하나만 지정하면 숫자와 영문이 한글
글꼴로 나와 어색해진다.

실제 문서에 들어 있던 글꼴 이름이다. 이 이름을 그대로 써야 한다.

```text
함초롬바탕 · 함초롬돋움 · 한컴바탕 · 돋움체 · 맑은 고딕 · 신명 태고딕
```

문단 스타일은 단축으로도 걸린다. 개요 수준을 주면 나중에 차례가 잡힌다.

```python
hwp.Run("StyleShortcut1")     # 개요 1
hwp.Run("StyleShortcut2")     # 개요 2
```

### 표

```python
hwp.HAction.GetDefault("TableCreate", hwp.HParameterSet.HTableCreation.HSet)
t = hwp.HParameterSet.HTableCreation
t.Rows, t.Cols = 3, 4
t.WidthType, t.HeightType = 0, 0
t.CreateItemArray("ColWidth", 4)              # 반드시 먼저 배열을 만든다
for i in range(4):
    t.ColWidth.SetItem(i, hwp.MiliToHwpUnit(40.0))
hwp.HAction.Execute("TableCreate", t.HSet)
```

**`CreateItemArray` 를 먼저 부르지 않으면 `ColWidth.SetItem` 이 안 된다.**

표를 만들면 커서가 표 안에 있다. **다음 것을 넣기 전에 표 밖으로 나와야 한다.**

```python
hwp.Run("CloseEx")        # 표 밖으로
hwp.Run("MoveDocEnd")     # 문서 끝으로
```

칸 폭의 합이 본문 폭(170 mm)을 넘지 않게 한다. 넘으면 표가 지면 밖으로 나간다.

### 그림

```python
hwp.InsertPicture(경로, True, 0, False, False, 0)
```

인수는 `(경로, 문서에 포함, 크기방식, 뒤집기, 반전, 각도)` 순이다.
**두 번째를 `True` 로 두어 그림을 문서 안에 넣는다.** `False` 로 두면 연결만
되어, 그림 파일을 옮기면 보고서에서 사라진다.

**경로는 절대경로여야 한다.** 크기는 `10_그림.md` 대로 **인쇄 크기 그대로 그려서
1:1 로 넣는다.** 넣고 나서 줄이면 글자가 같이 줄어든다.

### 쪽번호

```python
hwp.HAction.GetDefault("PageNumPos", hwp.HParameterSet.HPageNumPos.HSet)
pn = hwp.HParameterSet.HPageNumPos
pn.DrawPos      = 6      # 아래 가운데
pn.NumberFormat = 0      # 아라비아 숫자
hwp.HAction.Execute("PageNumPos", pn.HSet)
```

**속성 이름은 `DrawPos` 다. `Pos` 가 아니다.** `Pos` 로 쓰면
`AttributeError: object has no attribute 'Pos'` 가 난다. 실제로 걸렸다.

속성 이름이 헷갈리면 그 자리에서 찍어 본다. 문서를 찾는 것보다 빠르다.

```python
o = hwp.HParameterSet.HPageNumPos
print([n for n in dir(o) if n[0].isupper()])
# ['CLSID','CreateItemArray','DrawPos','HSet','NewNumber','NumberFormat',
#  'PrefixChar','SideChar','SuffixChar','UserChar']
```

### 찾아 바꾸기

```python
hwp.HAction.GetDefault("AllReplace", hwp.HParameterSet.HFindReplace.HSet)
f = hwp.HParameterSet.HFindReplace
f.FindString    = "2021E10"
f.ReplaceString = "2021-1"
f.IgnoreMessage = 1                 # 끝났다는 대화상자를 막는다
hwp.HAction.Execute("AllReplace", f.HSet)
```

**`IgnoreMessage = 1` 을 빼지 마라.** 빼면 다 바꾼 뒤 대화상자가 떠서 스크립트가
멈춘 채로 남는다.

`11_보고서.md` 의 경고가 여기에도 해당한다. `AllReplace` 는 본문과 표는 훑지만
**그림 안 글자는 못 바꾼다.** 그림은 다시 그려야 한다.

### 읽기와 세기

```python
n = hwp.PageCount                    # 쪽 수
t = hwp.GetTextFile("TEXT", "")      # 본문 전체를 글자로
```

`GetTextFile` 은 `90_점검표.md` 의 금지어 검사에 그대로 쓴다.

### 저장과 PDF

```python
hwp.SaveAs(r"C:\...\보고서_v2.hwpx", "HWPX", "")
hwp.SaveAs(r"C:\...\보고서_v2.pdf",  "PDF",  "")
```

둘 다 되는 것을 확인했다. **PDF 를 만들 수 있으므로 `12_발표대본.md` 의 쪽 색인은
Word 를 거치지 않고 한글에서 바로 뽑는다.**

**덮어쓰지 마라.** `_v2` · `_v3` 로 번호를 올린다.

### 확인한 목록

```text
됨    InsertText · BreakPara · StyleShortcut1
됨    CharShape · ParagraphShape · PageSetup
됨    PointToHwpUnit · MiliToHwpUnit
됨    TableCreate (CreateItemArray 먼저) · CloseEx · MoveDocEnd
됨    InsertPicture
됨    PageNumPos (Pos 아니라 DrawPos)
됨    AllReplace (IgnoreMessage=1)
됨    InsertFieldTemplate · GetFieldList · PutFieldText
됨    GetTextFile · PageCount
됨    SaveAs HWPX · SaveAs PDF · Open forceopen:true
```

여기 없는 기능(차례 자동 생성, 머리말, 각주, 캡션 번호 자동 매기기)은
**확인하지 않았다.** 쓰기 전에 짧은 스크립트로 먼저 시험하고, 되면 이 목록에
한 줄 더한다.

`[남의 기록]` 표와 그림의 캡션 번호는 HWPX 에서 필드로 저장된다. 스크립트로
넣은 뒤 한글에서 "번호 다시 매기기"를 해야 번호가 맞는다.

---

## 2부. 직접 XML 다루기

라이브러리를 못 쓸 때의 최후 수단이다. **평소에는 python-hwpx 를 쓴다.**
원리를 알아야 문제가 났을 때 진단할 수 있으므로 적어 둔다.

### 구조

hwpx 는 zip 이다. 실제 파일을 풀면 이렇다.

```text
mimetype                  'application/hwp+zip'   무압축. 반드시 첫 항목
version.xml               한글 판번호             무압축
Contents/header.xml       글꼴 · 글자모양 · 문단모양 · 스타일 정의
Contents/section0.xml     본문. 쪽 설정과 글자가 여기 있다
Contents/content.hpf      묶음 명세
settings.xml
META-INF/container.xml    어디가 본체인지 가리킨다
META-INF/manifest.xml
META-INF/container.rdf
Preview/PrvText.txt       미리보기 글자 (UTF-8)
Preview/PrvImage.png      미리보기 그림
```

본문 문단은 이렇게 생겼다.

```xml
<hp:p paraPrIDRef="22" styleIDRef="0">
  <hp:run charPrIDRef="14">
    <hp:t>GK2A 위성 강우자료의 도시 유역 SWMM 적용성 평가</hp:t>
  </hp:run>
</hp:p>
```

```text
hp:p    문단.  paraPrIDRef 가 header.xml 의 문단모양을 가리킨다
hp:run  같은 글자모양이 이어지는 토막.  charPrIDRef 가 글자모양
hp:t    실제 글자.  찾아 바꿀 때 여기만 건드리면 된다
```

쪽 설정은 `section0.xml` 안에 있다.

```xml
<hp:pagePr width="59528" height="84188">
  <hp:margin left="8504" right="8504" top="5668" bottom="4252"
             header="4252" footer="4252"/>
</hp:pagePr>
```

`59528 / 283.465 = 210 mm`, `8504 / 283.465 = 30 mm` 다.

### 고쳐서 다시 압축하기

**`mimetype` 을 맨 앞에 무압축으로 두어야 한다.**

```python
import os, zipfile

def hwpx_고치기(src, dst, fn):
    """Contents/section*.xml 만 fn 으로 바꾸고 나머지는 그대로 옮긴다."""
    zin = zipfile.ZipFile(src)
    assert zin.namelist()[0] == "mimetype", \
        "mimetype 이 첫 항목이 아니다: %s" % zin.namelist()[0]

    if os.path.exists(dst):
        os.remove(dst)
    zout = zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED)
    바꾼수 = 0
    for info in zin.infolist():
        data = zin.read(info.filename)
        if info.filename.startswith("Contents/section"):
            s = data.decode("utf-8")
            s, n = fn(s)
            바꾼수 += n
            data = s.encode("utf-8")
        ct = (zipfile.ZIP_STORED
              if info.filename in ("mimetype", "version.xml")
              else zipfile.ZIP_DEFLATED)
        zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
        zi.compress_type = ct
        zi.external_attr = info.external_attr
        zout.writestr(zi, data)
    zout.close()
    zin.close()
    assert 바꾼수 > 0, "바꿀 것을 하나도 못 찾았다"
    return 바꾼수
```

쓰는 쪽. **몇 곳을 바꿨는지 반드시 센다.**

```python
def 바꾸기(xml):
    n = xml.count("{{사상명}}")
    print("[바꿈] %d 곳" % n)
    return xml.replace("{{사상명}}", "2021-1"), n

hwpx_고치기(양식, 산출, 바꾸기)
```

**`section0.xml` 하나만 보지 마라.** 문서가 길면 `section1.xml`, `section2.xml`
로 갈린다. 위 코드처럼 `Contents/section` 으로 시작하는 것을 전부 훑는다.

### 고친 뒤 검증

```python
z = zipfile.ZipFile(산출)
assert z.testzip() is None                          # zip 무결성
assert z.namelist()[0] == "mimetype"
assert z.infolist()[0].compress_type == zipfile.ZIP_STORED

import xml.etree.ElementTree as ET
ET.fromstring(z.read("Contents/section0.xml"))      # XML 이 깨지지 않았나
```

**여기까지 통과해도 한글이 여는지는 별개다.** 실제로 이 검사를 다 통과한
파일이 한글에서 안 열린 적이 있다. 반드시 열어서 확인한다.

### 글자만 뽑기

한글 없이 본문만 읽을 때 쓴다. `22_문서분석.md` 의 훑기에 그대로 쓸 수 있다.

```python
import re, zipfile

def hwpx_글자(path):
    z = zipfile.ZipFile(path)
    out = []
    for nm in z.namelist():
        if re.match(r"Contents/section\d+\.xml$", nm):
            s = z.read(nm).decode("utf-8")
            out += re.findall(r"<hp:t>(.*?)</hp:t>", s, re.S)
    return "\n".join(out)
```

---

## 함정

```text
증상  스크립트가 아무 것도 찍지 않고 2분 넘게 멈춰 있다
원인  gencache.EnsureDispatch 가 타입 라이브러리를 처음 만들고 있다
      실제로 120초 시간초과로 죽었다. 두 번째부터는 즉시 뜬다
대처  win32.Dispatch 를 쓴다. 그리고 python 을 -u 로 돌린다
      -u 가 없으면 print 가 버퍼에 갇혀 어디서 멈췄는지도 알 수 없다
```

```text
증상  RegisterModule 이 False 를 돌려준다
원인  보안 모듈이 등록되어 있지 않다
      (HKCU\Software\HNC\HwpAutomation\Modules 에 값이 0 개)
대처  그대로 진행한다. 이 상태에서도 Open 과 SaveAs 가 정상으로 됐다
```

```text
증상  Open 에서 com_error(-2147417851, 서버에서 예외 오류) 가 난다
원인  문서가 하나도 없는 상태에서 바로 Open 했다. 또는 파일이 깨졌다
대처  Open 앞에 Run("FileNew") 를 부른다. 그래도 나면 파일이 깨진 것이다
```

```text
증상  같은 파일이 어떤 때는 열리고 어떤 때는 한글이 죽는다
원인  COM 인스턴스를 되풀이해 만들고 죽여 한글이 불안정해졌다
      나중에는 Run("FileNew") 조차 실패했다
대처  인스턴스 하나를 끝까지 쓰고 마지막에 한 번만 Quit 한다
      이미 불안정하면 Hwp.exe 를 모두 죽이고 다시 시작한다
      tasklist //FI "IMAGENAME eq Hwp.exe"
```

```text
증상  hwpx 를 만들어 냈는데 한글에서 빈 문서가 뜨거나 한글이 죽는다
원인  HWPX 를 처음부터 만들어 냈다.  [남의 기록] 도 같은 증상이다
대처  한글이 만든 양식을 열어 값만 바꾸는 방식으로 바꾼다
```

```text
증상  변환은 성공했다는데 내용이 줄었다
원인  변환기가 인용문과 따옴표 구간을 오류 없이 지웠다  [남의 기록]
대처  원본과 글자 수를 대조한다. 보존율이 100 퍼센트가 아니면 쓰지 않는다
```

```text
증상  표식 {{...}} 을 넣었는데 치환에서 안 잡힌다
원인  한글이 글자를 여러 hp:t 토막으로 쪼개 표식이 갈라졌다
대처  바꾼 개수를 세어 0 이면 멈춘다. 표식은 한 줄에 하나만 두고
      앞뒤에 다른 글자를 붙이지 않는다
```

```text
증상  pn.Pos = 6 에서 AttributeError 가 난다
원인  쪽번호 위치 속성 이름은 DrawPos 다
대처  dir(o) 로 속성 이름을 찍어 확인한다
```

```text
증상  TableCreate 에서 ColWidth.SetItem 이 안 된다
원인  CreateItemArray("ColWidth", 칸수) 를 먼저 부르지 않았다
대처  배열을 먼저 만들고 SetItem 한다
```

```text
증상  표를 만든 뒤 넣은 글자가 표 안으로 들어간다
원인  표를 만들면 커서가 표 안에 남는다
대처  Run("CloseEx") 로 나오고 Run("MoveDocEnd") 로 끝으로 간다
```

```text
증상  AllReplace 뒤에 스크립트가 멈춘 채로 남는다
원인  다 바꿨다는 대화상자가 떴다
대처  IgnoreMessage = 1 을 준다
```

```text
증상  보고서를 옮겼더니 그림이 사라졌다
원인  InsertPicture 의 두 번째 인수를 False 로 두어 연결만 되었다
대처  True 로 두어 문서 안에 넣는다
```

```text
증상  hwpx 를 고쳐 다시 압축했더니 한글이 못 연다
원인  mimetype 이 첫 항목이 아니거나 압축되었다
대처  mimetype 을 맨 앞에 ZIP_STORED 로 쓴다
```

```text
증상  글자를 바꿨는데 탐색기 미리보기에는 옛 글자가 보인다
원인  Preview/PrvText.txt 와 PrvImage.png 는 그대로 옮겨졌다
대처  본문에는 지장이 없다. 신경 쓰이면 한글로 한 번 열어 다시 저장한다
```

```text
증상  긴 문서인데 뒷부분 글자가 안 잡힌다
원인  Contents/section0.xml 만 읽었다. 길면 section1, section2 로 갈린다
대처  section\d+\.xml 을 전부 훑는다
```

```text
증상  Hwp.exe 가 보이지 않는 채로 쌓인다
원인  예외가 나서 Quit() 를 못 부르고 끝났다
대처  try ... finally 로 감싼다
```
