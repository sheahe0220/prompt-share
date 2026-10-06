# 세션 핸드오프 — 하네스/오케스트레이션 지침 갱신

> **목적:** 이 세션(2026-06-09)에서 진행한 작업, 생성·수정 파일, 검증된 1차 출처 사실, 적용 방법을 한 파일로 정리한다. 다른 Cowork 프로젝트에 그대로 이식하기 위한 핸드오프 문서다.
> **작성 시각:** 2026-06-09 03:32

---

## 1. 이 세션에서 한 일 (요약)

1. `hanes` 폴더의 하네스 환경 설치 가이드 2종을 1차 출처로 검증 후 v2로 갱신.
2. 멀티 에이전트 오케스트레이션 지침(`ORCHESTRATION_GUIDE.md` = 석사학위논문 프로젝트 `CLAUDE.md` 본문)을 harness 검증 사양으로 v2 갱신하고 활성 `CLAUDE.md`에 적용.
3. (이 문서) 전체 핸드오프 정리.

---

## 2. 생성·수정 파일 경로

### 2.1 하네스 설치 가이드 v2 (원본 유지, 신규 폴더에 v2 생성)

| 구분 | 절대경로 |
|---|---|
| 원본 v1 (유지) | `C:\Users\SGJEONG99\Desktop\hanes\harness_setup_guide.md` |
| 원본 v1 (유지) | `C:\Users\SGJEONG99\Desktop\hanes\harness_setup_instructions.md` |
| 갱신 v2 | `C:\Users\SGJEONG99\Desktop\hanes\2026-06-09_0325\harness_setup_guide_v2.md` |
| 갱신 v2 | `C:\Users\SGJEONG99\Desktop\hanes\2026-06-09_0325\harness_setup_instructions_v2.md` |

### 2.2 오케스트레이션 지침 v2

| 구분 | 절대경로 |
|---|---|
| 갱신 v2 (버전 보존본) | `C:\Users\SGJEONG99\OneDrive\문서\Claude\Projects\석사학위논문\2026-06-09_0328\ORCHESTRATION_GUIDE_v2.md` |
| 활성 적용본 (교체됨) | `C:\Users\SGJEONG99\OneDrive\문서\Claude\Projects\석사학위논문\CLAUDE.md` |
| 업로드 원본 v1 (참조) | 사용자가 업로드한 `ORCHESTRATION_GUIDE.md` (v1) |

### 2.3 이 핸드오프 문서

| 구분 | 절대경로 |
|---|---|
| 핸드오프 | `C:\Users\SGJEONG99\OneDrive\문서\Claude\Projects\석사학위논문\2026-06-09_0332\SESSION_HANDOFF_harness_orchestration.md` |

---

## 3. 검증된 사실과 정정 (1차 출처)

### 3.1 정정 1 — superpowers 마켓플레이스 식별자 오류

- **틀린 기존값:** 마켓플레이스 `obra/superpowers`, 설치 `superpowers@superpowers-dev`.
- **정정값:** 마켓플레이스 등록 저장소 `obra/superpowers-marketplace`, 설치 `superpowers@superpowers-marketplace`.
- `obra/superpowers` 는 **프레임워크 코드** 저장소이고, 플러그인 마켓플레이스로 등록할 저장소는 `obra/superpowers-marketplace` 로 분리돼 있다.
- 대안 경로: 공식 마켓플레이스 경유 `superpowers@claude-plugins-official`.
- 출처: <https://github.com/obra/superpowers-marketplace>, <https://github.com/obra/superpowers>

### 3.2 정정 2 — harness Agent Teams 플래그 위상

- 기존 가이드는 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 을 "미확인 실험 기능"으로 표기.
- **정정:** 해당 플래그는 현재 Claude Code 공식 문서에 harness 정식 요구사항으로 등재.
- harness 는 **Subagents 폴백 모드**가 있어 플래그 없이도 단발 작업은 동작(= Cowork 경로).
- harness 현재 버전 **v1.2.0**, Apache-2.0, GitHub 3.6k stars.
- 출처: <https://github.com/revfactory/harness>, <https://code.claude.com/docs/en/agent-teams>

### 3.3 확인되어 유지된 값

- harness 마켓플레이스 `revfactory/harness`, 설치 `harness@harness` (정확).
- 공식 마켓플레이스 `anthropics/claude-plugins-official` (정확).

---

## 4. harness 핵심 사양 (오케스트레이션 지침에 반영한 내용)

### 4.1 실행 모드 2종

| 모드 | 구현 | 전제 | 적용 |
|---|---|---|---|
| Agent Teams (기본) | `TeamCreate + SendMessage + TaskCreate` | `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` | 2개 이상 에이전트 상호 통신·협업 |
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

---

## 5. 다른 Cowork 프로젝트에 적용하는 법

### 5.1 오케스트레이션 지침 이식

1. `ORCHESTRATION_GUIDE_v2.md` 내용을 대상 프로젝트 폴더의 `CLAUDE.md` 에 붙여넣는다. (프로젝트별 자동 적용.)
2. **Cowork 환경 주의:** Agent Teams 플래그가 적용 안 될 수 있으므로 Subagents 폴백 모드로 동작. 지침의 "0. 실행 모드" 절이 이 폴백을 명시한다. 산출물에 폴백 사실 한 줄 표기.
3. 검수 단계(작성자≠검수자)는 모드와 무관하게 유지.

### 5.2 하네스 플러그인 설치 (Claude Code / Cowork)

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

## 6. 참고문헌 (오케스트레이션 지침 [1]~[8])

[1] Anthropic, *How we built our multi-agent research system* (2025). https://www.anthropic.com/engineering/multi-agent-research-system
[2] Anthropic, *Building Effective Agents* (2024). https://www.anthropic.com/research/building-effective-agents
[3] LangChain, *langgraph-supervisor*. https://github.com/langchain-ai/langgraph-supervisor-py
[4] Gu et al., *A Survey on LLM-as-a-Judge*, arXiv:2411.15594 (2024). https://arxiv.org/abs/2411.15594
[5] Shinn et al., *Reflexion*, NeurIPS 2023, arXiv:2303.11366. https://arxiv.org/abs/2303.11366
[6] Wu et al., *AutoGen*, arXiv:2308.08155 (2023). https://arxiv.org/abs/2308.08155
[7] revfactory, *harness* (v1.2.0, Apache-2.0). https://github.com/revfactory/harness
[8] Anthropic, *Agent Teams* (공식 문서). https://code.claude.com/docs/en/agent-teams
