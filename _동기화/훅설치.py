r"""~/.claude/settings.json 에 Prompt 훅 두 개를 넣는다. PC 마다 한 번만 돌리면 된다.

무엇을 왜 만들었나
  Prompt 를 고친 뒤 손으로 내보내는 것을 잊는다. 새 세션이 시작될 때마다
  자동으로 내보내게 하면 잊을 일이 없다.
  2026-09-29 부터 노트북과 연구실 PC 가 GitHub(sheahe0220/claude_play, 비공개)로
  같은 지침을 쓴다. 한쪽에서 고친 것이 다른 쪽에 자동으로 오게 훅을 둘로 늘렸다.

무엇을 하나
  SessionStart  _sync.py        GitHub 에서 받고(pull) 내보낸다
  Stop          _sync.py push   답이 끝날 때 바뀐 것이 있으면 commit · push
  기존 설정(enabledPlugins, 다른 훅)은 건드리지 않는다. 넣기 전에 백업한다.
  파이썬은 이 스크립트를 돌린 파이썬을 쓴다(PC 마다 경로가 달라서).

주의
  훅이 도는 시점은 세션 시작이다. 그 세션의 CLAUDE.md 는 이미 읽힌 뒤일 수
  있으므로 고친 내용은 그다음 세션부터 걸린다.
  지침 본문은 junction 으로 직결되어 있어 즉시 반영된다.

실행
  <python.exe> -X utf8 _동기화\훅설치.py          넣는다
  <python.exe> -X utf8 _동기화\훅설치.py --확인    무엇이 바뀌는지만 본다
  <python.exe> -X utf8 _동기화\훅설치.py --제거    뺀다
"""
import datetime
import json
import os
import shutil
import sys

여기 = os.path.dirname(os.path.abspath(__file__))
뿌리 = os.path.dirname(여기)
설정 = os.path.join(os.path.expanduser("~"), ".claude", "settings.json")

PY = sys.executable
# 한글 경로를 셸에 넘기면 코드페이지에 따라 깨진다. ASCII 이름의 진입점을 쓴다.
진입점 = os.path.join(뿌리, "_sync.py")

표시 = "prompt-sync"      # 우리가 넣은 훅을 알아보는 표시
훅목록 = [
    # (event, command, timeout, statusMessage)
    ("SessionStart", '"%s" -X utf8 "%s"' % (PY, 진입점), 90, "prompt-sync: GitHub 에서 받고 내보내는 중"),
    ("Stop", '"%s" -X utf8 "%s" push' % (PY, 진입점), 90, "prompt-sync: GitHub 에 올리는 중"),
]

확인만 = "--확인" in sys.argv
제거 = "--제거" in sys.argv


def 우리것인가(h):
    for x in h.get("hooks", []):
        if 표시 in x.get("statusMessage", "") or "Prompt\_sync.py" in x.get("command", "") \
                or os.path.normcase(진입점) in os.path.normcase(x.get("command", "")):
            return True
    return False


def main():
    assert os.path.exists(설정), "settings.json 이 없다: %s" % 설정
    assert os.path.exists(진입점), "진입점이 없다: %s" % 진입점
    assert " " not in PY or os.path.exists(PY), "파이썬 경로가 이상하다: %s" % PY

    원문 = open(설정, encoding="utf-8").read()
    cfg = json.loads(원문)
    훅들 = cfg.setdefault("hooks", {})

    바꾼수 = 0
    for 사건, 명령, 제한, 표시말 in 훅목록:
        목록 = 훅들.setdefault(사건, [])
        남길것 = [h for h in 목록 if not 우리것인가(h)]
        이미 = len(남길것) != len(목록)
        if 제거:
            if 이미:
                print("[제거] %s 훅" % 사건)
                바꾼수 += 1
            목록[:] = 남길것
        else:
            새것 = {"hooks": [{"type": "command", "command": 명령,
                              "timeout": 제한, "statusMessage": 표시말}]}
            목록[:] = [새것] + 남길것      # ours first: pull before anything else reads files
            print("[%s] %s 훅\n       %s" % ("갱신" if 이미 else "추가", 사건, 명령))
            바꾼수 += 1
        if not 목록:
            훅들.pop(사건, None)
    if not 훅들:
        cfg.pop("hooks", None)

    새문 = json.dumps(cfg, ensure_ascii=False, indent=2) + "\n"
    if 새문 == 원문:
        print("[같음] 바꿀 것이 없다")
        return 0
    assert 바꾼수 > 0, "바꾼 훅이 0 개인데 설정이 달라졌다"
    if 확인만:
        print("\n확인만 돌렸다. 쓰지 않았다.")
        return 0

    백업 = 설정 + ".bak." + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copy2(설정, 백업)
    print("[백업] %s" % 백업)

    with open(설정, "w", encoding="utf-8", newline="\n") as f:
        f.write(새문)

    # 되읽어 확인한다. 깨진 json 을 남기면 다음 세션이 안 뜬다
    다시 = json.loads(open(설정, encoding="utf-8").read())
    assert set(다시) >= set(cfg) - {"hooks"}, "기존 설정이 날아갔다. 백업에서 되돌려라"
    print("[확인] json 정상. 기존 설정 유지됨. 다음 세션부터 자동으로 받고 올린다")
    return 0


if __name__ == "__main__":
    sys.exit(main())
