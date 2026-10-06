# 세션 핸드오프 — 하네스/오케스트레이션 지침 적용 (2026-06-09)

다른 Cowork 프로젝트에도 그대로 적용할 수 있도록, 이번 세션에서 한 일·수정 경로·정정 내용·근거·재현 방법을 모두 정리한 문서다.

---

## 0. 한눈에 요약

이번 세션은 두 가지를 했다.

1. **하네스 설치 가이드 2개 파일의 오류 정정** — superpowers 마켓플레이스/설치 식별자가 틀려 있던 것을 GitHub 실제 저장소(2026-06 확인) 기준으로 수정.
2. **오케스트레이션(멀티 에이전트) 지침을 프로젝트 CLAUDE.md에 영구 적용** — 자동 메모리 폴더에 쓰려 했으나 이번 세션에서 읽기 전용이라, 연결된 폴더의 CLAUDE.md에 반영.

---

## 1. 수정/생성된 파일 (경로 + 내용)

### 1-1. 하네스 가이드 정정 (Desktop\hanes\)

| 파일 | 경로 | 작업 |
|---|---|---|
| harness_setup_guide.md | `C:\Users\SGJEONG99\Desktop\hanes\harness_setup_guide.md` | superpowers 식별자 정정 + 보강 |
| harness_setup_instructions.md | `C:\Users\SGJEONG99\Desktop\hanes\harness_setup_instructions.md` | 동일 정정 |

### 1-2. 오케스트레이션 지침 적용 (프로젝트 CLAUDE.md)

| 파일 | 경로 | 작업 |
|---|---|---|
| CLAUDE.md | `C:\Users\SGJEONG99\Desktop\대심도 과제\과업_산출\30_회의_발표\2026-04-25_3차년도_착수보고\CLAUDE.md` | "오케스트레이션 지침" 6개 절 + 참고문헌 append |

### 1-3. 이 문서

- `C:\Users\SGJEONG99\OneDrive\문서\Claude\Projects\대심도 과제\SESSION_HANDOFF_하네스_오케스트레이션_적용.md`

---

## 2. 하네스 마켓플레이스 — 정확한 식별자 (2026-06 검증)

| 항목 | 마켓플레이스 add | 플러그인 install | 비고 |
|---|---|---|---|
| 공식 | `anthropics/claude-plugins-official` | (다양) | superpowers도 여기서 설치 가능 |
| harness | `revfactory/harness` | `harness@harness` | ✅ 정확 (v1.2.0) |
| superpowers | `obra/superpowers-marketplace` | `superpowers@superpowers-marketplace` | ⚠️ 아래 정정 |

### 무엇이 틀렸었나 (핵심 정정)

- **틀림:** 마켓플레이스 `obra/superpowers`, 설치 `superpowers@superpowers-dev`
- **맞음:** 마켓플레이스 `obra/superpowers-marketplace`, 설치 `superpowers@superpowers-marketplace`
- 이유: `obra/superpowers`는 **플러그인 본체** 저장소라 마켓플레이스로 등록되지 않는다. 마켓플레이스 저장소는 `obra/superpowers-marketplace`.
- 대안: superpowers는 공식 마켓플레이스에도 등재 → `/plugin install superpowers@claude-plugins-official` 로도 설치 가능.

### harness 요구사항

- 현재 v1.2.0. README의 Requirements에 **Agent Teams 플래그가 공식 요구사항**으로 명시:
  ```bash
  export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1   # .zshrc / .bashrc
  ```
  docs: https://code.claude.com/docs/en/agent-teams
- 이 플래그는 **Claude Code 전용 실험 기능**. 플래그가 없으면 harness는 Subagents 모드로 폴백.
- **Cowork에서 멀티 에이전트 팀 실행이 그대로 동작하는지는 미검증** (스킬 파일은 로드돼도 팀 오케스트레이션은 제약 가능성).

### CLI 설치 (3개 마켓플레이스)

```bash
# Git 먼저 설치돼 있어야 함 (git --version 확인)
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin marketplace add revfactory/harness
claude plugin marketplace add obra/superpowers-marketplace

claude plugin install harness@harness
claude plugin install superpowers@superpowers-marketplace
```

세션 내부 슬래시 커맨드도 동일: `/plugin marketplace add ...` / `/plugin install ...`

### 출처

- https://github.com/revfactory/harness (README, v1.2.0)
- https://github.com/obra/superpowers-marketplace (README)
- 본체: https://github.com/obra/superpowers

---

## 3. 오케스트레이션 지침 (멀티 에이전트 하네스) — 전문

> 비자명한 작업은 단일 처리하지 말고 서브에이전트를 나눠 **작업→검수→확정** 단계로 처리한다. 검수 강도는 작업 규모에 따라 자동 조절한다. 근거는 1차 출처 기반.

### 1. 기본 구조 — Orchestrator–Worker
리드(오케스트레이터) 1이 작업을 분석·분해하고 worker에게 위임한다. worker끼리 직접 소통하지 않으며 "다음에 무엇을 할지" 판단은 오케스트레이터가 보유. 각 worker에 ⑴목표 ⑵출력형식 ⑶도구·소스 ⑷작업경계를 자기완결적으로 전달한다. [1][2]
> 근거: Anthropic orchestrator-worker 구조(리드 1 + 병렬 서브에이전트 3~5)로 단일 대비 90.2% 향상 보고. [1]

### 2. 작업 흐름
1. **분해(Plan)** — 독립 단위는 병렬, 의존 단위는 순차. [2]
2. **실행(Work)** — 각 단위를 worker에 배정, 독립이면 동시 실행.
3. **검수(Verify)** — 산출물을 **별도 에이전트**가 평가. 작성자≠검수자. [2][4]
4. **확정(Confirm)** — 통과분만 반영, 실패 단위만 재작업→재검수(루프). [3][5]

### 3. 검수 강도 — 작업 규모로 자동 판단
- **사소**(파일명·1~2줄·단순조회): 검수 생략, 자체확인.
- **일반**(스크립트·데이터처리·문서1편): worker 산출 후 **검수 1회**.
- **고위험**(수치계산·모델 캘리브레이션·다중파일·보고서/논문 핵심수치·모델결과 해석): 검수 후 **다른 에이전트 교차 재검수**, 코드·수치는 가능하면 **독립 재실행** 검증. [5]

### 4. 역할 분담
- **탐색(Explore)** — 넓게 훑어 위치·후보 찾고 결론만 회수.
- **설계(Plan)** — 구현 전략·단계·트레이드오프 수립, 코드 미수정.
- **작업(Worker)** — 실제 코드·문서·분석 생성. [1]
- **검수(Verifier / LLM-as-a-judge)** — 정확성·논리·재현성 점검. 수치 재계산, 코드 재실행, 주장 출처 대조. **판정에 근거(reasoning) 함께 요구**. [4]

### 5. 운영 원칙
- 작성자≠검수자. 같은 에이전트가 자기 산출물 검수 금지. [2][4]
- 검수는 "통과/수정요청"을 **근거와 함께** 반환. 모호한 OK 금지. [4]
- 독립 작업은 한 번에 병렬, 순차 의존 시에만 대기. [1][2]
- **단순함 우선** — 더 단순한 방법으로 충분하면 멀티에이전트 미사용. [2]
- 진행 상황은 전체 대비 **퍼센트** 표기(예: `[3/5 | 60%]`).
- 불확실/가설은 검수에서 구분 표기, 1차 출처 검증 자료만 사용.

### 6. 적용 트리거
- 3단계 이상 또는 다중 파일 작업 → 위 흐름 적용.
- 수치·코드·보고서 핵심 결과물 → 반드시 검수 단계.
- 단순 대화·단발 조회 → 흐름 생략, 바로 응답. [2]

### 참고문헌
[1] Anthropic, *How we built our multi-agent research system* (2025). https://www.anthropic.com/engineering/multi-agent-research-system
[2] Anthropic, *Building Effective Agents* (2024). https://www.anthropic.com/research/building-effective-agents
[3] LangChain, *langgraph-supervisor*. https://github.com/langchain-ai/langgraph-supervisor-py
[4] Gu et al., *A Survey on LLM-as-a-Judge*, arXiv:2411.15594 (2024). https://arxiv.org/abs/2411.15594
[5] Shinn et al., *Reflexion*, NeurIPS 2023, arXiv:2303.11366. https://arxiv.org/abs/2303.11366
[6] Wu et al., *AutoGen*, arXiv:2308.08155 (2023). https://arxiv.org/abs/2308.08155

---

## 4. 다른 Cowork 프로젝트에 적용하는 법

### 방법 A — 프로젝트별 CLAUDE.md (권장, 이번에 쓴 방식)
적용할 프로젝트 폴더 루트에 `CLAUDE.md`를 만들고 **위 3장 "오케스트레이션 지침" 전문**을 붙여넣는다. 그 폴더에서 Cowork/Claude Code 작업 시 자동 로드된다. 프로젝트 종속이 아닌 범용 지침이라 어느 폴더에든 그대로 복붙 가능.

### 방법 B — 일회성
새 채팅 첫 메시지에 3장 전문을 그대로 붙여넣으면 그 대화에 한해 적용.

### 방법 C — 자동 메모리(세션 제약 있음)
원래는 자동 메모리 폴더에 feedback 메모리로 저장하는 게 정석이나 (아래 5장 참조) 환경에 따라 쓰기가 막힐 수 있음. 가능한 환경이라면 메모리에 저장하는 편이 모든 프로젝트에 전역 적용돼 가장 깔끔.

---

## 5. 발견된 환경 제약 (중요)

- **자동 메모리 폴더에 이번 세션에서 쓸 수 없었음.**
  - 정석 경로: `...\spaces\<space-id>\memory\` (feedback 타입 .md + MEMORY.md 인덱스)
  - 이번 세션에서는 이 폴더가 **읽기 전용으로만 마운트**(bash 마운트 `.auto-memory`도 `r-x`)되어 Write 도구가 "연결된 폴더 밖"이라며 거부.
  - → 그래서 CLAUDE.md 반영으로 대체. 다음 세션에서 메모리 쓰기가 열리면 동일 내용을 feedback 메모리(`orchestration-harness.md`)로 남길 것.
- 함의: Cowork에서 "기억해둬"가 항상 자동 메모리로 영구 저장되는 것은 아님. 확실히 남기려면 **연결된 폴더의 파일(CLAUDE.md 등)**로 박아두는 게 안전.

---

## 6. 다음 작업 시 체크리스트 (재현용)

1. 하네스 설치 안내할 때 식별자는 2장 표 그대로 (superpowers는 `-marketplace` 붙는 쪽).
2. 비자명 작업은 3장 흐름(작업→검수→확정), 작성자≠검수자, 고위험은 독립 재실행 교차검증.
3. 진행률은 `[n/N | %]` 표기.
4. 불확실 정보는 1차 출처(공식 레포·논문·공식 블로그) 검증 후 인용.
5. 영구 반영이 필요하면 메모리 쓰기 시도 → 막히면 CLAUDE.md로 폴백.
