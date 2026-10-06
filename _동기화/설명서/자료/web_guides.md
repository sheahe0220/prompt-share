# Claude Code 가이드 · 치트시트 · 팁 웹 조사

조사일 2026-09-29. 출처 25 곳(한국어 13, 영어 12). 팁 대조 기준은 공식 문서 확인일 2026-09-29 (commands, best-practices, memory, vs-code, skills, interactive-mode, model-config, discover-plugins).

판정 표기: 일치 = 현재 공식과 맞음, 옛 정보 = 예전 동작, 공식 문서에 없음 = 확인한 공식 쪽에서 찾지 못함(반대 의견 포함).

## 1. 출처 한눈에

| ID | 제목 | 언어 | 운영 | 날짜 | 추천 |
|---|---|---|---|---|---|
| E1 | [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) | en | 공식 Anthropic | 날짜 표시 없음 (본문에 v2.1.283 언급, 확인일 2026-09-29). 옛 주소 anthropic.com/engineering/claude-code-best-practices 는 이 쪽으로 308 영구 이동 | 상 |
| E2 | [Using CLAUDE.md files: Customizing Claude Code for your codebase](https://claude.com/blog/using-claude-md-files) | en | 공식 Anthropic | 2025-11-25 | 중 |
| E3 | [How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code) | en | 공식 Anthropic | 2025-07-24 | 중 |
| E4 | [Claude Code cheatsheet](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet) | en | 공식 Anthropic | 2026-08-07 갱신 | 상 |
| E5 | [How I use Claude Code (+ my best tips)](https://www.builder.io/blog/claude-code) | en | 기업 (Builder.io, 글쓴이 Steve Sewell) | 2025-07-11 | 하 |
| E6 | [Claude Code Cheat Sheet - Commands, Shortcuts, Tips [2026]](https://computingforgeeks.com/claude-code-cheat-sheet/) | en | 개인 (Josphat Mutai, 기술 블로그) | 2026-09-26 갱신 (v2.1.282 확인) | 상 |
| E7 | [Claude Code Cheat Sheet 2026: Shortcuts, Commands & Flags](https://blakecrosley.com/guides/claude-code-cheatsheet) | en | 개인 (Blake Crosley) | 2026-09-26 갱신 (v2.1.283 기준) | 중 |
| E8 | [Claude Code in VS Code: Setup, Features, and Workflow](https://www.datacamp.com/tutorial/claude-code-in-vs-code) | en | 기업 (DataCamp, 글쓴이 Khalid Abdelaty) | 2026-04-11 게시, 2026-07-22 수정 | 상 |
| E9 | [Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md) | en | 기업 (HumanLayer, 글쓴이 Kyle) | 2025-11-25 | 상 |
| E10 | [How I Use Every Claude Code Feature](https://blog.sshh.io/p/how-i-use-every-claude-code-feature) | en | 개인 (Shrivu Shankar, Substack) | 2025-11-02 | 중 |
| E11 | [Skip the Terminal (And 8 Other Claude Code Tricks for Non-Technical Users)](https://hannahstulberg.substack.com/p/skip-the-terminal-and-8-other-claude) | en | 개인 (Hannah Stulberg, Substack 뉴스레터) | 2026-01-01 | 중 |
| E12 | [Malicious Coding Agent Skills and the Risk of Dynamic Context](https://securitylabs.datadoghq.com/articles/malicious-skills-supply-chain-risks-in-coding-agents-with-dynamic-context/) | en | 기업 (Datadog Security Labs, Nick Frichette · Ryan Simon) | 2026-05-11 | 상 |
| K1 | [Claude Code 모범 사례 (한국어 공식 문서)](https://code.claude.com/docs/ko/best-practices) | ko | 공식 Anthropic | 날짜 표시 없음 (영어판과 같은 v2.1.283 내용, 확인일 2026-09-29) | 상 |
| K2 | [Claude Code v2.1 슬래시 명령어와 키보드 단축키 총정리](https://velog.io/@scarleter99/Claude-Code-v2.1-%EC%8A%AC%EB%9E%98%EC%8B%9C-%EB%AA%85%EB%A0%B9%EC%96%B4%EC%99%80-%ED%82%A4%EB%B3%B4%EB%93%9C-%EB%8B%A8%EC%B6%95%ED%82%A4-%EC%B4%9D%EC%A0%95%EB%A6%AC) | ko | 개인 (velog scarleter99) | 2026-01-30 (v2.1.23 기준) | 중 |
| K3 | [[번역] CLAUDE.md 완벽 가이드](https://velog.io/@surim014/claude-md-guide) | ko | 개인 (velog Sonny 번역, 원문 Builder.io 'CLAUDE.md guide') | 2026-01-28 | 상 |
| K4 | [Claude Code 사용 가이드](https://tech.hyperithm.com/claude_code_guides) | ko | 기업 (하이퍼리즘 기술 블로그, 이한결) | 2025-06-04 | 하 |
| K5 | [(완결판) 따라하기만 하면 되는 클로드코드 업무 자동화](https://brunch.co.kr/@sukistory/84) | ko | 개인 (브런치 Suki) | 2026-02-06 | 중 |
| K6 | [2026 클로드 코드(Claude Code) 사용법 : 설치부터 실전 활용까지](https://blog.highoutputclub.com/2026-claude-code-for-non-developers/) | ko | 기업 (하이아웃풋클럽) | 2026-02-15 | 중 |
| K7 | [Claude Code의 모든 기능 활용법 (GeekNews 소개글)](https://news.hada.io/topic?id=24099) | ko | 커뮤니티 (GeekNews, 원문 E10 요약) | [추정] 2025-11 (페이지에 '10달전'으로만 표시) | 중 |
| K8 | [Claude Code 사용법 및 주요 명령 (GPTers 스터디 글)](https://www.gpters.org/wealth/post/claude-code-usage-key-tXdand1rtThxlWV) | ko | 커뮤니티 (GPTers, 작성자 Develiper) | 2026-05-18 | 하 |
| K9 | [Claude Code로 코드 리뷰 자동화하기, 설정부터 실패 학습 루프까지](https://www.mimul.com/blog/claude-code-review/) | ko | 개인 (Mimul Tech blog) | 2026-02-24 작성, 2026-04-16 갱신 | 중 |
| K10 | [개발자를 위한 Claude Code 토큰 사용량 최적화 전략 (요즘IT)](https://yozm.wishket.com/magazine/detail/3677/) | ko | 기업 (요즘IT, 필자 길벗) | 2026-03-26 | 중 |
| K11 | [소프트웨어 3.0 시대를 맞이하며 (토스 기술 블로그)](https://toss.tech/article/44539) | ko | 기업 (토스, 김용성) | 2026-01-26 | 중 |
| K12 | [클로드 코드(Claude Code) 기본 필수 명령어 완벽 정리](https://www.nolavoza.com/technology/claude-code-essential-commands-guide/) | ko | 개인 (노라보자 블로그) | 2026-06-17 | 중 |
| K13 | [Claude Code를 200% 활용하는 방법: spec-kit, Everything Claude Code, Oh My ClaudeCode 완벽 가이드](https://velog.io/@sammy0329/Claude-Code%EB%A5%BC-200-%ED%99%9C%EC%9A%A9%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-spec-kit-Everything-Claude-Code-Oh-My-ClaudeCode-%EC%99%84%EB%B2%BD-%EA%B0%80%EC%9D%B4%EB%93%9C) | ko | 개인 (velog sammy) | 2026-02-02 | 하 |

## 2. 출처별 상세

### E1. Best practices for Claude Code

주소: https://code.claude.com/docs/en/best-practices  
언어 en, 운영 공식 Anthropic, 날짜 날짜 표시 없음 (본문에 v2.1.283 언급, 확인일 2026-09-29). 옛 주소 anthropic.com/engineering/claude-code-best-practices 는 이 쪽으로 308 영구 이동

무엇이 들어 있나. 맥락 창이 가장 귀한 자원이라는 전제에서 검증 수단 주기, 탐색-계획-구현 순서, 구체적 프롬프트, CLAUDE.md 작성, 세션 관리, 병렬 실행을 설명한다. 흔한 실패 유형(잡다한 세션, 반복 수정, 비대한 CLAUDE.md, 검증 없는 신뢰, 무한 탐색)과 처방을 끝에 정리한다.

좋은 점. 가장 최신이고 명령 이름이 정확하다. 좋은 예와 나쁜 예를 표로 대조해 비개발자도 흉내 내기 쉽다.

한계 · 주의. 예시가 모두 코드 작업(OAuth, 테스트)이라 보고서 · 엑셀 업무로 옮겨 읽어야 한다. 병렬 세션 · worktree 절은 비개발자에게 과하다.

추천도 상. 모든 비공식 자료를 대조할 기준 문서이고 2026-09 판이다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| 일을 맡길 때 확인 방법을 같이 준다(예: '합계가 원본 시트와 같은지 비교해서 보여줘'). 성공했다고 말하지 말고 증거(출력, 비교 결과)를 보이게 한다 | 일치 |  |
| Shift+Tab 으로 계획 모드에 들어가 먼저 계획을 받고, Ctrl+G 로 계획을 편집기에서 고친 뒤 실행한다 | 일치 |  |
| 관련 없는 일로 넘어갈 때 /clear. 같은 문제를 두 번 고쳐도 안 되면 /clear 후 배운 점을 넣은 새 프롬프트로 다시 시작 | 일치 |  |
| 맥락에 남길 필요 없는 짧은 질문은 /btw 로 묻는다 | 일치 |  |
| Esc 로 멈추고, Esc 두 번 또는 /rewind 로 대화와 파일을 되돌린다. 단 Bash 명령으로 바뀐 파일은 되돌리지 못하니 git 을 대신하지 않는다 | 일치 |  |

### E2. Using CLAUDE.md files: Customizing Claude Code for your codebase

주소: https://claude.com/blog/using-claude-md-files  
언어 en, 운영 공식 Anthropic, 날짜 2025-11-25

무엇이 들어 있나. CLAUDE.md 에 넣을 것(프로젝트 요약, 표준, 자주 쓰는 명령, 작업 흐름)과 /init 사용법, 파일 위치 계층을 설명한다. 키와 비밀번호를 넣지 말 것, .claude/commands 로 반복 프롬프트를 명령으로 만들 것도 권한다.

좋은 점. 공식 블로그라 방향은 믿을 만하고 짧다. 보안 주의(비밀값 금지)가 명시돼 있다.

한계 · 주의. # 키로 메모리를 추가하는 옛 기능을 현재형으로 적었다. 길이 권고가 수치 없이 '짧게' 뿐이다(공식 문서는 200 줄 미만).

추천도 중. 공식이지만 10 개월 전 글이라 일부 조작법이 바뀌었다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| /init 으로 CLAUDE.md 초안을 만든 뒤 사람이 읽고 고친다 | 일치 |  |
| 대화 중 # 로 시작하는 줄을 입력해 CLAUDE.md 에 규칙을 바로 추가한다 | 옛 정보 | 현재 입력 접두어 표에는 / ! @ : ? 만 있다. 'CLAUDE.md 에 추가해' 라고 말하거나 /memory 로 연다 |
| CLAUDE.md 에 API 키 · 비밀번호 · 접속 문자열을 넣지 않는다 | 공식 문서에 없음 | 확인한 네 쪽에는 명시 문장이 없으나 상식적 보안 권고다 |
| .claude/commands/ 폴더에 md 파일로 자주 쓰는 프롬프트를 저장해 /이름 으로 부른다 | 일치 | 공식은 이제 스킬(.claude/skills/이름/SKILL.md)로 합쳐졌고 옛 폴더도 계속 작동한다고 적는다 |
| 서로 다른 작업 사이에 /clear | 일치 |  |

### E3. How Anthropic teams use Claude Code

주소: https://claude.com/blog/how-anthropic-teams-use-claude-code  
언어 en, 운영 공식 Anthropic, 날짜 2025-07-24

무엇이 들어 있나. Anthropic 사내 부서(법무, 마케팅, 데이터, 보안 등)가 Claude Code 를 쓴 사례와 팀별 요령을 모았다. 코딩 경험이 없는 직원이 '대시보드 조회, 쿼리 실행, 엑셀 출력' 같은 단계를 말로 설명해 자동화한 예가 들어 있다.

좋은 점. 비개발 부서 사례가 많아 사무 업무에 옮기기 쉽다. 스크린샷 활용, 단계 분해 같은 요령이 구체적이다.

한계 · 주의. 사례 중심이라 명령어 정보는 적고, 2025 년 기능 기준이다. 성과 수치는 자사 홍보 성격이 있다.

추천도 중. 비개발자 활용 발상에는 좋으나 조작법 참고서는 아니다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| 상황을 말로 설명하기 어려우면 화면 캡처를 붙여 넣고 설명한다 | 일치 | Windows 에서 이미지 붙여넣기는 Alt+V |
| 큰 일을 단계로 나눠 한 단계씩 맡긴다(조회, 계산, 엑셀 출력) | 일치 |  |
| 자주 저장 지점을 만들고 결과가 틀리면 되돌린 뒤 다시 시도한다 | 일치 | /rewind 와 git 으로 되돌리기 |
| 수백 건의 반복 문안 작업은 CSV 로 입력을 주고 한꺼번에 처리시킨다 | 공식 문서에 없음 | 명령이 아닌 활용 요령 |
| 검토 역할을 따로 두는 두 에이전트 구성으로 작성과 검토를 나눈다 | 일치 | 공식은 서브에이전트 검토 단계를 권한다 |

### E4. Claude Code cheatsheet

주소: https://support.claude.com/en/articles/14553413-claude-code-cheatsheet  
언어 en, 운영 공식 Anthropic, 날짜 2026-08-07 갱신

무엇이 들어 있나. 기본 슬래시 명령과 단축키를 용도별로 모은 한 쪽짜리 요약이다. 세션, 계획 모드, 토큰 같은 용어 풀이가 있어 처음 쓰는 사람을 겨냥한다.

좋은 점. 공식이고 짧아 브라우저 탭에 띄워 두기 좋다. 비개발자 용어 풀이가 있다.

한계 · 주의. 명령 설명이 한 줄씩이라 깊이는 없다. Shift+Tab 순서 설명이 공식 interactive-mode 쪽 표기와 조금 다르다.

추천도 상. 비개발자 첫 참고서로 가장 알맞다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| / 를 치면 쓸 수 있는 명령 목록이 뜨고, 빈 입력에서 ? 를 치면 단축키 목록이 뜬다 | 일치 |  |
| @ 뒤에 파일 경로를 적어 파일을 지정한다 | 일치 |  |
| Esc 두 번으로 되감기 메뉴를 연다 | 일치 |  |
| /usage 로 사용량을 본다(/cost 는 별칭) | 일치 |  |
| Shift+Tab 으로 권한 모드를 바꾼다 | 일치 | 공식 표기는 Manual(default), acceptEdits, plan, 그리고 가능할 때 auto 순환 |

### E5. How I use Claude Code (+ my best tips)

주소: https://www.builder.io/blog/claude-code  
언어 en, 운영 기업 (Builder.io, 글쓴이 Steve Sewell), 날짜 2025-07-11

무엇이 들어 있나. 개발사 대표가 일상에서 쓰는 요령(메시지 대기열, Esc, /clear, 훅, GitHub 앱)을 소개한다. 자사 시각 편집 도구 홍보가 붙어 있다.

좋은 점. 널리 인용된 글이라 다른 글들의 원형을 알 수 있다. 메시지를 줄 세워 보내는 요령은 여전히 유효하다.

한계 · 주의. 권한 확인을 끄는 --dangerously-skip-permissions 를 상시 쓰라고 권하고, # 메모리 단축키 같은 옛 기능이 있다. Builder.io 제품 홍보가 섞였다.

추천도 하. 비개발 사무 환경에서 따라 하면 위험한 권고가 있고 1 년 넘은 정보다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| claude --dangerously-skip-permissions 로 늘 권한 확인을 끄고 쓴다 | 옛 정보 | 현재 v2.1.283 부터 분류기가 위험 동작만 막는 auto 모드가 기본이다. 권한 무시는 격리 환경에서만 |
| /terminal-setup 으로 Shift+Enter 줄바꿈을 켠다 | 일치 | Windows Terminal 은 기본 지원, 어느 터미널이든 \ + Enter 가 된다 |
| # 로 시작해 기억할 내용을 추가한다 | 옛 정보 |  |
| 멈출 때는 Ctrl+C 가 아니라 Esc | 일치 | Ctrl+C 는 두 번 누르면 종료된다 |
| Ctrl+V 로 클립보드 이미지를 붙여 넣는다 | 일치 | Windows 는 Alt+V |

### E6. Claude Code Cheat Sheet - Commands, Shortcuts, Tips [2026]

주소: https://computingforgeeks.com/claude-code-cheat-sheet/  
언어 en, 운영 개인 (Josphat Mutai, 기술 블로그), 날짜 2026-09-26 갱신 (v2.1.282 확인)

무엇이 들어 있나. 슬래시 명령, 단축키, 인쇄 모드(claude -p) 플래그를 한 쪽에 모으고 최근 추가 · 폐지된 기능을 따로 적었다. 모델 전환, 노력 수준(/effort), 배경 실행 같은 최근 기능을 다룬다.

좋은 점. 매우 최근 판이고 변경 이력 절이 있어 옛 글을 걸러 낼 때 쓸모 있다.

한계 · 주의. /ultraplan 폐지 이유를 '노력 수준으로 통합'이라 적었는데 공식은 '계획 모드를 쓰라'고 한다. 개발자 대상이라 플래그가 많다.

추천도 상. 최신성과 정확도가 높고 폐지 목록이 있다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| /effort 로 추론 깊이를 바꾼다(low 에서 max) | 일치 |  |
| Alt+P 로 입력을 지우지 않고 모델을 바꾼다 | 일치 |  |
| \ 뒤에 Enter 로 줄을 바꾼다(모든 터미널) | 일치 |  |
| think, think harder 대신 ultrathink 만 특수 단어로 인식된다 | 일치 | 공식 model-config: ultrathink 만 인식, 나머지는 일반 문장 |
| /cost 로 사용량 확인 | 일치 | /usage 의 별칭 |

### E7. Claude Code Cheat Sheet 2026: Shortcuts, Commands & Flags

주소: https://blakecrosley.com/guides/claude-code-cheatsheet  
언어 en, 운영 개인 (Blake Crosley), 날짜 2026-09-26 갱신 (v2.1.283 기준)

무엇이 들어 있나. 명령, 단축키, CLI 플래그, 권한 모드, 모델별 가격을 버전 이력과 함께 정리한 참고표다. /goal, /code-review, /diff 같은 최근 기능을 다룬다.

좋은 점. 공식 최신판과 버전이 같고 변경점을 버전 번호로 적었다.

한계 · 주의. 가격 수치(/fast 등)는 공식 가격 쪽과 대조하지 않았다[판정보류]. 개발자 기능 비중이 크다.

추천도 중. 정확하지만 사무 사용자에게는 분량 대비 쓸 곳이 적다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| /goal 로 완료 조건을 걸면 조건이 충족될 때까지 계속 일한다 | 일치 |  |
| /diff 로 지금까지 바뀐 내용을 본다 | 일치 |  |
| /code-review 로 바뀐 코드의 오류를 따로 검토시킨다 | 일치 | /review 는 별칭 |
| Ctrl+X Ctrl+K 로 배경 에이전트를 모두 멈춘다 | 일치 |  |
| auto 모드가 모든 요금제의 대화형 세션 기본값이다 | 일치 | v2.1.283 이상 |

### E8. Claude Code in VS Code: Setup, Features, and Workflow

주소: https://www.datacamp.com/tutorial/claude-code-in-vs-code  
언어 en, 운영 기업 (DataCamp, 글쓴이 Khalid Abdelaty), 날짜 2026-04-11 게시, 2026-07-22 수정

무엇이 들어 있나. VS Code 확장을 여는 법, 단축키, @ 참조, 계획 모드 문서 검토, 차이 보기, 되감기를 화면과 함께 설명한다. 다른 확장과 충돌할 때 대처도 적었다.

좋은 점. VS Code 사용자에게 필요한 단축키를 표 하나로 정리했다.

한계 · 주의. auto 모드를 Team/Enterprise 전용이라 적었고, 요구 VS Code 판을 1.98 이상으로 적었다(공식은 1.94.0 이상). 두 곳 모두 옛 정보다.

추천도 상. VS Code 확장으로 쓰는 사무 사용자에게 바로 쓸모 있다. 옛 두 줄만 걸러 읽으면 된다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| 편집기에서 줄을 고른 뒤 Alt+K 로 '@파일#5-10' 참조를 넣는다 | 일치 |  |
| Ctrl+Esc 로 편집기와 Claude 입력창 사이 초점을 옮긴다 | 일치 |  |
| Ctrl+Shift+Esc 로 새 대화 탭을 연다 | 일치 |  |
| Ctrl+Shift+T 로 방금 닫은 Claude 탭을 다시 연다 | 일치 |  |
| auto 모드는 Team/Enterprise 연구 미리보기 전용 | 옛 정보 | v2.1.283 부터 터미널과 VS Code 대화형 세션의 기본 시작 모드 |

### E9. Writing a good CLAUDE.md

주소: https://www.humanlayer.dev/blog/writing-a-good-claude-md  
언어 en, 운영 기업 (HumanLayer, 글쓴이 Kyle), 날짜 2025-11-25

무엇이 들어 있나. 지시가 많아질수록 모델이 전체를 고르게 덜 따른다는 관찰에서 출발해 CLAUDE.md 를 최소한으로 쓰라고 주장한다. 무엇(WHAT) · 왜(WHY) · 어떻게(HOW) 세 가지만 담고 세부는 별도 문서로 빼서 가리키라고 권한다.

좋은 점. 왜 짧아야 하는지 논리가 분명하고, 세부 문서를 필요할 때 읽게 하는 구조(점진 공개)를 구체적으로 보인다.

한계 · 주의. /init 자동 생성을 쓰지 말라는 주장은 공식 권고와 반대다. 300 줄 기준은 공식 200 줄보다 느슨하다.

추천도 상. 지침 파일을 오래 관리하는 사람에게 가장 실용적인 원칙서다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| CLAUDE.md 는 300 줄 미만, 가능하면 60 줄 안팎 | 일치 | 공식은 파일당 200 줄 미만 권장 |
| 상세 절차는 별도 md 파일로 빼고 CLAUDE.md 에는 '어디를 읽어라'만 적는다 | 일치 | @ 가져오기는 시작 시 모두 읽히므로 절약이 안 된다. 경로만 적거나 스킬 · 경로 한정 규칙을 쓴다 |
| 서식 규칙은 CLAUDE.md 에 쓰지 말고 도구(포매터 · 훅)에 맡긴다 | 일치 |  |
| /init 자동 생성은 쓰지 말고 한 줄씩 직접 쓴다 | 공식 문서에 없음 | 공식은 반대로 /init 초안 후 다듬기를 권한다 |

### E10. How I Use Every Claude Code Feature

주소: https://blog.sshh.io/p/how-i-use-every-claude-code-feature  
언어 en, 운영 개인 (Shrivu Shankar, Substack), 날짜 2025-11-02

무엇이 들어 있나. 대기업 모노레포에서 CLAUDE.md, 슬래시 명령, 서브에이전트, 훅, 스킬, MCP 를 어떻게 쓰는지 기능마다 의견을 적었다. 결과물(PR 품질)로만 평가하는 '설정 후 방치' 철학을 내세운다.

좋은 점. 공식과 다른 의견을 근거와 함께 제시해 선택지를 넓혀 준다. 훅을 제출 시점에 거는 요령이 실용적이다.

한계 · 주의. /compact 를 피하라, 커스텀 서브에이전트를 쓰지 말라 같은 개인 의견이 공식 권고와 다르다. 개발팀 규모 환경 전제다.

추천도 중. 심화 참고용. 초심 사무 사용자가 그대로 따르기엔 의견성이 강하다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| /clear 후 자작 명령 /catchup 으로 바뀐 파일을 다시 읽혀 재시작한다 | 공식 문서에 없음 | /catchup 은 사용자 정의 명령 |
| /compact 는 불투명하니 피한다 | 공식 문서에 없음 | 공식은 /compact <지시> 로 남길 것을 지정하라고 권한다 |
| 커스텀 슬래시 명령은 최소로 둔다 | 공식 문서에 없음 |  |
| 훅은 파일 쓰기 때가 아니라 커밋 · 제출 시점에 검사해 막는다 | 일치 | 공식: 반드시 일어나야 할 일은 훅, Stop 훅으로 검사 통과 전 종료 차단 |

### E11. Skip the Terminal (And 8 Other Claude Code Tricks for Non-Technical Users)

주소: https://hannahstulberg.substack.com/p/skip-the-terminal-and-8-other-claude  
언어 en, 운영 개인 (Hannah Stulberg, Substack 뉴스레터), 날짜 2026-01-01

무엇이 들어 있나. 비개발자가 Claude Code 를 쓸 때 개발자에게는 당연하지만 초심자는 모르는 요령 9 가지를 소개한다. 터미널 대신 IDE, 숨김 파일 보기, 병렬 세션, 상태줄, 음성 입력을 다룬다.

좋은 점. 비개발자 관점이라 사무 사용자에게 바로 와닿는다. 무료로 읽힌다.

한계 · 주의. Cursor 를 권하고 음성 입력 도구 추천 링크가 있다(제휴 성격). 압축 시점 50-60 % 는 근거 없는 경험칙이다.

추천도 중. 발상은 좋으나 특정 제품 권유가 섞였다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| 검은 터미널 대신 VS Code 같은 편집기 안에서 쓴다 | 일치 | 공식은 VS Code 확장을 VS Code 에서의 권장 방식으로 소개 |
| 탐색기에서 숨김 파일을 보이게 해 .claude 폴더를 직접 본다 | 공식 문서에 없음 |  |
| 파일이나 그림을 입력창으로 끌어다 놓는다 | 일치 |  |
| 상태줄로 맥락 사용률을 보고 50-60 % 에서 직접 압축한다 | 공식 문서에 없음 | 상태줄(/statusline)은 공식, 수치 기준은 없음 |
| 일마다 세션을 따로 열어 맥락을 섞지 않는다 | 일치 |  |

### E12. Malicious Coding Agent Skills and the Risk of Dynamic Context

주소: https://securitylabs.datadoghq.com/articles/malicious-skills-supply-chain-risks-in-coding-agents-with-dynamic-context/  
언어 en, 운영 기업 (Datadog Security Labs, Nick Frichette · Ryan Simon), 날짜 2026-05-11

무엇이 들어 있나. 스킬 안의 !`명령` 줄(동적 맥락)이 모델이 내용을 보기 전에 실행된다는 점을 이용해 토큰을 빼내는 실제 악성 스킬 사례를 분석했다. 설치 전 점검 목록과 조직 차원 차단 설정을 제시한다.

좋은 점. 남의 스킬을 들일 때 무엇을 열어 봐야 하는지 가장 구체적이다. 공식 문서 동작과도 맞는다.

한계 · 주의. 보안 업체 글이라 자사 탐지 제품 언급이 있다. 명령어 안내서는 아니다.

추천도 상. 스킬 · 플러그인 설치 전 점검 기준으로 꼭 읽을 글이다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| SKILL.md 에서 !` 로 시작하는 줄을 찾아 curl · wget 같은 네트워크 명령이 있는지 본다 | 일치 | 공식 skills: 명령 결과가 먼저 치환된 뒤 Claude 에 전달 |
| 머리말의 allowed-tools: Bash(*) 같은 넓은 허용을 경계한다 | 일치 | 공식: allowed-tools 는 작업공간 신뢰와 무관하게 적용되니 검토하라 |
| disableSkillShellExecution 설정으로 스킬의 셸 실행을 막을 수 있다 | 일치 |  |
| .claude 폴더 변경은 코드 리뷰를 거친다 | 공식 문서에 없음 |  |

### K1. Claude Code 모범 사례 (한국어 공식 문서)

주소: https://code.claude.com/docs/ko/best-practices  
언어 ko, 운영 공식 Anthropic, 날짜 날짜 표시 없음 (영어판과 같은 v2.1.283 내용, 확인일 2026-09-29)

무엇이 들어 있나. 영어판 모범 사례의 한국어 번역으로 검증 수단, 계획 모드, 구체적 프롬프트, CLAUDE.md, 세션 관리, 자동화를 같은 순서로 담았다. /goal, /btw, auto 모드 같은 최신 내용까지 반영돼 있다.

좋은 점. 공식 최신 내용을 한국어로 읽을 수 있다.

한계 · 주의. 기계 번역 느낌이 강하다('주방 싱크 세션', '당신'). 용어가 영어와 섞여 있어 영어판과 나란히 보는 편이 낫다.

추천도 상. 한국어 자료 중 유일하게 공식이고 최신이다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| CLAUDE.md 각 줄에 '이 줄을 지우면 Claude 가 실수하는가'를 묻고 아니면 지운다 | 일치 |  |
| /context 로 CLAUDE.md 가 실제로 읽혔는지 확인한다 | 일치 |  |
| @ 로 파일을 지정하고, 그림은 붙여 넣거나 끌어다 놓는다 | 일치 |  |
| /rename 으로 세션 이름을 붙이고 claude --continue 또는 --resume 으로 이어 간다 | 일치 |  |
| 한 줄만 자꾸 무시되면 그 줄에만 IMPORTANT 를 붙인다. 여러 줄에 붙이면 효과가 없다 | 일치 |  |

### K2. Claude Code v2.1 슬래시 명령어와 키보드 단축키 총정리

주소: https://velog.io/@scarleter99/Claude-Code-v2.1-%EC%8A%AC%EB%9E%98%EC%8B%9C-%EB%AA%85%EB%A0%B9%EC%96%B4%EC%99%80-%ED%82%A4%EB%B3%B4%EB%93%9C-%EB%8B%A8%EC%B6%95%ED%82%A4-%EC%B4%9D%EC%A0%95%EB%A6%AC  
언어 ko, 운영 개인 (velog scarleter99), 날짜 2026-01-30 (v2.1.23 기준)

무엇이 들어 있나. 슬래시 명령을 세션 · 설정 · 정보 · 파일 · 리뷰로 나누고 줄바꿈, 배경 실행, 확장 사고 단축키를 표로 정리했다. 당시 변경 공지를 인용해 폐지된 기능도 적었다.

좋은 점. 한국어로 된 표 정리 중 가장 깔끔하고 분류가 좋다.

한계 · 주의. v2.1.23 기준이라 그 뒤 폐지된 /pr-comments 가 남아 있고, 'ultrathink 는 더 이상 아무것도 하지 않는다'는 당시 문장은 현재 공식과 다르다(현재는 ultrathink 를 인식).

추천도 중. 구성은 좋으나 8 개월 사이 여러 항목이 바뀌었다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| \ + Enter 로 줄바꿈(가장 호환성 높음) | 일치 |  |
| Ctrl+B 로 오래 걸리는 명령을 배경으로 돌린다 | 일치 |  |
| Alt+T 로 확장 사고를 켜고 끈다 | 일치 | 공식: Opus 5.5 · Sonnet 5.5 · Fable 은 항상 사고하므로 효과 없음 |
| /pr-comments 로 PR 댓글 보기 | 옛 정보 | v2.1.91 에서 폐지 |
| ultrathink 는 더 이상 효과가 없다 | 옛 정보 | 현재 공식 model-config 는 ultrathink 를 그 턴의 깊은 추론 요청으로 인식한다 |

### K3. [번역] CLAUDE.md 완벽 가이드

주소: https://velog.io/@surim014/claude-md-guide  
언어 ko, 운영 개인 (velog Sonny 번역, 원문 Builder.io 'CLAUDE.md guide'), 날짜 2026-01-28

무엇이 들어 있나. CLAUDE.md 에 넣을 것(한 줄 설명, 구체적 스타일, 명령, 주의사항)과 @ 가져오기, .claude/rules/, 하위 폴더 CLAUDE.md 로 나누는 법을 설명한다. # 단축키가 2.0.70 에서 없어졌다는 점을 명시했다.

좋은 점. 옛 # 단축키 폐지를 짚은 드문 한국어 글이다. 규칙 폴더와 계층 구조 설명이 공식과 맞는다.

한계 · 주의. 300 줄 기준은 공식 200 줄보다 느슨하다. 폐지 버전 번호 2.0.70 은 공식 문서에서 확인하지 못했다[판정보류: 공식 changelog 에서 확인].

추천도 상. CLAUDE.md 를 한국어로 익히기에 가장 정확하다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| CLAUDE.md 는 300 줄 미만 | 일치 | 공식은 200 줄 미만 |
| # 단축키는 없어졌으니 Claude 에게 'CLAUDE.md 에 추가해'라고 요청한다 | 일치 |  |
| 주제별 규칙은 .claude/rules/ 폴더에 파일로 나눈다 | 일치 |  |
| 검토에서 지적된 규칙 위반을 CLAUDE.md 에 추가할 신호로 삼는다 | 일치 | 공식 memory: 같은 실수가 두 번 나면 추가 |

### K4. Claude Code 사용 가이드

주소: https://tech.hyperithm.com/claude_code_guides  
언어 ko, 운영 기업 (하이퍼리즘 기술 블로그, 이한결), 날짜 2025-06-04

무엇이 들어 있나. 사내 개발자용으로 설치, IDE 연동, 핵심 명령, MCP, 메모리, 권한, 장시간 세션, worktree 를 한 문서에 담았다. /compact 에 요약 지시를 붙이는 식의 실전 예가 있다.

좋은 점. 국내 기업이 사내 교육용으로 만든 체계적 목차다.

한계 · 주의. 2025-06 판이라 # 메모리 저장, think hard 프롬프트, --dangerously-skip-permissions 같은 옛 방식이 현재형으로 적혀 있다.

추천도 하. 구조는 좋으나 1 년 넘게 갱신되지 않아 옛 조작법이 많다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| 프롬프트를 # 로 시작하면 어느 메모리에 저장할지 묻는다 | 옛 정보 |  |
| 'think hard' 라고 써서 더 깊이 생각하게 한다 | 옛 정보 | 현재는 ultrathink 만 인식, think hard 는 일반 문장 |
| --dangerously-skip-permissions 는 dev container 같은 격리 환경에서만 쓴다 | 공식 문서에 없음 | 확인한 쪽에는 없음. 현재는 auto 모드가 기본 |
| /compact 뒤에 요약 방향을 지시한다 | 일치 |  |
| Shift+Tab 으로 계획 · 자동 수락 · 일반 모드를 바꾼다 | 일치 |  |

### K5. (완결판) 따라하기만 하면 되는 클로드코드 업무 자동화

주소: https://brunch.co.kr/@sukistory/84  
언어 ko, 운영 개인 (브런치 Suki), 날짜 2026-02-06

무엇이 들어 있나. 비개발자가 설치부터 폴더 세팅, 업무 자동화까지 따라 하도록 단계별로 안내한다. 마크다운 '프로젝트 셋팅 가이드' 문서를 주면 Claude 가 폴더 구조를 만들고 일을 진행하는 방식을 보여 준다.

좋은 점. 비개발 실무자 눈높이에 맞춘 순서와 말투다.

한계 · 주의. 유료 강의(인프런, 패스트캠퍼스) 홍보가 들어 있다. npm 설치 명령을 안내하는데 공식 설치 쪽은 이번에 대조하지 않았다[판정보류: code.claude.com/docs/en/setup 에서 확인].

추천도 중. 첫걸음 안내로 좋으나 홍보와 설치법 최신성 확인이 필요하다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| npm install -g @anthropic-ai/claude-code 로 설치 | 공식 문서에 없음 | 확인한 네 쪽에 설치법이 없어 대조 못 함 |
| 작업 폴더로 이동한 뒤 claude 를 실행한다 | 일치 |  |
| 참고 파일 경로를 먼저 알려 주고 원하는 결과를 설명한다 | 일치 | @ 로 파일 지정 |
| 셋팅 가이드 문서를 주고 폴더 구조를 만들게 한다 | 공식 문서에 없음 |  |

### K6. 2026 클로드 코드(Claude Code) 사용법 : 설치부터 실전 활용까지

주소: https://blog.highoutputclub.com/2026-claude-code-for-non-developers/  
언어 ko, 운영 기업 (하이아웃풋클럽), 날짜 2026-02-15

무엇이 들어 있나. 비개발자를 대상으로 설치, 폴더에서 실행, CLAUDE.md, MCP 연동, 활용 시나리오(랜딩 페이지, 콘텐츠 자동화, 대시보드)를 소개한다. 요금제 비용도 적었다.

좋은 점. 비개발자 활용 장면이 구체적이다.

한계 · 주의. 교육 프로그램 · 멤버십 광고가 있다. 설치 명령이 macOS/Linux 위주라 Windows 사용자는 공식 설치 쪽을 따로 봐야 한다.

추천도 중. 입문 동기 부여용. 조작법 세부는 공식으로 보완해야 한다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| macOS/Linux 에서 curl 설치 스크립트로 설치 | 공식 문서에 없음 | 확인한 네 쪽 밖. Windows 해당 없음 |
| 프로젝트 폴더에서 claude 실행 | 일치 |  |
| CLAUDE.md 로 프로젝트 정보를 기억시킨다 | 일치 |  |
| MCP 로 Slack · Notion 을 연결한다 | 일치 | claude mcp add |

### K7. Claude Code의 모든 기능 활용법 (GeekNews 소개글)

주소: https://news.hada.io/topic?id=24099  
언어 ko, 운영 커뮤니티 (GeekNews, 원문 E10 요약), 날짜 [추정] 2025-11 (페이지에 '10달전'으로만 표시)

무엇이 들어 있나. E10(sshh) 글을 한국어로 요약하고 국내 개발자 댓글 토론을 붙였다. 댓글에서 CLAUDE.md 준수율을 높이는 강조 표기, /compact 지연 문제 같은 반론이 오간다.

좋은 점. 원문 요약과 한국 개발자 반응을 함께 볼 수 있다.

한계 · 주의. 요약이라 원문 맥락이 빠진다. 댓글의 '대문자 강조로 95 % 준수' 는 근거 없는 수치다.

추천도 중. 심화 토론 참고용.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| CLAUDE.md 에는 '하지 말 것'보다 대안을 적는다 | 공식 문서에 없음 | 공식은 구체적이고 검증 가능한 문장을 권함 |
| 중요한 규칙은 ALWAYS 같은 강조로 표시한다 | 일치 | 공식: 한 줄에만 강조, 여러 줄 강조는 무효 |
| /clear 후 필요한 파일만 다시 읽혀 시작한다 | 일치 |  |
| 복잡한 명령은 짧은 스크립트로 감싸 Claude 에게 준다 | 공식 문서에 없음 |  |

### K8. Claude Code 사용법 및 주요 명령 (GPTers 스터디 글)

주소: https://www.gpters.org/wealth/post/claude-code-usage-key-tXdand1rtThxlWV  
언어 ko, 운영 커뮤니티 (GPTers, 작성자 Develiper), 날짜 2026-05-18

무엇이 들어 있나. 스터디원 참고용으로 슬래시 명령, 단축키, 입력 접두어, 작업 모드, CLAUDE.md, 서브에이전트, 훅, MCP, IDE 통합을 14 절로 정리했다.

좋은 점. 범위가 넓고 한국어 입문자 커뮤니티에서 많이 읽힌다.

한계 · 주의. 2026-05 작성인데도 폐지된 /vim, /pr_comments 와 # 메모리 접두어를 현재형으로 적었다. 옛 자료를 옮겨 온 것으로 보인다[추정].

추천도 하. 작성일보다 내용이 오래돼 초심자가 헷갈리기 쉽다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| # 로 시작해 CLAUDE.md 에 추가 | 옛 정보 |  |
| /vim 으로 Vim 모드 전환 | 옛 정보 | v2.1.92 에서 폐지, /config 의 Editor mode 사용 |
| /pr_comments 로 PR 댓글 조회 | 옛 정보 | v2.1.91 에서 폐지 |
| /cost 로 토큰 사용량과 비용 확인 | 일치 | /usage 별칭 |
| ! 로 시작하면 셸 명령을 바로 실행 | 일치 |  |

### K9. Claude Code로 코드 리뷰 자동화하기, 설정부터 실패 학습 루프까지

주소: https://www.mimul.com/blog/claude-code-review/  
언어 ko, 운영 개인 (Mimul Tech blog), 날짜 2026-02-24 작성, 2026-04-16 갱신

무엇이 들어 있나. CLAUDE.md, 설정, 에이전트, 스킬, 규칙, 명령, MCP 의 역할을 층으로 나누고 코드 리뷰 자동화에 적용했다. 같은 지적이 반복되지 않도록 실패를 메모리와 규칙으로 올리는 '실패 학습 루프'를 제안한다.

좋은 점. 지침을 어디에 둘지(사실은 CLAUDE.md, 절차는 스킬) 구분이 명확하고 공식과 맞는다.

한계 · 주의. Rust 개발 예시라 사무 사용자는 원리만 가져와야 한다. SKILL.md 500 줄 · CLAUDE.md 50 줄 수치는 저자 기준이다.

추천도 중. 설계 원리는 좋으나 예시가 개발 전용이다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| CLAUDE.md 에는 사실, 여러 단계 절차는 스킬로 뺀다 | 일치 |  |
| CLAUDE.md 50 줄 이하 | 일치 | 공식은 200 줄 미만, 더 엄격한 기준 |
| 훅으로 위험 명령을 막고 편집 뒤 자동 정리를 건다 | 일치 |  |
| 여러 과업에서 반복되는 실패는 사용자 홈의 .claude/rules 로 올린다 | 일치 | 사용자 규칙은 모든 프로젝트에 적용되니 충돌 주의 |

### K10. 개발자를 위한 Claude Code 토큰 사용량 최적화 전략 (요즘IT)

주소: https://yozm.wishket.com/magazine/detail/3677/  
언어 ko, 운영 기업 (요즘IT, 필자 길벗), 날짜 2026-03-26

무엇이 들어 있나. 토큰이 무엇이고 왜 한글이 더 많이 쓰는지, 입력 · 출력 토큰이 비용과 속도에 주는 영향을 설명한다. CLAUDE.md 축소, 문서 분리, 필요한 MCP 만 켜기, 구체적 요청, 세션 분리를 권한다.

좋은 점. 비용 관점에서 왜 짧게 쓰고 세션을 나눠야 하는지 설명해 사무 사용자도 이해하기 쉽다.

한계 · 주의. '80-90 % 축소', 'MCP 로 5-7 % 절약' 같은 수치는 출처가 없다. 검색 결과에는 '클로드 코드 폴더 세팅하기'로 떴으나 실제 3677 번 글은 토큰 최적화 글이었다.

추천도 중. 원리 설명은 좋고 수치는 참고만 한다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| CLAUDE.md 의 불필요한 서술을 지우고 구조화한다 | 일치 |  |
| 세부 안내는 별도 문서로 나눠 필요할 때만 읽게 한다 | 일치 | @ 가져오기는 시작 시 모두 읽히니 경로만 적거나 스킬로 |
| 지금 일에 필요한 MCP 만 켠다 | 일치 | /doctor, /skill-doctor 가 안 쓰는 항목을 알려 줌 |
| '개선해줘' 대신 무엇을 몇에서 몇으로 바꿀지 구체적으로 적는다 | 일치 |  |
| 기능별로 세션을 나누고 /clear, /compact 를 쓴다 | 일치 |  |

### K11. 소프트웨어 3.0 시대를 맞이하며 (토스 기술 블로그)

주소: https://toss.tech/article/44539  
언어 ko, 운영 기업 (토스, 김용성), 날짜 2026-01-26

무엇이 들어 있나. Claude Code 를 LLM 을 실제 업무에 연결하는 '하네스'로 보고 슬래시 명령 · 서브에이전트 · 스킬 · MCP · CLAUDE.md 를 전통 소프트웨어 계층에 빗대어 설명한다. 맥락 창을 메모리처럼 관리하라는 원칙을 강조한다.

좋은 점. 각 구성 요소가 무슨 역할인지 한 표로 이해하게 해 준다.

한계 · 주의. 개념 설명 위주라 명령 사용법은 거의 없다. 비유가 개발자에게 익숙한 용어다.

추천도 중. 구성 요소 이해용. 조작 안내서는 아니다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| 맥락 창을 한정된 메모리처럼 아껴 쓴다 | 일치 |  |
| 스킬은 필요할 때 펼쳐지는 구조로 나눠 둔다 | 일치 |  |
| 되돌리기 어려운 작업에서만 사람 확인을 받는다 | 공식 문서에 없음 | 공식은 권한 모드와 auto 분류기로 다룬다 |

### K12. 클로드 코드(Claude Code) 기본 필수 명령어 완벽 정리

주소: https://www.nolavoza.com/technology/claude-code-essential-commands-guide/  
언어 ko, 운영 개인 (노라보자 블로그), 날짜 2026-06-17

무엇이 들어 있나. 초보자가 알아야 할 필수 명령(/help, /clear, /compact, /init, /quit)과 설정 · 비용 명령, 단축키를 정리했다. 홈 폴더에 커스텀 명령을 만드는 법도 짧게 다룬다.

좋은 점. 초보자 눈높이의 쉬운 설명이다.

한계 · 주의. '20-30 분마다 /compact' 권고는 공식 근거가 없다. 커스텀 명령은 이제 스킬로 합쳐졌다는 설명이 없다.

추천도 중. 입문용으로 무난하나 몇 가지 경험칙이 근거 없이 적혀 있다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| 20-30 분마다 /compact 를 실행한다 | 공식 문서에 없음 | 공식은 일이 바뀔 때 /clear, 자동 압축이 기본 |
| 사용자 홈의 .claude/commands/ 에 md 파일을 넣어 개인 명령을 만든다 | 일치 | 스킬(.claude/skills)이 현재 권장 형태 |
| /quit 로 종료 | 일치 | /exit 의 별칭 |
| @README.md 처럼 @ 로 파일을 가리킨다 | 일치 |  |

### K13. Claude Code를 200% 활용하는 방법: spec-kit, Everything Claude Code, Oh My ClaudeCode 완벽 가이드

주소: https://velog.io/@sammy0329/Claude-Code%EB%A5%BC-200-%ED%99%9C%EC%9A%A9%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-spec-kit-Everything-Claude-Code-Oh-My-ClaudeCode-%EC%99%84%EB%B2%BD-%EA%B0%80%EC%9D%B4%EB%93%9C  
언어 ko, 운영 개인 (velog sammy), 날짜 2026-02-02

무엇이 들어 있나. 남이 만든 대형 플러그인 묶음 세 가지(spec-kit, Everything Claude Code, Oh My ClaudeCode)의 설치 명령과 쓰는 법을 비교한다. 컨텍스트 낭비와 토큰 급증 같은 주의도 표로 적었다.

좋은 점. 남의 플러그인을 들일 때 어떤 명령이 무엇을 설치하는지 보여 준다. 활성 MCP 를 줄이라는 주의가 있다.

한계 · 주의. 남의 규칙 폴더를 사용자 홈 .claude/rules 에 통째로 복사하라고 안내한다(모든 프로젝트에 적용되어 기존 지침과 충돌 위험). 훅 · 스크립트 내용을 검토하라는 안내는 약하다. 모델 이름이 옛 판(Opus 4.5 등)이다.

추천도 하. 사무 사용자가 따라 하면 설정이 크게 오염될 수 있다. 설치 전 점검 사례로만 읽는다.

| 사무 사용자에게 쓸 만한 팁 | 공식 대조 | 비고 |
|---|---|---|
| /plugin marketplace add 소유자/저장소 로 마켓플레이스를 추가하고 /plugin install 로 설치한다 | 일치 | 명령은 맞다. 공식은 설치 전 세부 창의 Will install 목록을 읽으라고 한다 |
| 받은 rules 폴더를 사용자 홈 .claude/rules/ 로 통째로 복사한다 | 공식 문서에 없음 | 사용자 규칙은 모든 프로젝트에 적용되고 충돌 시 어느 쪽을 따를지 보장되지 않는다(공식 memory) |
| 활성 MCP 는 10 개 이하로 둔다 | 공식 문서에 없음 |  |
| 복잡한 설계는 Opus 4.5, 일반은 Sonnet 4.5 | 옛 정보 | 현재 기본은 Opus 5.5 |

## 3. 여러 출처가 권하는 실천 15 가지

| 순위 | 실천 | 권하는 출처 | 공식 문서 |
|---|---|---|---|
| 1 | 관련 없는 일로 넘어갈 때 /clear 로 맥락을 비운다. 같은 문제를 두 번 고쳐도 안 되면 새로 시작하고 배운 점을 첫 프롬프트에 넣는다. | E1, K1, E2, K10, E10, K7 | 일치 (best-practices 'Course-correct', 'Manage context') |
| 2 | CLAUDE.md 는 짧게 유지하고 줄마다 '지우면 실수하는가'를 묻는다. 수치는 출처마다 50 에서 500 줄로 다르나 공식은 파일당 200 줄 미만을 권한다. | E1, K1, E9, K3, K9, K10, E2 | 일치 (memory 'Size: target under 200 lines') |
| 3 | /init 으로 CLAUDE.md 초안을 만들고 사람이 읽고 다듬는다. | E2, K3, K12, E1 | 일치 (HumanLayer E9 만 반대) |
| 4 | 여러 단계 절차 · 가끔 쓰는 지식은 CLAUDE.md 가 아니라 스킬이나 별도 문서로 빼고 필요할 때 읽게 한다. | E1, E9, K9, K11, K10 | 일치 (단 @ 가져오기는 시작 시 모두 읽혀 절약되지 않는다) |
| 5 | 여러 파일을 건드리거나 방법이 불확실한 일은 계획 모드(Shift+Tab 또는 /plan)로 계획부터 받고 검토한 뒤 실행한다. 한 문장으로 설명되는 작은 일은 바로 시킨다. | E1, K1, E8, K4, E4 | 일치 |
| 6 | 일을 맡길 때 확인 방법을 같이 주고, 성공 주장 대신 증거(출력, 비교 결과)를 보이게 한다. | E1, K1, E3 | 일치 (best-practices 첫 절) |
| 7 | 파일은 @ 로 지정하고, 설명하기 어려운 상황은 화면 캡처를 붙여 넣는다(Windows 는 Alt+V). | E1, E4, E8, E3, K5, K12 | 일치 |
| 8 | 틀린 방향이면 Esc 로 바로 멈추고, Esc 두 번이나 /rewind 로 되돌린다. Bash 로 바뀐 파일은 복원되지 않으니 원본은 따로 보관한다. | E1, E4, E5, E6, E7 | 일치 (checkpointing 경고 포함) |
| 9 | 긴 작업 중 맥락이 차면 /compact 뒤에 남길 내용을 지시한다. CLAUDE.md 에 '압축 시 수정한 파일 목록은 남겨라' 같은 지시를 둘 수 있다. | E1, K4, K10 | 일치 (E10 · K7 은 /compact 회피를 권해 이견) |
| 10 | /context 로 맥락 사용량과 읽힌 지침 파일을, /usage 로 사용량 한도를 확인한다. | E4, K1, E11, K12 | 일치 (/cost 는 /usage 별칭) |
| 11 | 자료 조사 · 대량 파일 훑기는 서브에이전트에 맡겨 본 대화 맥락을 아낀다. | E1, E2, E3, K11 | 일치 (E10 은 커스텀 서브에이전트에 부정적) |
| 12 | 반드시 매번 일어나야 할 일(검사, 차단)은 CLAUDE.md 문장이 아니라 훅으로 건다. | E1, E9, E10, K9 | 일치 (CLAUDE.md 는 권고, 훅은 결정적) |
| 13 | 같은 지시를 자꾸 붙여 넣게 되면 스킬(또는 옛 형태의 .claude/commands)로 만들어 /이름 으로 부른다. 부작용 있는 절차는 disable-model-invocation: true 로 수동 호출만 허용한다. | E2, E5, K12, E11, E1 | 일치 (커스텀 명령은 스킬로 통합) |
| 14 | VS Code 확장에서 쓰면 Alt+K 로 선택 영역을 참조하고, 계획 모드 계획을 문서로 열어 주석을 달 수 있어 비개발자에게 편하다. | E8, E11, E1 | 일치 (vs-code) |
| 15 | 세션에 /rename 으로 이름을 붙이고 claude --continue, --resume 또는 /resume 으로 이어 간다. | E1, K1 | 일치 |

## 4. 흔한 오해와 옛 조언

**프롬프트를 # 로 시작하면 CLAUDE.md(메모리)에 저장된다** (E2, E5, K4, K8). 현재 입력 접두어는 / ! @ : ? 뿐이다(interactive-mode). 'CLAUDE.md 에 추가해'라고 요청하거나 /memory 로 파일을 연다. K3 는 2.0.70 에서 제거라 적었으나 버전 번호는 공식에서 확인 못 함[판정보류].

**think < think hard < think harder < ultrathink 순으로 사고량이 커진다** (K4). 현재 공식 model-config 는 ultrathink 만 특수 단어로 인식하고 think, think hard 는 일반 문장으로 넘긴다. 사고 깊이는 /effort 로 정한다.

**ultrathink 는 더 이상 아무 효과가 없다** (K2). 2026-01 당시 문장이다. 현재 공식은 ultrathink 를 그 턴에 깊은 추론을 요청하는 단어로 인식한다(세션 effort 는 그대로).

**/vim, /pr-comments 를 쓸 수 있다** (K8, K2). /pr-comments 는 v2.1.91, /vim 은 v2.1.92 에서 폐지됐다. Vim 모드는 /config 의 Editor mode.

**/ultraplan 은 노력 수준으로 통합됐다** (E6). 공식 commands: /ultraplan 은 폐지, 계획 모드를 쓰라고 적었다.

**--dangerously-skip-permissions 로 권한 확인을 늘 끄고 쓰면 편하다** (E5). v2.1.283 부터 분류기가 위험한 동작만 막는 auto 모드가 기본 시작 모드다. 권한 무시는 격리 환경에서만 쓴다.

**auto 모드는 Team/Enterprise 전용 미리보기다** (E8). v2.1.283 이상에서 터미널과 VS Code 대화형 세션의 기본 시작 모드(이전 판은 Pro, Max, Team).

**VS Code 확장은 1.98 이상이 필요하다** (E8). 공식 vs-code 쪽 요구 사항은 VS Code 1.94.0 이상.

**/cost 는 따로 있는 비용 명령이다** (K8, E6, K12). /cost 와 /stats 는 /usage 의 별칭이다. 기능은 같다.

**20-30 분마다 /compact 하거나 맥락 50-60 % 에서 압축해야 한다** (K12, E11). 공식 근거가 없는 경험칙이다. 공식은 일이 바뀔 때 /clear, 필요할 때 /compact <지시>, 부분 압축은 /rewind 의 요약 기능을 권한다.

**CLAUDE.md 를 @ 가져오기로 쪼개면 맥락이 절약된다** (K10(일부), K3(일부)). 공식 memory: @ 가져오기 파일도 시작할 때 모두 읽힌다. 절약하려면 경로 한정 규칙(.claude/rules 의 paths)이나 스킬을 쓴다.

**Ctrl+V 로 그림을 붙여 넣는다** (E5). macOS 기준 설명이다. 공식 interactive-mode 에서 Windows 는 Alt+V.

**CLAUDE.md 에 적으면 Claude 가 반드시 지킨다** (K7 댓글). 공식 memory: CLAUDE.md 는 맥락일 뿐 강제 설정이 아니다. 반드시 막아야 할 동작은 훅이나 권한 규칙(permissions.deny)으로 건다.

## 5. 남의 명령 · 스킬 · 훅 · 플러그인을 들일 때 볼 것

1. **설치 전에 원문을 연다**. 요약 사이트가 아니라 저장소의 SKILL.md 본문, scripts 폴더, hooks 설정, .mcp.json, 플러그인의 plugin.json 을 직접 읽는다. /plugin 세부 창의 'Will install' 목록(명령, 에이전트, 스킬, 훅, MCP)을 확인한다. (근거: 공식 discover-plugins, E12)
2. **!`명령` 줄을 찾는다**. 스킬 본문의 !`...` 과 ```! 블록은 Claude 가 내용을 보기 전에 이 PC 에서 실행된다. curl, wget, Invoke-WebRequest, gh auth token, 환경변수 · .ssh · 키 파일 접근이 있으면 들이지 않는다. (근거: 공식 skills, E12)
3. **allowed-tools 를 확인한다**. 스킬 머리말의 allowed-tools 는 작업공간 신뢰와 무관하게 호출된 턴 동안 확인 없이 도구를 쓰게 한다. Bash(*) 처럼 넓은 허용은 거절하거나 좁힌다. (근거: 공식 skills, E12)
4. **훅이 무엇을 언제 실행하는지 본다**. 플러그인과 남의 저장소 .claude/settings.json 의 hooks 는 매 도구 호출이나 세션 시작 때 셸 명령을 돌린다. 외부 전송, 파일 삭제, 설정 덮어쓰기가 있는지 본다. (근거: 공식 discover-plugins, E12)
5. **범위는 좁게 설치한다**. 처음에는 local 범위(이 저장소, 나만)로 설치해 시험하고, user 범위로 올리는 것은 검토 뒤에 한다. 남의 rules 를 사용자 홈 .claude/rules 로 통째로 복사하지 않는다. 모든 과업에 적용되고 기존 지침과 충돌하면 어느 쪽을 따를지 보장되지 않는다. (근거: 공식 discover-plugins, 공식 memory, K13)
6. **자동 갱신을 켜지 않는다**. 서드파티 · 커뮤니티 마켓플레이스는 자동 갱신이 기본 꺼짐이다. 켜 두면 검토하지 않은 새 판이 들어온다. 갱신은 손으로 하고 바뀐 부분을 다시 읽는다. (근거: 공식 discover-plugins)
7. **맥락 비용을 잰다**. 설치 뒤 /skill-doctor, /doctor, claude plugin details <이름> 으로 매 턴 추가되는 토큰을 보고 안 쓰는 것은 끈다. 대형 묶음 플러그인은 지침 파일과 스킬을 대량으로 얹는다. (근거: 공식 commands, 공식 discover-plugins, K13)
8. **외부 업로드 경로를 확인한다**. 설치 스크립트나 스킬이 결과를 공개 저장소 · 웹 호스팅 · 분석 서버로 보내는지 본다. 발주처 자료와 미공개 결과가 섞인 과업 폴더에서는 특히 그렇다. (근거: E12, 사용자 전역 규칙)
9. **조직 차원 차단 설정을 안다**. disableSkillShellExecution 을 켜면 사용자 · 프로젝트 · 플러그인 스킬의 셸 실행이 막힌다. 스킬을 자주 들이는 환경이면 검토한다. (근거: 공식 skills, E12)
10. **설치 명령 한 줄을 그대로 붙여 넣지 않는다**. curl ... | bash, npm -g, uv tool install 같은 한 줄 설치는 무엇을 받아 어디에 쓰는지 먼저 확인한다. 블로그 글의 명령은 판이 바뀌었을 수 있으니 공식 설치 쪽과 대조한다. (근거: K5, K6, K13)

## 6. 확인하지 못한 것

- wikidocs.net 의 클로드 코드 입문서 두 쪽(342291, 329814)은 HTTP 403 으로 열리지 않아 목록에서 뺐다.
- K3 가 적은 '# 단축키 2.0.70 에서 제거' 버전 번호는 공식 changelog 에서 확인하지 않았다.
- K5 · K6 의 설치 명령(npm, curl 스크립트)은 공식 setup 쪽과 대조하지 않았다.
- E7 의 가격 수치(/fast 등)는 공식 가격 쪽과 대조하지 않았다.
- K7 게시일은 페이지에 상대 표기('10달전')만 있어 2025-11 로 추정했다.
- 각 쪽 내용은 WebFetch 요약으로 읽었고, 옛 정보 판정이 걸린 E2, K4, K8 은 원문 문장을 다시 인용받아 확인했다. 나머지는 요약 단계의 누락 가능성이 있다.
