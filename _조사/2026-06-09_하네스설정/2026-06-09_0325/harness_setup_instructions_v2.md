# INSTRUCTION: 하네스 환경 설정 (v2, 2026-06-09 검증)

이 파일을 읽으면, 아래 순서대로 Claude 하네스 환경(3개 마켓플레이스)을 설정하도록 사용자를 안내/실행하라. 단계마다 검증을 거친 뒤 다음으로 넘어간다.

> **v1 대비 수정**: superpowers 마켓플레이스 `obra/superpowers` → `obra/superpowers-marketplace`, 설치 `superpowers@superpowers-dev` → `superpowers@superpowers-marketplace`. harness 플래그는 공식 요구사항으로 확정(Subagents 폴백 모드 존재).

## 등록 대상 마켓플레이스
- claude-plugins-official → `anthropics/claude-plugins-official`
- harness-marketplace → `revfactory/harness`
- superpowers-marketplace → `obra/superpowers-marketplace`  (프레임워크 코드 저장소 `obra/superpowers` 와 구분)

## 실행 순서

1. **Git 확인** → 검증: `git --version` 이 버전을 출력. 없으면 OS별 설치 안내 후 재확인.

2. **마켓플레이스 등록** (환경에 따라 택1)
   - Cowork/데스크톱 UI: Customize → manage plugins → 각 GitHub 링크 추가.
   - Claude Code CLI:
     ```
     /plugin marketplace add anthropics/claude-plugins-official
     /plugin marketplace add revfactory/harness
     /plugin marketplace add obra/superpowers-marketplace
     ```
   → 검증: 마켓플레이스 목록에 3개가 모두 보이는지 확인. 표시된 실제 마켓플레이스명을 기록.

3. **플러그인 설치**
   ```
   /plugin install harness@harness
   /plugin install superpowers@superpowers-marketplace
   ```
   install 커맨드의 `@마켓플레이스명`은 2단계에서 기록한 실제 이름으로 맞춘다.
   superpowers 는 공식 마켓플레이스 경유 `superpowers@claude-plugins-official` 로도 설치 가능.
   → 검증: `/` 또는 `+` 에서 해당 스킬/커맨드(`/brainstorm`, `/write-plan`, `/execute-plan` 등)가 나타나는지 확인.

4. **harness 사전조건 (Agent Teams)**
   ```
   export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
   ```
   셸 프로파일(.zshrc/.bashrc)에 추가 후 재시작. 공식 문서(code.claude.com/docs/en/agent-teams)의 정식 요구사항.
   → 폴백: 플래그를 못 켜는 환경(예: Cowork)이면 harness 의 **Subagents 모드**로 단발 작업만 수행(에이전트 간 통신 없음). 팀 오케스트레이션이 필요하면 Claude Code CLI 에서 플래그를 켤 것.

5. **재시작 후 동작 확인** → 검증: harness 트리거(`build a harness for this project` / `하네스 구성해줘` / `ハーネスを構成して`) 또는 superpowers 스킬이 응답하는지 확인.

## 알려진 제약
- harness 기본 모드(Agent Teams: `TeamCreate + SendMessage + TaskCreate`)는 위 플래그가 켜진 Claude Code 환경에서 동작. Cowork 에서의 팀 실행은 플래그 미적용 가능성으로 Subagents 폴백 권장.
- superpowers 의 SessionStart 훅 등 Claude Code 전용 동작은 Cowork 에서 그대로 동작하지 않을 수 있음.
- 마켓플레이스/플러그인 정확한 식별자는 각 저장소 `.claude-plugin/marketplace.json` 의 `name` 기준.

## 출처
- <https://github.com/revfactory/harness> (v1.2.0, Requirements: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)
- <https://code.claude.com/docs/en/agent-teams>
- <https://github.com/obra/superpowers-marketplace>
