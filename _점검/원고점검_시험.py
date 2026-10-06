r"""원고점검.py 가 심어 둔 결함을 모두 잡고, 정상 문헌은 조용한지 본다.

원고점검.py 를 고친 뒤 반드시 돌린다. 시험 원고는 임시 폴더에 만든다.
--crossref 시험은 api.crossref.org 에 참고문헌 5 개를 묻는다(인터넷 필요).

Rerun: C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe -X utf8 원고점검_시험.py
"""
import os
import subprocess
import sys
import tempfile

import docx

HERE = os.path.join(tempfile.gettempdir(), "원고점검_시험")
TOOL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "원고점검.py")
os.makedirs(HERE, exist_ok=True)
DOC = os.path.join(HERE, "시험원고.docx")
for f in ("시험원고_crossref.json", "시험원고_원고점검.md"):
    if os.path.exists(os.path.join(HERE, f)):
        os.remove(os.path.join(HERE, f))

d = docx.Document()
for p in [
    "1. Introduction",
    "SWMM was calibrated for the Sinwol basin.",                                   # used before defined
    "The Storm Water Management Model (SWMM) simulates urban runoff.",
    "The Nash-Sutcliffe efficiency (NSE) and the Kling-Gupta efficiency (KGE) were used "
    "(Gupta et al., 2009; Moriasi et al., 2007).",
    "RMSE was also computed for a rainfall of 50mm.",                               # undefined + unit
    "Smith et al. (2020) reported a similar bias.",                                  # not in list
    "Beven and Binley (1992) discussed equifinality.",
    "김철수 등(2019)은 도시 유역의 유출을 분석하였다.",
    "The study area is shown in Fig. 1 and the results in Fig. 3.",                  # Fig. 3 missing
    "Parameters are listed in Table 1.",
    "Fig. 1. Study area.",
    "Fig. 2. Observed and simulated hydrographs.",                                   # never cited
    "Table 1. Calibrated parameters.",
    "Table 3. Performance metrics.",                                                 # gap: no Table 2
    "References",
    "Beven, K., Binley, A., 1992. The future of distributed models: model calibration and "
    "uncertainty prediction. Hydrol. Process. 6, 279-298. https://doi.org/10.1016/j.jhydrol.2009.08.003",
    "Gupta, H.V., Kling, H., Yilmaz, K.K., Martinez, G.F., 2009. Decomposition of the mean squared "
    "error and NSE performance criteria: Implications for improving hydrological modelling. "
    "J. Hydrol. 377, 80-91. https://doi.org/10.1016/j.jhydrol.2009.08.003",
    "Jeong, S., 2021. Deep tunnel hydraulics revisited. J. Hydrol. 600, 1-10. "
    "https://doi.org/10.1016/j.jhydrol.2099.99.999",                                 # fake DOI, uncited
    "Moriasi, D.N., Arnold, J.G., Van Liew, M.W., Bingner, R.L., Harmel, R.D., Veith, T.L., 2007. "
    "Model evaluation guidelines for systematic quantification of accuracy in watershed simulations. "
    "Transactions of the ASABE 50(3), 885-900.",
    "김철수, 이영희, 2019. 도시 유역 유출 분석. 한국수자원학회논문집 52(1), 1-10.",
]:
    d.add_paragraph(p)
d.save(DOC)

r = subprocess.run([sys.executable, "-X", "utf8", TOOL, DOC, "--crossref"], capture_output=True,
                   text=True, encoding="utf-8")
print(r.stdout, r.stderr[-1500:])
o = r.stdout
expect = {
    "missing citation": "본문 인용이 목록에 없다: smith (2020)",
    "missing figure": "본문이 없는 그림 을 부른다: [3]",
    "table gap": "표 캡션 번호가 빈다: [2]",
    "uncited figure": "캡션은 있는데 본문에서 부르지 않는 그림: [2]",
    "uncited reference": "목록에 있는데 본문에서 인용하지 않았다: Jeong",
    "abbr before def": "정의보다 먼저 쓰인 약어 1 개: SWMM",
    "abbr undefined": "RMSE",
    "unit spacing": "50mm",
    "fake DOI": "DOI 가 Crossref 에 없다(지어낸 DOI 일 수 있다) 10.1016/j.jhydrol.2099.99.999",
    "wrong DOI": "[1] DOI 의 논문이 목록과 다르다",
}
miss = [k for k, v in expect.items() if v not in o]
silent = [s for s in ("gupta (2009)", "moriasi (2007)", "김철수 (2019)", "beven (1992)",
                      "[2] DOI 의 논문", "[4] 찾지 못함", "[4] 제목 검색으로")
          if s in o]
print("missed:", miss)
print("should be silent:", silent)
assert r.returncode == 1, "should fail, got %d" % r.returncode
assert not miss, miss
assert not silent, silent
print("OK: all 10 planted manuscript defects caught, good references silent")
