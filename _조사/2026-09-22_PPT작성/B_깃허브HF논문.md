# AI 활용 발표자료(PPT) 생성: GitHub · Hugging Face · 논문 조사

조사일 2026-09-22. 별 수 · 마지막 push · 라이선스는 모두 이날 `gh api repos/OWNER/NAME` 와
`gh search repos` 출력에서 옮겼다. 논문 ID 와 요지는 Hugging Face Papers(`hf://papers/<id>/paper.md`)
초록과 arXiv 검색 결과에서 옮겼다. 별 수는 조사 시점 값이며 하루 단위로 변한다.

## 1. 결론

Windows + Python + 한국어 본문 조건에서 바로 쓸 수 있는 조합은 세 층이다.

첫째, **생성 엔진**은 python-pptx(파이썬, 이미 설치됨) 또는 PptxGenJS(Node)다. Anthropic 의 공식
pptx 스킬은 새로 만들 때 PptxGenJS, 양식 기반 수정 때 XML 직접 편집, 읽을 때 markitdown 을 쓰도록
나누어 놓았다. 둘째, **읽기와 검수**는 microsoft/markitdown(pptx 를 슬라이드별 마크다운으로)과
LibreOffice 렌더링(그림으로 바꿔 눈으로 확인)이다. 셋째, **라이브 편집**이 필요하면 Windows COM
으로 실행 중인 PowerPoint 를 조작하는 MCP 서버(ykuwai/ppt-mcp, Ayushmaniar/powerpoint-mcp)가 있다.

연구 쪽의 일관된 교훈은 세 가지다. (1) 빈 캔버스에서 한 번에 만들기보다 **참조 양식의 슬라이드를
골라 편집하는 방식**이 내용 · 디자인 · 일관성 모두에서 낫다(PPTAgent). (2) 통째로 그림을 생성하기보다
**코드(프로그램)로 슬라이드를 만드는 방식**이 편집 가능성과 품질에서 낫다(AutoPresent). (3) **렌더링한
결과를 다시 보고 고치는 반복 루프**가 넘침(overflow) · 정렬 오류를 줄인다(Paper2Poster, DeepPresenter,
PPTPilot). 반대로 현재 모델들은 의미 이해에 비해 공간 배치 추론이 약하다(PPTBench).

## 2. GitHub 저장소 표

별 수 내림차순이 아니라 용도별로 묶었다. "WPK 적합" 은 Windows · Python · 한국어 흐름 적합도에 대한
조사자 판단이다.

### 2.1 생성 엔진 · 변환 도구 (AI 없이도 쓰는 기반)

| 저장소 | 별 | 마지막 push | 라이선스 | 용도 · 출력 | WPK 적합 |
|---|---|---|---|---|---|
| microsoft/markitdown | 186,214 | 2026-09-21 | MIT | 오피스 문서를 마크다운으로 변환. pptx 읽기용 | 높음. pip 설치, Python |
| hakimel/reveal.js | 72,333 | 2026-09-18 | MIT | HTML 발표 프레임워크. 출력 HTML(PDF 인쇄 가능) | 중간. pptx 가 아님 |
| slidevjs/slidev | 48,784 | 2026-09-16 | MIT | 개발자용 마크다운 슬라이드(Vue). HTML, PDF, pptx(그림 기반) 내보내기 | 중간. Node 필요 |
| jgm/pandoc | 46,369 | 2026-09-21 | GPL-2.0 | 범용 문서 변환. 마크다운에서 pptx 로 변환 가능, 참조 양식(reference-doc) 지정 | 높음. Windows 설치판 있음 |
| marp-team/marp | 12,547 | 2026-07-29 | MIT | 마크다운 발표 생태계 입구 저장소 | 중간 |
| marp-team/marp-cli | 3,827 | 2026-09-08 | MIT | Marp 마크다운을 HTML, PDF, pptx 로 변환 | 중간. pptx 는 기본 그림 기반 [추정], 편집 가능 pptx 는 실험 옵션 [판정보류: `marp --help` 로 확인] |
| gitbrent/PptxGenJS | 6,187 | 2025-11-28 | MIT | JavaScript 로 pptx 생성. 네이티브 차트 지원 | 높음. Anthropic pptx 스킬의 새 문서 생성 엔진 |
| quarto-dev/quarto-cli | 6,013 | 2026-09-21 | NOASSERTION | Pandoc 기반 과학 출판. revealjs, pptx, beamer 출력 | 높음. 수치 결과와 그림을 코드로 엮을 때 |
| scanny/python-pptx | 3,537 | 2024-08-07 | MIT | Python 으로 pptx 생성 · 수정. PyPI 최신 1.0.2(2024-08-07 업로드) | 높음. 이미 설치됨. 다만 2024-08 이후 저장소 push 없음 |

### 2.2 AI 발표자료 생성기 (완결형 앱)

| 저장소 | 별 | 마지막 push | 라이선스 | 용도 · 출력 | WPK 적합 |
|---|---|---|---|---|---|
| presenton/presenton | 10,677 | 2026-09-21 | Apache-2.0 | 자체 호스팅 AI 발표자료 생성기(Gamma 대체). 프롬프트 · 문서 · 자기 pptx 디자인에서 생성, 편집 가능한 pptx · PDF 내보내기. Docker 또는 Windows 데스크톱 앱. Ollama 등 로컬 모델 가능 | 중간. 기본 원격 기능 끄기 필요(3장) |
| allweonedev/presentation-ai | 3,032 | 2026-06-05 | MIT | ALLWEONE 오픈소스 AI 발표 생성기(Next.js). 요청서의 `ALLWEONE/presentation-ai` 는 404, 실제 위치는 이것 | 낮음. 외부 키 여러 개 필요 |
| tonyqinatcmu/SlideBot-AI | 1,215 | 2026-01-31 | MIT | AI 발표 생성기 | [판정보류] README 미확인 |

### 2.3 에이전트 스킬 · 연구 코드

| 저장소 | 별 | 마지막 push | 라이선스 | 용도 · 출력 | WPK 적합 |
|---|---|---|---|---|---|
| anthropics/skills | 177,496 | 2026-09-10 | 저장소 null, pptx 스킬은 Proprietary(LICENSE.txt) | Agent Skills 공개 저장소. `skills/pptx` 는 생성(PptxGenJS) · 양식 편집(XML) · 읽기(markitdown) · 썸네일 · 검증(validate.py) · LibreOffice 변환 스크립트 포함 | 높음. Claude Code 에 이미 `anthropic-skills:pptx` 로 있음 |
| icip-cas/PPTAgent | 5,046 | 2026-09-21 | MIT | PPTAgent(EMNLP 2025) · DeepPresenter(ACL 2026) 구현. 현재 main 은 Claude Code · Codex 용 PPTAgent Skill | 낮음. Skill 요구사항이 Linux(WSL 포함) 또는 macOS. 논문 재현은 v0.2.0 · v1.1.38 태그 |
| Paper2Poster/Paper2Poster | 3,949 | 2026-06-08 | MIT | 논문에서 편집 가능한 pptx 포스터 생성(NeurIPS 2025) | 중간. LLM API 필요 |
| HKUDS/Paper2Slides | 3,833 | 2026-05-20 | MIT | 논문에서 발표자료 원클릭 생성 | 낮음. 이미지 생성 API 키 필요(3장) |
| llmsresearch/paperbanana | 2,376 | 2026-09-17 | [판정보류] | Google PaperBanana 오픈 구현. 학술 그림 자동 생성 | 발표 그림 보조용 |
| CRui5in/paper-ppt-agent | 1,063 | 2026-08-19 | AGPL-3.0 | 논문 PDF · LaTeX 에서 편집 가능한 PPT 생성 | 중간. AGPL 전파 조건 주의 |
| LearnPrompt/humanize-ppt | 947 | 2026-07-31 | NOASSERTION | AST 기반 개요(outline) 연출 도구 | [판정보류] |
| sunbigfly/ppt-agent-skills | 899 | 2026-06-08 | NOASSERTION | 코드 주도 발표자료 생성 프레임워크(중국어권) | [판정보류] |
| para-lost/AutoPresent | 180 | 2025-05-26 | MIT | AutoPresent(CVPR 2025) 코드 · SlidesBench | 연구 참고용 |
| nusnlp/SlideTailor | 60 | 2026-04-18 | [판정보류] | SlideTailor(AAAI 2026) | 연구 참고용 |
| RehgLab/ArcDeck | 52 | 2026-08-28 | MIT | ArcDeck(ECCV 2026). 담화 트리로 서사 흐름을 잡는 논문-슬라이드 생성 | 연구 참고용. Claude 플러그인판(RehgLab/ArcDeck-Claude-Plugin, 별 0) 있음 |
| vinsontang1/SlideCoder | 48 | 2025-10-20 | [판정보류] | SlideCoder(EMNLP 2025) 코드 | 연구 참고용 |
| jkf87/lecture-ppt-generator | 2 | 2026-03-05 | null | 한국어 강의 스토리보드에서 pptx 생성 스킬. html2pptx 파이프라인, CJK 넘침 보정 | 한국어 사례로 참고만. 별 2, 검증 안 됨 |

### 2.4 PowerPoint MCP 서버

| 저장소 | 별 | 마지막 push | 라이선스 | 방식 | WPK 적합 |
|---|---|---|---|---|---|
| GongRzhe/Office-PowerPoint-MCP-Server | 1,854 | 2025-12-31 | MIT | python-pptx 기반 파일 조작 MCP. **archived=true(보관됨)** | 낮음. 유지보수 중단 |
| Ayushmaniar/powerpoint-mcp | 114 | 2026-05-01 | null(라이선스 없음) | pywin32 COM 으로 실행 중인 PowerPoint 조작. Windows 전용. 읽기 · 실시간 편집 · 수식 · 애니메이션 | 높음(기능), 라이선스 미표기 |
| ykuwai/ppt-mcp | 78 | 2026-09-18 | null(라이선스 없음) | COM 기반 라이브 PowerPoint 조작, 도구 156 개. Windows 11 · macOS | 높음(기능), 라이선스 미표기 |
| Ichigo3766/powerpoint-mcp | 54 | 2025-03-27 | MIT | 파일 생성 MCP(supercurses/powerpoint 포크) | 낮음. 1 년 넘게 정체 |
| samos123/pptx-mcp | 35 | 2025-05-20 | Apache-2.0 | python-pptx 기반 단순 MCP | 낮음 |

### 2.5 어썸 리스트

| 저장소 | 별 | 마지막 push | 라이선스 | 비고 |
|---|---|---|---|---|
| ToseaAI/awesome-html-slide-skills | 158 | 2026-06-23 | [판정보류] | Claude Code · Codex 용 HTML 슬라이드 스킬 목록 |
| aspose-slides/Awesome-Presentations | 36 | 2021-12-24 | MIT | 무료 발표 도구 목록. 오래됨 |
| runablehq/Awesome-presentation-tools | 30 | 2025-11-25 | null | 발표 도구 목록 |
| scraperai/awesome-presentations | 13 | 2026-07-21 | CC0-1.0 | 단일 프롬프트로 만든 AI 발표자료 사례 모음 |
| cosen1024/awesome-presentation-skills | 6 | 2026-09-21 | CC0-1.0 | 편집 가능 pptx · HTML · 그림 중심 발표 스킬 목록 |

규모가 크고 관리가 잘 되는 어썸 리스트는 찾지 못했다. `gh search repos "awesome presentation"` 상위가
별 116 이하였다.

## 3. 보안 · 외부 전송 주의

전역 규칙("과업 자료를 공개 URL 로 올리지 마라")에 비추어 보면 아래가 걸린다.

**presenton/presenton**: 사용자 API 키를 쓰는 방식(BYOK)이며 Ollama 로 로컬 모델도 된다. 그러나 코드에
Mixpanel 원격 측정(`servers/nextjs/utils/mixpanel.ts`)이 있고 `DISABLE_ANONYMOUS_TRACKING=true` 를 주기
전에는 켜져 있다(`app/api/telemetry-status/route.ts` 에서 확인). 또 README 가 "Community gallery 는 기본으로
켜져 Presenton community service 에서 디자인을 읽는다" 고 적고, 폐쇄망이면 `PRESENTON_COMMUNITY_ENABLED=false`
로 끄라고 한다. 과업 자료로 쓰려면 두 변수를 끄고 로컬 모델을 쓴다.

**icip-cas/PPTAgent**: 현재 main README 는 Atria · 端砚(Duanyan) 외부 API 키 발급을 전면에 권한다
(`ATRIA_API_KEY`, `VISUAL_API_KEY`). 설치 대상이 Linux · macOS 이고 `sudo apt-get` 과 npm 설치가 있다.
훅 설치 여부는 [판정보류](설치 스크립트 `skills/pptagent/` 원문을 열어 확인 필요).

**allweonedev/presentation-ai**: OpenAI · Together AI · FAL · Tavily 키와 **UploadThing 토큰(외부 파일
업로드 서비스)** 을 요구한다. 과업 자료에는 부적합하다.

**HKUDS/Paper2Slides**: `.env` 에 API 키 필요. 이미지 생성 기본값이 OpenRouter 경유
`google/gemini-3-pro-image-preview` 로, 원고 내용이 외부로 나간다.

**Paper2Poster, CRui5in/paper-ppt-agent, AutoPresent**: LLM API 를 부른다 [추정: 로컬 모델 대체 가능성은
각 README 확인 필요].

**COM 기반 MCP(ykuwai, Ayushmaniar)**: 외부 전송은 없지만 실행 중인 PowerPoint 를 통째로 조작하므로
열린 다른 문서까지 건드릴 수 있다. 두 저장소 모두 라이선스가 없어(GitHub API `license: null`) 재배포 ·
수정 권리가 불분명하다.

**anthropics/skills pptx**: 스킬 자체는 로컬 스크립트(Python · node · LibreOffice)뿐이다. 라이선스는
Proprietary 로 Anthropic 이용약관을 따르므로 재배포하지 않는다. 이미 이 PC 에 `anthropic-skills:pptx` 로 있다.

**Hugging Face Space 의 pptx 변환기들**(예: innoai/PptxToJpgZip-En, Ray1907/docx-to-pptx-converter): 모두
좋아요 0 이고, 파일을 남의 서버에 올리는 방식이므로 과업 자료에는 쓰지 않는다.

## 4. Hugging Face 자원

**Spaces**: `search hf://spaces pptx --sort likes` 상위 10 개가 모두 좋아요 0 이었다. 쓸 만한 대표 Space 는
찾지 못했다.

**데이터셋**: `Yqy6/Slides-Align`(다운로드 22,650, 2026-01-15 갱신)은 SlidesGen-Bench 의 사람 선호 정렬
데이터(Slides-Align1.5k)로 보인다 [추정: 이름과 저자 Yunqiao Yang 일치, 카드 미확인]. `biglab/slides2struct`
(다운로드 1,049), `gigant/tib_slides`(다운로드 885)는 슬라이드 이해 · 구조화용이다.

**컬렉션**: ICIP 조직에 `DeepPresenter` · `PPTAgent` 컬렉션이 있다(DeepPresenter-9B 미세조정 모델과 과제집,
PPTAgent README 의 2026/03 소식).

## 5. 논문

| 논문 | arXiv | 학회 · 시기 | 요지 |
|---|---|---|---|
| DOC2PPT | 2101.11796 | AAAI 2022 | 문서-슬라이드 생성 과제 정의. 계층적 seq2seq, 요약 · 그림 검색 · 레이아웃 예측. 약 6K 문서-덱 쌍 공개 |
| AutoPresent | 2501.00912 | CVPR 2025 | SlidesBench(학습 7k, 시험 585, 310 덱 10 분야). 통째 그림 생성보다 **프로그램 생성**이 품질이 높고 편집 가능. 8B 모델이 GPT-4o 에 근접. 자기 수정 반복이 품질 향상 |
| PPTAgent | 2501.03936 | EMNLP 2025 | 참조 발표자료를 분석해 슬라이드 기능 유형 · 내용 스키마 추출, 개요 작성 후 **참조 슬라이드를 골라 편집 동작으로 생성**. 평가 틀 PPTEval 은 Content · Design · Coherence 세 차원. 세 차원 모두 기존 방법보다 우수 |
| PASS | 2501.06497 | 2025-01 | 워드 문서에서 슬라이드와 AI 음성 발표까지 생성, LLM 기반 지표로 평가 |
| Paper2Poster | 2505.21497 | NeurIPS 2025 | 포스터 벤치마크. 시각 품질 · 텍스트 일관성 · VLM 판정 6 기준 · PaperQuiz(포스터만 보고 논문 내용 퀴즈 풀기). GPT-4o 출력은 첫인상은 좋으나 텍스트가 산만하고 PaperQuiz 가 낮음. 렌더링 후 VLM 피드백 루프로 넘침 제거. 오픈 모델판이 토큰 87 % 절감 |
| PreGenie | 2505.21660 | 2025-05 | MLLM 모듈형 틀. 레이아웃 · 요약 · 그림 이해 문제를 분리해 처리 |
| SlideCoder | 2506.07964 | EMNLP 2025 | 참조 이미지에서 편집 가능한 슬라이드 코드 생성. Slide2Code 벤치마크, 7B SlideMaster 공개, 기존 대비 최대 40.5 점 향상 |
| Paper2Video | 2510.05096 | 2025-10 | 슬라이드 · 레이아웃 정리 · 자막 · 음성 · 발표자 영상까지 통합(HF 추천 120) |
| EvoPresent | 2510.05571 | 2025-10 | 서사 · 미감 · 발표를 다중 과제 강화학습으로 자기 개선 |
| PPTBench | 2512.02624 | 2025-12 | pptx 958 개, 표본 4,439 개(탐지 · 이해 · 수정 · 생성). **모델은 내용은 이해하지만 공간 배치를 일관되게 못 만든다**(정렬 어긋남, 요소 겹침) |
| PPTArena | 2512.03042 | 2025-12 | 기존 덱 **제자리 편집** 벤치마크(100 덱, 2,125 슬라이드, 800 개 넘는 편집). PPTPilot 이 고수준 도구와 결정적 XML 조작을 오가며 계획-편집-점검 루프로 10 %p 넘게 앞섬. 긴 문서 규모 작업은 여전히 약함 |
| SlideGen | 2512.04529 | 2025-12 | 협업 멀티모달 에이전트로 과학 슬라이드 생성 |
| SlideTailor | 2512.20292 | AAAI 2026 | 예시 쌍과 양식에서 사용자 선호를 암묵 추출, 발표 대본(chain-of-speech)과 정렬 |
| SlidesGen-Bench | 2601.09487 | 2026-01 | 생성 방식과 무관하게 렌더링 결과로 평가. Content · Aesthetics · **Editability** 세 차원을 계산식으로 측정. 상용 방식을 양식 기반 · 코드 기반 · 그림 기반 세 갈래로 분류 |
| DECKBench | 2602.13318 | 2026-02 | 학술 슬라이드 생성과 다회 편집 지시 이행 평가. 충실도 · 일관성 · 레이아웃 · 지시 이행 |
| DeepPresenter | 2602.22839 | ACL 2026 | 조사자-발표자 두 에이전트. 내부 추론이 아니라 **렌더링된 슬라이드를 보고 반성**(environment-grounded reflection). 9B 미세조정판도 경쟁력 |
| PresentBench | 2603.07244 | 2026-03 | 238 사례, 사례당 평균 54.1 개 예/아니오 점검 항목. 사람 선호와 정렬도가 높음. **NotebookLM 이 다른 방법보다 크게 앞섬** |
| Learning to Present | 2603.16839 | 2026-03 | 역명세 보상으로 HTML 발표 생성 에이전트를 강화학습 |
| ArcDeck | 2604.11969 | ECCV 2026 | 담화 트리로 논리 흐름을 모델링, 직접 요약보다 우수 |
| AeSlides | 2604.22840 | 2026-04 | 검증 가능한 미감 지표를 보상으로 레이아웃 개선 |
| PresentAgent-2 | 2605.11363 | 2026-05 | 조사 · 멀티모달 슬라이드 · 발표 영상까지 범용 에이전트 |
| MemSlides | 2606.17162 | 2026-06 | 장기 사용자 프로필 · 작업 기억 · 도구 기억 분리로 다회 국소 수정 안정화(HF 추천 57) |
| Inverse Planning | 2607.00407 | 2026-07 | 페이지 단위 개인화를 역계획으로 정식화 |
| ResearchStudio-Reel | 2607.04438 | 2026-07 | 공통 논문 추출기에 포스터 · 영상 · 블로그 스킬을 결합, **통과/실패 품질 관문**(HF 추천 60) |
| ConvDeck | 2609.00226 | EMNLP 2026 Findings | 단계별 사용자 피드백을 받는 대화형 논문-슬라이드 생성 |

HF 추천 수는 조사일의 `upvotes` 값이다. 학회 표기는 저장소 설명 또는 README 에 적힌 것이고, 없으면
arXiv 게시 연월만 적었다.

## 6. 실무 교훈 (지침서용)

1. **양식을 먼저 정하고 편집한다.** PPTAgent(2501.03936)는 참조 슬라이드 선택 후 편집을, PPTArena(2512.03042)는
   대부분의 덱이 처음부터가 아니라 수정으로 다듬어진다는 점을 근거로 제자리 편집을 강조한다. 기관 양식 pptx 를
   두고 슬라이드를 복제 · 채우는 방식이 맞다. Anthropic pptx 스킬의 "양식 편집" 경로(`thumbnail.py` 로 배치
   고르기, `add_slide.py` 로 복제, `clean.py`, `validate.py --original`)가 이 방식이다.
2. **그림 한 장으로 만들지 말고 코드로 만든다.** AutoPresent(2501.00912)는 프로그램 생성이 품질과 편집 가능성에서
   낫다고 보고했고, SlidesGen-Bench(2601.09487)는 편집 가능성을 별도 평가 차원으로 둔다. NotebookLM 같은 그림
   기반 도구가 PresentBench(2603.07244)에서 높은 점수를 받았지만, 수정 가능한 산출물이 필요한 보고용에는 한계가 있다.
3. **렌더링해서 다시 본다.** Paper2Poster(2505.21497)의 Painter-Commenter 루프, DeepPresenter(2602.22839)의
   환경 기반 반성, PPTPilot 의 계획-편집-점검 루프가 같은 결론이다. Windows 에서는 LibreOffice 또는 PowerPoint COM
   으로 PNG 를 뽑아 확인하는 단계를 필수로 둔다. 한국어는 글자 폭이 넓어 넘침이 잦으므로 더 중요하다 [추정].
4. **배치는 사람이 정한 틀에 맡긴다.** PPTBench(2512.02624)에 따르면 모델은 좌표 배치에 약하다. 좌표를 모델이
   자유롭게 정하게 하지 말고 양식의 자리표시자(placeholder)나 고정 격자를 쓰게 한다.
5. **평가는 점검표로 한다.** PresentBench 의 예/아니오 점검 항목, PPTEval 의 Content · Design · Coherence,
   Paper2Poster 의 PaperQuiz(슬라이드만 보고 핵심 질문에 답할 수 있는가)를 지침서의 검수 항목으로 옮길 수 있다.
6. **서사 구조를 먼저 세운다.** ArcDeck(2604.11969)과 PPTAgent 모두 개요 단계를 따로 둔다. 개요 확정 후 슬라이드 생성.

## 7. 확인하지 못한 것

marp-cli 의 편집 가능 pptx 옵션 이름, PPTAgent Skill 설치 스크립트의 훅 여부, llmsresearch/paperbanana ·
ToseaAI · SlideTailor · SlideCoder 저장소의 라이선스, `Yqy6/Slides-Align` 데이터셋 카드, SlideBot-AI 와
humanize-ppt 의 동작 방식은 원문을 열지 않았다. Marker(요청서의 `Marker/markitdown`)라는 저장소는 조회하지
않았고 microsoft/markitdown 으로 대신했다.
