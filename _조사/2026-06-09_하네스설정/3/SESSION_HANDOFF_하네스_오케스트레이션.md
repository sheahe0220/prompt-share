# 세션 핸드오프 — 하네스 / 오케스트레이션 설정 정리

작성: 2026-06-09 / 목적: 이 세션에서 진행한 내용을 다른 프로젝트(Cowork)에 그대로 이식하기 위한 자기완결 문서.

---

## 0. 한눈에 요약 (TL;DR)

이 세션에서 한 일은 세 가지다.

1. `hanes` 폴더의 하네스 셋업 가이드 2개를 GitHub 실측으로 검증해 갱신했다. 가장 큰 정정은 **Superpowers 마켓플레이스 식별자**였다.
2. 업로드한 `ORCHESTRATION_GUIDE.md` 개정판을 프로젝트 루트 `CLAUDE.md`의 오케스트레이션 섹션에 반영했다.
3. "Cowork에서 하네스/슈퍼파워가 적용되는가"를 정리했다. 결론: **오케스트레이션 지침(텍스트) + 내장 Agent 서브에이전트는 적용되지만, harness/superpowers 플러그인 자체는 별개이며 Cowork 호환은 미검증**이다.

다른 프로젝트에 이식할 때 핵심은 2번(오케스트레이션 지침을 그 프로젝트의 `CLAUDE.md`에 붙여넣기)이다. 본 문서 6장에 전체 텍스트가 들어 있다.

---

## 1. 개념 구분 (가장 중요)

혼동하기 쉬운 두 가지를 분리한다.

| 구분 | 정체 | Cowork 적용 여부 |
|---|---|---|
| **오케스트레이션 "지침"** | `CLAUDE.md`에 들어가는 텍스트 행동 규칙. Claude가 매 세션 읽고 따른다. | **적용됨.** Claude가 읽고 따른다. 내장 Agent 도구로 실제 서브에이전트 실행도 가능. |
| **harness / superpowers "플러그인"** | 마켓플레이스에서 설치하는 실제 플러그인(스킬·커맨드·훅). | **별개. 미검증.** 설치 필요. 일부 기능은 Claude Code 전용. |

지침을 `CLAUDE.md`에 넣었다고 해서 플러그인이 깔리는 것은 아니다. 둘은 독립적이다.

### Cowork에서 실제로 보장되는 것
- `CLAUDE.md`의 오케스트레이션 지침을 Claude가 읽고 따름.
- 내장 Agent(Task) 도구로 서브에이전트 실행 가능: `claude`, `Explore`, `Plan`, `general-purpose` 타입. 작성자/검수자 분리, 병렬 worker 실행 등을 실제 수행 가능.

### Cowork에서 미검증/제약인 것
- harness 플러그인의 **Agent Teams** 기능 → `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 플래그 요구(Claude Code 전용 실험 기능).
- superpowers 플러그인의 **SessionStart 훅**, `/brainstorm`·`/write-plan`·`/execute-plan` **슬래시 커맨드** → Claude Code 전용.
- 현재 이 Cowork 세션의 스킬 목록에 harness/superpowers는 **없음**(미설치 상태).

---

## 2. 이번 세션에서 만지거나 만든 파일 (경로 총정리)

### 갱신한 하네스 가이드 (원본 유지, 타임스탬프 폴더에 갱신본)
- 원본:
  - `C:\Users\SGJEONG99\Desktop\hanes\harness_setup_guide.md`
  - `C:\Users\SGJEONG99\Desktop\hanes\harness_setup_instructions.md`
- 갱신본:
  - `C:\Users\SGJEONG99\Desktop\hanes\2026-06-09_0325\harness_setup_guide.md`
  - `C:\Users\SGJEONG99\Desktop\hanes\2026-06-09_0325\harness_setup_instructions.md`

### 오케스트레이션 지침 반영 (제자리 수정)
- `C:\Users\SGJEONG99\OneDrive\문서\Claude\Projects\MS_SWMM\CLAUDE.md`
  - 113행 이하 "오케스트레이션 지침" 섹션을 업로드 개정판으로 교체.
  - 이 파일은 프로젝트 루트라 매 세션 자동 로드됨(= 지속 적용).

### 본 핸드오프 문서
- `C:\Users\SGJEONG99\OneDrive\문서\Claude\Projects\MS_SWMM\2026-06-09_0332\SESSION_HANDOFF_하네스_오케스트레이션.md`

---

## 3. 하네스 가이드 갱신 핵심 (GitHub 실측 검증 결과)

### Superpowers 식별자 정정 (최대 오류)
- 기존(틀림): 마켓플레이스 `obra/superpowers`, 설치 `superpowers@superpowers-dev`
- 정정(맞음): 마켓플레이스 **`obra/superpowers-marketplace`**, 설치 **`superpowers@superpowers-marketplace`**
- `obra/superpowers`는 코어 플러그인 소스 저장소이고, 등록 대상 마켓플레이스가 아님.
- 마켓플레이스 내 추가 플러그인(선택): `elements-of-style`, `superpowers-developing-for-claude-code`, `private-journal-mcp` (모두 `@superpowers-marketplace`).

### Harness 최신 정보
- 저장소 `revfactory/harness` (v1.2.0, Apache 2.0).
- 트리거: "build a harness for this project" / "하네스 구성해줘" / "ハーネスを構成して".
- 6단계 워크플로: 도메인 분석 → 팀 아키텍처 설계 → 에이전트 정의 생성 → 스킬 생성 → 통합·오케스트레이션 → 검증.
- 6개 팀 패턴: Pipeline, Fan-out/Fan-in, Expert Pool, Producer-Reviewer, Supervisor, Hierarchical Delegation.
- 실행 모드: **Agent Teams**(기본, 협업 2+ 에이전트) / **Subagents**(단발 작업).
- 요구사항: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` (공식 문서 https://code.claude.com/docs/en/agent-teams).
- 글로벌 스킬 직접 설치: `cp -r skills/harness ~/.claude/skills/harness`.
- 자매 저장소: `revfactory/harness-100`(사전 제작 100종, EN+KO), `revfactory/claude-code-harness`(A/B 실험: 저자 측정 +60%, 49.5→79.3, n=15, 제3자 재현 미완).

### 3개 마켓플레이스 설치 커맨드 (Claude Code CLI)
```bash
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin marketplace add revfactory/harness
claude plugin marketplace add obra/superpowers-marketplace

claude plugin install harness@harness
claude plugin install superpowers@superpowers-marketplace
```
Cowork/데스크톱 UI에서는 Customize → manage plugins → 위 GitHub 링크 추가.

---

## 4. 다른 Cowork 프로젝트에 적용하는 법

### 4-1. 오케스트레이션 지침 이식 (권장, 즉시 효과)
대상 프로젝트 폴더에 `CLAUDE.md`를 만들고 본 문서 **6장 전체 텍스트**를 붙여넣는다. 그러면 그 폴더 작업 시 Claude가 자동으로 읽고 따른다. 일회성으로는 채팅 첫 메시지에 6장을 붙여넣어도 된다.

### 4-2. harness/superpowers 플러그인 설치 (선택, Cowork 호환 미검증)
3장의 마켓플레이스 커맨드로 설치. 단, Agent Teams 플래그·훅·슬래시 커맨드는 Cowork에서 동작 보장이 안 되므로, 설치 후 실제로 트리거가 응답하는지 확인 필요. 안 되면 4-1의 지침 + 내장 Agent 서브에이전트로 폴백.

### 4-3. 점검 체크리스트
- [ ] 대상 프로젝트 루트에 `CLAUDE.md` 존재 및 오케스트레이션 섹션 포함?
- [ ] (플러그인 설치 시) 마켓플레이스 3개가 목록에 보이는가?
- [ ] (플러그인 설치 시) `/` 또는 `+`에서 harness/superpowers 스킬이 뜨는가?
- [ ] harness 사용 시 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 설정(Claude Code 한정)?

---

## 5. 알아둘 제약·미확인 사항 (정직하게)

- 이 Cowork 세션에는 harness/superpowers 플러그인이 **설치돼 있지 않다**(스킬 목록 기준).
- harness의 Agent Teams, superpowers의 훅·슬래시 커맨드는 **Claude Code 전용**이며 Cowork 동작은 미검증.
- A/B "+60%" 수치는 저자 자체 측정(n=15)이며 제3자 재현은 아직 없음. 의사결정 시 내부 파일럿 권장.
- 업로드된 원본 파일(uploads 영역)은 임시·읽기 전용이라 보존되지 않음. 실효 저장소는 각 프로젝트의 `CLAUDE.md`.

---

## 6. 오케스트레이션 지침 전체 텍스트 (복사용 — 다른 프로젝트 CLAUDE.md에 붙여넣기)

```markdown
# 오케스트레이션 지침 (멀티 에이전트 하네스)

> **사용법:** 이 파일 내용을 프로젝트 폴더의 `CLAUDE.md`에 붙여넣으면 그 폴더 작업 시 자동 적용된다. 일회성으로는 채팅 첫 메시지에 그대로 붙여넣어도 된다. 특정 프로젝트에 종속되지 않는 범용 지침이다.
>
> 각 항목의 근거는 공개된 1차 출처(공식 엔지니어링 블로그·동료심사 논문·공식 레포)에 기반한다. 문서 끝 **참고문헌** 참조.

---

비자명한 작업은 단일 처리하지 말고, **일군(서브에이전트)을 나눠** 작업·검수·확정 단계로 처리한다. 검수 강도는 작업 규모에 따라 자동으로 조절한다.

## 1. 기본 구조 — Orchestrator–Worker

하나의 **리드(오케스트레이터) 에이전트**가 작업을 분석·분해하고, 전문 **worker 에이전트**들에게 위임한다. worker끼리는 직접 소통하지 않으며, "다음에 무엇을 할지"의 모든 판단은 오케스트레이터가 보유한다. 각 worker에게는 ⑴ 명확한 목표, ⑵ 출력 형식, ⑶ 사용할 도구·소스 안내, ⑷ 작업 경계를 자기완결적으로 전달한다. [1][2]

> 근거: Anthropic은 이 orchestrator-worker 구조(리드 1 + 병렬 서브에이전트 3~5)로 내부 리서치 평가에서 단일 에이전트 대비 90.2% 향상을 보고했다. [1]

## 2. 작업 흐름

1. **분해(Plan)** — 작업을 독립 단위로 쪼갠다. 의존성 없는 단위는 병렬, 있는 단위는 순차로 배치한다. (Anthropic 5대 워크플로 중 *parallelization* / *orchestrator-worker*) [2]
2. **실행(Work)** — 각 단위를 worker에 배정한다. 서로 독립이면 한 번에 동시 실행한다.
3. **검수(Verify)** — 산출물을 **별도 에이전트**가 평가한다. 작성자와 검수자는 반드시 분리한다. (*evaluator-optimizer*: 생성 LLM과 평가 LLM을 분리해 피드백 루프 구성) [2][4]
4. **확정(Confirm)** — 검수 통과분만 최종 반영한다. 실패 시 해당 단위만 재작업 → 재검수(루프). [3][5]

## 3. 검수 강도 — 작업 규모로 자동 판단

명확한 평가 기준이 있고 반복 개선의 가치가 측정 가능할 때 검수 루프가 가장 효과적이다. [2] 따라서 규모에 맞춰 단계 수를 조절한다.

- **사소** (파일명 변경, 1~2줄 수정, 단순 조회): 검수 생략, 자체 확인만.
- **일반** (스크립트 작성, 데이터 처리, 문서 1편): worker 산출 후 **검수 1회**.
- **고위험** (수치 계산·모델 캘리브레이션, 다중 파일 변경, 보고서/논문 핵심 수치, 모델 결과 해석): 검수 후 **다른 에이전트가 교차 재검수**. 코드·수치는 가능하면 **독립 재실행**으로 검증한다. (Reflexion: 피드백을 언어로 반영해 다음 시도를 개선하는 루프; 코딩 벤치 HumanEval pass@1 91% 달성) [5]

## 4. 역할 분담

- **탐색(Explore)** — 넓게 파일·자료를 훑어 위치·후보를 찾고 결론만 회수한다.
- **설계(Plan)** — 구현 전략·단계·트레이드오프를 수립한다. 코드는 건드리지 않는다.
- **작업(Worker)** — 실제 코드·문서·분석을 생성한다. [1]
- **검수(Verifier / LLM-as-a-judge)** — 정확성·논리·재현성을 점검한다. 수치는 재계산, 코드는 재실행, 주장은 출처와 대조한다. 일관성 확보·편향 완화를 위해 **판정에 근거(reasoning)를 함께 요구**한다. [4]

## 5. 운영 원칙

- **작성자 ≠ 검수자.** 같은 에이전트가 자기 산출물을 검수하지 않는다. [2][4]
- 검수는 "통과 / 수정요청"을 **근거와 함께** 반환한다. 모호한 OK 금지. [4]
- 독립 작업은 한 번에 띄워 병렬 실행한다. 순차 의존이 있을 때만 기다린다. [1][2]
- **단순함 우선** — 더 단순한 방법으로 충분하면 멀티에이전트를 쓰지 않는다. 프롬프트→평가→필요 시에만 다단계 확장. [2]
- 진행 상황은 전체 단계 대비 현재 위치를 **퍼센트**로 표시한다. (예: `[3/5 | 60%]`)
- 불확실/가설 사항은 검수 단계에서 명확히 구분해 표기하고, 1차 출처가 검증된 자료만 사용한다.

## 6. 적용 트리거

- 3단계 이상 또는 다중 파일이 걸린 작업 → 위 흐름을 적용한다.
- 수치·코드·보고서 핵심 결과물 → 반드시 검수 단계를 거친다.
- 단순 대화·단발 조회 → 흐름 생략, 바로 응답한다. [2]

---

## 참고문헌

[1] Anthropic, *How we built our multi-agent research system* (Engineering blog, 2025). https://www.anthropic.com/engineering/multi-agent-research-system — orchestrator-worker 구조, 병렬 서브에이전트, 자기완결적 태스크 기술, 90.2% 향상.

[2] Anthropic, *Building Effective Agents* (2024). https://www.anthropic.com/research/building-effective-agents — 5대 워크플로 패턴(prompt chaining, routing, parallelization, orchestrator-worker, evaluator-optimizer)과 "단순함 우선" 원칙.

[3] LangChain, *langgraph-supervisor* (공식 라이브러리/레포). https://github.com/langchain-ai/langgraph-supervisor-py — 중앙 supervisor가 worker를 조율하고 통신·위임을 통제하는 계층형 멀티에이전트 구현.

[4] Gu et al., *A Survey on LLM-as-a-Judge*, arXiv:2411.15594 (2024). https://arxiv.org/abs/2411.15594 — LLM 평가자의 신뢰성·일관성·편향 완화 설계.

[5] Shinn et al., *Reflexion: Language Agents with Verbal Reinforcement Learning*, NeurIPS 2023, arXiv:2303.11366. https://arxiv.org/abs/2303.11366 — 언어적 자기반성 피드백 루프, HumanEval pass@1 91%.

[6] Wu et al., *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation*, arXiv:2308.08155 (2023). https://arxiv.org/abs/2308.08155 — 다중 에이전트 대화 기반 협업 프레임워크(참고: 대안적 협업 패턴).
```

---

## 7. 출처

- Harness: https://github.com/revfactory/harness , https://code.claude.com/docs/en/agent-teams , https://github.com/revfactory/harness-100 , https://github.com/revfactory/claude-code-harness
- Superpowers: https://github.com/obra/superpowers-marketplace , https://github.com/obra/superpowers
- 오케스트레이션 근거: 위 6장 참고문헌 [1]~[6].
