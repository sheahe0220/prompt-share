# Claude 하네스 환경 설정 가이드 (v2, 2026-06-09 검증)

세 개의 플러그인 마켓플레이스(공식 + Harness + Superpowers)를 Claude Code / Cowork에 등록하는 설치 가이드.

> **v1 대비 수정 요약**
> - superpowers 마켓플레이스 식별자 정정: `obra/superpowers` → `obra/superpowers-marketplace`, 설치 `superpowers@superpowers-dev` → `superpowers@superpowers-marketplace`.
> - harness 의 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 은 이제 Claude Code 공식 문서에 정식 요구사항으로 등재됨(실험 미확인 항목 아님). 단 harness 는 Subagents 폴백 모드가 있어 플래그 없이도 단발 작업은 동작.
> - harness 현재 버전 v1.2.0, Apache-2.0.

| 라벨 | 저장소 |
|---|---|
| claude-plugins-official | `https://github.com/anthropics/claude-plugins-official` |
| harness-marketplace | `https://github.com/revfactory/harness.git` |
| superpowers-marketplace | `https://github.com/obra/superpowers-marketplace.git` |

> 참고: superpowers 의 **프레임워크 코드**는 `obra/superpowers` 에 있지만, 플러그인 마켓플레이스로 등록할 저장소는 `obra/superpowers-marketplace` 다. superpowers 는 Anthropic 공식 마켓플레이스(`claude-plugins-official`)를 통해서도 설치 가능하다.

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
3. 위 표의 세 링크를 각각 추가한다. (superpowers 는 반드시 `obra/superpowers-marketplace` 를 추가할 것.)
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
# (대안) 공식 마켓플레이스 경유:
# claude plugin install superpowers@claude-plugins-official
```

세션 내부에서는 슬래시 커맨드로도 가능:

```
/plugin marketplace add revfactory/harness
/plugin install harness@harness

/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

`/plugin` 이 인식되지 않으면 Claude Code 를 갱신한다: `npm update -g @anthropic-ai/claude-code` 후 세션 재시작.

설치 후 `claude` 재시작.

---

## 주의사항

- **harness (v1.2.0)**: Agent Teams 기능이 전제다.
  ```bash
  export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1   # .zshrc / .bashrc 에 추가
  ```
  이는 현재 Claude Code 공식 문서(<https://code.claude.com/docs/en/agent-teams>)에 정식 요구사항으로 명시돼 있다.
  - **기본 모드(Agent Teams)**: `TeamCreate + SendMessage + TaskCreate` 로 2개 이상 에이전트가 협업. 위 플래그 필요.
  - **폴백 모드(Subagents)**: Agent 도구 직접 호출. 에이전트 간 통신이 없는 단발 작업용이며 **플래그 없이도 동작**한다. Cowork처럼 팀 오케스트레이션 플래그를 못 켜는 환경에서는 이 모드로 폴백.
  - 트리거 문구: `build a harness for this project` / `하네스 구성해줘` / `ハーネスを構成して`.
- **superpowers**: TDD·디버깅 등 코딩 방법론 + 워크플로 강제(plan→test→review) + SessionStart 훅 중심. `/brainstorm`, `/write-plan`, `/execute-plan` 등 커맨드 제공. 지식노동(Cowork) 맥락에선 스킬은 뜨지만 Code 전용 훅 동작은 그대로 안 맞을 수 있음.
- 마켓플레이스명(`@harness`, `@superpowers-marketplace` 등)은 저장소의 `.claude-plugin/marketplace.json` 의 `name` 필드를 따른다. 추가 직후 표시되는 이름으로 install 커맨드를 맞출 것.

---

## 출처

- harness 저장소/요구사항/설치: <https://github.com/revfactory/harness> (v1.2.0, Apache-2.0, "Requirements: Agent Teams enabled `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`")
- Agent Teams 공식 문서: <https://code.claude.com/docs/en/agent-teams>
- superpowers 마켓플레이스/설치: <https://github.com/obra/superpowers-marketplace>, <https://github.com/obra/superpowers>
- Cowork 플러그인/마켓플레이스: support.claude.com — "Use plugins in Claude"
