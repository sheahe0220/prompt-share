# 세션 핸드오프 (정본) — 하네스 / 오케스트레이션 지침

> **목적:** 세 개의 핸드오프 문서를 하나로 병합한 정본. 이 세션(2026-06-09)에서 한 일, 생성·수정 파일, 1차 출처로 검증한 사실과 정정, harness 사양, 다른 Cowork 프로젝트 이식 방법, 그리고 오케스트레이션 지침 전문을 모두 담는다.
> **병합본 작성:** 2026-06-09 03:37
> **주의:** 세 원본은 각기 다른 프로젝트(MS_SWMM / 석사학위논문 / 대심도 과제)에서 작성돼 경로만 달랐다. 본 정본은 프로젝트 경로를 `<프로젝트 폴더>`로 일반화한다. 어느 Cowork 프로젝트에든 그대로 복붙 가능.

---

## 0. 개념 구분 (가장 먼저 이해할 것)

혼동하기 쉬운 두 가지를 분리한다. 같은 게 아니다.

| 구분 | 정체 | Cowork 적용 |
|---|---|---|
| **오케스트레이션 "지침"** | `CLAUDE.md`에 넣는 텍스트 행동 규칙. Claude가 매 세션 읽고 따른다. | **적용됨.** 내장 Agent(서브에이전트) 도구로 실제 실행도 가능. |
| **harness / superpowers "플러그인"** | 마켓플레이스에서 설치하는 실제 플러그인(스킬·커맨드·훅). | **별개. 일부 기능 Cowork 미검증.** 설치 필요. |

지침을 `CLAUDE.md`에 넣었다고 플러그인이 깔리는 것은 아니다.

---

## 1. 이 세션에서 한 일 (요약)

1. `hanes` 폴더의 하네스 환경 설치 가이드 2종을 1차 출처(GitHub 실제 저장소, 2026-06 확인)로 검증 후 갱신. 최대 정정은 **superpowers 마켓플레이스/설치 식별자**.
2. 멀티 에이전트 오케스트레이션 지침을 harness 검증 사양으로 갱신하고 활성 `CLAUDE.md`에 적용.
3. (이 문서) 전체 핸드오프 정리 및 3개 문서 병합.

---

## 2. 생성·수정 파일 경로

### 2.1 하네스 설치 가이드 (원본 유지 + 타임스탬프 폴더에 갱신본)

| 구분 | 경로 |
|---|---|
| 원본 (유지) | `C:\Users\SGJEONG99\Desktop\hanes\harness_setup_guide.md` |
| 원본 (유지) | `C:\Users\SGJEONG99\Desktop\hanes\harness_setup_instructions.md` |
| 갱신본 | `C:\Users\SGJEONG99\Desktop\hanes\2026-06-09_0325\harness_setup_guide.md` |
| 갱신본 | `C:\Users\SGJEONG99\Desktop\hanes\2026-06-09_0325\harness_setup_instructions.md` |

### 2.2 오케스트레이션 지침 적용 (활성 CLAUDE.md)

| 구분 | 경로 |
|---|---|
| 활성 적용본 (교체됨) | `<프로젝트 폴더>\CLAUDE.md` 의 "오케스트레이션 지침" 섹션 |
| 버전 보존본(선택) | `<프로젝트 폴더>\<타임스탬프>\ORCHESTRATION_GUIDE_v2.md` |

> 활성 `CLAUDE.md`는 프로젝트 루트에 있어 매 세션 자동 로드된다(= 지속 적용). 세션에 따라 실제 적용 프로젝트는 MS_SWMM / 석사학위논문 / 대심도 과제로 달랐다.

### 2.3 이 병합 문서

- `C:\Users\SGJEONG99\Desktop\hanes\MERGED_2026-06-09_0337\SESSION_HANDOFF_하네스_오케스트레이션_MERGED.md`

---

## 3. 검증된 사실과 정정 (1차 출처)

### 3.1 정정 1 — superpowers 마켓플레이스 식별자 오류

- **틀린 기존값:** 마켓플레이스 `obra/superpowers`, 설치 `superpowers@superpowers-dev`.
- **정정값:** 마켓플레이스 등록 저장소 **`obra/superpowers-marketplace`**, 설치 **`superpowers@superpowers-marketplace`**.
- `obra/superpowers`는 프레임워크/코어 코드 저장소이고, 마켓플레이스로 등록할 저장소는 `obra/superpowers-marketplace`로 분리돼 있다.
- 마켓플레이스 내 추가 플러그인(선택): `elements-of-style`, `superpowers-developing-for-claude-code`, `private-journal-mcp` (모두 `@superpowers-marketplace`).
- 출처: <https://github.com/obra/superpowers-marketplace>, <https://github.com/obra/superpowers>

### 3.2 정정 2 — harness Agent Teams 플래그 위상

- 기존 가이드는 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`을 "미확인 실험 기능"으로 표기.
- **정정:** 해당 플래그는 harness 저장소 Requirements에 정식 요구사항으로 등재(공식 문서 링크 포함).
- harness는 **Subagents 폴백 모드**가 있어 플래그 없이도 단발 작업은 동작(= Cowork 경로).
- harness 현재 **v1.2.0**, Apache-2.0, GitHub 약 3.6k stars.
- 출처: <https://github.com/revfactory/harness>, <https://code.claude.com/docs/en/agent-teams>

### 3.3 확인되어 유지된 값

- harness 마켓플레이스 `revfactory/harness`, 설치 `harness@harness` (정확).
- 공식 마켓플레이스 `anthropics/claude-plugins-official` (정확).

---

## 4. harness 핵심 사양 (오케스트레이션 지침에 반영)

### 4.1 실행 모드 2종

| 모드 | 구현 | 전제 | 적용 |
|---|---|---|---|
| Agent Teams (기본) | `TeamCreate + SendMessage + TaskCreate` | `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` | 2+ 에이전트 상호 통신·협업 |
| Subagents (폴백) | Agent 도구 직접 호출 | 플래그 불필요 | 단발 위임, **Cowork 기본 경로** |

### 4.2 6개 팀 아키텍처 패턴 → 작업 흐름 매핑

| 패턴 | 적용 상황 | 지침 위치 |
|---|---|---|
| Pipeline | 순차 의존 작업 | 흐름 2단계 순차 |
| Fan-out/Fan-in | 병렬 독립 작업 | 흐름 2단계 병렬 |
| Expert Pool | 맥락별 선택적 전문가 호출 | 역할 분담 |
| Producer-Reviewer | 생성 후 품질 검수 | 검수(작성자≠검수자) |
| Supervisor | 중앙 동적 분배 | Orchestrator–Worker |
| Hierarchical Delegation | 상향식 재귀 위임 | 고위험 다단 분해 |

### 4.3 근거 수치 (가설로 표기할 것)

- harness 저자 자체측정 A/B(15개 SW 과제): 평균 품질 49.5→79.3(**+60%**), 승률 15/15, 출력 분산 −32%.
- **저자 측정·제3자 재현 미완.** 채택 전 자체 파일럿 측정 권장.

### 4.4 자매 저장소

- `revfactory/harness-100` — 10개 도메인 100종 사전 제작 하네스(EN+KO, 200패키지).
- `revfactory/claude-code-harness` — A/B 효과 측정 실험 레포.

---

## 5. 다른 Cowork 프로젝트에 적용하는 법

### 방법 A — 프로젝트별 CLAUDE.md (권장)

대상 프로젝트 폴더 루트에 `CLAUDE.md`를 만들고 **7장 "오케스트레이션 지침" 전문**을 붙여넣는다. 그 폴더에서 작업 시 자동 로드된다. 프로젝트 종속이 아닌 범용 지침이라 어느 폴더에든 복붙 가능.

**Cowork 환경 주의:** Agent Teams 플래그가 적용 안 될 수 있으므로 Subagents 폴백 모드로 동작. 산출물에 폴백 사실 한 줄 표기. 검수 단계(작성자≠검수자)는 모드와 무관하게 유지.

### 방법 B — 일회성

새 채팅 첫 메시지에 7장 전문을 붙여넣으면 그 대화에 한해 적용.

### 방법 C — 자동 메모리 (세션 제약 가능)

정석은 자동 메모리 폴더(`...\spaces\<space-id>\memory\`)에 feedback/reference 메모리(.md) + `MEMORY.md` 인덱스로 저장하는 것. 단 환경에 따라 메모리 폴더가 **읽기 전용으로 마운트**되어 쓰기가 막힐 수 있음(한 세션에서 실제 발생). 이 경우 방법 A(CLAUDE.md)로 폴백.

> **함의:** Cowork에서 "기억해둬"가 항상 자동 메모리로 영구 저장되는 것은 아니다. 확실히 남기려면 연결된 폴더의 파일(CLAUDE.md 등)로 박아두는 게 안전하다.

### 하네스 플러그인 설치 (Claude Code / Cowork)

```
# 마켓플레이스 등록
/plugin marketplace add anthropics/claude-plugins-official
/plugin marketplace add revfactory/harness
/plugin marketplace add obra/superpowers-marketplace

# 플러그인 설치
/plugin install harness@harness
/plugin install superpowers@superpowers-marketplace

# harness 팀 모드 전제 (Claude Code 한정)
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

- Cowork 데스크톱 UI: Customize → manage plugins → 위 GitHub 링크 3개 추가 후 Install.
- `/plugin` 미인식 시: `npm update -g @anthropic-ai/claude-code` 후 재시작.

---

## 6. 다음 작업 시 체크리스트 (재현용)

1. 하네스 설치 안내 시 식별자는 3장 표 그대로(superpowers는 `-marketplace` 붙는 쪽).
2. 비자명 작업은 7장 흐름(작업→검수→확정), 작성자≠검수자, 고위험은 독립 재실행 교차검증.
3. 진행률은 `[n/N | %]` 표기.
4. 불확실 정보는 1차 출처(공식 레포·논문·공식 블로그) 검증 후 인용. A/B 수치는 가설로 표기.
5. 영구 반영이 필요하면 메모리 쓰기 시도 → 막히면 CLAUDE.md로 폴백.

---

## 7. 오케스트레이션 지침 전문 (복사용 — 대상 프로젝트 CLAUDE.md에 붙여넣기)

```markdown
# 오케스트레이션 지침 (멀티 에이전트 하네스)

> **사용법:** 이 파일 내용을 프로젝트 폴더의 `CLAUDE.md`에 붙여넣으면 그 폴더 작업 시 자동 적용된다. 일회성으로는 채팅 첫 메시지에 그대로 붙여넣어도 된다. 특정 프로젝트에 종속되지 않는 범용 지침이다.
>
> 각 항목의 근거는 공개된 1차 출처(공식 엔지니어링 블로그·동료심사 논문·공식 레포)에 기반한다. 문서 끝 **참고문헌** 참조.

## 0. 실행 모드 (Cowork/Claude Code 공통)

- 기본은 **Agent Teams**(TeamCreate + SendMessage + TaskCreate). 단 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`이 필요하며 Cowork에서는 미적용일 수 있다.
- 플래그가 없거나 Cowork 환경이면 **Subagents 폴백**(Agent 도구 직접 호출)으로 동작한다. 폴백 사용 시 산출물에 한 줄 명시한다.
- 어느 모드든 검수 단계(작성자≠검수자)는 유지한다.

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

[1] Anthropic, *How we built our multi-agent research system* (Engineering blog, 2025). https://www.anthropic.com/engineering/multi-agent-research-system
[2] Anthropic, *Building Effective Agents* (2024). https://www.anthropic.com/research/building-effective-agents
[3] LangChain, *langgraph-supervisor*. https://github.com/langchain-ai/langgraph-supervisor-py
[4] Gu et al., *A Survey on LLM-as-a-Judge*, arXiv:2411.15594 (2024). https://arxiv.org/abs/2411.15594
[5] Shinn et al., *Reflexion: Language Agents with Verbal Reinforcement Learning*, NeurIPS 2023, arXiv:2303.11366. https://arxiv.org/abs/2303.11366
[6] Wu et al., *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation*, arXiv:2308.08155 (2023). https://arxiv.org/abs/2308.08155
[7] revfactory, *harness* (v1.2.0, Apache-2.0). https://github.com/revfactory/harness
[8] Anthropic, *Agent Teams* (공식 문서). https://code.claude.com/docs/en/agent-teams
```
