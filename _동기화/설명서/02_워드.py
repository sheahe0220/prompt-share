r"""본문.txt(간단한 표시법) + 그림\ 으로 사용설명서 Word 와 PDF 를 만들고, 쪽마다 그림으로 뽑아 점검한다.

왜 있나
  지인(토목 설계 실무, AI 처음)에게 zip 으로 줄 "VS Code 에서 클로드 코드 쓰기" 사용설명서
  (2026-09-29 사용자 요청). 판형은 메이플 대시보드 설치안내(03_make_docx.py)를 따른다:
  A4, 여백 2 cm, 맑은 고딕 12pt, 줄 간격 1.25, 제목 주황 #E8590C, 가운데 아래 쪽번호, 그림 아래 회색 캡션.
  같은 스크립트가 명령 총정리(명령총정리.txt)도 만든다(--본문 으로 바꿔 줌).
  산출은 _v1, _v2 ... 로 번호를 올리고 덮어쓰지 않는다.

표시법 (본문 파일)
  #표지 제목 / @부제 글 / # 장 / ## 절 / @쪽나눔
  @상자 머리 | 첫 줄        (다음 줄들은 빈 줄까지 같은 상자)
  @팁 글 / @주의 글 / @작게 글
  @표 ... @끝               (칸은 " | ", 첫 줄은 머리)
  [그림 파일.png | 캡션]  또는  [그림 파일.png | 캡션 | 최대 높이 cm]
  ① ... 로 시작하는 줄은 단계, 그 밖의 줄은 문단. **굵게**

실행
  C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe -X utf8 _동기화\설명서\02_워드.py
  ... --본문 명령총정리.txt --이름 클로드코드_명령총정리
"""
import os
import re
import sys
import warnings

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from PIL import Image

warnings.filterwarnings("error", category=DeprecationWarning)

여기 = os.path.dirname(os.path.abspath(__file__))
그림폴더 = os.path.join(여기, "그림")
출력폴더 = os.path.join(여기, "산출")


def 인자(이름, 기본):
    return sys.argv[sys.argv.index(이름) + 1] if 이름 in sys.argv else 기본


본문파일 = os.path.join(여기, 인자("--본문", "본문.txt"))
기본이름 = 인자("--이름", "VSCode_클로드코드_사용설명서")

주황 = RGBColor(0xE8, 0x59, 0x0C)
회색 = RGBColor(0x55, 0x55, 0x55)
본문폭, 그림최대높이 = 17.0, 7.5   # cm (v3: 9.0 left single boxes stranded on pages 8 and 13)
단계 = "①②③④⑤⑥⑦⑧⑨⑩"
셈 = {"그림": 0, "표": 0, "상자": 0, "장": 0}

doc = Document()
st = doc.styles["Normal"]
st.font.name = "맑은 고딕"
st.element.rPr.rFonts.set(qn("w:eastAsia"), "맑은 고딕")
st.font.size = Pt(11.5)
st.paragraph_format.space_after = Pt(4)
st.paragraph_format.line_spacing = 1.25
for 이름, 크기 in (("Heading 1", 18), ("Heading 2", 14.5), ("Title", 26)):
    h = doc.styles[이름]
    h.font.name = "맑은 고딕"
    h.element.rPr.rFonts.set(qn("w:eastAsia"), "맑은 고딕")
    h.font.size = Pt(크기)
    h.font.color.rgb = 주황 if 이름 != "Title" else RGBColor(0x22, 0x22, 0x22)
s = doc.sections[0]
s.page_width, s.page_height = Cm(21.0), Cm(29.7)
s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Cm(2.0)


def 쪽번호(section):
    p = section.footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for kind, txt in (("begin", None), (None, "PAGE"), ("separate", None), ("end", None)):
        r = p.add_run()
        e = OxmlElement("w:fldChar") if kind else OxmlElement("w:instrText")
        if kind:
            e.set(qn("w:fldCharType"), kind)
        else:
            e.set(qn("xml:space"), "preserve")
            e.text = txt
        r._r.append(e)


def 굵게넣기(p, text, size=None, color=None):
    for i, t in enumerate(text.split("**")):
        if not t:
            continue
        r = p.add_run(t)
        r.bold = i % 2 == 1
        if size:
            r.font.size = Pt(size)
        if color:
            r.font.color.rgb = color


def 문단(text, size=None, color=None, align=None, indent=None):
    p = doc.add_paragraph()
    굵게넣기(p, text, size, color)
    if align is not None:
        p.alignment = align
    if indent:
        p.paragraph_format.left_indent = Cm(indent)
    return p


def 칠하기(cell, hexfill):
    tcPr = cell._tc.get_or_add_tcPr()
    e = OxmlElement("w:shd")
    e.set(qn("w:val"), "clear")
    e.set(qn("w:fill"), hexfill)
    tcPr.append(e)


def 셀글(cell, text, bold_all=False, size=None):
    cell.text = ""
    줄 = text.split("\n")
    for k, ln in enumerate(줄):
        p = cell.paragraphs[0] if k == 0 else cell.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        굵게넣기(p, "**%s**" % ln if bold_all else ln, size)


def 그림(파일, 캡션, 최대높이=None):
    p0 = os.path.join(그림폴더, 파일)
    assert os.path.exists(p0), "그림이 없다: %s" % p0
    iw, ih = Image.open(p0).size
    w = 본문폭
    h = w * ih / iw
    한도 = 최대높이 or 그림최대높이
    if h > 한도:
        h, w = 한도, 한도 * iw / ih
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(p0, width=Cm(w), height=Cm(h))
    c = 문단(캡션, size=10, color=회색, align=WD_ALIGN_PARAGRAPH.CENTER)
    c.paragraph_format.space_after = Pt(10)
    셈["그림"] += 1


def 표(행들):
    칸수 = len(행들[0])
    assert all(len(r) == 칸수 for r in 행들), "표 칸 수가 다르다: %s" % 행들[0]
    t = doc.add_table(rows=0, cols=칸수)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    # column widths follow the mean text length (equal widths wasted space on short columns)
    평균 = [sum(len(r[j]) for r in 행들) / len(행들) for j in range(칸수)]
    몫 = [max(2.2, a) ** 0.8 for a in 평균]
    너비 = [max(1.8, 본문폭 * m / sum(몫)) for m in 몫]
    너비 = [w * 본문폭 / sum(너비) for w in 너비]
    for i, r in enumerate(행들):
        cells = t.add_row().cells
        for j, v in enumerate(r):
            cells[j].width = Cm(너비[j])
            셀글(cells[j], v, bold_all=(i == 0), size=10)
            for p in cells[j].paragraphs:
                p.paragraph_format.line_spacing = 1.0
            if i == 0:
                칠하기(cells[j], "FDE7DA")
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    셈["표"] += 1


def 상자(머리, 줄들, fill="F4F4F4"):
    t = doc.add_table(rows=1, cols=2)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    a, b = t.rows[0].cells
    a.width, b.width = Cm(3.0), Cm(14.0)
    셀글(a, 머리, bold_all=True, size=10.5)
    칠하기(a, "FDE7DA")
    셀글(b, "\n".join(줄들), size=10.5)
    칠하기(b, fill)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    셈["상자"] += 1


def main():
    줄 = open(본문파일, encoding="utf-8").read().split("\n")
    쪽번호(doc.sections[0])
    나눔 = False
    i = 0
    while i < len(줄):
        ln = 줄[i].rstrip()
        if not ln:
            i += 1
            continue
        if ln.startswith("#표지 "):
            doc.add_paragraph()
            p = doc.add_paragraph(ln[4:], style="Title")
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif ln.startswith("@부제 "):
            문단(ln[4:], size=14, color=회색, align=WD_ALIGN_PARAGRAPH.CENTER).paragraph_format.space_after = Pt(24)
        elif ln == "@쪽나눔":
            # an empty break paragraph can spill onto its own page; break before the next heading instead
            나눔 = True
        elif ln.startswith("# "):
            h = doc.add_heading(ln[2:], level=1)
            h.paragraph_format.page_break_before = 나눔
            나눔 = False
            셈["장"] += 1
        elif ln.startswith("## "):
            doc.add_heading(ln[3:], level=2)
        elif ln.startswith("@상자 "):
            머리, 첫 = ln[4:].split(" | ", 1)
            묶음 = [첫]
            while i + 1 < len(줄) and 줄[i + 1].strip() and not 줄[i + 1].startswith(("@", "#", "[그림"))                     and 줄[i + 1][0] not in 단계:
                i += 1
                묶음.append(줄[i].rstrip())
            상자(머리, 묶음)
        elif ln.startswith("@팁 "):
            상자("팁", [ln[3:]], fill="EEF5EC")
        elif ln.startswith("@주의 "):
            상자("주의", [ln[4:]], fill="FBECEC")
        elif ln.startswith("@작게 "):
            문단(ln[4:], size=10, color=회색)
        elif ln == "@표":
            행들 = []
            while True:
                i += 1
                assert i < len(줄), "@표 가 @끝 없이 끝났다"
                if 줄[i].strip() == "@끝":
                    break
                if 줄[i].strip():
                    행들.append([c.strip() for c in 줄[i].split(" | ")])
            표(행들)
        elif ln.startswith("[그림 "):
            m = re.match(r"\[그림 (\S+) \| (.+?)(?: \| (\d+(?:\.\d+)?))?\]$", ln)
            assert m, "그림 줄 형식이 틀렸다: %s" % ln
            그림(m.group(1), m.group(2), float(m.group(3)) if m.group(3) else None)
        elif ln[0] in 단계:
            문단(ln, indent=0.4)
        else:
            assert not ln.startswith("@"), "모르는 표시: %s" % ln
            문단(ln)
        i += 1

    os.makedirs(출력폴더, exist_ok=True)
    k = 1
    while os.path.exists(os.path.join(출력폴더, "%s_v%d.docx" % (기본이름, k))):
        k += 1
    경로 = os.path.join(출력폴더, "%s_v%d.docx" % (기본이름, k))
    doc.save(경로)
    assert 셈["장"] > 0, "장이 0 개다"
    print("docx %s  %s" % (경로, 셈))
    pdf = 경로[:-5] + ".pdf"
    워드로PDF(경로, pdf)
    쪽그림(pdf)


def 워드로PDF(docx, pdf):
    import pythoncom
    import win32com.client as win32
    pythoncom.CoInitialize()
    word = win32.Dispatch("Word.Application")
    word.Visible = False
    try:
        d = word.Documents.Open(os.path.abspath(docx), ReadOnly=True)
        d.ExportAsFixedFormat(os.path.abspath(pdf), 17)   # wdExportFormatPDF
        d.Close(False)
    finally:
        word.Quit()
    assert os.path.getsize(pdf) > 10000, "PDF 가 비었다"
    print("pdf  %s" % pdf)


def 쪽그림(pdf):
    """Every page as a small PNG on one sheet, for a visual check."""
    import pdfplumber
    with pdfplumber.open(pdf) as f:
        쪽 = [p.to_image(resolution=45).original.convert("RGB") for p in f.pages]
    w, h = 쪽[0].size
    열 = 6
    행 = (len(쪽) + 열 - 1) // 열
    판 = Image.new("RGB", (열 * (w + 10), 행 * (h + 10)), "white")
    for n, im in enumerate(쪽):
        판.paste(im, ((n % 열) * (w + 10), (n // 열) * (h + 10)))
    out = pdf[:-4] + "_쪽점검.png"
    판.save(out)
    print("쪽 %d 개, 점검 그림 %s" % (len(쪽), out))


if __name__ == "__main__":
    main()
