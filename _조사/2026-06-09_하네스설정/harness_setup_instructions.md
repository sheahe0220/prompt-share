# INSTRUCTION: 하네스 환경 설정

이 파일을 읽으면, 아래 순서대로 Claude 하네스 환경(3개 마켓플레이스)을 설정하도록 사용자를 안내/실행하라. 단계마다 검증을 거친 뒤 다음으로 넘어간다.

## 등록 대상 마켓플레이스
- claude-plugins-official → `anthropics/claude-plugins-official`
- harness → `revfactory/harness`
- superpowers-marketplace → `obra/superpowers-marketplace`  (※ `obra/superpowers` 아님 — 그건 플러그인 본체)

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
   (superpowers는 `/plugin install superpowers@claude-plugins-official` 로도 설치 가능 — 공식 마켓플레이스에도 등재.)
   → 검증: `/` 또는 `+` 에서 해당 스킬/커맨드가 나타나는지 확인.

4. **harness 사전조건 (Claude Code 한정)**
   ```
   export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
   ```
   셸 프로파일(.zshrc/.bashrc)에 추가 후 재시작.
   → 주의: Cowork에서는 이 플래그가 적용되지 않을 수 있으므로, 팀 오케스트레이션이 안 되면 스킬 단독 사용으로 폴백.

5. **재시작 후 동작 확인** → 검증: harness 트리거("build a harness for this project" / "하네스 구성해줘") 또는 superpowers 스킬이 응답하는지 확인.

## 알려진 제약
- harness(v1.2.0)는 Requirements에 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 명시. 플래그 없으면 Subagents 모드로 폴백, 멀티 에이전트 팀 실행은 Cowork에서 미검증.
- superpowers의 SessionStart 훅 등 Claude Code 전용 동작은 Cowork에서 그대로 동작하지 않을 수 있음.
- 마켓플레이스/플러그인 정확한 식별자는 각 저장소 `.claude-plugin/marketplace.json` 의 `name` 기준.
- (2026-06 검증) harness=`revfactory/harness`+`harness@harness`, superpowers=`obra/superpowers-marketplace`+`superpowers@superpowers-marketplace`.
