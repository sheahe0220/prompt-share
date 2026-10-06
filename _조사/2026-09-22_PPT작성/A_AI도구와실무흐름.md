# AI 로 PowerPoint 만들기: 도구 · 실무 흐름 · 실패 유형 조사

조사일 2026-09-22. 대상 사용자: Windows, Office 2024(영구 라이선스로 가정), python-pptx, Claude Code, Claude.ai 를 쓰는 수문 · 환경공학 연구자.

표기 규칙. 각 주장 뒤에 출처 번호 [S n] 을 붙였고 출처 목록은 문서 끝에 있다. 날짜는 원문에 적힌 것만 옮겼다. 원문에서 날짜를 못 찾으면 "날짜 미확인" 으로 적었다. 추정은 [추정], 확인 못 한 것은 [판정보류] 로 표시했다. 경쟁사가 쓴 비교 글(presentations.ai, deckary, anygen, 2slides, slidegmm 등)은 이해관계가 있으므로 수치 근거로 쓰지 않고 참고로만 표시했다.

## 0. 이 사용자에게 가장 중요한 결론 다섯 가지

첫째, **Office 2024 영구 라이선스에는 Copilot 이 없다.** Microsoft Q&A 의 자원봉사 답변(2026-07-06)은 "Copilot 은 Office Home 2024 일회성 구매에 포함되지 않고 Microsoft 365 구독에만 묶인다" 고 적었다 [S 16]. 공식 FAQ 도 발표 생성 · 파일에서 발표 만들기는 Copilot 라이선스가 필요하다고 한다 [S 5]. 자원봉사 답변은 공식 문서가 아니므로 [추정] 수준이지만 PowerPoint 리본에 Copilot 단추가 있는지 직접 보면 바로 확인된다.

둘째, **Claude for PowerPoint 추가 기능도 Windows 에서는 Microsoft 365 구독 빌드를 요구한다.** 공식 문서의 지원 목록은 "PowerPoint on Windows with a Microsoft 365 subscription, build 16.0.13127.20296 or later", 웹판, Mac 16.46 이상이고, 미지원 목록에 "PowerPoint 2016 and 2019 perpetual or volume license" 가 있다 [S 2]. Office 2024 영구판은 두 목록 어디에도 이름이 없다 [판정보류]. 확인 방법: AppSource 에서 설치를 시도하거나, PowerPoint 웹판(무료 계정)에서 쓰는 우회로를 시험한다.

셋째, 따라서 이 사용자에게 현실적인 경로는 **Claude Code + python-pptx(또는 pptxgenjs) + 기관 템플릿 + 렌더링 검수** 이다. Anthropic 공식 pptx 스킬이 바로 이 흐름(템플릿 썸네일, XML 편집, validate, soffice 로 PDF, pdftoppm 으로 이미지, 눈으로 검수)을 문서화해 두었다 [S 1]. 이 사용자 PC 에는 PowerPoint 가 있으므로 LibreOffice 대신 PowerPoint COM(`Presentation.Export`, `Slide.Export`, `ExportAsFixedFormat`)으로 렌더링하면 실제 발표 환경과 같은 글꼴 · 줄바꿈으로 검수할 수 있다 [S 17].

넷째, **"편집 가능한 .pptx" 라는 말을 믿지 말고 열어서 확인해야 한다.** NotebookLM 슬라이드(이미지 모델로 그림), Marp 기본 출력, Slidev 기본 출력은 슬라이드 전체가 그림이다 [S 22][S 23][S 24]. Gamma · Canva · Beautiful.ai · 망고보드는 내보내기에서 일부 요소(차트, 효과 걸린 텍스트, 그룹 안 텍스트)가 그림으로 바뀐다 [S 7][S 10][S 12][S 14].

다섯째, 여러 실무 글이 공통으로 **"구성안(스토리라인)을 먼저 세우고 슬라이드는 나중에"** 를 권한다. Copilot 자체도 대상 청중을 묻고 개요를 먼저 만든 뒤 슬라이드를 만든다 [S 4]. 국내 실무 후기는 "기초가 되는 PPT 구성안이 정교하게 짜여지지 않으면 제대로된 결과물을 얻기가 힘들다" 고 적었다 [S 27].

## 1. 도구별 정리

### 1.1 Anthropic Claude 계열

Claude 로 슬라이드를 만드는 길은 2026-09 현재 다섯 갈래다.

**(a) Claude.ai 파일 생성(코드 실행).** Free, Pro, Max, Team, Enterprise 전 요금제에서 코드 실행과 파일 생성이 가능하고, 샌드박스에서 코드를 돌려 .pptx 를 만든다. 파일당 최대 30MB [S 3]. 도움말은 외부 파일 · 웹사이트에 숨긴 지시로 데이터 유출이나 악성 코드 실행이 유도될 수 있다고 경고한다 [S 3].

**(b) Anthropic 공식 pptx 스킬(github.com/anthropics/skills).** Claude.ai 파일 생성과 Claude Code 가 쓰는 스킬의 원문이다. 상세 요약은 4 절에 따로 둔다. SKILL.md 최종 수정 커밋은 2026-07-17 (#1447, ".potx 템플릿 지원, pack/unpack 을 zip/unzip 으로 대체, 샌드박스에서 LibreOffice 프로필을 호출마다 새로 준비") 이다 [S 1]. 이전 판(2026-02-04 커밋 #330)은 "html2pptx 를 tgz 로 묶음" 이라고 적혀 있었으나 현재 SKILL.md 에는 html2pptx 가 없고 새 덱은 pptxgenjs 로 만든다 [S 1]. 인터넷의 옛 해설 글이 html2pptx 흐름을 설명하면 옛 판 기준이다.

**(c) Claude for PowerPoint(Office 추가 기능).** Pro, Max, Team, Enterprise 에 정식 제공 [S 2]. 슬라이드 마스터 · 레이아웃 · 글꼴 · 색 구성을 읽어 그 템플릿으로 슬라이드를 만들고, 선택한 슬라이드만 고치며, 글머리표를 다이어그램이나 "editable native PowerPoint charts" 로 바꾼다고 적혀 있다 [S 2]. 한계로 "Final client deliverables without human review" 에는 권하지 않으며, 외부 템플릿 · 공급업체 파일에 프롬프트 주입 위험이 있다고 경고한다 [S 2]. 대화 기록은 브라우저 IndexedDB 에 로컬 저장되고, 입력 · 출력은 백엔드에서 30 일 안에 삭제된다고 적혀 있다 [S 2]. 지원 빌드 문제는 0 절 참조.

**(d) Claude Design(Anthropic Labs).** 2026-04-17 연구 미리보기로 출시, Pro · Max · Team · Enterprise 대상 [S 18]. 코드베이스와 디자인 파일을 읽어 디자인 시스템(색, 서체, 컴포넌트)을 만들고, 결과를 PDF, PPTX, 단독 HTML, Canva 로 내보낸다 [S 18]. TechCrunch 는 "Canva 로 보내면 완전히 편집 가능" 하다고 Anthropic 이 말했다고 보도했다 [S 19]. **PPTX 내보내기가 텍스트 상자 단위로 편집 가능한지는 공식 문서에서 확인하지 못했다** [판정보류]. 확인 방법: 짧은 덱 하나를 PPTX 로 받아 PowerPoint 에서 텍스트 선택이 되는지 본다.

**(e) Claude Slides.** 2026-09-16 발표. "You can edit directly, present straight from Claude, or download as PowerPoint or PDF", "All three are in beta on paid plans", Pro · Max 부터 수 주에 걸쳐 배포 [S 20]. 출시 6 일째라 실사용 후기는 찾지 못했다. PPTX 편집성은 [판정보류].

**연구 근거.** Leinonen, Zhang, Hellas (arXiv 2605.13532, 2026-05-13 제출)는 강의 노트로 NotebookLM, Claude, M365 Copilot, Cursor, Claude Code 가 만든 슬라이드를 비교했고, 코딩 보조 도구(Cursor, Claude Code)가 가장 정확하고 교육적으로 타당한 슬라이드를 만들었으며 학생들은 AI 생성 슬라이드를 강사 제작물과 비슷한 품질로 평가하고 구별하지 못했다고 보고했다 [S 21]. 초록 요약 기반이며 본문 수치는 확인하지 않았다.

### 1.2 Microsoft Copilot in PowerPoint

기능: 프롬프트로 새 발표 만들기, Word 파일(업무용 Copilot 은 PDF · 암호화 문서 포함)에서 발표 만들기, 기관 템플릿 · Organization Asset Library 활용 [S 4][S 5][S 6]. 새 발표를 만들 때 대상 청중, 발표 · 이미지 스타일을 묻고 개요를 먼저 만든 뒤 대화로 개요를 다듬고 나서 슬라이드를 만든다 [S 4]. "Starting with a template will let Copilot know that you'd like to retain the presentation's theme and design" [S 4]. 파일 참조로 만들 때는 같은 프롬프트에 추가 맥락을 넣을 수 없고 파일은 한 번에 하나다 [S 6].

한계: 품질은 영어에서 가장 높고 다른 언어는 점차 개선 예정, Designer 제안은 en-US 만 공식 지원, Rewrite 는 도형이 아닌 텍스트 상자에서만 동작 [S 5]. 한국어는 2024 년에 추가된 16 개 언어에 포함되어 있다 [S 26]. 출력은 PowerPoint 네이티브이므로 편집 가능하다.

비용: Microsoft 365 구독과 Copilot 권한 필요. Office 2024 영구판에는 없음 [S 5][S 16].

### 1.3 Gamma

형식: 웹 기반 카드형 문서. PDF, PNG, PPTX, Google Slides(업로드) 내보내기 [S 7]. 표는 편집 가능 상태로 나가지만 "PowerPoint does not support rounded corners on tables" 라서 모서리가 각지게 나간다 [S 7]. 내보내기는 편집 모드가 아닌 발표 모드 기준이다 [S 7].

공식 도움말이 인정한 내보내기 불일치 원인: Zoom to fit 설정, 차트 · 다이어그램 크기 어긋남(다시 내보내기로 해결), Google Slides 가 내장 글꼴을 무시하고 대체, 큰 이미지가 많으면 이미지 누락(압축 권고) [S 8].

요금: gamma.app/pricing 은 403 으로 직접 확인하지 못했다. 2 차 자료에 따르면 Free(1 회성 400 크레딧, 내보내기에 "Made by Gamma" 배지), Plus, Pro, Ultra [S 7][S 9]. 무료 요금제 배지는 공식 도움말로 확인됨 [S 7]. 가격 수치는 [판정보류].

### 1.4 Canva (Magic Design)

Canva 도움말 페이지는 403 으로 원문 확인을 못 했다. 2 차 자료에 따르면 PPTX, PDF, MP4 로 내보내며, 대부분의 텍스트는 편집 가능하나 일부 글꼴과 효과가 그림으로 평면화되고, Canva 에서 만든 차트는 Excel 연결 차트가 아닌 그룹 그래픽으로 나가는 경우가 많아 PowerPoint 에서 네이티브 차트를 새로 넣으라는 조언이 있다 [S 10]. 모두 [추정] 등급(비공식 출처). Claude Design 결과를 Canva 로 보낼 수 있다 [S 18].

### 1.5 Beautiful.ai

공식 블로그(2026-08-17)는 PPT 로 내보내면 오디오와 애니메이션이 옮겨지지 않으며 "for the best experience from beginning to end we recommend designing and presenting in Beautiful.ai" 라고 스스로 적었다 [S 11]. 2 차 자료는 차트가 정적 이미지로 나가고 일부 그래픽이 평면화된다고 보고하나 [S 12] 경쟁사 글이므로 [추정]. PPT 가져오기 · 내보내기는 Pro 이상이라는 2 차 자료가 있다 [S 12] [판정보류].

### 1.6 Napkin AI (다이어그램 전용)

글을 붙이면 다이어그램 · 인포그래픽을 만든다. 공식 블로그는 PPT 로 내보내면 "change fonts, tweak colors, resize elements, add animations" 가 가능하다고 적었다(게시일 미확인) [S 13]. 2 차 자료에 따르면 무료는 PNG · PDF, PPT · SVG 내보내기는 Plus 이상 [S 13 참고 2 차] [판정보류]. 연구 발표에서 개념도 · 흐름도를 만든 뒤 PowerPoint 에서 다듬는 용도로 쓸 수 있다 [추정].

### 1.7 Google Slides Gemini / Gemini 앱 / NotebookLM

Google Slides 안에서 Gemini 로 여러 장짜리 발표를 한 번에 생성하는 기능은 2026-06-30 발표, 출시 당시 영어(미국)만, Business · Enterprise Standard/Plus, Google AI Pro/Ultra 대상 [S 25]. 결과는 Slides 네이티브라 편집 가능하고 Slides 에서 PPTX 로 받을 수 있다(PPTX 변환 품질은 [판정보류]). 2025-10 에는 Gemini 앱 Canvas 에서 슬라이드를 만들어 Google Slides 로 내보내는 기능이 나왔다 [S 25 검색 결과, workspaceupdates 2025-10].

NotebookLM Slide Decks 는 Nano Banana Pro 이미지 모델로 만든다(공식 블로그 2025-12-16) [S 22]. 2 차 자료에 따르면 PPTX 로 내보내도 슬라이드마다 그림 한 장이라 텍스트 편집이 안 된다 [S 22 참고 2 차] [추정]. 국내 비교 글도 NotebookLM 의 PPT 편집성을 "불가", 한글을 "약간 깨짐" 으로 평가했다 [S 28].

### 1.8 Presenton (오픈소스)

GitHub presenton/presenton, Apache-2.0, 별 10,677 개, 마지막 push 2026-09-21 (GitHub API 조회, 2026-09-22) [S 15]. 자체 호스팅(Docker) 또는 데스크톱 앱, Ollama · OpenAI · Gemini · Anthropic 등 여러 모델 공급자, 기존 PPTX 로 템플릿 만들기, "Fully editable PPTX export" 를 내세운다 [S 15]. 템플릿은 HTML · Tailwind 로 만든다고 README 에 적혀 있다 [S 15]. 발주처 자료를 외부 SaaS 에 올리지 못하는 경우 로컬 모델로 돌릴 수 있다는 점이 장점이다 [추정]. 한글 글꼴 처리 품질은 확인하지 않았다 [판정보류].

### 1.9 Genspark / Manus

Genspark: 공식 문서 페이지가 403 이라 원문 확인 실패. 2 차 자료는 편집 가능한 PPTX, 네이티브 차트, 2025-12 부터 PPTX 를 템플릿으로 가져오기 가능하다고 적었고, 경쟁사 리뷰는 내보내기 충실도와 디자인이 약점이라고 평가했다 [S 29] [추정]. 국내 비교 글은 한글 "양호", 편집성 "중간" [S 28].

Manus: 공식 블로그에 따르면 Nano Banana Pro 로 슬라이드를 통째로 그림으로 만든 뒤 점 찍어 고치는 편집 기능을 추가했다(게시일 "Thursday, December 18", 연도 미표기) [S 30]. PPTX 내보내기가 텍스트 네이티브인지 그림인지는 원문에서 확인하지 못했다 [판정보류].

### 1.10 국내 도구

**미리캔버스.** 주제만 넣으면 구성부터 디자인까지 만든다. 무료는 월 5 회, 최대 30 쪽, Pro 는 무제한. PDF, PNG, JPG, PPTX, MP4, GIF. 입력 텍스트와 업로드 자료를 AI 학습에 쓰지 않는다고 명시 [S 31]. PPT 다운로드 옵션이 "텍스트 편집 가능 / 개별 요소 이미지화 / 통이미지" 세 가지라는 설명이 검색 결과에 있으나 헬프센터 원문은 403 으로 직접 확인하지 못했다 [S 31 참고] [추정]. 국내 비교 글은 한글 품질 "최고" 로 평가 [S 28].

**망고보드.** "편집 가능한 텍스트로 PPTX 다운로드" 가이드 원문: 그룹 안 텍스트, 표 안 텍스트, 모션 · 세로쓰기 · 그림자 · 윤곽선 효과가 걸린 텍스트, 그라데이션 · 링크가 있는 텍스트는 편집 불가(그림)로 저장되며, 옵션을 고르지 않으면 모든 텍스트가 그림으로 변환된다 [S 14]. 슬라이드 노트도 PPTX 에 포함 가능 [S 14 관련 가이드 364]. AI 슬라이드 생성 기능 자체의 공식 설명은 찾지 못했다 [판정보류].

**한컴(한쇼).** 한컴오피스 구독형에 AI 기능이 있다는 일반 설명만 찾았고, 한쇼에서 AI 가 발표를 생성하는 기능의 공식 문서는 찾지 못했다 [판정보류]. 확인 방법: hancom.com 제품 페이지와 한컴 어시스턴트 도움말을 직접 연다.

### 1.11 도구 대조표

| 도구 | PPTX 편집성(원문 근거) | 이 사용자 환경 적합성 |
|---|---|---|
| Claude Code + 공식 pptx 스킬 / python-pptx | 네이티브, 템플릿 유지 가능 [S 1] | 높음. 로컬 · 템플릿 · 검수 자동화 |
| Claude for PowerPoint | 네이티브, 네이티브 차트 [S 2] | M365 구독 빌드 필요, Office 2024 영구판 [판정보류] |
| Claude Design / Slides | PPTX 내보내기 있음, 편집 수준 [판정보류] [S 18][S 20] | 초안 · 디자인 탐색용 |
| Copilot in PowerPoint | 네이티브 [S 4] | Office 2024 영구판에 없음 [S 16] |
| Gamma | 대체로 편집 가능, 레이아웃 어긋남 인정 [S 7][S 8] | 초안용, 발주처 자료 업로드 주의 |
| Canva | 일부 평면화, 차트는 그림 [S 10] [추정] | 디자인 소재용 |
| Beautiful.ai | 애니메이션 · 오디오 손실 [S 11] | 낮음 |
| Napkin AI | 도형 편집 가능 [S 13] | 개념도용 |
| NotebookLM | 슬라이드 전체가 그림 [S 22] [추정] | 요약 확인용, 납품 불가 |
| Presenton | 편집 가능 주장 [S 15] | 로컬 모델 필요 시 후보 |
| 미리캔버스 · 망고보드 | 옵션 따라 텍스트 편집 가능, 효과 텍스트는 그림 [S 14][S 31] | 한글 디자인 소재 |

## 2. 실무 흐름

### 2.1 구성안 먼저, 슬라이드는 나중에

Copilot 은 청중 · 스타일을 묻고 개요를 먼저 만들며 개요를 대화로 고친 뒤 슬라이드를 만든다 [S 4]. Claude 로 슬라이드를 만드는 방법을 정리한 글(2026-02-22)은 자료 업로드, 개요 요청, 구조 다듬기, 디자인 지정과 함께 생성, 슬라이드별 반복을 권하고, "Claude produces the best slide content of any AI tool" 이지만 "Design is functional, not beautiful", 20 장이 넘으면 일관성이 떨어진다고 적었다 [S 32]. 국내 브런치 후기(2026-05-03)는 1 장 시범으로 스타일을 검증한 뒤 Claude Project 의 지침에 디자인 프롬프트, 지식에 로고 · 글꼴을 두고, 10 장이 넘으면 작동이 불량해지고 Pro 요금제로 20 장에서 사용 한도에 닿았으므로 10 장씩 나눠 만들라고 권했다 [S 27]. 국내 8 개 도구 비교(2026-03-19)는 "중요한 건 도구 자체보다 프롬프트를 얼마나 잘 쓰느냐" 라고 결론지었다 [S 28].

Claude for PowerPoint 공식 문서의 권장도 같은 방향이다. "Start with your template already applied before asking Claude to generate content", 요청은 구체적으로, 결과는 반드시 검토 [S 2]. 예시 프롬프트도 "Simplify the text on slide 3, it's too dense", "Reorder slides to lead with recommendations first" 처럼 한 장 또는 한 구간 단위다 [S 2].

### 2.2 템플릿에 채우기 vs 처음부터 생성

공식 pptx 스킬은 둘을 명확히 나눈다. 새 덱은 pptxgenjs 스크립트로 처음부터, 기존 덱 · 템플릿은 압축 해제 후 `ppt/slides/slideN.xml` 을 고치고 다시 압축한다 [S 1]. 템플릿 흐름에서는 `thumbnail.py` 로 레이아웃 그리드를 보고 `markitdown` 으로 내용을 읽어 내용 구간마다 템플릿 슬라이드를 대응시키며, 모든 구간을 같은 제목 + 글머리표 슬라이드에 넣지 말라고 한다 [S 1]. "Template slots ≠ source items" : 템플릿 칸이 4 개인데 내용이 3 개면 네 번째 묶음(그림 + 텍스트 상자) 전체를 지우라고 한다 [S 1].

python-pptx 로 템플릿을 채울 때의 스킬 경고 세 가지: 슬라이드 복제 기능이 없다(`add_slide(layout)` 뿐), `text_frame.text = "..."` 는 문단을 서식 없는 한 run 으로 뭉개므로 `run.text` 에 넣어야 한다, 템플릿 그림에 흔한 SVG/EMF 를 `add_picture` 가 읽지 못한다 [S 1]. python-pptx 공식 문서는 자리표시자(placeholder)를 `idx` 로 찾아 채우는 방식을 설명한다 [S 33].

Quarto(pandoc) 로 Markdown 에서 PPTX 를 만들면 `reference-doc` 템플릿을 쓸 수 있으나 템플릿에 "Title Slide, Title and Content, Section Header, Two Content, Comparison, Content with Caption, and Blank" 레이아웃이 있어야 하고, 레이아웃은 내용에 따라 자동 선택되며 수동 지정은 아직 안 된다 [S 34]. 기본 템플릿은 `quarto pandoc -o template.pptx --print-default-data-file reference.pptx` 로 받는다 [S 34].

### 2.3 Markdown 기반 경로(Marp, Slidev, reveal.js)

Marp 기본 PPTX 는 "pre-rendered slide images" 라서 편집이 안 된다. 관리자는 디자인 재현성을 우선했다고 설명한다 [S 23]. Marp CLI v4.1.0 의 `--pptx-editable` 은 PDF 로 렌더한 뒤 LibreOffice Impress 로 가져오는 실험 기능이며 "Some slides may throw an error or output the incomplete result" [S 23].

Slidev 기본 PPTX 도 "all the slides in the PPTX file will be exported as images" 이다. `pptx-editable` 형식은 브라우저에서 잰 뒤 PowerPoint 도형으로 다시 짓지만 SVG(Mermaid, 아이콘), canvas, KaTeX 수식, CSS 그라데이션 등은 그림으로 남고, 글꼴은 내장되지 않으며 줄바꿈이 브라우저와 다를 수 있다 [S 24].

Claude 스킬 가운데 frontend-slides 는 .pptx 대신 브라우저에서 실행되는 단일 HTML 을 만든다(세일즈클루 블로그 2026-03-20) [S 35]. 발표 현장에서 PowerPoint 파일을 요구하는 학회 · 발주처 보고에는 맞지 않는다 [추정].

결론적으로 **발주처나 공동저자가 PowerPoint 에서 고쳐야 하는 자료라면 Markdown 경로는 편집성에서 불리하고, 수식이 많은 연구 발표에서는 수식이 그림으로 남는다** [S 23][S 24].

### 2.4 차트와 데이터

공식 pptx 스킬: PowerPoint 가 그릴 수 있는 차트는 `addChart()` 로 네이티브로 넣고, 추세선 · 오차막대처럼 라이브러리가 노출하지 않는 기능도 그림으로 대체하지 말고 계열을 직접 계산하거나 OOXML 을 후처리하라. Sankey, 네트워크, chord 처럼 PowerPoint 에 없는 형식만 그림으로 넣는다 [S 1]. 기본 차트는 제목 · 데이터 레이블 없이 밋밋하게 나오므로 옵션을 켜라고 한다 [S 1]. 누적 막대에 `dataLabelPosition: outEnd` 를 주거나 보조축 콤보 차트에 `valAxes`, `catAxes` 를 두 개씩 주지 않으면 PowerPoint 가 파일을 손상으로 본다 [S 1].

Claude for PowerPoint 는 네이티브 차트를 만든다고 적혀 있다 [S 2]. Canva 차트는 그룹 그래픽으로 나가는 경우가 많다는 2 차 보고가 있다 [S 10] [추정].

수문 연구자에게는 matplotlib 으로 그린 그림을 인쇄 크기 그대로 넣는 방식과 네이티브 차트 방식이 갈린다. 공동 편집자가 값을 고쳐야 하면 네이티브, 논문 그림과 동일해야 하면 그림이 낫다 [추정].

### 2.5 이미지 생성과 라이선스

Copilot FAQ 는 생성 콘텐츠가 "sometimes will be very similar to existing internet content" 이고 부정확할 수 있다고 적었다 [S 5]. 문화체육관광부 · 한국저작권위원회 "생성형 AI 저작권 안내서" (2023-12-27 발표)의 핵심은 인간의 창작적 기여가 저작권 등록 요건이라는 점이다(2 차 요약 기준) [S 36]. 미리캔버스는 사업 목적 사용은 허용하되 생성 결과를 템플릿으로 재판매하는 것은 금지한다 [S 31]. 망고보드는 다운로드 시 저작권 관련 사항을 따로 확인하라고 적었다 [S 14]. 발주처 보고서에 AI 생성 이미지를 넣을 때는 도구별 약관을 직접 확인해야 한다 [추정].

### 2.6 프롬프트 패턴 (원문에서 확인된 것만)

Claude for PowerPoint 공식 예시: "Create a market sizing section, 3 slides covering TAM, SAM, SOM with supporting visuals", "Add an executive summary slide using the one-column content layout", "Turn these bullets into a process flow diagram", "Restructure the storyline across slides 4 to 7" [S 2]. 지속 지침(Instructions) 칸에 "always use one-line bullets" 같은 규칙을 두라고 한다 [S 2].

Copilot 은 청중 · 스타일 질문에 답하게 한 뒤 개요를 다듬는다 [S 4]. 국내 후기는 유명 브랜드 디자인 시스템 프롬프트(getdesign.md)를 복사해 글꼴 · 로고 · 비율을 바꿔 쓰는 방식을 소개했다 [S 27]. 브랜드 모방 프롬프트는 상표 · 디자인권 문제를 검토해야 한다 [추정].

## 3. 알려진 실패 유형과 대응

### 3.1 텍스트 넘침 · 과다

공식 pptx 스킬은 시각 검수에서 **텍스트 넘침 또는 상자 · 슬라이드 경계에서 잘림을 가장 먼저 보라** 고 하며 "It is the most common defect and always user-visible" 이라고 적었다 [S 1]. 대응: 글꼴 크기 축소, 여러 장으로 나누기, 상자 확대. 잘린 채 내보내지 말 것 [S 1]. 연구자 블로그(Leon Furze, 2026-07-26)와 여러 실무 글도 텍스트 과다를 AI 덱의 가장 뚜렷한 흔적으로 든다 [S 37].

### 3.2 뻔한 디자인

공식 pptx 스킬의 "Avoid" 목록: 같은 레이아웃 반복, 본문 가운데 정렬, 기본 파랑, 텍스트만 있는 슬라이드, 제목 아래 강조선("these are a hallmark of AI-generated slides"), 슬라이드 폭 머리 · 바닥 띠나 카드 한쪽 테두리 같은 장식 띠("These read as AI-generated filler"), 크림 · 베이지 배경, 저대비 [S 1]. 권장: 주제에 맞춘 팔레트에서 한 색이 60-70 % 시각 비중, 제목 36-44pt, 본문 14-16pt, 여백 0.5 인치 이상, 블록 간격 0.3-0.5 인치 [S 1].

Leon Furze 는 환각 외에도 섹션 제목에 해석성 부제를 붙이는 습관(예 "Assessment" 를 "Assessment: rethinking what we value and why it matters" 로) 같은 문체상 흔적을 지적했다 [S 37].

### 3.3 숫자 환각

실무 글들이 성장률 · 시장 규모 같은 수치를 지어내 차트까지 그리는 사례를 경고하고 모든 수치를 출처와 대조하라고 권한다 [S 37]. Copilot FAQ 도 생성 콘텐츠가 부정확 · 오해 소지가 있을 수 있다고 적었다 [S 5]. Claude for PowerPoint 는 사람 검토 없는 최종 납품을 권하지 않는다 [S 2]. 대응 [추정]: 수치는 AI 가 생성하지 말고 원자료 CSV 에서 코드로 읽어 넣으며, 슬라이드마다 수치 출처를 발표자 노트에 남긴다.

### 3.4 PowerPoint 에서 열 때 손상 · 깨짐

공식 pptx 스킬이 실측으로 적은 손상 원인: 색상 hex 에 `#` 을 붙이거나 8 자리(알파 포함)로 쓰기, 그림자 offset 음수, 옵션 객체를 두 번 재사용(pptxgenjs 가 내부에서 값을 바꿈), 누적 막대 `outEnd` 레이블, 보조축 콤보 차트 축 선언 누락, `<p:presentation>` 자식 순서 바꾸기 [S 1]. 특히 "pptxgenjs emits chart XML PowerPoint refuses to open, and every other tool accepts: python-pptx opens those decks, LibreOffice renders them, the XSD passes them" 라고 적었다. 즉 **LibreOffice 로 렌더가 잘 돼도 PowerPoint 에서 안 열릴 수 있다** [S 1]. XML 을 스크립트로 고칠 때 `xml.etree.ElementTree` 로 왕복하면 네임스페이스 접두어가 바뀌어 덱이 손상되니 `defusedxml.minidom` 을 쓰라고 한다 [S 1]. 슬라이드 파일을 손으로 복사하지 말고 `add_slide.py` 를 쓰며, 복제한 슬라이드는 원본의 차트 파트를 공유하므로 한쪽 차트를 고치면 다른 쪽도 바뀐다 [S 1].

### 3.5 글꼴(한글 포함)

공식 pptx 스킬: pptx 에 적은 글꼴은 사용자의 PowerPoint 가 그리는데, 검수용 LibreOffice 는 없는 글꼴을 폭이 다른 글꼴로 대체하므로 검수 이미지의 넘침 여부가 실제와 다를 수 있다. 안전 글꼴은 Arial, Calibri, Cambria, Times New Roman, Courier New, Bookman Old Style, Century Schoolbook. Georgia, Trebuchet MS, Garamond, Consolas 등은 검수 신뢰도가 낮으니 10 % 여유를 두라. Aptos 는 기본값으로 쓰지 말라 [S 1]. **이 목록에 한글 글꼴은 없다.** 맑은 고딕 등 한글 글꼴은 스킬이 검증 대상으로 다루지 않는다 [S 1 기준 판단].

LibreOffice 쪽 대체 글꼴 문제는 별도 오픈소스 이슈에서도 "a substituted font is silent" 라서 대체로 인한 줄바꿈 증가가 레이아웃 결함과 구별되지 않는다고 기록되어 있다 [S 38].

python-pptx 의 `font.name` 은 라틴 문자에만 적용되고 한중일 문자에는 적용되지 않는다는 이슈가 있다(scanny/python-pptx #768, 2021-11-12) [S 39]. 원인은 동아시아 글꼴이 `<a:ea>` 요소로 따로 지정되기 때문이며 [S 40], 이를 고치는 커뮤니티 도구로 pptx-ea-font, pptx-tool 이 있다 [S 40]. 대응 [추정]: 한글 글꼴은 run 의 `rPr` 에 `a:latin` 과 함께 `a:ea` 를 직접 넣거나, 템플릿 테마 글꼴(주 · 보조 글꼴의 동아시아 지정)을 맞춰 두고 코드에서는 글꼴을 지정하지 않는다.

Gamma 도움말은 Google Slides 가 PPTX 에 내장된 글꼴을 무시한다고 적었다 [S 8]. Slidev `pptx-editable` 은 글꼴을 내장하지 않는다 [S 24]. PowerPoint 의 `ExportAsFixedFormat` 에는 라이선스상 내장이 안 되는 글꼴을 비트맵으로 넣는 `BitmapMissingFonts` 인자가 있다 [S 17].

### 3.6 편집 불가 출력

슬라이드 전체가 그림인 경우: NotebookLM [S 22] [추정], Marp 기본 [S 23], Slidev 기본 [S 24], 망고보드 옵션 미선택 시 [S 14]. 일부만 그림: Slidev editable 의 SVG · 수식 [S 24], 망고보드 효과 텍스트 [S 14], Canva 차트 [S 10] [추정], Beautiful.ai 차트 [S 12] [추정]. 확인법 [추정]: 받은 파일을 `markitdown` 으로 텍스트를 뽑아 슬라이드별 글자 수가 0 인지 보거나 [S 1 의 markitdown 사용], python-pptx 로 슬라이드별 그림 도형 비율을 센다.

### 3.7 템플릿 잔재

공식 pptx 스킬은 템플릿 사용 시 남은 자리표시자 문구를 grep 으로 찾게 한다. `markitdown output.pptx | grep -iE "\bx{3,}\b|lorem|ipsum|\bTODO|\[insert|this.*(page|slide).*layout"` 결과가 있으면 성공이라고 말하기 전에 고치라고 한다 [S 1]. 제목이 두 줄로 늘어나면 한 줄 기준으로 놓인 장식선이 어긋나는 것도 검수 항목이다 [S 1].

## 4. Anthropic 공식 pptx 스킬 SKILL.md 요약 (원문 대조)

출처: https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md, 2026-09-22 에 raw 파일 238 줄을 내려받아 읽음. 최종 커밋 2026-07-17 [S 1]. 폴더 구성은 SKILL.md, LICENSE.txt, scripts/ 이다. 라이선스 표기는 "Proprietary" 이다.

**작업 선택.** .pptx 는 XML 묶음 ZIP 이다. 새 덱은 pptxgenjs 스크립트, 기존 덱 · 템플릿 편집은 압축 해제, `ppt/slides/slideN.xml` 편집, 재압축. 읽기는 `markitdown deck.pptx`, 시각 그리드는 `python scripts/thumbnail.py deck.pptx`.

**스크립트.** `thumbnail.py`(템플릿 레이아웃 고르기용 라벨 그리드. 두 번째 인자로 덱 이름을 주지 않으면 기본 `thumbnails` 로 다른 덱의 그리드를 덮어씀. 12 장 넘으면 여러 파일로 나뉨. 시각 검수용 아님), `add_slide.py`(슬라이드 · 레이아웃 복제와 패키지 등록. `-o` 를 안 주면 입력 파일을 덮어씀), `clean.py`(참조 없는 슬라이드 · 미디어 · rels 삭제, `<p:sldIdLst>` 확정 후 실행), `office/validate.py`(스키마, 관계, 콘텐츠 형식, 차트, 슬라이드 검사. 템플릿 기반이면 `--original` 로 템플릿 자체 오류를 기준선 처리), `office/soffice.py`(LibreOffice 래퍼. 샌드박스에서 맨 soffice 는 멈춤).

**편집 순서.** 추가 · 삭제 · 재배열 같은 구조 작업을 모두 끝낸 뒤 내용을 고친다. 압축은 풀린 폴더 안에서 `zip -Xr` 로 하고, 기존 출력 파일을 먼저 지워야 삭제한 파트가 남지 않는다. 목록 항목은 한 항목에 `<a:p>` 하나, 글머리표 문자 `•` 를 직접 쓰지 말고 레이아웃에서 상속, 앞뒤 공백이 있는 텍스트는 `xml:space="preserve"`.

**디자인 지침.** 3.2 절 참조. 팔레트 예시 10 종(예 "Ocean Gradient" 065A82 / 1C7293 / 21295C, "Forest & Moss" 2C5F2D / 97BC62 / F5F5F5)을 표로 제시한다.

**QA (Required).** "Your first render usually has a few real issues ... Find and fix those, re-render only the slides you changed, and stop." 세 단계로 되어 있다.

(1) 내용 QA: `markitdown output.pptx` 로 누락 · 오탈자 · 순서 확인, 템플릿이면 위 grep 으로 자리표시자 잔재 확인.

(2) 파일 QA(필수): `python scripts/office/validate.py output.pptx` (처음부터 만든 덱), `--original src.pptx` (템플릿 기반). 관계 · 콘텐츠 형식 · 차트 같은 구조 검사는 `--original` 과 무관하게 보고된다. 실패마다 고칠 방법을 알려 주며, 포장된 XML 을 손으로 고치지 말고 생성기에서 고쳐 다시 만들라고 한다.

(3) 시각 QA: 슬라이드를 이미지로 바꿔 모든 장을 본다. "After staring at the generating code you tend to see what you expect rather than what rendered, so look at the images fresh (a subagent works well for this if you have one)". 점검 목록: 텍스트 넘침 · 잘림(가장 먼저), 요소 겹침, 출처 · 바닥글이 위 내용과 충돌, 간격 0.3 인치 미만, 고르지 않은 간격, 가장자리 여백 0.5 인치 미만, 열 정렬 불일치, 저대비 텍스트 · 아이콘, 텍스트 교체 후 어긋난 템플릿 장식, 너무 좁아 과도하게 줄바꿈되는 상자, 남은 자리표시자.

**이미지 변환 명령(원문 그대로).**

```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
rm -f slide-*.jpg
pdftoppm -jpeg -r 150 output.pdf slide
ls -1 "$PWD"/slide-*.jpg
```

pdftoppm 은 쪽수에 따라 0 을 채운다(10 장 미만 `slide-1.jpg`, 10-99 장 `slide-01.jpg`, 100 장 이상 `slide-001.jpg`). 고친 뒤에는 네 명령을 모두 다시 돌려야 한다. PDF 를 다시 만들지 않으면 이미지에 수정이 반영되지 않는다.

**의존성.** pptxgenjs(npm), markitdown[pptx], Pillow, defusedxml, lxml(pip), LibreOffice, pdftoppm(Poppler).

**이 사용자 환경에 옮길 때의 차이 [추정].** 스킬은 Linux 샌드박스를 전제로 LibreOffice 로 렌더한다. 이 사용자는 Windows 에 PowerPoint 가 있으므로 `win32com` 으로 `Presentation.Export(Path, "png", ScaleWidth, ScaleHeight)` 또는 `ExportAsFixedFormat` 으로 PDF 를 만든 뒤 이미지화하면 한글 글꼴 대체 문제 없이 실제 모습으로 검수할 수 있다 [S 17]. 다만 PowerPoint COM 은 한 번에 한 인스턴스라 병렬 렌더에 불리하다는 점은 확인하지 않았다 [판정보류]. validate.py 와 markitdown 검사는 그대로 쓸 수 있다.

## 5. 확인하지 못한 것

gamma.app/pricing, Canva 도움말, 미리캔버스 헬프센터, Genspark 문서, wikidocs 클로드 코드 가이드, Medium Copilot 후기는 403 으로 원문을 열지 못했다. 해당 항목은 2 차 자료 기반이며 [추정] 또는 [판정보류] 로 표시했다. 한컴 AI 의 슬라이드 생성 기능은 공식 근거를 찾지 못했다. Claude Design · Claude Slides 의 PPTX 가 텍스트 단위로 편집되는지, Office 2024 영구판에서 Claude for PowerPoint 가 설치되는지는 직접 시험으로만 확인할 수 있다. 요즘IT · velog 에서 이 주제의 구체 실무 글은 찾지 못했다.

## 출처

- [S 1] anthropics/skills, skills/pptx/SKILL.md. https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md (raw 파일 2026-09-22 조회, 최종 커밋 2026-07-17 #1447, 이전 커밋 2026-02-04 #330)
- [S 2] Claude Docs, "Use Claude for PowerPoint". https://claude.com/docs/office-agents/powerpoint (support.claude.com/en/articles/13521390 에서 이동, 날짜 미확인)
- [S 3] Claude Help Center, "Create and edit files with Claude". https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude (날짜 미확인)
- [S 4] Microsoft Support, "Create a new presentation with Copilot in PowerPoint". https://support.microsoft.com/en-us/powerpoint/copilot/create-a-new-presentation-with-copilot-in-powerpoint (날짜 미확인)
- [S 5] Microsoft Support, "Frequently asked questions about Copilot in PowerPoint". https://support.microsoft.com/en-us/powerpoint/frequently-asked-questions-about-copilot-in-powerpoint (날짜 미확인)
- [S 6] Microsoft Support, "Create a presentation from existing files". https://support.microsoft.com/en-au/topic/create-a-presentation-from-existing-files-beb15deb-3241-4711-a480-9cbd8dc4d755 (검색 요약 기반)
- [S 7] Gamma Help Center, "What's the easiest way to export my Gamma?". https://help.gamma.app/en/articles/8022861-what-s-the-easiest-way-to-export-my-gamma
- [S 8] Gamma Help Center, "Why doesn't my exported PDF or PowerPoint match what I see in Gamma?". https://help.gamma.app/en/articles/15939201
- [S 9] (2 차, 참고) Gamma 요금 정리 글들: https://www.eesel.ai/blog/gamma-pricing , https://flowith.io/blog/gamma-app-pricing-2026-free-vs-plus-vs-pro/
- [S 10] (2 차, 참고) https://www.buildfastwithai.com/ai-tools/canva-magic-design , https://pptproductivity.com/blog/how-to-create-a-canva-presentation-and-edit-in-powerpoint
- [S 11] Beautiful.ai 블로그, "How to Export to PPT ... and why you shouldn't" (2026-08-17). https://www.beautiful.ai/blog/how-to-export-to-ppt-and-why-you-shouldnt
- [S 12] (2 차, 경쟁사 글) https://www.presentations.ai/blog/beautiful-ai-review , https://deckary.com/blog/beautiful-ai-review
- [S 13] Napkin AI 블로그, "PPT Export & File Import". https://www.napkin.ai/blog/napkin-launches-ppt-export-files-import/ (날짜 미확인). 요금은 2 차 https://www.therundown.ai/tools/napkin-ai
- [S 14] 망고보드 가이드 363 "편집 가능한 텍스트로 파워포인트 파일(PPTX) 다운로드". https://www.mangoboard.net/guide/363 . 관련 가이드 364(슬라이드 노트) https://www.mangoboard.net/guide/364
- [S 15] presenton/presenton GitHub README 및 API(2026-09-22 조회). https://github.com/presenton/presenton
- [S 16] Microsoft Q&A, "Is Microsoft copilot included in my purchase of Microsoft Office Home 2024?" (2026-07-06, 자원봉사 Independent Advisor 답변). https://learn.microsoft.com/en-au/answers/questions/5938660
- [S 17] Microsoft Learn, Presentation.Export / Slide.Export / ExportAsFixedFormat (PowerPoint VBA). https://learn.microsoft.com/office/vba/api/powerpoint.presentation.export , https://learn.microsoft.com/office/vba/api/powerpoint.slide.export , https://learn.microsoft.com/office/vba/api/powerpoint.presentation.exportasfixedformat
- [S 18] Anthropic, "Introducing Claude Design by Anthropic Labs" (2026-04-17). https://www.anthropic.com/news/claude-design-anthropic-labs . 보조: Claude Academy https://academy.claude.com/tutorials/using-claude-design-for-presentations-and-slide-decks
- [S 19] TechCrunch (2026-04-17). https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/
- [S 20] Claude 블로그, "Claude Cowork and chat are now one Claude" (2026-09-16). https://claude.com/blog/cowork-is-now-claude . 보조: VentureBeat https://venturebeat.com/technology/anthropic-is-killing-off-cowork-and-folding-it-into-claude-launching-claude-docs-and-claude-slides
- [S 21] Leinonen, Zhang, Hellas, "AI-Generated Slides: Are They Good? Can Students Tell?" arXiv 2605.13532 (2026-05-13). https://arxiv.org/abs/2605.13532
- [S 22] Google 블로그, "8 ways to make the most out of Slide Decks in NotebookLM" (2025-12-16). https://blog.google/technology/google-labs/8-ways-to-make-the-most-out-of-slide-decks-in-notebooklm/ . PPTX 가 그림이라는 내용은 2 차: https://www.androidpolice.com/gemini-feature-fixes-notebooklm-slide-deck-limitation/
- [S 23] marp-team Discussion #82 "Exported PPTX cannot re-edit". https://github.com/orgs/marp-team/discussions/82
- [S 24] Slidev 문서 "Exporting". https://sli.dev/guide/exporting.html
- [S 25] Google Workspace Updates (2026-06-30). https://workspaceupdates.googleblog.com/2026/06/create-fully-native-and-editable-presentations-with-Gemini-in-Google-Slides.html . 2025-10: https://workspaceupdates.googleblog.com/2025/10/generate-presentations-in-gemini-app.html (검색 요약 기반)
- [S 26] Microsoft Tech Community, "New languages supported in Copilot for Microsoft 365". https://techcommunity.microsoft.com/blog/microsoft365copilotblog/new-languages-supported-in-copilot-for-microsoft-365/4126276 (검색 요약 기반)
- [S 27] 브런치 대기만손, "AI, 아니 클로드로 PPT 만들기" (2026-05-03). https://brunch.co.kr/@sonteady/103
- [S 28] 브런치 sukistory, "AI PPT 만들기, 8개 도구 직접 비교해봤습니다" (2026-03-19). https://brunch.co.kr/@sukistory/103
- [S 29] (2 차, 경쟁사 글) https://www.presentations.ai/blog/genspark-review , Genspark changelog https://www.genspark.ai/docs/ai_slides_changelog (원문 403)
- [S 30] Manus 블로그, "Slides Created with Nano Banana Pro Are Now Editable". https://manus.im/blog/edit-slides-created-on-manus-with-nano-banana-pro (게시 "Thursday, December 18", 연도 미표기)
- [S 31] 미리캔버스 "프레젠테이션 AI로 PPT 만들기". https://www.miricanvas.com/features/ko/ai-presentation-maker . 다운로드 옵션은 헬프센터(403) https://help.miricanvas.com/hc/ko/articles/360039561892 의 검색 요약
- [S 32] The AI Corner, Ruben Dominguez, "Every Way to Make Slides with Claude in 2026" (2026-02-22). https://www.the-ai-corner.com/p/every-way-to-make-slides-with-claude
- [S 33] python-pptx 문서 "Working with placeholders". https://python-pptx.readthedocs.io/en/latest/user/placeholders-using.html
- [S 34] Quarto 문서 "PowerPoint". https://quarto.org/docs/presentations/powerpoint.html
- [S 35] 세일즈클루 블로그, frontend-slides (2026-03-20). https://salesclue.io/blog/claude-skill-with-frontend-slides
- [S 36] 문화체육관광부 · 한국저작권위원회 "생성형 AI 저작권 안내서" (2023-12-27) 요약: https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=32443 , https://ditoday.com/gai-copyright/ (2 차)
- [S 37] Leon Furze, "Problem Patterns in AI: Beyond Hallucinations" (2026-07-26). https://leonfurze.com/2026/07/26/problem-patterns-in-ai-beyond-hallucinations/ . 보조(경쟁사): https://www.presentations.ai/blog/common-ai-presentation-mistakes (검색 요약 기반)
- [S 38] openooxml/betteroffice Issue #763 "a substituted font is silent". https://github.com/openooxml/betteroffice/issues/763 (검색 요약 기반)
- [S 39] scanny/python-pptx Issue #768 (2021-11-12). https://github.com/scanny/python-pptx/issues/768
- [S 40] AndersonBY/pptx-ea-font https://github.com/AndersonBY/pptx-ea-font , achimnol/pptx-tool https://github.com/achimnol/pptx-tool , python-pptx 문서 "Font typeface" https://python-pptx.readthedocs.io/en/latest/dev/analysis/txt-font-typeface.html (검색 요약 기반)
