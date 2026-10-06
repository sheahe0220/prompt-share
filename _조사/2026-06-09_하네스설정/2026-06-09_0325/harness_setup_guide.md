# Claude 하네스 환경 설정 가이드

세 개의 플러그인 마켓플레이스(공식 + Harness + Superpowers)를 Claude Code / Cowork에 등록하는 설치 가이드.
(2026-06-09 갱신: Superpowers 마켓플레이스 식별자 정정, Harness 최신 정보 반영)

| 라벨 | 저장소 |
|---|---|
| claude-plugins-official | `https://github.com/anthropics/claude-plugins-official` |
| harness | `https://github.com/revfactory/harness.git` |
| superpowers-marketplace | `https://github.com/obra/superpowers-marketplace.git` |

> 갱신 핵심: 기존 가이드는 Superpowers를 `obra/superpowers` 저장소 + `@superpowers-dev` 이름으로 안내했으나, 실제 마켓플레이스 저장소는 `obra/superpowers-marketplace`이며 install 식별자는 `@superpowers-marketplace`다. `obra/superpowers`는 코어 플러그인 소스 저장소이고, 등록 대상 마켓플레이스가 아니다.

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

설치 후 `claude` 재시작.

> superpowers-marketplace에는 코어 외에 추가 플러그인이 함께 들어있다(선택 설치):
> - `elements-of-style@superpowers-marketplace` — 영문 글쓰기 가이드(Strunk, The Elements of Style)
> - `superpowers-developing-for-claude-code@superpowers-marketplace` — 플러그인/스킬/MCP 개발 자료
> - `private-journal-mcp@superpowers-marketplace` — 시맨틱 검색 기반 비공개 저널 MCP

---

## Harness 개요 (갱신)

`revfactory/harness`는 도메인 한 줄 설명을 받아 에이전트 팀과 그들이 쓰는 스킬을 자동 생성하는 메타 스킬이다(v1.2.0, Apache 2.0). "build a harness for this project" / "하네스 구성해줘" / "ハーネスを構成して" 트리거로 동작하며, 6단계 워크플로(도메인 분석 → 팀 아키텍처 설계 → 에이전트 정의 생성 → 스킬 생성 → 통합·오케스트레이션 → 검증)를 거쳐 `.claude/agents/`와 `.claude/skills/`를 만든다.

6개 팀 아키텍처 패턴: Pipeline, Fan-out/Fan-in, Expert Pool, Producer-Reviewer, Supervisor, Hierarchical Delegation.

실행 모드는 두 가지다. 기본은 **Agent Teams**(TeamCreate + SendMessage + TaskCreate, 협업이 필요한 2개 이상 에이전트)이고, 협업이 불필요한 단발 작업은 **Subagents**(Agent 도구 직접 호출)로 동작한다.

마켓플레이스 설치 외에 글로벌 스킬로 직접 설치도 가능:
```bash
cp -r skills/harness ~/.claude/skills/harness
```

관련 자매 저장소:
- **`revfactory/harness-100`** — 10개 도메인 100종 사전 제작 하네스(EN+KO, 총 200패키지). 각 하네스는 전문 에이전트 4~5개 + 오케스트레이터 스킬 + 도메인 스킬로 구성.
- **`revfactory/claude-code-harness`** — A/B 효과 측정 실험. 저자 측정 결과 평균 품질 49.5 → 79.3(+60%), 15/15 승률, 분산 −32% (n=15, 저자 측정, 제3자 재현 미완).

---

## 주의사항 (갱신)

- **harness — Agent Teams 활성화가 요구사항이다.** 저장소 Requirements에 명시:
  ```bash
  export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1   # .zshrc / .bashrc 에 추가
  ```
  공식 문서: <https://code.claude.com/docs/en/agent-teams>. 이 플래그는 Claude Code 전용 실험 기능이라, **Cowork에서 멀티 에이전트 팀 실행이 그대로 동작하는지는 미확인**. 팀이 안 뜨면 Subagents 모드 또는 스킬 단독 사용으로 폴백.
- **superpowers**: TDD·디버깅 등 코딩 방법론 + `/brainstorm`·`/write-plan`·`/execute-plan` 커맨드 + SessionStart 훅 중심. 지식노동(Cowork) 맥락에선 스킬은 뜨지만 Code 전용 훅 동작은 안 맞을 수 있음.
- 마켓플레이스명(`@harness`, `@superpowers-marketplace` 등)은 저장소의 `.claude-plugin/marketplace.json` 의 `name` 필드를 따른다. 추가 직후 표시되는 이름으로 install 커맨드를 맞출 것.

---

## 출처

- Cowork 플러그인/마켓플레이스: support.claude.com — "Use plugins in Claude"
- harness 설치 / Requirements(Agent Teams 플래그): <https://github.com/revfactory/harness>, <https://code.claude.com/docs/en/agent-teams>
- harness-100: <https://github.com/revfactory/harness-100>
- A/B 실험: <https://github.com/revfactory/claude-code-harness>
- superpowers 마켓플레이스/설치: <https://github.com/obra/superpowers-marketplace>, <https://github.com/obra/superpowers>
