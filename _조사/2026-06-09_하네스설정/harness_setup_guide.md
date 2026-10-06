# Claude 하네스 환경 설정 가이드

세 개의 플러그인 마켓플레이스(공식 + Harness + Superpowers)를 Claude Code / Cowork에 등록하는 설치 가이드.

| 라벨(마켓플레이스명) | 저장소 |
|---|---|
| claude-plugins-official | `https://github.com/anthropics/claude-plugins-official` |
| harness | `https://github.com/revfactory/harness.git` |
| superpowers-marketplace | `https://github.com/obra/superpowers-marketplace.git` |

> 주의: superpowers는 **`obra/superpowers`가 아니라 `obra/superpowers-marketplace`** 가 마켓플레이스 저장소다. `obra/superpowers`는 플러그인 본체 저장소라 마켓플레이스로 등록되지 않는다. (검증: github.com/obra/superpowers-marketplace README, 2026-06 확인)

---

## 0. 사전 준비 — Git 설치 (제일 처음)

마켓플레이스는 GitHub 저장소를 git으로 받아오므로 Git이 먼저 설치돼 있어야 한다.

- **Windows**: <https://git-scm.com/download/win> 설치 후 `git --version`
- **macOS**: `xcode-select --install` 또는 `brew install git`
- **Linux**: `sudo apt install git` (Debian/Ubuntu)

검증: `git --version` 출력 확인.

---

## 방법 A — Cowork / Claude 데스크톱 UI

1. Customize 메뉴를 연다 (플러그인·스킬·커넥터 통합 관리 메뉴).
2. **manage plugins**에서 마켓플레이스 추가 → GitHub 저장소 링크를 붙여넣는다.
3. 위 표의 세 링크를 각각 추가한다.
4. 추가된 마켓플레이스에서 원하는 플러그인을 Install.
5. 설치 후 `/` 입력 또는 `+` 버튼으로 스킬이 뜨는지 확인.

> 참고: Cowork는 기본 Knowledge Work 마켓플레이스 외에 Anthropic 마켓플레이스 및 임의의 GitHub 저장소를 마켓플레이스로 추가할 수 있다.

---

## 방법 B — Claude Code CLI

```bash
# 1) 마켓플레이스 등록
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin marketplace add revfactory/harness
claude plugin marketplace add obra/superpowers-marketplace

# 2) 플러그인 설치
claude plugin install harness@harness
claude plugin install superpowers@superpowers-marketplace
```

세션 내부에서는 슬래시 커맨드로도 가능:

```
/plugin marketplace add revfactory/harness
/plugin install harness@harness

/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

> superpowers는 공식 마켓플레이스에도 올라와 있어, 마켓플레이스 추가 없이 `/plugin install superpowers@claude-plugins-official` 로도 설치할 수 있다. (검증: github.com/obra/superpowers-marketplace README)

설치 후 `claude` 재시작.

---

## 주의사항 (확인 필요)

- **harness** (현재 v1.2.0): 에이전트 팀 기능 플래그가 **공식 요구사항**이다.
  ```bash
  export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1   # .zshrc / .bashrc 에 추가
  ```
  README의 Requirements 항목에 명시됨(docs: code.claude.com/docs/en/agent-teams). 이건 Claude Code 전용 실험 기능이라, **Cowork에서 멀티 에이전트 팀 실행이 그대로 동작하는지는 미확인**. 스킬 파일은 로드돼도 팀 오케스트레이션은 제약 가능성 있음. 플래그가 없으면 harness는 Subagents 모드로 폴백한다.
- **superpowers**: TDD·디버깅 등 코딩 방법론 + SessionStart 훅 중심. 지식노동(Cowork) 맥락에선 스킬은 뜨지만 Code 전용 훅 동작은 안 맞을 수 있음. superpowers-marketplace에는 core(`superpowers`) 외에 `elements-of-style`, `superpowers-developing-for-claude-code`, `private-journal-mcp` 등도 함께 제공된다.
- 마켓플레이스명(`@harness`, `@superpowers-marketplace` 등)은 저장소의 `.claude-plugin/marketplace.json` 의 `name` 필드를 따른다. 추가 직후 표시되는 이름으로 install 커맨드를 맞출 것.

---

## 출처

- Cowork 플러그인/마켓플레이스: support.claude.com — "Use plugins in Claude"
- harness 설치 / agent teams 플래그: github.com/revfactory/harness (README, v1.2.0, 2026-06 확인)
- superpowers: github.com/obra/superpowers-marketplace (README, 2026-06 확인), 본체 github.com/obra/superpowers
