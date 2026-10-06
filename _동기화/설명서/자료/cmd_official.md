# Claude Code 명령 공식 참조 (한국어)

만든 날 2026-09-29. CLI 2.1.283, VS Code 확장 2.1.284. 모든 줄은 code.claude.com 공식 문서나 이 PC 의 `claude --help` 출력에 근거한다. 슬래시 명령의 출처는 https://code.claude.com/docs/en/commands 이다.

VS Code 칸의 뜻: 됨은 vs-code 문서가 확장에서 쓴다고 적은 것, 안 됨은 문서가 삭제나 대체를 적은 것, 확인 못 함은 문서가 '일부만 지원, / 로 확인'이라고만 한 것이다.

## 1. 슬래시 명령

### 대화·세션 (20)

| 명령 | 별칭 | 인자 | 하는 일 | 쓰는 때 | VS Code | 근거 |
|---|---|---|---|---|---|---|
| `/add-dir` |  | `<path>` | 이번 세션에서 파일을 읽고 고칠 작업 폴더를 하나 더 붙인다. | 과업 폴더에서 일하다 공용 원자료 폴더도 읽게 할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/background` | /bg | `[prompt]` | 현재 세션을 백그라운드 에이전트로 떼어 내 계속 돌리고 터미널을 비운다. | 648 회 모의 같은 긴 작업을 걸어 두고 다른 일을 할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/branch` |  | `[name]` | 지금 시점에서 대화를 갈라 다른 방향을 시험하고 원래 대화는 보존한다. | 보정 방법 A 와 B 를 따로 시험해 볼 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음. 같은 기능은 메시지 위 되감기 버튼의 Fork conversation from here |
| `/btw` |  | `[question]` | 대화 기록에 남기지 않고 현재 세션에 대해 곁가지 질문을 한다. | 모의 도중 이 변수가 무슨 뜻인지 잠깐 물을 때 | 됨 | vs-code 문서 'Use the prompt box' 절에 명시 (답이 옆 패널에 열림) |
| `/cd` |  | `<path>` | 대화를 유지한 채 세션의 작업 폴더를 옮긴다. | 과업 폴더를 잘못 잡고 시작했을 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/clear` | /reset, /new | `[name]` | 문맥을 비운 새 대화를 시작한다. 이전 대화는 /resume 으로 돌아갈 수 있다. | SWMM 작업을 끝내고 보고서 작업으로 넘어갈 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/compact` |  | `[instructions]` | 지금까지의 대화를 요약해 문맥 공간을 비운다. 요약 초점을 지시할 수 있다. | 긴 자료 조사 뒤 핵심만 남기고 이어갈 때 | 됨 | vs-code 문서 'Use the prompt box' 절에 명시 (문맥 표시기 설명에 /compact 수동 실행 명시) |
| `/copy` |  | `[N]` | 마지막(또는 N 번째 전) 응답을 클립보드로 복사한다. 코드 블록이 있으면 고르게 한다. | Claude 가 쓴 표를 보고서에 붙여 넣을 때 | 됨 | vs-code 문서 'Use the prompt box' 절에 명시 (v2.1.277 이상) |
| `/desktop` | /app |  | 현재 세션을 Claude Code 데스크톱 앱에서 이어 간다. macOS 나 x64 Windows 와 구독이 필요하다. | 터미널 작업을 데스크톱 앱 화면으로 옮길 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/exit` | /quit |  | CLI 를 끝낸다. 백그라운드 세션에 붙어 있으면 떼어 내기만 한다. | 터미널 세션을 마칠 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/export` |  | `[filename]` | 현재 대화를 평문으로 내보낸다. 파일명을 주면 바로 저장한다. | 그날 대화를 일지 근거로 남길 때 | 됨 | vs-code 문서 'Use the prompt box' 절에 명시 (v2.1.280 이상) |
| `/fork` |  | `[prompt]` | 현재 대화를 새 백그라운드 세션으로 복사하고 여기서는 계속 일한다. | 같은 문맥으로 그림 작업을 따로 돌릴 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/goal` |  | `[condition\|clear]` | 조건이 충족될 때까지 여러 턴에 걸쳐 계속 일하게 하는 목표를 건다. | 검증 스크립트가 통과할 때까지 고치게 할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/list-agents` | /peers |  | 메시지를 보낼 수 있는 서브에이전트, 팀원, 다른 세션 이름을 나열한다. | 다른 창의 세션에 결과를 넘기려 할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/recap` |  |  | 현재 세션을 한 줄로 요약한다. | 점심 뒤 어디까지 했는지 볼 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/rename` |  | `[name]` | 현재 세션 이름을 바꾼다. 이름을 빼면 대화에서 자동으로 짓는다. | 세션을 과업명으로 구분할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음. 확장은 명령 팔레트 Rename Session Tab |
| `/resume` | /continue | `[session]` | ID 나 이름으로 예전 대화를 이어 가거나 세션 선택기를 연다. | 어제 하던 보고서 대화를 이어 갈 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/rewind` | /checkpoint, /undo |  | 대화나 코드(또는 둘 다)를 이전 시점으로 되돌리거나 선택 메시지부터 요약한다. | Claude 가 스크립트를 잘못 고쳐 되돌릴 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음. 확장은 메시지 위 되감기 버튼(Rewind code to here 등)으로 같은 일 |
| `/stop` |  |  | 붙어 있는 백그라운드 세션을 멈춘다(기록과 worktree 는 남는다). | 백그라운드 모의 세션을 끝낼 때 | 확인 못 함 | commands 문서: 백그라운드 세션에 붙어 있을 때만 사용 가능. 확장에서의 동작은 언급 없음 |
| `/subtask` |  | `<task>` | 전체 대화를 물려받은 서브에이전트를 백그라운드로 띄우고 결과를 이 대화로 돌려받는다. | 본 작업 중 참고문헌 확인만 따로 맡길 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |

### 모델·속도 (5)

| 명령 | 별칭 | 인자 | 하는 일 | 쓰는 때 | VS Code | 근거 |
|---|---|---|---|---|---|---|
| `/advisor` |  | `[model\|off]` | 작업 중 요소마다 두 번째 모델에게 조언을 받는 advisor 도구를 켜거나 끈다. | 까다로운 보정 스크립트를 짤 때 다른 모델의 검토를 곁들일 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/autocompact` |  | `[auto\|<tokens>]` | 문맥 창이 얼마나 차면 자동 압축할지 정하고 사용자 설정에 저장한다. | 긴 모의 로그를 다루는 세션에서 압축 시점을 늦출 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/effort` |  | `[level\|auto\|status\|ultracode [on\|off]]` | 추론 노력 수준(low 에서 xhigh, max, auto)을 정하거나 ultracode 를 켜고 끈다. | 간단한 파일 정리는 low, 수식 검토는 high 로 둘 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음. 확장은 모델 선택기의 Effort 줄로 같은 조정 |
| `/fast` |  | `[on\|off]` | fast 모드를 켜거나 끈다. | 간단한 이름 바꾸기를 빨리 끝낼 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/model` |  | `[model]` | 모델을 바꾸고 새 세션 기본값으로 저장한다. 선택기에서 좌우 화살표로 노력 수준도 조정한다. | 보고서 문장 다듬기는 가벼운 모델로 바꿀 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음. 확장은 명령 메뉴의 Switch model 과 모델 이름 버튼으로 같은 일 |

### 지침·기억 (2)

| 명령 | 별칭 | 인자 | 하는 일 | 쓰는 때 | VS Code | 근거 |
|---|---|---|---|---|---|---|
| `/init` |  |  | 프로젝트에 CLAUDE.md 안내 파일을 만든다. | 새 과업 폴더를 처음 열었을 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/memory` |  |  | CLAUDE.md 파일을 편집하고 auto memory 를 켜고 끄거나 항목을 본다. | 과업 고정사실을 지침에 추가할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음. 확장은 명령 메뉴 Customize 의 Memory, Instructions 로 같은 일 |

### 권한·안전 (6)

| 명령 | 별칭 | 인자 | 하는 일 | 쓰는 때 | VS Code | 근거 |
|---|---|---|---|---|---|---|
| `/auto-mode-setup` |  |  | 프로젝트와 최근 세션을 보고 auto 모드의 environment 항목 초안을 만들어 사용자 설정에 저장한다. | auto 모드가 자주 막는 명령을 줄이고 싶을 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/fewer-permission-prompts` |  |  | [번들 스킬] 기록을 훑어 자주 쓰는 읽기 전용 Bash 와 MCP 호출을 찾아 프로젝트 settings.json 허용 목록에 넣는다. | ls, git status 허용을 매번 누르기 번거로울 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/permissions` | /allowed-tools |  | 도구 권한의 allow, ask, deny 규칙을 관리한다. | rm 명령은 늘 묻게 규칙을 걸 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음. 확장은 Customize 의 Permissions |
| `/plan` |  | `[description]` | plan 모드로 바로 들어간다. 설명을 주면 그 작업의 계획부터 세운다. | 보고서 장 구성을 바꾸기 전에 계획부터 볼 때 | 됨 | vs-code 문서 'Use the prompt box' 절에 명시 (v2.1.280 이상, /plan open 도 있음) |
| `/sandbox` |  |  | sandbox 모드를 켜고 끈다(지원 플랫폼 한정). | 모르는 스크립트를 격리해 돌릴 때 | 됨 | vs-code 문서 'Use the prompt box' 절에 명시 (v2.1.280 이상) |
| `/security-review` |  |  | 현재 브랜치와 origin 기본 브랜치의 차이를 보안 취약점 관점에서 검토한다. | 외부에 공개할 웹 도구를 올리기 전 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |

### 도구·확장 (30)

| 명령 | 별칭 | 인자 | 하는 일 | 쓰는 때 | VS Code | 근거 |
|---|---|---|---|---|---|---|
| `/agents` |  |  | v2.1.198 부터는 서브에이전트를 만들려면 Claude 에게 요청하거나 agents 폴더를 직접 고치라는 안내만 출력한다. | 자료 조사용 서브에이전트를 새로 두고 싶을 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/artifacts` |  |  | 내가 소유하거나 공유받은 아티팩트 목록을 보고 세션에 붙이거나 브라우저로 연다. | 지난번 만든 결과 대시보드를 다시 열 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/batch` |  | `<instruction>` | [번들 스킬] 큰 변경을 5-30 개 독립 단위로 나눠 계획하고, 승인하면 단위마다 worktree 에서 병렬 서브에이전트로 처리한다. | 스크립트 수십 개의 경로 변수를 한꺼번에 바꿀 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/chrome` |  |  | Claude in Chrome 연동 설정을 연다. | 기상청 누리집 자료 내려받기를 브라우저로 맡길 때 | 됨 | vs-code 문서 'Use the prompt box' 절에 명시 (claude.ai 로그인 필요) |
| `/claude-api` |  | `[migrate\|upgrade\|managed-agents-onboard\|prompt-audit\|cost-optimize\|build-eval\|hillclimb]` | [번들 스킬] Claude API 와 Managed Agents 참고 자료를 불러오고 이전, 비용 절감, 평가 작성 같은 하위 작업을 돕는다. | 사내 문서 요약 도구를 API 로 짤 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/code-review` | /review | `[low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [pr#\|branch\|path]` | [번들 스킬] 현재 변경분이나 지정 PR 의 정확성 버그를 검토하고, --fix 로 고치거나 ultra 로 클라우드 심층 검토를 돌린다. | 집계 스크립트를 고친 뒤 버그가 없는지 볼 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/dataviz` |  | `[request]` | [번들 스킬] 차트와 대시보드 설계 지침을 불러와 형태, 색, 색각 이상 대비 검사를 적용한다. | 수위 시계열 그래프 색을 정할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/deep-research` |  | `<question>` | [번들 워크플로] 웹 검색을 여러 갈래로 펼쳐 출처를 교차 확인하고 인용 달린 보고서를 만든다. | LID 시설 해외 설계기준 동향을 조사할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/design` |  | `[brief]` | [번들 스킬] UI 시안, 화면 흐름, 포스터를 Claude Design 아티팩트 캔버스로 만든다. | 학회 포스터 배치 시안을 잡을 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/design-sync` |  | `[hint]` | [번들 스킬] 저장소의 React 디자인 시스템을 변환해 Claude Design 에 올린다. | 웹 대시보드 부품을 Claude Design 에서 쓰려 할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/diff` |  |  | 작업 트리의 변경 사항과 Claude 가 한 편집을 검토한다. | Claude 가 스크립트를 고친 내용을 확인할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음. 확장은 편집마다 diff 를 따로 보여 줌 |
| `/hooks` |  |  | 도구 이벤트에 걸린 훅 설정을 본다. | 자동 저장 훅이 걸려 있는지 볼 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음. 확장은 명령 메뉴 Customize 의 Hooks 로 보기와 편집 가능 |
| `/ide` |  |  | IDE 연동을 관리하고 상태를 본다. | 외부 터미널의 claude 를 VS Code 와 잇을 때 | 확인 못 함 | vs-code 문서: 외부 터미널에서 /ide 를 실행해 VS Code 에 연결하라고 적음(확장 패널 안에서의 동작은 언급 없음) |
| `/install-github-app` |  |  | 저장소에 Claude GitHub App 과 GitHub Actions 를 설치하도록 안내한다. | 과업 코드 저장소에 자동 리뷰를 붙일 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/install-slack-app` |  |  | Claude Slack 앱을 설치한다(브라우저 OAuth). | 팀 Slack 에 Claude 를 들일 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/mcp` |  | `[reconnect <server>\|enable\|disable [<server>\|all]]` | MCP 서버 연결과 OAuth 인증을 관리한다. | Notion 연결이 끊겼을 때 다시 잇기 | 됨 | vs-code 문서 'Use the prompt box' 절에 명시 (MCP 절: 채팅 패널에서 /mcp) |
| `/plugin` |  | `[subcommand]` | 플러그인 메뉴를 열거나 list, install, enable, disable 을 바로 실행한다. | 새 플러그인을 들일 때 | 됨 | vs-code 문서: 프롬프트 창에 /plugins 를 치면 Manage plugins 화면이 열림 |
| `/reload-plugins` |  | `[--force]` | 재시작 없이 활성 플러그인을 다시 읽는다. | 플러그인을 설치한 직후 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/reload-skills` |  |  | 스킬과 명령 폴더를 다시 훑어 세션 중 추가된 스킬을 쓸 수 있게 한다. | 새 스킬 파일을 방금 만들었을 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/review` |  | `[low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [pr#\|branch\|path]` | /code-review 의 별칭이다. | PR 번호를 주고 검토할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/run` |  |  | [번들 스킬] 프로젝트 앱을 띄우고 조작해 변경이 실제로 동작하는지 본다. | 대시보드 앱을 고친 뒤 실제로 띄워 볼 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/run-skill-generator` |  |  | [번들 스킬] /run 과 /verify 가 앱을 빌드, 실행하는 법을 프로젝트 스킬로 적는다. | 앱 실행 절차를 한 번 정리해 둘 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/simplify` |  | `[target]` | [번들 스킬] 바뀐 코드를 재사용, 단순화, 효율, 추상화 수준 관점으로 검토해 고친다(버그 탐색은 아님). | 급히 짠 집계 스크립트를 정리할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/skill-doctor` |  |  | 스킬마다 문맥 비용과 사용 빈도를 보여 줘 끌 스킬을 찾게 한다. | 스킬이 너무 많아 문맥이 무거울 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/skills` |  |  | 사용 가능한 스킬 목록을 보고 스킬마다 보이기 설정을 바꾼다. | 과업 스킬이 제대로 실렸는지 볼 때 | 됨 | vs-code 문서 'Use the prompt box' 절에 명시 (/skills 입력 시 목록 창, v2.1.280 이상) |
| `/slides` |  | `[brief]` | [번들 스킬] 요약 지시로 Claude Slides 아티팩트 발표자료를 새로 만든다. | 중간보고 초안 슬라이드를 빠르게 잡을 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/ultrareview` |  | `[PR or branch]` | 클라우드 샌드박스에서 다중 에이전트 심층 코드 검토를 돌린다. /code-review ultra 의 별칭이다. | 공개 전 중요한 코드 변경을 깊게 볼 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/verify` |  |  | [번들 스킬] 앱을 빌드, 실행, 관찰해 코드 변경이 의도대로 동작하는지 확인한다. | 고친 대시보드가 실제로 뜨는지 확인할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/workflow-authoring` |  |  | [번들 스킬] 동적 워크플로 스크립트 작성 참고 자료를 불러온다. | 저장된 워크플로 스크립트를 손으로 고치기 전 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/workflows` |  |  | 실행 중이거나 끝난 워크플로 진행 화면을 열어 보고 멈추고 저장한다. | deep-research 진행 상황을 볼 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |

### 상태·사용량 (11)

| 명령 | 별칭 | 인자 | 하는 일 | 쓰는 때 | VS Code | 근거 |
|---|---|---|---|---|---|---|
| `/context` |  | `[all]` | 현재 문맥 사용량을 색 격자로 보여 주고 줄일 곳을 제안한다. | 응답이 느려져 문맥이 얼마나 찼는지 볼 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음. 확장은 입력창에 문맥 표시기가 따로 있음 |
| `/cost` |  |  | /usage 의 별칭이다. | 이번 세션 비용을 볼 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/doctor` | /checkup | `[prompt-audit [path]]` | [번들 스킬] 설치, PATH, 설정 파일, 안 쓰는 스킬과 MCP, 느린 훅을 점검하고 확인을 받아 고친다. prompt-audit 은 지침 파일 점검이다. | 업데이트 뒤 Claude Code 가 이상할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/insights` |  |  | 이 PC 의 최근 세션을 분석한 HTML 보고서를 만든다. | 한 달간 어떻게 썼는지 돌아볼 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/rate-limit-options` |  |  | 사용 한도에 걸렸을 때 기다렸다 자동 계속, 사용 크레딧 추가, 요금제 올리기 선택지를 보인다. 메뉴에 없어 전체 이름을 쳐야 한다. | 한도에 걸려 작업이 멈췄을 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/release-notes` |  |  | 버전별 변경 기록을 본다. | 업데이트 뒤 무엇이 바뀌었는지 볼 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/stats` |  |  | /usage 의 별칭이며 Stats 탭으로 열린다. | 사용 통계를 볼 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/status` |  |  | 버전, 모델, 계정, 연결 상태를 보여 준다. | 어느 계정과 모델로 돌고 있는지 확인할 때 | 됨 | vs-code 문서 'Use the prompt box' 절에 명시 (v2.1.280 이상) |
| `/tasks` | /bashes |  | 이 세션의 백그라운드 작업(서브에이전트, 셸)을 보고 관리한다. | 돌려 둔 모의 셸이 아직 도는지 볼 때 | 됨 | vs-code 문서 'Use the prompt box' 절에 명시 (에이전트 지도가 열림, v2.1.277 이상) |
| `/usage` |  |  | 세션 비용, 요금제 사용 한도, 활동 통계를 보여 준다. | 이번 주 한도가 얼마나 남았는지 볼 때 | 됨 | vs-code 문서 'Use the prompt box' 절에 명시 (Account & usage 창이 열림) |
| `/usage-credits` |  |  | 한도에 걸렸을 때 사용 크레딧을 설정하거나 관리자에게 요청한다. 예전 이름은 /extra-usage. | 마감 직전 한도에 걸렸을 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |

### 원격·예약 (8)

| 명령 | 별칭 | 인자 | 하는 일 | 쓰는 때 | VS Code | 근거 |
|---|---|---|---|---|---|---|
| `/autofix-pr` |  | `[prompt]` | 현재 브랜치의 PR 을 지켜보다가 CI 실패나 리뷰 의견이 오면 고쳐 올리는 클라우드 세션을 띄운다. | GitHub 에 올린 분석 코드 PR 의 검사 실패를 맡길 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/loop` | /proactive | `[interval] [prompt]` | [번들 스킬] 세션이 열려 있는 동안 프롬프트를 주기적으로 되풀이한다. 간격을 빼면 Claude 가 스스로 정한다. | 10 분마다 모의 로그 진행률을 확인할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/mobile` | /ios, /android |  | Claude 모바일 앱 내려받기 QR 코드를 보여 준다. | 현장에서 폰으로 이어 보려 할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/remote-control` | /rc |  | 이 세션을 claude.ai 나 모바일 앱에서 원격 조작할 수 있게 한다. | 사무실 PC 의 모의를 출장지 폰으로 살필 때 | 됨 | vs-code 문서: Customize 의 Slash commands 목록에서 /usage, /remote-control 같은 명령을 골라 실행 |
| `/remote-env` |  |  | CLI 에서 여는 클라우드 세션의 기본 클라우드 환경을 고른다. | 클라우드 세션을 자주 쓸 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/schedule` | /routines | `[description]` | 클라우드에서 도는 루틴(예약 작업)을 만들고 고치고 나열하고 실행한다. | 매일 아침 관측 자료 수집을 예약할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/teleport` | /tp |  | 클라우드 세션을 이 터미널로 끌어온다. | 웹에서 시작한 작업을 PC 에서 이어 갈 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/web-setup` |  |  | 로컬 gh 자격으로 클라우드 세션용 GitHub 계정을 연결한다. | 클라우드 세션에서 저장소를 쓸 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |

### 계정·설정 (18)

| 명령 | 별칭 | 인자 | 하는 일 | 쓰는 때 | VS Code | 근거 |
|---|---|---|---|---|---|---|
| `/config` | /settings | `[key=value ...]` | 설정 화면을 열거나 key=value 로 설정을 바로 바꾼다. | 테마나 기본 모델을 바꿀 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/design-login` |  |  | /design-sync 용 디자인 시스템 접근을 claude.ai 계정으로 승인한다. | 사내 디자인 시스템을 올리기 전 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/import` |  | `[codex\|gemini\|cursor] [--dry-run] [--yes]` | Codex, Gemini CLI, Cursor 설정(지침, MCP, 명령, 스킬)을 Claude Code 로 가져온다. | 다른 AI 도구에서 쓰던 지침을 옮길 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/keybindings` |  |  | 단축키 설정 파일을 연다. | Ctrl+S 같은 키를 바꾸고 싶을 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/login` |  |  | Anthropic 계정으로 로그인한다. | 구독 계정을 바꿀 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/logout` |  |  | Anthropic 계정에서 로그아웃한다. | 공용 PC 에서 작업을 마칠 때 | 됨 | vs-code 문서 'Use the prompt box' 절에 명시 (v2.1.277 이상) |
| `/output-style` |  | `[style]` | 출력 스타일 목록을 보거나 바꾼다. | 설명형 답이 필요할 때 스타일을 바꿈 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음. 확장은 Customize 의 Output styles |
| `/passes` |  |  | 친구에게 Claude Code 무료 1 주를 공유한다. 자격 계정에만 보인다. | 동료에게 체험을 권할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/privacy-settings` |  |  | 개인정보 설정을 보고 바꾼다. Pro, Max 전용이다. | 대화가 학습에 쓰이는지 확인할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/scroll-speed` |  |  | 마우스 휠 스크롤 속도를 조정한다. fullscreen 렌더링 전용이다. | 터미널 스크롤이 너무 빠를 때 | 확인 못 함 | commands 문서: fullscreen 렌더링 전용(터미널). 확장에서의 동작은 언급 없음 |
| `/setup-bedrock` |  |  | Amazon Bedrock 인증, 리전, 모델을 설정하는 마법사다. 환경변수 설정 전에는 숨겨져 있다. | 사내 AWS 로 Claude 를 쓸 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/setup-vertex` |  |  | Google Cloud Agent Platform 인증과 리전을 설정하는 마법사다. 환경변수 설정 전에는 숨겨져 있다. | 사내 GCP 로 Claude 를 쓸 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/statusline` |  |  | Claude Code 상태 줄을 설정한다. | 터미널 하단에 과업명과 모델을 띄울 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/terminal-setup` |  |  | VS Code 등 터미널에 줄바꿈용 Shift+Enter 단축키를 설치한다. | 통합 터미널에서 claude 를 쓰며 여러 줄을 입력할 때 | 확인 못 함 | commands 문서: VS Code 를 포함한 터미널용 설정. 확장 패널 안의 동작은 언급 없음 |
| `/theme` |  |  | 색 테마를 바꾼다(자동, 밝게, 어둡게, 색각 보정 등). | 밝은 사무실에서 화면이 안 보일 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/tui` |  | `[default\|fullscreen]` | 터미널 UI 렌더러를 바꾸고 대화를 유지한 채 다시 띄운다. | 터미널 화면이 깜빡일 때 fullscreen 으로 | 확인 못 함 | commands 문서: 터미널 렌더러 설정. 확장에서의 동작은 언급 없음 |
| `/update-config` |  | `[request]` | [번들 스킬] 말로 설명한 설정 변경(허용 명령, 환경변수, 훅)을 settings.json 에 반영한다. | python 실행 경로를 늘 허용하게 할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/upgrade` |  |  | 상위 요금제로 바꾸는 페이지를 브라우저로 연다. | 한도가 자주 찰 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |

### 기타 (15)

| 명령 | 별칭 | 인자 | 하는 일 | 쓰는 때 | VS Code | 근거 |
|---|---|---|---|---|---|---|
| `/bug` | /share | `[report]` | 버그를 신고하거나 대화를 공유한다. 보낼 기록 범위를 고르고 동의 화면을 거친다. | 도구가 이상하게 멈춘 상황을 신고할 때 | 됨 | vs-code 문서 'Use the prompt box' 절에 명시, commands 문서도 확장에서는 자체 신고 창이 열린다고 적음 |
| `/color` |  | `[color\|default]` | 이 세션의 입력창 색을 바꾼다. | 여러 창을 띄워 두고 과업별로 색을 구분할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/debug` |  | `[description]` | [번들 스킬] 이 세션의 디버그 로그를 켜고 로그를 읽어 문제를 진단한다. | MCP 서버가 계속 연결 실패할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/feedback` |  | `[report]` | 제품 의견을 보낸다. /bug 와 같은 창과 동의 절차를 쓴다. | 기능 개선 의견을 보낼 때 | 됨 | vs-code 문서 'Use the prompt box' 절에 명시 |
| `/focus` |  |  | 마지막 입력, 도구 호출 한 줄 요약, 최종 답만 보이는 focus 보기를 켜고 끈다. fullscreen 렌더링 전용이다. | 긴 도구 출력 없이 결론만 볼 때 | 안 됨 | commands 문서: fullscreen 렌더링 전용이고 VS Code 확장은 명령 메뉴의 자체 Focus view 토글(Ctrl+Alt+F)을 쓴다고 적음 |
| `/heapdump` |  |  | 메모리 진단용 힙 스냅숏과 메모리 분석을 바탕화면에 쓴다. 메뉴에 숨겨져 있어 전체 이름을 쳐야 한다. | Claude Code 메모리 사용이 비정상적으로 클 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/help` |  |  | 도움말과 사용 가능한 명령을 보여 준다. | 명령 이름이 기억나지 않을 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/powerup` |  |  | 짧은 대화형 강습으로 Claude Code 기능을 익힌다. | 처음 쓰는 동료에게 기능을 보여 줄 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/pr-comments` |  | `[PR]` | v2.1.91 에서 삭제됐다. 예전에는 PR 댓글을 가져와 보였다. | 해당 없음(삭제됨) | 안 됨 | commands 문서: Removed in v2.1.91 |
| `/radio` |  |  | Claude FM lo-fi 라디오를 브라우저로 연다. | 긴 모의를 기다릴 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/stickers` |  |  | Claude Code 스티커를 주문한다. | 해당 업무 없음 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/team-onboarding` |  |  | 최근 30 일 사용 기록으로 팀원용 온보딩 안내서를 만든다. | 신입에게 Claude Code 사용법을 넘길 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음 |
| `/ultraplan` |  | `<prompt>` | 삭제됐다. plan 모드를 쓰라고 안내한다. | 해당 없음(삭제됨) | 안 됨 | commands 문서: Removed |
| `/vim` |  |  | v2.1.92 에서 삭제됐다. /config 의 Editor mode 를 쓴다. | 해당 없음(삭제됨) | 안 됨 | commands 문서: Removed in v2.1.92 |
| `/voice` |  | `[hold\|tap\|off]` | 음성 받아쓰기를 켜거나 모드를 정한다. Claude.ai 계정이 필요하다. | 긴 지시를 말로 입력할 때 | 확인 못 함 | vs-code 문서: 확장은 명령의 일부만 지원, / 입력으로 확인하라고만 적음. [추정] 확장 번들(2.1.284)에 'Speech-to-text is not supported in this environment' 문구가 있음 |

## 2. 명령줄(CLI)

| 문법 | 하는 일 | 예 | 출처 |
|---|---|---|---|
| `claude` | 대화형 세션을 시작한다. | `claude` | https://code.claude.com/docs/en/cli-reference |
| `claude "query"` | 첫 질문을 넣고 대화형 세션을 시작한다. | `claude "이 폴더 구조를 설명해 줘"` | https://code.claude.com/docs/en/cli-reference |
| `claude -p "query"` | 질문 하나에 답하고 끝낸다(비대화형). | `claude -p "이 함수 설명"` | https://code.claude.com/docs/en/cli-reference |
| `cat file \| claude -p "query"` | 파이프로 넘긴 내용을 처리한다. | `cat logs.txt \| claude -p "오류 설명"` | https://code.claude.com/docs/en/cli-reference |
| `claude -c` | 현재 폴더의 가장 최근 대화를 이어 간다. | `claude -c` | https://code.claude.com/docs/en/cli-reference |
| `claude -c -p "query"` | 최근 대화를 이어 비대화형으로 답만 받는다. | `claude -c -p "형식 오류 점검"` | https://code.claude.com/docs/en/cli-reference |
| `claude -r "<session>" "query"` | ID 나 이름으로 세션을 이어 간다. | `claude -r "보고서작업" "3 장 마무리"` | https://code.claude.com/docs/en/cli-reference |
| `claude agents [options]` | 백그라운드 세션을 보고 보내는 agent view 를 연다. --json 은 목록만 출력. | `claude agents --json` | claude --help (2.1.283, 이 PC) |
| `claude attach <id>` | 백그라운드 세션을 이 터미널에 붙인다. | `claude attach 7c5dcf5d` | claude --help (2.1.283, 이 PC) |
| `claude auth login [--claudeai\|--console\|--email <email>\|--sso]` | Anthropic 계정에 로그인한다. | `claude auth login --console` | claude --help (2.1.283, 이 PC) |
| `claude auth logout` | Anthropic 계정에서 로그아웃한다. | `claude auth logout` | claude --help (2.1.283, 이 PC) |
| `claude auth status [--json\|--text]` | 인증 상태를 보여 준다(기본 JSON). | `claude auth status --text` | claude --help (2.1.283, 이 PC) |
| `claude auto-mode config` | 현재 적용 중인 auto 모드 설정을 JSON 으로 출력한다. | `claude auto-mode config` | claude --help (2.1.283, 이 PC) |
| `claude auto-mode critique [--model <model>]` | 내가 쓴 auto 모드 규칙에 대해 AI 의견을 받는다. | `claude auto-mode critique` | claude --help (2.1.283, 이 PC) |
| `claude auto-mode defaults [--label <prefix>]` | 기본 auto 모드 규칙(environment, allow, soft_deny, hard_deny)을 JSON 으로 출력한다. | `claude auto-mode defaults` | claude --help (2.1.283, 이 PC) |
| `claude auto-mode reset [-y]` | 사용자 설정의 autoMode 절을 지워 기본값으로 되돌린다. | `claude auto-mode reset` | claude --help (2.1.283, 이 PC) |
| `claude daemon status` | 백그라운드 세션 감독 프로세스 상태를 출력한다(--help 명령 목록에는 없음). | `claude daemon status` | https://code.claude.com/docs/en/cli-reference |
| `claude daemon stop --any` | 감독 프로세스와 그 세션을 멈춘다. --keep-workers 로 세션은 남긴다. | `claude daemon stop --any` | https://code.claude.com/docs/en/cli-reference |
| `claude doctor` | 세션 없이 설치와 설정 진단을 읽기 전용으로 출력한다. | `claude doctor` | claude --help (2.1.283, 이 PC) |
| `claude gateway [--config <path>]` | 기업용 인증, 원격측정 게이트웨이를 띄운다(관리자용). | `claude gateway --config gw.yaml` | claude --help (2.1.283, 이 PC) |
| `claude import [source] [--dry-run] [--yes]` | codex, gemini, cursor 설정을 가져오는 /import 세션을 시작한다. | `claude import codex --dry-run` | claude --help (2.1.283, 이 PC) |
| `claude install [target] [--force]` | 네이티브 빌드를 설치하거나 다시 설치한다(stable, latest, 버전). | `claude install stable` | claude --help (2.1.283, 이 PC) |
| `claude logs <id>` | 백그라운드 세션의 최근 터미널 출력을 찍는다. | `claude logs 7c5dcf5d` | claude --help (2.1.283, 이 PC) |
| `claude mcp add [options] <name> <commandOrUrl> [args...]` | MCP 서버를 추가한다. -t 전송방식, -s 범위(local, user, project), -e 환경변수, -H 헤더. | `claude mcp add --transport http sentry https://mcp.sentry.dev/mcp` | claude --help (2.1.283, 이 PC) |
| `claude mcp add-json [-s scope] <name> <json>` | JSON 문자열로 MCP 서버를 추가한다. | `claude mcp add-json my '{...}'` | claude --help (2.1.283, 이 PC) |
| `claude mcp add-from-claude-desktop [-s scope]` | Claude Desktop 의 MCP 서버를 가져온다(Mac, WSL 전용). | `claude mcp add-from-claude-desktop` | claude --help (2.1.283, 이 PC) |
| `claude mcp get <name>` | MCP 서버 하나의 상세를 본다. | `claude mcp get sentry` | claude --help (2.1.283, 이 PC) |
| `claude mcp list` | 설정된 MCP 서버 목록과 상태를 본다. | `claude mcp list` | claude --help (2.1.283, 이 PC) |
| `claude mcp login [--no-browser] <name>` | MCP 서버 OAuth 인증을 한다. | `claude mcp login sentry` | claude --help (2.1.283, 이 PC) |
| `claude mcp logout <name>` | MCP 서버에 저장된 OAuth 자격을 지운다. | `claude mcp logout sentry` | claude --help (2.1.283, 이 PC) |
| `claude mcp remove [-s scope] <name>` | MCP 서버를 지운다. | `claude mcp remove sentry` | claude --help (2.1.283, 이 PC) |
| `claude mcp reset-project-choices` | 이 프로젝트 .mcp.json 서버의 승인, 거부 선택을 초기화한다. | `claude mcp reset-project-choices` | claude --help (2.1.283, 이 PC) |
| `claude mcp serve [-d] [--verbose]` | Claude Code 자신을 MCP 서버로 띄운다. | `claude mcp serve` | claude --help (2.1.283, 이 PC) |
| `claude plugin details <name>` | 플러그인 구성 요소와 예상 토큰 비용을 보여 준다. | `claude plugin details code-review` | claude --help (2.1.283, 이 PC) |
| `claude plugin disable [-a] [-s scope] [plugin]` | 켜진 플러그인을 끈다. | `claude plugin disable code-review` | claude --help (2.1.283, 이 PC) |
| `claude plugin enable [-s scope] <plugin>` | 꺼진 플러그인을 켠다. | `claude plugin enable code-review` | claude --help (2.1.283, 이 PC) |
| `claude plugin eval [options] [target]` | 플러그인 평가 사례를 돌려 점수를 낸다. | `claude plugin eval ./my-plugin` | claude --help (2.1.283, 이 PC) |
| `claude plugin init\|new <name>` | 사용자 skills 폴더에 새 플러그인 뼈대를 만든다. | `claude plugin init my-tool` | claude --help (2.1.283, 이 PC) |
| `claude plugin install\|i [-s scope] <plugin>` | 마켓플레이스에서 플러그인을 설치한다(plugin@marketplace). | `claude plugin install code-review@claude-plugins-official` | claude --help (2.1.283, 이 PC) |
| `claude plugin list [--json] [--available]` | 설치된 플러그인 목록을 본다. | `claude plugin list` | claude --help (2.1.283, 이 PC) |
| `claude plugin prune\|autoremove [--dry-run]` | 더는 필요 없는 자동 설치 의존성을 지운다. | `claude plugin prune --dry-run` | claude --help (2.1.283, 이 PC) |
| `claude plugin tag [path]` | 플러그인 배포용 git 태그를 검증 후 만든다. | `claude plugin tag --dry-run` | claude --help (2.1.283, 이 PC) |
| `claude plugin uninstall\|remove [-s scope] <plugin>` | 플러그인을 제거한다. | `claude plugin uninstall code-review` | claude --help (2.1.283, 이 PC) |
| `claude plugin update [-s scope] <plugin>` | 플러그인을 최신으로 갱신한다(재시작 필요). | `claude plugin update code-review` | claude --help (2.1.283, 이 PC) |
| `claude plugin validate [--strict] <path>` | 플러그인이나 마켓플레이스 매니페스트를 검증한다. | `claude plugin validate .` | claude --help (2.1.283, 이 PC) |
| `claude plugin marketplace add <source>` | URL, 경로, GitHub 저장소로 마켓플레이스를 추가한다. | `claude plugin marketplace add owner/repo` | claude --help (2.1.283, 이 PC) |
| `claude plugin marketplace list [--json]` | 설정된 마켓플레이스 목록을 본다. | `claude plugin marketplace list` | claude --help (2.1.283, 이 PC) |
| `claude plugin marketplace remove\|rm <name>` | 마켓플레이스를 지운다. | `claude plugin marketplace rm my-market` | claude --help (2.1.283, 이 PC) |
| `claude plugin marketplace update [name]` | 마켓플레이스를 원본에서 갱신한다(이름 없으면 전부). | `claude plugin marketplace update` | claude --help (2.1.283, 이 PC) |
| `claude project purge [path] [--all] [--dry-run] [-i] [-y]` | 한 프로젝트의 Claude Code 상태(기록, 작업, 편집 이력)를 모두 지운다. | `claude project purge --dry-run` | claude --help (2.1.283, 이 PC) |
| `claude remote-control [options]` | claude.ai 나 모바일 앱에서 조작할 수 있는 Remote Control 서버를 띄운다. | `claude remote-control --name 사무실PC` | claude remote-control --help |
| `claude remote-control --spawn <same-dir\|worktree\|session>` | 원격 세션을 같은 폴더, worktree, 단일 세션 중 어떻게 띄울지 정한다. | `claude remote-control --spawn worktree` | claude remote-control --help |
| `claude remote-control --capacity <N>` | 동시 세션 최대 수(기본 32). | `claude remote-control --capacity 4` | claude remote-control --help |
| `claude remote-control -c \| --session-id <id>` | 이 폴더에서 마지막으로 쓴 원격 세션이나 지정 세션에 다시 붙는다. | `claude remote-control -c` | claude remote-control --help |
| `claude respawn <id>\|--all` | 백그라운드 세션을 현재 버전으로 다시 띄운다. | `claude respawn --all` | claude --help (2.1.283, 이 PC) |
| `claude rm <id>` | 백그라운드 세션과 (안전하면) 그 worktree 를 지운다. | `claude rm 7c5dcf5d` | claude --help (2.1.283, 이 PC) |
| `claude self-hosted-runner` | 이 PC 를 자체 호스팅 환경에 등록해 클라우드 세션을 받게 한다(--help 명령 목록에는 없음). | `claude self-hosted-runner` | https://code.claude.com/docs/en/cli-reference |
| `claude setup-token` | CI, 스크립트용 장기 인증 토큰을 만든다(구독 필요). | `claude setup-token` | claude --help (2.1.283, 이 PC) |
| `claude stop\|kill <id>` | 백그라운드 세션을 멈춘다(대화는 남음). | `claude stop 7c5dcf5d` | claude --help (2.1.283, 이 PC) |
| `claude ultrareview [target] [--json] [--post] [--timeout <min>]` | 클라우드 다중 에이전트 코드 검토를 돌려 결과를 출력한다. | `claude ultrareview 123` | claude --help (2.1.283, 이 PC) |
| `claude update\|upgrade` | 업데이트를 확인하고 설치한다. | `claude update` | claude --help (2.1.283, 이 PC) |
| `--add-dir <directories...>` | 추가 작업 폴더에 파일 접근을 허용한다. | `claude --add-dir D:\원자료` | claude --help (2.1.283, 이 PC) |
| `--advisor <model>` | 이 세션에 advisor 도구를 켠다(--help 에는 없음). | `claude --advisor opus` | https://code.claude.com/docs/en/cli-reference |
| `--agent <agent>` | 이 세션에 쓸 에이전트를 정한다. | `claude --agent my-reviewer` | claude --help (2.1.283, 이 PC) |
| `--agents <json-or-file>` | 사용자 서브에이전트를 JSON 으로 정의한다. | `claude --agents '{"reviewer":{...}}'` | claude --help (2.1.283, 이 PC) |
| `--allow-dangerously-skip-permissions` | 권한 무시 모드를 Shift+Tab 순환에 넣되 처음부터 켜지는 않는다. | `claude --permission-mode plan --allow-dangerously-skip-permissions` | claude --help (2.1.283, 이 PC) |
| `--allowedTools, --allowed-tools <tools...>` | 묻지 않고 실행할 도구 규칙. | `claude --allowedTools "Bash(git *)" Edit` | claude --help (2.1.283, 이 PC) |
| `--append-subagent-system-prompt[-file]` | 모든 서브에이전트 시스템 프롬프트 끝에 글이나 파일 내용을 덧붙인다(--help 에는 없음). | `claude --append-subagent-system-prompt "한국어로 답"` | https://code.claude.com/docs/en/cli-reference |
| `--append-system-prompt <prompt>` | 기본 시스템 프롬프트 끝에 글을 덧붙인다. | `claude --append-system-prompt "표는 대조에만"` | claude --help (2.1.283, 이 PC) |
| `--append-system-prompt-file <file>` | 파일 내용을 기본 시스템 프롬프트 끝에 덧붙인다(--help 에는 없음). | `claude --append-system-prompt-file ./규칙.txt` | https://code.claude.com/docs/en/cli-reference |
| `--autocompact <auto\|tokens>` | 이 세션의 자동 압축 창 크기를 정한다. | `claude --autocompact 500k` | claude --help (2.1.283, 이 PC) |
| `--ax-screen-reader` | 화면낭독기용 평문 출력. | `claude --ax-screen-reader` | claude --help (2.1.283, 이 PC) |
| `--bare` | 훅, LSP, 플러그인 동기화, auto memory, CLAUDE.md 자동 탐색을 건너뛰는 최소 모드. | `claude --bare -p "query"` | claude --help (2.1.283, 이 PC) |
| `--betas <betas...>` | API 요청에 베타 헤더를 넣는다(API 키 사용자). | `claude --betas interleaved-thinking` | claude --help (2.1.283, 이 PC) |
| `--bg, --background` | 세션을 백그라운드로 띄우고 바로 돌아온다. | `claude --bg "모의 결과 집계"` | claude --help (2.1.283, 이 PC) |
| `--brief` | 에이전트가 사용자에게 보내는 SendUserMessage 도구를 켠다(CLI reference 표에는 없음). | `claude --brief` | claude --help (2.1.283, 이 PC) |
| `--channels` | (연구 미리보기) 채널 알림을 들을 MCP 서버를 지정한다(--help 에는 없음). | `claude --channels plugin:x@y` | https://code.claude.com/docs/en/cli-reference |
| `--chrome / --no-chrome` | Claude in Chrome 연동을 켜거나 끈다. | `claude --chrome` | claude --help (2.1.283, 이 PC) |
| `--client-data-url <url>` | 서명된 설정 문서 URL 을 읽는다(CLI reference 표에는 없음). | `claude --client-data-url https://...` | claude --help (2.1.283, 이 PC) |
| `--cloud [description\|session_id\|url]` | 클라우드 세션을 만들거나 기존 세션에 붙는다. --remote 는 옛 별칭. | `claude --cloud "로그인 버그 수정"` | claude --help (2.1.283, 이 PC) |
| `-c, --continue` | 현재 폴더의 최근 대화를 이어 간다. | `claude -c` | claude --help (2.1.283, 이 PC) |
| `--dangerously-load-development-channels` | 허용 목록 밖 채널을 개발용으로 켠다(--help 에는 없음). | `claude --dangerously-load-development-channels server:x` | https://code.claude.com/docs/en/cli-reference |
| `--dangerously-skip-permissions` | 모든 권한 확인을 건너뛴다(bypassPermissions). 격리 환경 전용 권고. | `claude --dangerously-skip-permissions` | claude --help (2.1.283, 이 PC) |
| `-d, --debug [filter]` | 디버그 모드(범주 거르기 가능). | `claude --debug="mcp,startup"` | claude --help (2.1.283, 이 PC) |
| `--debug-file <path>` | 디버그 로그를 지정 파일에 쓴다. | `claude --debug-file C:\swmm_work\debug.log` | claude --help (2.1.283, 이 PC) |
| `--disable-slash-commands` | 모든 스킬과 명령을 끈다. | `claude --disable-slash-commands` | claude --help (2.1.283, 이 PC) |
| `--disallowedTools, --disallowed-tools <tools...>` | 거부할 도구 규칙. | `claude --disallowedTools "Bash(rm *)"` | claude --help (2.1.283, 이 PC) |
| `--effort <level>` | 이 세션의 노력 수준(low, medium, high, xhigh, max; 문서는 ultracode 도 적음). | `claude --effort high` | claude --help (2.1.283, 이 PC) |
| `--enable-auto-mode` | v2.1.111 에서 삭제됨. --permission-mode auto 를 쓴다. | `claude --permission-mode auto` | https://code.claude.com/docs/en/cli-reference |
| `--environment <environment_id>` | 자체 호스팅 환경에서 새 클라우드 세션을 만든다. | `claude --environment ccpool_abc` | claude --help (2.1.283, 이 PC) |
| `--exclude-dynamic-system-prompt-sections` | PC 별 정보를 시스템 프롬프트에서 첫 사용자 메시지로 옮겨 캐시 재사용을 높인다. | `claude -p --exclude-dynamic-system-prompt-sections "q"` | claude --help (2.1.283, 이 PC) |
| `--exec` | Claude 세션 대신 셸 명령을 PTY 백그라운드 작업으로 돌린다(--bg 와 함께, --help 에는 없음). | `claude --bg --exec "python run.py"` | https://code.claude.com/docs/en/cli-reference |
| `--fallback-model <model>` | 주 모델이 과부하일 때 대신 쓸 모델(쉼표 목록). | `claude --fallback-model sonnet` | claude --help (2.1.283, 이 PC) |
| `--file <specs...>` | 시작할 때 file_id:상대경로 로 파일을 내려받는다(CLI reference 표에는 없음). | `claude --file file_abc:doc.txt` | claude --help (2.1.283, 이 PC) |
| `--fork-session` | 이어 갈 때 새 세션 ID 로 갈라낸다(--resume, --continue 와 함께). | `claude --resume abc123 --fork-session` | claude --help (2.1.283, 이 PC) |
| `--forward-subagent-text` | 서브에이전트 글과 생각 블록을 출력 스트림에 넘긴다(-p, stream-json). | `claude -p --output-format stream-json --forward-subagent-text "q"` | claude --help (2.1.283, 이 PC) |
| `--from-pr [value]` | PR 에 연결된 세션을 이어 가거나 선택기를 연다. | `claude --from-pr 123` | claude --help (2.1.283, 이 PC) |
| `--ide` | 시작할 때 IDE 가 하나면 자동 연결한다. | `claude --ide` | claude --help (2.1.283, 이 PC) |
| `--include-hook-events` | 훅 이벤트를 출력 스트림에 넣는다(stream-json). | `claude -p --output-format stream-json --include-hook-events "q"` | claude --help (2.1.283, 이 PC) |
| `--include-partial-messages` | 부분 메시지 조각을 도착하는 대로 넣는다(-p, stream-json). | `claude -p --output-format stream-json --verbose --include-partial-messages "q"` | claude --help (2.1.283, 이 PC) |
| `--init / --init-only / --maintenance` | Setup 훅을 init 또는 maintenance 로 먼저 돌린다. --init-only 는 훅만 돌리고 끝낸다(--help 에는 없음). | `claude --init-only` | https://code.claude.com/docs/en/cli-reference |
| `--input-format <text\|stream-json>` | -p 입력 형식. | `claude -p --input-format stream-json --output-format stream-json` | claude --help (2.1.283, 이 PC) |
| `--json-schema <schema>` | 결과를 JSON Schema 로 검증한 구조화 출력으로 받는다. | `claude -p --json-schema '{...}' "q"` | claude --help (2.1.283, 이 PC) |
| `--max-budget-usd <amount>` | API 지출 상한(-p 전용). | `claude -p --max-budget-usd 2 "q"` | claude --help (2.1.283, 이 PC) |
| `--max-turns` | 에이전트 턴 수 상한(-p 전용, --help 에는 없음). | `claude -p --max-turns 3 "q"` | https://code.claude.com/docs/en/cli-reference |
| `--mcp-config <configs...>` | JSON 파일이나 문자열에서 MCP 서버를 읽는다. | `claude --mcp-config ./mcp.json` | claude --help (2.1.283, 이 PC) |
| `--model <model>` | 이 세션의 모델(별칭 fable, opus, sonnet 이나 전체 이름). | `claude --model sonnet` | claude --help (2.1.283, 이 PC) |
| `-n, --name <name>` | 세션 표시 이름을 정한다. | `claude -n 보고서3장` | claude --help (2.1.283, 이 PC) |
| `--no-session-persistence` | 세션을 디스크에 저장하지 않는다(-p 전용). | `claude -p --no-session-persistence "q"` | claude --help (2.1.283, 이 PC) |
| `--output-format <text\|json\|stream-json>` | -p 출력 형식. | `claude -p "q" --output-format json` | claude --help (2.1.283, 이 PC) |
| `--permission-mode <mode>` | 시작 권한 모드(acceptEdits, auto, bypassPermissions, manual, dontAsk, plan; 문서는 default 도 적음). | `claude --permission-mode plan` | claude --help (2.1.283, 이 PC) |
| `--permission-prompt-tool` | 비대화형에서 권한 질문을 받을 MCP 도구를 지정한다(--help 에는 없음). | `claude -p --permission-prompt-tool mcp__auth__prompt "q"` | https://code.claude.com/docs/en/cli-reference |
| `--permission-prompts <host\|none>` | -p 에서 권한 질문을 누가 답할지. none 이면 자동 거부. | `claude -p --permission-prompts none "q"` | claude --help (2.1.283, 이 PC) |
| `--plugin-dir <path>` | 폴더나 .zip 플러그인을 이 세션에만 싣는다. | `claude --plugin-dir ./my-plugin` | claude --help (2.1.283, 이 PC) |
| `--plugin-url <url>` | URL 의 플러그인 .zip 을 이 세션에만 싣는다. | `claude --plugin-url https://example.com/p.zip` | claude --help (2.1.283, 이 PC) |
| `-p, --print` | 응답을 출력하고 끝낸다(파이프용). 작업공간 신뢰 확인을 건너뛰므로 믿는 폴더에서만. | `claude -p "q"` | claude --help (2.1.283, 이 PC) |
| `--prompt-suggestions [value]` | 턴마다 다음 입력 예측을 낸다. | `claude -p --output-format stream-json --verbose --prompt-suggestions "q"` | claude --help (2.1.283, 이 PC) |
| `--ref <branch>` | --environment 와 함께 새 세션의 기준 브랜치를 정한다(--help 에는 없음). | `claude -p "q" --environment ccpool_abc --ref main` | https://code.claude.com/docs/en/cli-reference |
| `--remote-control [name], --rc` | Remote Control 을 켠 대화형 세션을 시작한다. | `claude --remote-control 사무실` | claude --help (2.1.283, 이 PC) |
| `--remote-control-session-name-prefix <prefix>` | 자동 생성 원격 세션 이름 앞말(기본 호스트 이름). | `claude --remote-control --remote-control-session-name-prefix swmm` | claude --help (2.1.283, 이 PC) |
| `--replay-user-messages` | stdin 사용자 메시지를 stdout 으로 되돌려 확인한다(stream-json 입출력). | `claude -p --input-format stream-json --output-format stream-json --replay-user-messages` | claude --help (2.1.283, 이 PC) |
| `--restricted` | 명령 실행 도구와 WebFetch 를 빼고 사용자, 프로젝트 설정을 무시하는 제한 모드. | `claude --restricted` | claude --help (2.1.283, 이 PC) |
| `-r, --resume [value]` | 세션 ID 로 잇거나 선택기를 연다. | `claude -r` | claude --help (2.1.283, 이 PC) |
| `--safe-mode` | CLAUDE.md, 스킬, 플러그인, 훅, MCP 같은 사용자 설정을 모두 끄고 시작한다(고장 진단용). | `claude --safe-mode` | claude --help (2.1.283, 이 PC) |
| `--session-id <uuid>` | 지정 UUID 로 세션을 만든다. | `claude --session-id 550e8400-e29b-41d4-a716-446655440000` | claude --help (2.1.283, 이 PC) |
| `--setting-sources <sources>` | 읽을 설정 원천(user, project, local). | `claude --setting-sources user` | claude --help (2.1.283, 이 PC) |
| `--settings <file-or-json>` | 추가 설정 파일이나 JSON 을 이 세션에 덮어 쓴다. | `claude --settings ./test-settings.json` | claude --help (2.1.283, 이 PC) |
| `--strict-mcp-config` | --mcp-config 의 MCP 서버만 쓴다. | `claude --mcp-config a.json --strict-mcp-config` | claude --help (2.1.283, 이 PC) |
| `--system-prompt <prompt>` | 시스템 프롬프트 전체를 바꾼다. | `claude --system-prompt "You are a Python expert"` | claude --help (2.1.283, 이 PC) |
| `--system-prompt-file <file>` | 파일 내용으로 시스템 프롬프트를 바꾼다(--help 에는 없음). | `claude --system-prompt-file ./prompt.txt` | https://code.claude.com/docs/en/cli-reference |
| `--system-prompt-snapshot <on\|off>` | 시스템 프롬프트를 첫 요청에 기록해 재사용할지(on 기본) 매번 새로 만들지. | `claude --system-prompt-snapshot off` | claude --help (2.1.283, 이 PC) |
| `--teammate-mode` | 에이전트 팀 팀원 표시 방식(in-process, auto, tmux, iterm2, --help 에는 없음). | `claude --teammate-mode in-process` | https://code.claude.com/docs/en/cli-reference |
| `--teleport [session]` | 클라우드 세션을 로컬 터미널에서 잇는다. | `claude --teleport` | claude --help (2.1.283, 이 PC) |
| `--tmux` | worktree 용 tmux 세션을 만든다(--worktree 필요). | `claude -w feature --tmux` | claude --help (2.1.283, 이 PC) |
| `--tools <tools...>` | 쓸 수 있는 기본 도구를 제한한다("" 전부 끔, default). | `claude --tools "Read,Edit"` | claude --help (2.1.283, 이 PC) |
| `--verbose` | 자세한 출력(설정의 viewMode 를 덮음). | `claude --verbose` | claude --help (2.1.283, 이 PC) |
| `-v, --version` | 버전을 출력한다. 이 PC 는 2.1.283. | `claude -v` | claude --help (2.1.283, 이 PC) |
| `-w, --worktree [name]` | 새 git worktree 에서 세션을 시작한다. | `claude -w 보정실험` | claude --help (2.1.283, 이 PC) |
| `-h, --help` | 도움말을 출력한다. 하위 명령마다 claude <sub> --help 가 된다. | `claude mcp --help` | claude --help (2.1.283, 이 PC) |

## 3. 단축키

### VS Code 확장 (11)

| 키 | 하는 일 | 출처 |
|---|---|---|
| `Ctrl+Esc` | 편집기와 Claude 입력창 사이 초점 전환 | https://code.claude.com/docs/en/vs-code |
| `Ctrl+Shift+Esc` | 새 대화를 편집기 탭으로 연다 | https://code.claude.com/docs/en/vs-code |
| `Ctrl+N` | 새 대화 시작(Claude 에 초점, enableNewConversationShortcut 이 true 일 때) | https://code.claude.com/docs/en/vs-code |
| `Ctrl+Shift+T` | 마지막으로 닫은 Claude 세션 탭 다시 열기 | https://code.claude.com/docs/en/vs-code |
| `Alt+K` | 현재 파일과 선택 줄을 @ 참조로 넣기(편집기에 초점) | https://code.claude.com/docs/en/vs-code |
| `Ctrl+Alt+F` | Focus view 켜고 끄기(도구 활동 숨김) | https://code.claude.com/docs/en/vs-code |
| `Ctrl+Shift+P 후 'Claude Code'` | 명령 팔레트에서 확장 명령 전체 보기 | https://code.claude.com/docs/en/vs-code |
| `Shift+Enter` | 보내지 않고 줄바꿈 | https://code.claude.com/docs/en/vs-code |
| `Ctrl+O` | 생각(thinking) 블록 전부 펼치기, 접기 | https://code.claude.com/docs/en/vs-code |
| `Ctrl+`` | 통합 터미널 열기(여기서 claude CLI 실행) | https://code.claude.com/docs/en/vs-code |
| `좌우 화살표(권한 질문 선택지에서)` | 승인 저장 위치(모든 프로젝트, 이 세션 등) 바꾸기 | https://code.claude.com/docs/en/vs-code |

### 터미널 CLI (37)

| 키 | 하는 일 | 출처 |
|---|---|---|
| `Ctrl+C` | 실행 중 작업 중단. 비어 있으면 첫 번째는 입력 지움, 두 번째는 종료 | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+D` | 세션 종료(두 번 눌러 확인) | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+X Ctrl+K` | 이 세션의 백그라운드 서브에이전트 모두 정지(3 초 안에 두 번) | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+G 또는 Ctrl+X Ctrl+E` | 입력을 기본 텍스트 편집기에서 쓰기 | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+L` | 화면 다시 그리기(입력과 대화 유지) | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+O` | 자세한 기록(transcript) 보기 켜고 끄기 | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+R` | 명령 기록 역검색 | https://code.claude.com/docs/en/interactive-mode |
| `Alt+V (Windows)` | 클립보드 이미지 붙여넣기(다른 OS 는 Ctrl+V) | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+B` | 실행 중 Bash 명령과 에이전트를 백그라운드로 | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+T` | Claude 할 일 목록 보이기, 숨기기 | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+S` | 입력 임시 보관, 빈 입력에서 다시 누르면 복원 | https://code.claude.com/docs/en/interactive-mode |
| `Tab` | 자동완성 수락, 권한 질문에 댓글 달기 | https://code.claude.com/docs/en/interactive-mode |
| `위/아래 화살표, Ctrl+P/Ctrl+N` | 커서 이동 또는 명령 기록 탐색 | https://code.claude.com/docs/en/interactive-mode |
| `Esc` | Claude 응답 중단(한 작업은 유지) 또는 창 닫기 | https://code.claude.com/docs/en/interactive-mode |
| `Esc 두 번` | 입력이 있으면 지우고 기록에 저장, 비어 있으면 되감기(rewind) 메뉴 | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+Enter 또는 Ctrl+X Ctrl+S` | 대기열 메시지를 지금 보내기 | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+X Enter` | 메시지를 대기열로 제출(작업 중 끼어들지 않음) | https://code.claude.com/docs/en/keybindings |
| `Shift+Tab (Windows 일부 환경은 Alt+M)` | 권한 모드 순환(Manual, acceptEdits, plan, 가능하면 bypass, auto) | https://code.claude.com/docs/en/interactive-mode |
| `Alt+P` | 입력을 지우지 않고 모델 바꾸기 | https://code.claude.com/docs/en/interactive-mode |
| `Alt+T` | 확장 사고 켜고 끄기(Opus 5.5, Sonnet 5.5, Fable 은 늘 켜짐이라 효과 없음) | https://code.claude.com/docs/en/interactive-mode |
| `Alt+O` | fast 모드 켜고 끄기 | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+A / Ctrl+E` | 줄 처음 / 끝으로 | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+K / Ctrl+U` | 커서부터 줄 끝까지 / 줄 처음까지 지우기 | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+W` | 앞의 공백까지 지우기(경로 한 덩어리) | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+Backspace (Windows)` | 앞 낱말 하나 지우기 | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+Y / Alt+Y` | 지운 글 붙여넣기 / 붙여넣기 기록 순환 | https://code.claude.com/docs/en/interactive-mode |
| `Alt+B / Alt+F / Alt+D` | 낱말 뒤로 / 앞으로 / 낱말 끝까지 지우기 | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+_ 또는 Ctrl+Shift+-` | 입력 편집 되돌리기 | https://code.claude.com/docs/en/interactive-mode |
| `\ 뒤 Enter` | 줄바꿈(모든 터미널) | https://code.claude.com/docs/en/interactive-mode |
| `Shift+Enter` | 줄바꿈(Windows Terminal 기본, 그 외는 /terminal-setup) | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+J` | 줄바꿈(설정 없이 모든 터미널) | https://code.claude.com/docs/en/interactive-mode |
| `? (빈 입력에서)` | 단축키 도움말 패널 | https://code.claude.com/docs/en/interactive-mode |
| `q, Ctrl+C, Esc (기록 보기 안)` | 기록 보기 닫기 | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+E (기록 보기 안, classic 렌더러)` | 모든 내용 보이기 토글 | https://code.claude.com/docs/en/interactive-mode |
| `{ / } (기록 보기 안, fullscreen)` | 이전 / 다음 사용자 입력으로 이동 | https://code.claude.com/docs/en/interactive-mode |
| `Space 길게 또는 짧게` | 음성 받아쓰기(켜 둔 경우) | https://code.claude.com/docs/en/interactive-mode |
| `Ctrl+T (/theme 선택기 안)` | 코드 구문 강조 켜고 끄기 | https://code.claude.com/docs/en/interactive-mode |

### 데스크톱 앱 (18)

| 키 | 하는 일 | 출처 |
|---|---|---|
| `Ctrl+/` | 단축키 목록 보기 | https://code.claude.com/docs/en/desktop |
| `Ctrl+N` | 새 세션 | https://code.claude.com/docs/en/desktop |
| `Ctrl+W` | 세션 닫기 | https://code.claude.com/docs/en/desktop |
| `Ctrl+Tab / Ctrl+Shift+Tab` | 다음 / 이전 세션 | https://code.claude.com/docs/en/desktop |
| `Ctrl+Shift+] / Ctrl+Shift+[` | 다음 / 이전 세션 | https://code.claude.com/docs/en/desktop |
| `Esc` | Claude 응답 멈추기 | https://code.claude.com/docs/en/desktop |
| `Ctrl+Shift+D` | diff 창 켜고 끄기 | https://code.claude.com/docs/en/desktop |
| `Ctrl+Shift+B` | 브라우저 창 켜고 끄기 | https://code.claude.com/docs/en/desktop |
| `Ctrl+Shift+S` | 브라우저에서 요소 고르기 | https://code.claude.com/docs/en/desktop |
| `Ctrl+`` | 터미널 창 켜고 끄기 | https://code.claude.com/docs/en/desktop |
| `Ctrl+\` | 초점 창 닫기 | https://code.claude.com/docs/en/desktop |
| `Ctrl+;` | 곁가지 대화(side chat) 열기 | https://code.claude.com/docs/en/desktop |
| `Ctrl+O` | 보기 모드 순환 | https://code.claude.com/docs/en/desktop |
| `Ctrl+Shift+M` | 권한 모드 메뉴 | https://code.claude.com/docs/en/desktop |
| `Ctrl+Shift+I` | 모델 메뉴 | https://code.claude.com/docs/en/desktop |
| `Ctrl+Shift+E` | 노력 수준 메뉴 | https://code.claude.com/docs/en/desktop |
| `1 에서 9` | 열린 메뉴의 항목 고르기 | https://code.claude.com/docs/en/desktop |
| `Ctrl+Enter (diff 댓글)` | diff 줄 댓글을 한꺼번에 제출 | https://code.claude.com/docs/en/desktop |

## 4. 입력 기호

| 기호 | 뜻 | 되는 곳 | 출처 |
|---|---|---|---|
| `/ (맨 앞)` | 명령이나 스킬 실행. 문장 중간에서 공백 뒤 / 는 자동완성만 되고 실행은 맨 앞일 때만. | 터미널 CLI, VS Code 확장, 데스크톱 앱 | https://code.claude.com/docs/en/interactive-mode ; https://code.claude.com/docs/en/vs-code ; https://code.claude.com/docs/en/desktop |
| `! (맨 앞)` | 셸 모드. 명령을 바로 돌리고 출력을 대화에 넣으면 Claude 가 이어서 답한다. | 터미널 CLI 됨, VS Code 확장 안 됨(비교표 '! Bash shortcut: No') | https://code.claude.com/docs/en/interactive-mode ; https://code.claude.com/docs/en/vs-code |
| `@` | 파일, 폴더 경로 언급 자동완성. 폴더는 끝에 / 를 붙인다. | 터미널 CLI, VS Code 확장 | https://code.claude.com/docs/en/interactive-mode ; https://code.claude.com/docs/en/vs-code |
| `@파일#5-10` | 파일의 특정 줄 범위 참조(Alt+K 로 자동 삽입). | VS Code 확장 | https://code.claude.com/docs/en/vs-code |
| `@terminal:이름` | VS Code 터미널 출력(제목이 이름인 터미널)을 참조. | VS Code 확장 | https://code.claude.com/docs/en/vs-code |
| `@browser` | Chrome 브라우저 작업 지시(Claude in Chrome 확장 1.0.36 이상 필요). | VS Code 확장 | https://code.claude.com/docs/en/vs-code |
| `:이름:` | 이모지 단축코드 입력(두 글자 이상이면 제안). | 터미널 CLI (v2.1.217 이상) | https://code.claude.com/docs/en/interactive-mode |
| `? (빈 입력)` | 단축키 도움말 패널 토글. | 터미널 CLI | https://code.claude.com/docs/en/interactive-mode |
| `\ 뒤 Enter` | 줄바꿈. | 터미널 CLI | https://code.claude.com/docs/en/interactive-mode |

## 5. 확인 못 한 것

1. # 로 시작하는 입력(기억 빠르게 추가)은 이번에 받은 공식 문서 16 쪽(commands, interactive-mode, memory 등)에 없음. 현재 동작 [판정보류], 확인: 터미널에서 # 입력 시험 또는 memory 문서 재확인.
2. & 로 시작하는 입력은 받은 문서 어디에도 없음(검색 0 건). [판정보류], 확인: claude-code-on-the-web 문서 열람.
3. VS Code 확장에서 슬래시 명령 대부분의 동작 여부: 공식 문서는 '일부만 지원, / 를 쳐서 확인'이라고만 적음. 확장 목록은 실행 중 CLI 가 넘기는 supportedCommands 로 정해져(확장 번들 extension.js 확인) 세션을 열지 않고는 확정 불가. 확인: VS Code 에서 / 입력 후 목록 캡처.
4. /voice 의 VS Code 확장 동작: 확장 번들 2.1.284 에 'Speech-to-text is not supported in this environment' 문구가 있어 안 될 것으로 [추정].
5. /ide, /terminal-setup, /tui, /scroll-speed, /stop 의 VS Code 확장 패널 안 동작은 문서에 언급 없음.
6. claude daemon, claude self-hosted-runner 는 CLI reference 에 있으나 이 PC 의 claude --help 명령 목록(2.1.283)에는 없음. --help 로 따로 확인하지 않음.
7. --advisor, --append-system-prompt-file, --system-prompt-file, --max-turns, --exec, --init, --init-only, --maintenance, --permission-prompt-tool, --ref, --teammate-mode, --channels, --append-subagent-system-prompt 는 CLI reference 에만 있고 claude --help 출력에는 없음.
8. --brief, --client-data-url, --file 은 claude --help 에만 있고 CLI reference 플래그 표에는 없음.
9. --effort 의 ultracode 값, --permission-mode 의 default 값은 문서에만 있고 --help 선택지에는 없음(--help 는 manual 을 적음).
10. 문서 판(2026-09-29 받음)이 v2.1.284 기능을 적고 있으나 이 PC CLI 는 2.1.283 이라, 2.1.284 이상 요구 항목(/effort ultracode on|off 등)은 이 PC 에서 아직 안 될 수 있음.
11. 데스크톱 앱 단축키는 문서가 Cmd 기준이고 'Windows 는 Cmd 대신 Ctrl' 이라 적은 것을 옮긴 것. 데스크톱 앱에서 직접 확인하지 않음.
12. claude.ai 에 동기화된 사용자 스킬, 플러그인 명령(/std-* 등)은 공식 목록 밖이라 넣지 않음.
