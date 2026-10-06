r"""이 PC 밖으로 내보낼 사본을 dist\ 에 만든다. GitHub 와 claude.ai 웹용이다.

무엇을 왜 만들었나
  이 PC 의 Claude Code 는 ~/.claude 로 이미 걸려 있다. 그런데 claude.ai 웹 ·
  앱 채팅은 ~/.claude 를 읽지 않고, 다른 PC 나 클라우드 세션은 이 PC 에 없다.
  ~/.claude 의 스킬은 references 가 정션이라 그대로 옮기면 빈 폴더가 된다.
  그래서 정션 대신 실제 파일을 담은 사본을 따로 만든다.

무엇을 만드나
  dist\skills\std-*\          SKILL.md + references\ 실제 파일 (+ scripts\)
  dist\.claude-plugin\         이 폴더를 Claude Code 플러그인으로 만든다
  dist\web\std-*.zip           claude.ai  Customize > Skills > Upload a skill
  dist\web\preferences.txt     claude.ai  개인 선호 칸에 붙여 넣는 글
  .claude-plugin\marketplace.json   저장소를 마켓플레이스로 만든다 (저장소 뿌리)

원본은 Prompt\ 다. dist\ 는 만들 때마다 지우고 다시 만든다. 직접 고치지 마라.
스킬표는 내보내기.py 한 곳에만 둔다. 여기서 다시 적지 않고 불러 쓴다.

실행
  python.exe -X utf8 _동기화\배포_만들기.py
  내보내기.py 가 끝에서 이것을 부른다
"""
import importlib.util
import json
import os
import re
import shutil
import sys
import zipfile

여기 = os.path.dirname(os.path.abspath(__file__))
뿌리 = os.path.dirname(여기)
DIST = os.path.join(뿌리, "dist")

# 스킬표를 내보내기.py 에서 가져온다. 두 곳에 두면 갈린다
_spec = importlib.util.spec_from_file_location(
    "내보내기", os.path.join(여기, "내보내기.py"))
_m = importlib.util.module_from_spec(_spec)
_argv = sys.argv
sys.argv = [sys.argv[0]]              # 내보내기.py 가 --확인 을 읽지 않게
_spec.loader.exec_module(_m)
sys.argv = _argv
스킬 = _m.스킬
설명표 = _m.설명표

플러그인이름 = "sgj-prompt"
판 = "1.0.0"

SKILL_머리 = """---
name: %s
description: %s
---

<!-- 이 파일은 _동기화\\배포_만들기.py 가 만든다. 직접 고치지 마라.
     원본은 github.com/sheahe0220/claude_play 의 루트 md 파일들이다. -->

# %s

아래 파일을 **읽고 그대로 따른다.** 요약해서 기억하지 말고 필요할 때 연다.

%s

각 파일 끝의 `함정` 절을 반드시 본다. 실제로 한 번 틀려 본 것만 적혀 있다.
"""


def 이름검사(n):
    """agentskills.io 규격. 소문자 · 숫자 · 하이픈, 64자 이내, 하이픈 연속 금지."""
    assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", n) and len(n) <= 64, \
        "스킬 이름이 규격에 안 맞는다: %s" % n


def 한줄(s):
    return " ".join(s.split())


def 스킬만들기():
    """dist\\skills\\std-* 를 실제 파일로 만든다."""
    쓴것 = []
    for 이름, 파일들, 설명 in 스킬:
        이름검사(이름)
        설명1 = 한줄(설명)
        assert len(설명1) <= 1024, \
            "%s 설명이 %d 자다. 1024 를 넘으면 웹 업로드가 거절된다" % (이름, len(설명1))
        d = os.path.join(DIST, "skills", 이름)
        os.makedirs(os.path.join(d, "references"))
        목록 = "\n".join("- `references/%s`  %s" % (f, 설명표.get(f, ""))
                        for f in 파일들)
        # 설명은 따옴표로 감싼다. 콜론이 들어 있어 YAML 이 깨질 수 있다
        본문 = SKILL_머리 % (이름, json.dumps(설명1, ensure_ascii=False), 이름, 목록)
        with open(os.path.join(d, "SKILL.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(본문)
        for f in 파일들:
            shutil.copy2(os.path.join(뿌리, f), os.path.join(d, "references", f))
        쓴것.append((이름, len(설명1), len(파일들)))
    # 점검 스크립트
    # every .py in _점검 (2026-09-22: only 점검.py was copied, so ppt점검 · 양식대조
    # never reached plugin users on other PCs)
    sd = os.path.join(DIST, "skills", "std-check", "scripts")
    os.makedirs(sd)
    스크립트 = sorted(f for f in os.listdir(os.path.join(뿌리, "_점검")) if f.endswith(".py"))
    assert "점검.py" in 스크립트, "점검.py 가 없다"
    for f in 스크립트:
        shutil.copy2(os.path.join(뿌리, "_점검", f), os.path.join(sd, f))

    # 우리가 만든 도구 스킬은 폴더째 옮긴다
    도구 = os.path.join(뿌리, "_도구", "skills")
    if os.path.isdir(도구):
        for n in sorted(os.listdir(도구)):
            src = os.path.join(도구, n)
            if not os.path.isfile(os.path.join(src, "SKILL.md")):
                continue
            이름검사(n)
            앞 = open(os.path.join(src, "SKILL.md"), encoding="utf-8").read().split("---")[1]
            설명 = re.search(r"description:\s*(.*)", 앞, re.S).group(1).strip().strip('"')
            assert len(설명) <= 1024, "%s 설명이 %d 자다" % (n, len(설명))
            shutil.copytree(src, os.path.join(DIST, "skills", n),
                            ignore=shutil.ignore_patterns("__pycache__"))
            쓴것.append((n, len(설명), 0))
    return 쓴것


def 플러그인만들기():
    pd = os.path.join(DIST, ".claude-plugin")
    os.makedirs(pd)
    with open(os.path.join(pd, "plugin.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump({
            "name": 플러그인이름,
            "version": 판,
            "description": "작업 지침 모음. 폴더 · 그림 · 문서 · 자료 · 코드 · 점검",
            "author": {"name": "sheahe0220"},
            "license": "UNLICENSED",
        }, f, ensure_ascii=False, indent=2)
    md = os.path.join(뿌리, ".claude-plugin")
    os.makedirs(md, exist_ok=True)
    with open(os.path.join(md, "marketplace.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump({
            "name": 플러그인이름,
            "owner": {"name": "sheahe0220"},
            "metadata": {"description": "작업 지침 모음을 Claude Code 플러그인으로 배포한다"},
            "plugins": [{
                "name": 플러그인이름,
                "source": "./dist",
                "description": "작업 지침 6묶음. 이 PC 에서는 설치하지 마라(이미 ~/.claude 에 있다)",
            }],
        }, f, ensure_ascii=False, indent=2)


def 웹만들기():
    wd = os.path.join(DIST, "web")
    os.makedirs(wd)
    n = 0
    for 이름 in sorted(os.listdir(os.path.join(DIST, "skills"))):
        src = os.path.join(DIST, "skills", 이름)
        zp = os.path.join(wd, 이름 + ".zip")
        # Fixed timestamp and sorted order so an unchanged skill yields a
        # byte-identical zip. Otherwise every session-start export dirtied git
        # (2026-09-22: SKILL.md is rewritten each run, so its mtime moved)
        with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
            for d, ds, fs in os.walk(src):
                ds.sort()
                for f in sorted(fs):
                    p = os.path.join(d, f)
                    # zip 안은 std-xxx/SKILL.md 형태. 폴더 이름 = 스킬 이름
                    zi = zipfile.ZipInfo(os.path.relpath(p, os.path.dirname(src)),
                                         date_time=(2026, 1, 1, 0, 0, 0))
                    zi.compress_type = zipfile.ZIP_DEFLATED
                    zi.external_attr = 0o644 << 16
                    z.writestr(zi, open(p, "rb").read())
        n += 1
    # 개인 선호 글. 앞의 HTML 주석을 뗀다
    t = open(os.path.join(뿌리, "_전역", "웹_개인선호.md"), encoding="utf-8").read()
    t = re.sub(r"<!--.*?-->\s*", "", t, flags=re.S).strip() + "\n"
    with open(os.path.join(wd, "preferences.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    return n, len(t)


def main():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    쓴것 = 스킬만들기()
    플러그인만들기()
    zip수, 선호길이 = 웹만들기()

    print("[배포] %s" % DIST)
    for 이름, 길이, 수 in 쓴것:
        print("  %-12s 설명 %4d 자 · references %d 개" % (이름, 길이, 수))
    print("  웹 zip %d 개 · 개인 선호 %d 자" % (zip수, 선호길이))

    # 되읽어 확인한다. zip 안에 SKILL.md 가 제자리에 있나
    폴더들 = sorted(os.listdir(os.path.join(DIST, "skills")))
    for 이름 in 폴더들:
        with zipfile.ZipFile(os.path.join(DIST, "web", 이름 + ".zip")) as z:
            names = z.namelist()
        assert "%s/SKILL.md" % 이름 in [x.replace("\\", "/") for x in names], \
            "%s.zip 안에 SKILL.md 가 없다" % 이름
    assert zip수 == len(폴더들), "zip 수가 스킬 폴더 수와 다르다"
    print("  zip 구조 확인 완료")
    return 0


if __name__ == "__main__":
    sys.exit(main())
