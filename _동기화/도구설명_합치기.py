r"""세 갈래로 조사한 도구 설명(확장 · 플러그인과 장터 · MCP)을 합쳐 recipient\도구설명.json 을 만든다.

왜 있나
  지인 PC 의 클로드가 원작자 PC 에 깔린 도구 전부를 알고, 지인의 일에 빗대어 하나씩 물어보게
  하려고(2026-09-29 사용자 요청). 설명은 서브에이전트 셋이 마켓플레이스 · 설치본 · 공식 문서를
  보고 썼고(scratchpad 의 cat_*.json), 여기서 원작자가 등급만 조정해 합친다.
  시작하기.md 와 도구목록.md 는 받는사람_한파일.py 가 이 json 으로 만든다.

실행
  C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe -X utf8 _동기화\도구설명_합치기.py <cat_ext.json> <cat_plugin.json> <cat_mcp.json>
  나중에 새 도구를 깔면 recipient\도구설명.json 에 한 줄을 직접 더한다(받는사람_한파일.py 가
  설명이 빠진 도구를 찾으면 멈춘다).
"""
import json
import re
import os
import sys

여기 = os.path.dirname(os.path.abspath(__file__))
결과 = os.path.join(여기, "recipient", "도구설명.json")
필드 = ["id", "종류", "이름", "무엇", "비유", "등급", "조건", "설치", "출처", "확인"]

# 2026-09-29 등급 조정: 처음 쓰는 사람의 기본 묶음에는 계정 연결 · 추가 프로그램이 딸린 것을 넣지 않는다
조정 = {
    "claude.ai Claude Docs": ("물어봄", "문서가 claude.ai 서버에 저장된다. 발주처 자료를 넣어도 되는지 회사 규정을 먼저 확인한다."),
    "plugin:pdf-viewer:pdf": ("물어봄", None),
    "pdf-viewer@synced": ("물어봄", "Node.js 가 있어야 한다. PDF 를 읽기만 하는 것은 이것 없이 Python 으로도 된다."),
}
# @synced 는 원작자 claude.ai 계정에서 내려온 것. 원래 장터는 anthropics/knowledge-work-plugins (README 로 확인)
장터설치 = ("claude plugin marketplace add anthropics/knowledge-work-plugins 를 먼저 하고, "
         "claude plugin install {이름}@knowledge-work-plugins")


def main():
    assert len(sys.argv) == 4, __doc__
    목록 = []
    for p in sys.argv[1:]:
        목록 += json.load(open(p, encoding="utf-8"))
    assert len(목록) == 44 + 37 + 31, "개수가 112 가 아니다: %d" % len(목록)
    바꾼 = 0
    for d in 목록:
        if d["id"] in 조정:
            등급, 조건 = 조정[d["id"]]
            d["등급"] = 등급
            if 조건:
                d["조건"] = (조건 + " " + d.get("조건", "")).strip()
            바꾼 += 1
        if d["id"].endswith("@synced"):
            d["설치"] = 장터설치.format(이름=d["id"].split("@")[0])
            # the plugin agent guessed "enable it in claude.ai settings"; the install line above replaces that
            d["조건"] = re.sub(r"장터에서 까는 것이 아니라.*?(함께 찾는다\.|$)",
                             "원작자 PC 에는 claude.ai 계정에서 켜져 내려왔지만, 친구 PC 에서는 "
                             "Anthropic 의 knowledge-work-plugins 장터에서 깐다.", d.get("조건", ""), flags=re.S).strip()
            assert "판정보류" not in d["조건"], d["조건"]
            바꾼 += 1
        d["확인"] = bool(d.get("확인", False))
        for k in 필드:
            d.setdefault(k, "")
    assert 바꾼 == len(조정) + 5, "조정 개수가 이상하다: %d" % 바꾼   # 3 grade changes + 5 synced install lines
    ids = [d["id"] for d in 목록]
    assert len(set(ids)) == len(ids), "id 중복"
    글 = json.dumps([{k: d[k] for k in 필드} for d in 목록], ensure_ascii=False, indent=1)
    for c in ("\u2014", "\u2212", "~"):
        assert c not in 글, "금지 문자 %r" % c
    open(결과, "w", encoding="utf-8", newline="\n").write(글 + "\n")
    셈 = {}
    for d in 목록:
        셈[(d["종류"], d["등급"])] = 셈.get((d["종류"], d["등급"]), 0) + 1
    print("만듦 %s  (%d 개)" % (결과, len(목록)))
    for k in sorted(셈):
        print("  %-6s %-6s %d" % (k[0], k[1], 셈[k]))
    print("  확인=false:", [d["id"] for d in 목록 if not d["확인"]])


if __name__ == "__main__":
    main()
