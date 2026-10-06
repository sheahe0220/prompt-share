# 논문 작성법 근거 조사 (수문 · 수자원, SWMM 모형 논문용)

조사일 2026-09-22. 대상: Journal of Hydrology, Water Resources Research(WRR), HESS, 한국수자원학회논문집, 한국물환경학회지, 석박사 학위논문.

표지 규칙. [원문확인] 원문(PDF 또는 웹 본문)을 직접 열어 해당 문장을 확인함. [2차] 검색 요약 · 요약 사이트 · 2차 자료로만 확인함. [추정] 조사자의 추론. [미확인] 확인하지 못함.
쪽 번호는 원 학술지 쪽을 우선 적고, 재인쇄본 쪽만 확인한 경우 "재인쇄본 p.N" 으로 적는다.

---

## 0. 결론: 현행 지침 항목별 판정

현행 지침에서 **정면으로 근거와 부딪히는 것은 두 가지**다. 영문 논문에서 "수동태를 주로 쓰고 긴 문장을 쓴다" 와 "we 를 피하고 This study 를 주어로 쓴다" 이다. 주요 학술지와 양식 지침(Nature, APA 7, 이를 따르는 AGU, Whitesides)은 능동태와 1인칭 복수 we 를 권하거나 허용하고, 3인칭 자기 지칭은 모호하다고 본다. 우리가 겨냥하는 수문 학술지의 대표 논문들(Gupta et al. 2009 J. Hydrol., Hutton et al. 2016 WRR)도 we 를 쓴다. 문장 길이는 "짧고 직접적인 문장" 쪽이 근거다. 나머지 항목은 대체로 근거와 맞으나, 통계 보고와 모형 성능 보고는 보강이 필요하다.

| 현행 지침 | 판정 | 핵심 근거 |
|---|---|---|
| 학술 어조, 수동태 위주, 긴 문장 | **충돌 (수정 필요)** | Nature: 능동태가 이해를 돕는다 [원문확인]; Whitesides p.1377 "Use the active voice whenever possible" [원문확인]; Gopen & Swan: 주어 뒤에 동사를 빨리, 수동태는 이야기 주체가 목적어일 때 정당 [원문확인]; 초록 가독성 하락 실증(Plavén-Sigray et al. 2017) [원문확인 요약] |
| This study 를 주어로, we 회피 | **충돌 (영문은 수정, 국문은 유지)** | APA 7 4.16: 공저면 we, 3인칭 자기 지칭은 모호 [2차]; AGU 는 APA 양식을 따름 [원문확인]; J. Hydrol. · WRR 대표 논문의 we 사용 [원문확인]. 국문 논문의 "본 연구에서는" 은 한국어 관행 [추정] |
| 방법 · 결과는 과거, 일반 사실은 현재 | 유지 | Whitesides p.1377 결과는 과거시제 [원문확인]; APA 시제 관례(결론 · 함의 · 한계는 현재) [2차] |
| 문단당 한 생각, 주제문 먼저 | 유지 (보강) | Mensh & Kording 규칙 3(C-C-C)과 규칙 7 [원문확인]; 역개요(reverse outline) [원문확인 Caltech] |
| IMRaD | 유지 | Copernicus 절 순서 [원문확인]; 한국물환경학회지 제4조 4항 서론-연구방법-결과 및 고찰-결론 [원문확인] |
| 서론 끝에 목적 문장 | 유지 (보강) | Mensh & Kording 규칙 6 [원문확인]; Nature 요약문의 "Here we show" 문장 [원문확인]; 단, Whitesides 는 서론 첫 문장에 목적과 중요성을 쓰라고 함 p.1376 [원문확인] |
| 기호 정의 | 유지 (보강) | Copernicus: 수학 기호 이탤릭, 함수명 · 단위 · 화학식은 정체 [원문확인]; 한국수자원학회 투고지침: 수학기호 · 함수 외 기호 이탤릭 [원문확인] |
| 표가 본문을 반복하지 않게 | 유지 | Whitesides p.1376 "text ... serves just to explain the data" [원문확인]; Zhang 2014 규칙 4: 그림 · 표만으로 이야기가 서도록 [원문확인] |
| 통계는 n, 검정통계량, p | **보강 필요** | ASA p-value 성명(2016): p 값만으로 결론 내리지 말 것, 효과 크기와 구별 [2차]. 효과 크기 · 신뢰구간 · 정확한 p 를 함께 [추정 + APA 관례 2차] |
| 한계 절 | 유지 | Mensh & Kording 규칙 8 [원문확인]; Schimel 의 "Dealing with limitations" 장 [2차] |
| 심사 대응 3 범주 | 유지 가능, 형식 보강 | Noble 2017 10 규칙: 모든 지적에 응답, 직답 먼저, 바뀐 문장을 쪽 · 줄과 함께 인용 [원문확인]. "3 범주" 자체는 문헌 근거를 찾지 못함 [미확인] |

현행 지침에 **없는데 넣어야 할 것**은 다음이다. (1) 하나의 중심 기여와 제목(Mensh & Kording 규칙 1). (2) 개요 먼저 · 그림 먼저 작성 순서(Whitesides, Zhang). (3) 학술지별 필수 부속물: J. Hydrol. Highlights(3-5 개, 각 85 자 이내) · 데이터 진술 · CRediT · 생성형 AI 사용 진술, AGU Key Points(최대 3 개, 각 140 자 이내) · Open Research 절 · (WRR 은 선택이나 강력 권장) Plain Language Summary 200 단어 이내, HESS Code availability · Data availability · Author contribution. (4) 모형 보정 · 검증 보고 기준(Moriasi, Gupta/KGE, Knoben 기준선, Klemeš 분할 표본). (5) 코드와 워크플로 공개(Hutton et al. 2016).

---

## 1. 구조와 서사

### 1.1 Mensh & Kording (2017) "Ten simple rules for structuring papers" [원문확인]

Mensh B, Kording K (2017) PLOS Computational Biology 13(9): e1005619. https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619 (온라인 논문이라 쪽 번호 없음, 규칙 번호로 인용)

규칙 1. 하나의 중심 기여에 집중하고 그것을 제목에 담는다. 규칙 2. 내 연구를 모르는 실제 독자를 위해 쓴다(용어 정의, 약어 절제). 규칙 3. 문단 · 절 · 논문 전체에서 context-content-conclusion(C-C-C) 틀을 지킨다. 독자가 "왜 이 말을 하지?" 또는 "그래서?" 라고 묻지 않게 한다. 규칙 4. 한 주제를 한 번에 다루고(지그재그 금지) 비슷한 내용은 병렬 구조로 쓴다. 규칙 5. 초록에 완결된 이야기를 담는다(맥락에서 공백으로 좁히고, 방법 · 결과, 공백에 답하는 결론). 규칙 6. 서론은 점점 좁아지는 문단으로 공백을 보이고 논문의 기여를 밝힌다. 규칙 7. 결과는 그림이 받치는 선언적 진술의 연쇄로 제시하고, 각 문단은 질문을 세우고 답한다. 규칙 8. 토의는 공백을 어떻게 메웠는지, 해석의 한계, 분야에서의 의의를 다룬다. 규칙 9. 제목 · 초록 · 그림 · 개요에 시간을 배분하고, 계획한 문단마다 한 문장씩 개요를 먼저 쓴다. 규칙 10. 피드백으로 이야기를 줄이고 재활용한다.

지침 반영 [추정]: "문단당 한 생각, 주제문 먼저" 는 규칙 3 의 문단 수준 적용과 같다. 여기에 문단의 마지막 문장이 결론(conclusion) 역할을 하도록 한다는 점을 보탠다. 결과 절 소제목과 문단 첫 문장을 선언문으로 쓰라는 규칙 7 은 Whitesides 의 "정보가 담긴 소제목"(1.2 절)과 같은 방향이다.

### 1.2 Whitesides (2004) "Whitesides' Group: Writing a Paper" [원문확인]

Whitesides GM (2004) Advanced Materials 16(15): 1375-1377. DOI 10.1002/adma.200400767. 확인한 사본: https://mason.gmu.edu/%7Ehjing2/advice%20for%20phd%20students/Writing%20a%20paper-George%20Whiteside.pdf (1989-10-04 연구실 배포문이 바탕, p.1375 각주)

p.1375. 논문은 가설 · 자료 · 결론을 조직한 서술이다. "Interesting and unpublished" 는 "non-existent" 와 같다. 개요는 글의 개요가 아니라 목적 · 가설 · 결론이 붙은 "조직된 자료의 집합" 이다. 개요를 여러 번 돌리는 편이 전문을 여러 번 고쳐 쓰는 것보다 빠르다.
p.1376. 자료 수집이 "완료" 될 때까지 개요를 미루지 말라("No project is ever complete"). 지도교수와 개요를 4-5 회 주고받아 합의한 뒤 본문을 쓴다. 개요에는 본문을 거의 쓰지 말고 소제목 · 그림(캡션 포함) · 식 · 표를 제자리에 둔다. **초록은 쓰지 말고 논문이 끝난 뒤 쓴다.** 서론 첫 문장은 목적과 그 중요성을 간결하게 밝힌다. 결과 소제목은 "Measurement of Rates" 보다 "The Rate of Self-Exchange Decreases with the Polarity of the Solvent" 처럼 정보가 담기게 쓴다. 본문은 자료를 설명하는 부차적 역할이다.
p.1377. 결론은 요약이 아니라 한 단계 높은 분석과 의의를 적는다. 연대순이 아니라 중요도 순으로 조직한다. 문체 항목: 명사를 형용사로 쓰지 말 것, "this" 뒤에는 명사를 붙일 것, **실험 결과는 과거시제로 통일**, **"Use the active voice whenever possible"** (예: "It was observed that the solution turned red" 대신 "The solution turned red" 또는 "We observed that the solution turned red"), 비교는 끝까지 완결할 것.

지침 반영 [추정]: 작성 순서를 "개요(그림 · 표 포함) → 결과 · 방법 → 토의 · 결론 → 서론 → 초록 · 제목" 으로 명시한다. 개요 단계는 지도교수 검토 주기와 맞물린다.

### 1.3 Gopen & Swan (1990) "The Science of Scientific Writing" [원문확인]

Gopen GD, Swan JA (1990) American Scientist 78(6): 550-558. 확인한 재인쇄본: https://www.usenix.org/sites/default/files/gopen_and_swan_science_of_scientific_writing.pdf (16 쪽, 원 학술지 쪽과 대응은 [미확인])

재인쇄본 p.15 의 7 원칙: (1) 문법적 주어 뒤에 동사를 가능한 한 빨리 둔다. (2) 독자가 강조로 읽기를 바라는 새 정보는 문장 끝 강세 위치(stress position)에 둔다. (3) 문장이 이야기하는 대상은 문장 첫머리 화제 위치(topic position)에 둔다. (4) 앞에서 나온 옛 정보는 화제 위치에 두어 뒤로 잇고 앞으로 맥락을 준다. (5) 절의 행위는 동사로 표현한다. (6) 새것을 내놓기 전에 맥락을 준다. (7) 내용상 강조와 구조상 강조를 일치시킨다. 저자들은 이것이 "규칙" 이 아니며, 능동태를 기계적으로 고집하는 것도 실패한다고 쓴다(재인쇄본 p.15).

수동태에 관한 원문(재인쇄본 p.8): "Bees disperse pollen" 과 "Pollen is dispersed by bees" 는 둘 다 좋은 문장이며, 꽃가루 이야기를 이어 가는 문단이라면 수동문이 더 낫다. 즉 **태의 선택 기준은 "무엇이 그 문장의 이야기 주체인가" 이다.**

지침 반영 [추정]: "수동태 위주" 대신 "화제 위치에 이야기의 주체와 옛 정보를 두고, 그 결과로 능동 또는 수동을 고른다" 로 바꾼다. SWMM 방법 절에서 "The Manning's n of the conduits was adjusted ..." 처럼 대상이 주체인 수동문은 정당하다. 결과 · 해석 문장에서 "It was found that ..." 은 주어-동사를 멀리 떨어뜨리므로 피한다.

### 1.4 Schimel (2012) "Writing Science" [2차]

Schimel J (2012) Writing Science: How to Write Papers That Get Cited and Proposals That Get Funded. Oxford University Press. 원서 쪽 번호는 [미확인]. 확인한 2차 자료: Wei Xiao (2012-06-15) 예일-NUIST 발표 슬라이드 https://yncenter.sites.yale.edu/sites/default/files/xiao_wei_jun_2012.pdf (슬라이드 p.2, p.11-14)

슬라이드 p.2 의 장 구성: 1 Writing in science, 2 Science writing as storytelling, 3 Making a story sticky, 4 Story structure, 5 The opening, 6 The funnel, 7 The challenge, 8 Action, 9 The resolution, 10 Internal structure, 11 Paragraphs, 12 Sentences, 13 Flow, ..., 18 Dealing with limitations, 19 Writing global science, 20 Writing for the public.
슬라이드 p.11-13: OCAR(Opening, Challenge, Action, Resolution)는 가장 느린 구조로 학술 논문에 쓰이고, ABDCE(Action, Background, Development, Climax, Ending)는 더 빠르며(제안서), LDR(Lead, Development, Resolution)과 LD 는 결론을 앞에 둔다. 슬라이드 p.14: OCAR 이야기는 출발점으로 돌아오되 그 점이 이동해 있는 나선 구조다.

지침 반영 [추정]: 서론은 O(큰 문제) → C(구체 질문, 서론 끝 목적 문장) 로, 결과는 A, 결론은 R 로 대응시킨다. 결론이 서론의 질문으로 되돌아가 답하는지 점검한다.

### 1.5 Nature 요약문(summary paragraph) 작성법 [원문확인]

"How to construct a Nature summary paragraph", Nature guide to authors (2019-09). https://www.nature.com/documents/nature-summary-paragraph.pdf (1 쪽)

구성: 어느 분야 과학자도 이해할 분야 소개 1-2 문장, 인접 분야용 상세 배경 2-3 문장, 이 연구가 다루는 일반 문제 1 문장, **"here we show" 또는 그에 준하는 말로 주결과 1 문장**, 기존 지식과 비교한 결과의 의미 2-3 문장, 더 넓은 맥락 1-2 문장. 편집자가 필요하다고 보면 넓은 관점 2-3 문장을 더해 최대 300 단어. 예시는 190 단어(마지막 부분 포함 시 250 단어).

지침 반영 [추정]: J. Hydrol.(250 단어 이하) · AGU(250 단어 미만) 초록의 뼈대로 쓸 수 있다. "Here we show" 문장 자체가 we 를 쓰는 능동문이라는 점도 지침 개정 근거다.

### 1.6 기타: Zhang (2014), 역개요, 작성 순서

Zhang W (2014) "Ten simple rules for writing research papers" PLOS Comput Biol 10(1): e1003453. https://pmc.ncbi.nlm.nih.gov/articles/PMC3907284/ [원문확인]. 규칙 1 Make It a Driving Force(과제 설계 단계부터 논문 개요를 둔다), 규칙 2 Less Is More, 규칙 4 Be Logical: 그림과 표를 먼저 만들고 실험의 정보 흐름에 따라 배열하며, 각 그림 · 표는 캡션만으로 자족적이어서 "figures and tables alone can tell the story". 규칙 6 Be Concise. 이 논문은 절 작성 순서를 명시하지 않는다.

역개요(reverse outlining) [원문확인]: Caltech Hixon Writing Center, "Technique: Reverse Outlining (for a Scientific Article)" https://writing.caltech.edu/documents/24103/ReverseOutliningScientificWriting.pdf (p.1-2). 각 문단(또는 문장)의 요점을 여백에 최소 단어로 적어 흐름을 점검한다. 절별 전형 주제(서론 "Why", 방법 "How", 결과 "What", 토의 "So What")를 태그로 제시한다. 한 문장으로 요약되지 않는 문단은 둘 이상의 생각을 담은 것이라는 해석은 UW-Madison Writing Center https://writing.wisc.edu/handbook/reverseoutlines/ 등 [2차].

작성 순서 "방법 · 결과 먼저, 서론 · 초록 나중" 에 대해: 초록을 마지막에 쓰라는 것은 Whitesides p.1376 에서 [원문확인]. 방법 · 결과를 먼저 쓰라는 명시적 권고는 이번에 연 1 차 자료에서 찾지 못했다 [미확인]. 그림 · 표를 먼저 만들라는 것은 Whitesides p.1376 과 Zhang 규칙 4 에서 확인 [원문확인].

---

## 2. 문체: 태, 인칭, 문장 길이, 어휘

### 2.1 학술지 · 양식 지침의 입장

**Nature Portfolio** [원문확인] "How to write your paper" https://www.nature.com/nature-portfolio/for-authors/write : "Using the active voice ('we performed the experiment...') typically helps readers better understand concepts and results described in a paper." "Write clear and direct sentences." "Keep technical terms to the places where they are needed. Define abbreviations at first use and use them sparingly." "A reader should be able to understand what you found and why it matters from the title and abstract." 한 명사에 형용사를 여럿 겹치지 말고 단순한 문장으로 풀라는 권고는 검색 요약으로만 확인 [2차].

**APA 7** [2차] (apastyle.apa.org 는 봇 차단으로 본문을 열지 못함). https://apastyle.apa.org/style-grammar-guidelines/grammar/first-person-pronouns 와 https://apastyle.apa.org/blog/first-person-myth 의 검색 요약: 단독 저자는 I, 공저자는 we 를 쓴다. 격식을 위해 3인칭으로 자신을 가리키지 말라, 누가 행위했는지 모호해진다. 사람 일반을 가리키는 editorial we 는 피한다. 출처는 Publication Manual 7판 4.16 절, Concise Guide 2.16 절. 능동태가 기본이며, 행위자가 중요하지 않을 때 수동태가 낫다. 확인 방법: APA Publication Manual 7판 4.13(태) · 4.16(1인칭) 절을 직접 연다.

**AGU (WRR 발행)** [원문확인] "Grammar and Style Guide" https://www.agu.org/publications/authors/journals/grammar-style-guide : "AGU follows American Psychological Association (APA) style on grammar, punctuation, table formatting, citations, and references." 따라서 AGU 투고 원고에는 APA 의 1인칭 · 태 권고가 적용된다고 보는 것이 자연스럽다 [추정]. 구판 AGU Grammar and Style Guide(작성 연도 [미확인]) https://web.mst.edu/%7Esgao/research/resources/agu_grammar_style.pdf 의 예문도 "we made a log plot of the data"(p.10), "We performed the experiment at room temperature"(p.10), "we have used only data in which ..."(p.15)처럼 we 를 일상적으로 쓴다 [원문확인].

**Copernicus (HESS)** [원문확인] https://publications.copernicus.org/for_authors/manuscript_preparation.html : "All standard varieties of English are accepted in order to retain the author's voice. However, the variety should be consistent within each article." 태 · 인칭에 관한 명시 규정은 찾지 못함 [미확인].

**Elsevier (J. Hydrology)** [원문확인] Guide for authors https://www.sciencedirect.com/journal/journal-of-hydrology/publish/guide-for-authors : 태 · 인칭 규정은 없음. 초록은 "concise and factual", 250 단어 이하, 단독으로 읽힐 것, 비표준 약어는 피하고 불가피하면 초록 안에서 정의. 포용적 언어 사용 요구.

**Science (AAAS)** [2차]: "use first person, not third; do not use first person plural when singular is appropriate" 라는 지침이 있다는 검색 요약만 있음. science.org 가 403 으로 막혀 원문 미확인. 확인 방법: https://www.science.org/content/page/instructions-preparing-initial-manuscript 를 브라우저로 연다.

**ACS**: ACS 발표 슬라이드 "Active vs. Passive Voice in Scientific Writing"(2015) https://www.acs.org/content/dam/acsorg/events/professional-development/Slides/2015-04-09-active-passive.pdf 가 검색되었으나 열지 않음 [미확인]. ACS Guide to Scholarly Communication 의 해당 조항도 [미확인].

### 2.2 우리 분야 학술지에서 실제로 we 를 쓰는가

Gupta HV, Kling H, Yilmaz KK, Martinez GF (2009) "Decomposition of the mean squared error and NSE performance criteria" J. Hydrol. 377(1-2): 80-91. 투고본(NASA NTRS 사본) https://ntrs.nasa.gov/api/citations/20090027858/downloads/20090027858.pdf 초록: "Here, we present a diagnostically interesting decomposition of NSE ... While we propose and test an alternative criterion ..., we seek to show that ..." [원문확인, 투고본 p.5]
Hutton C, et al. (2016) "Most computational hydrology is not reproducible, so is it really science?" WRR 52(10): 7548-7555. https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2016wr019285 초록: "In order to overcome this problem we recommend that ..." [원문확인]

판정 [추정]: J. Hydrol. 과 WRR 모두 we 를 쓴 대표 논문이 있으므로, "we 회피" 는 이 학술지들의 관행과 맞지 않는다. 다만 이 두 편은 표본이지 전수 조사가 아니다. 확인 방법: 목표 학술지 최근호 10 편의 초록에서 we 빈도를 센다.

### 2.3 문장 길이와 가독성

Plavén-Sigray P, Matheson GJ, Schiffler BC, Thompson WH (2017) "The readability of scientific texts is decreasing over time" eLife 6: e27725. https://elifesciences.org/articles/27725 [원문확인 요약]: 123 개 학술지 709,577 편 초록(1881-2015)에서 Flesch Reading Ease 와 New Dale-Chall 지수 모두 해마다 가독성이 낮아졌다(연도와 상관 r = -0.93, 0.93). 2015 년에는 초록의 5 분의 1 이상이 대학원 졸업 수준을 넘는 난이도였다. 원인으로 저자 수 증가와 "novel", "robust" 같은 일반 과학 전문어의 증가를 든다.

판정 [추정]: "긴 문장" 을 권할 근거는 찾지 못했다. Nature 의 "clear and direct sentences", Gopen & Swan 의 주어-동사 근접 원칙, 위 가독성 실증이 모두 반대 방향이다. 지침은 "한 문장에 한 주장, 주어 뒤 동사를 가깝게" 로 바꾸는 것이 근거에 맞는다. 문장 길이의 수치 기준(예: 평균 몇 단어)을 권고한 1 차 자료는 찾지 못함 [미확인].

### 2.4 1인칭과 객관성

1인칭 사용과 독자 인식에 관한 실증 연구로 PNAS(2024) "'I' versus 'the author': The power of first-person voice when writing about science" https://www.pnas.org/doi/10.1073/pnas.2316966121 가 검색되었으나 403 으로 본문 미확인 [미확인]. 저자 · 결과를 인용하지 않는다.

### 2.5 평이한 언어 요약 (Plain Language Summary)

AGU "Plain Language Summary" https://www.agu.org/publications/authors/journals/plain-language-summary [원문확인]: PLS 는 초록과 같은 정보를 전혀 다른 말투로, 전문어 없이 쓴다. 한 문단 200 단어 이하. 학부 수준 독자를 상정하고, 분야 용어는 정의하며, 일반인에게 뜻이 다른 단어(skill, regime, signal, uncertainty, mean 등)를 조심한다. 구성 권장: 주제 개관 1-3 문장, 논문 개관 1-3 문장, 결과 요약 1-3 문장, 핵심 시사점 1-2 문장. 필수 학술지 목록(AGU Advances, GeoHealth, GRL, G-Cubed, JAMES, JGR 각지, Reviews of Geophysics, Space Weather)에 **WRR 은 없고**, 그 밖의 AGU 학술지는 "optional but strongly encouraged".

수문 모형 논문에서 특히 걸리는 단어 [추정]: uncertainty, calibration, efficiency, skill, parameter. PLS 에서는 풀어 쓴다.

---

## 3. 목표 학술지별 필수 요건

### 3.1 Journal of Hydrology (Elsevier) [원문확인]

https://www.sciencedirect.com/journal/journal-of-hydrology/publish/guide-for-authors (2026-09-22 열람)
초록 250 단어 이하, 단독으로 읽힐 것. 키워드 1-7 개, 영어, 여러 단어로 된 키워드("and", "of" 포함)는 피함. **Highlights 3-5 개, 각 85 자(공백 포함) 이하**, 새 결과와 새 방법을 담음. Graphical abstract 권장. 연구자료: 자료 저장소에 예치하고 논문에서 인용 · 연결, 불가하면 이유를 진술(Option C). **데이터 진술(Data statement) 필수.** **CRediT 저자 기여 진술 필수**(교신저자가 작성). **생성형 AI 사용 진술 필수**(절 제목 "Declaration of generative AI and AI-assisted technologies in the manuscript preparation process"). 소프트웨어 인용 예시(Zenodo DOI) 제시. 영어 외 언어 문헌은 영어 번역 제목으로 쓰고 원어를 괄호로 표시. Focussed Review 는 3,000 단어 · 참고문헌 80 개 이하. Research Article 의 단어 제한은 이번에 확인한 부분에서 찾지 못함 [미확인].

### 3.2 Water Resources Research (AGU) [원문확인]

AGU "Text & Graphics Requirements" https://www.agu.org/publications/authors/journals/text-graphics-requirements (curl 로 받은 본문)
**Key Points: 1-3 개, 각 140 자 이하, 약어 금지, 완결된 문장.** 초록: 조사의 성격과 중요한 결론을 요약, 색인에 적합하게, 인용은 원칙적으로 피함. 초록은 한 문단 250 단어 미만(PLS 페이지). PLS: 200 단어 이하, 전문어 · 약어 · 식 없이, WRR 은 선택. **Open Research 절(가용성 진술) 필수**: 자료와 소프트웨어의 인용 정보와 접근 위치를 적어야 하며, **"저자에게 요청하면 제공" 식 진술은 허용하지 않는다.** 가용성 진술에 적은 자료 · 소프트웨어는 참고문헌에 정식 인용한다. 표 · 그림을 받치는 자료는 저장소에 보존하고 DOI 또는 URL 을 Open Research 절에 적으며, 집계 표라면 집계 스크립트나 워크플로를 제공한다. 자료 · 소프트웨어를 보충자료(Supporting Information)에 넣지 말고 분야 저장소에 둔다. CRediT 로 기여 표시(2018 년부터 게재). 교신저자 ORCID 필수. 저자 자격: 구상 · 설계 또는 자료 취득 · 분석 · 해석 · 새 소프트웨어 작성, 원고 작성 또는 실질적 수정, 최종본 승인, 책임.

### 3.3 HESS (Copernicus) [원문확인]

https://publications.copernicus.org/for_authors/manuscript_preparation.html
절 순서: Title page, Abstract, Introduction, Sections, Conclusions, Appendices, **Code availability, Data availability**, Interactive computing environment, Sample availability, Video supplement, Team list, **Author contribution**, Competing interests, Acknowledgements, Financial support, References. 초록은 본문 없이 일반 독자가 이해할 수 있게. 코드는 FAIR 저장소 예치를 권장하고 그 경우 "Code availability" 절을 둔다. 자료 비공개 시 법 · 기관 정책 · 연구비 조건 등 상세 이유 필요. 수학 기호는 이탤릭, 함수명(sin, cos) · 화학식 · 물리 단위는 정체. 식은 오른쪽 괄호 안 아라비아 숫자, 본문에서는 "Eq." 로 지칭. 그림 색은 색각 이상 독자도 해석 가능해야 하며 Coblis 등으로 점검. 영어 변종은 자유이나 한 논문 안에서 일관. 저자 기여 절에 CRediT 권장(HESS 데이터 정책 페이지 https://www.hydrology-and-earth-system-sciences.net/policies/data_policy.html 검색 요약 [2차]).

지침 반영 [추정]: 세 학술지 공통으로 **자료 · 코드 가용성 절, CRediT 기여, 기호 이탤릭 규칙**이 들어간다. 현행 지침에 가용성 절 항목을 새로 둔다.

---

## 4. 수문 모형(보정 · 검증 · 불확도) 보고 기준

### 4.1 Moriasi et al. (2007) [원문확인]

Moriasi DN, Arnold JG, Van Liew MW, Bingner RL, Harmel RD, Veith TL (2007) "Model evaluation guidelines for systematic quantification of accuracy in watershed simulations" Trans. ASABE 50(3): 885-900. https://swat.tamu.edu/media/90109/moriasimodeleval.pdf
p.885(초록): 정량 통계 NSE, PBIAS, RSR 세 가지와 **그래프 기법을 함께** 쓰라고 권고. 일반적으로 NSE > 0.50 이고 RSR ≤ 0.70 이며 유량 PBIAS ±25 %, 유사 ±55 %, N · P ±70 % 이내면 "satisfactory". 추가 고려사항으로 단일 사상 모의, 실측 자료 품질과 양, 보정 절차, 평가 시간 간격, 과업 범위를 든다.
p.891 Table 4: **월 단위** 성능 등급(Very good: RSR 0.00-0.50, NSE 0.75-1.00, 유량 PBIAS ±10 % 미만; Good: RSR 0.50-0.60, NSE 0.65-0.75, 유량 PBIAS ±10-15 %; Satisfactory: RSR 0.60-0.70, NSE 0.50-0.65, 유량 PBIAS ±15-25 %; Unsatisfactory: RSR 0.70 초과, NSE 0.50 미만, 유량 PBIAS ±25 % 초과). 경계의 등호 포함 여부는 PDF 텍스트 추출에서 부등호 기호가 깨져 확인하지 못함 [미확인]; 인용 시 원표를 직접 본다.

### 4.2 Moriasi et al. (2015) [원문확인]

Moriasi DN, Gitau MW, Pai N, Daggupati P (2015) "Hydrologic and water quality models: Performance measures and evaluation criteria" Trans. ASABE 58(6): 1763-1785. https://web.ics.purdue.edu/%7Emgitau/pdf/Moriasi%20et%20al%202015.pdf
p.1763(초록): 유역 규모 모형의 유량은 일 · 월 · 연 R2 > 0.60, NSE > 0.50, PBIAS ≤ ±15 % 이면 "satisfactory". 현장 규모는 월 R2 > 0.70, d > 0.75. 대상 모형은 SWAT, HSPF, WARMF 등 유역 모형 문헌.
p.1777: 여러 그래프 · 통계 성능지표를 함께 쓰라고 권고하며, 이 기준은 보정과 검증 기간 모두에 적용한다.
p.1772(Table 5 부근): PBIAS 는 단일 사상 모의에는 쓸 수 없다는 단점을 적는다.

주의 [추정]: Moriasi 기준은 일 · 월 · 연 시간 간격의 유역 모형 문헌에서 나온 것이다. **분 단위 · 사상 기반 도시 배수 SWMM 모의에 그대로 옮기는 것은 외삽**이다. 논문에서 이 기준을 쓸 때는 "참고 기준으로 인용하되 시간 간격과 사상 기반 차이를 밝힌다" 고 적는 편이 심사에 안전하다. SWMM 문헌의 보고 성능 분포는 Niazi et al.(4.6 절)을 함께 인용한다.

### 4.3 Gupta et al. (2009): NSE 분해와 KGE [원문확인]

J. Hydrol. 377(1-2): 80-91. 투고본 https://ntrs.nasa.gov/api/citations/20090027858/downloads/20090027858.pdf (투고본 p.5 초록). NSE(따라서 MSE)를 상관 · 변동성 · 편의 성분으로 분해해 NSE 기반 보정에서 생기는 체계적 문제를 보이고, 대안 기준(이후 KGE 로 불림)을 제안 · 시험한다. 저자들은 주목적이 "더 나은 지표 제시" 가 아니라 MSE 계열 최적화의 체계적 문제를 보이는 것이라고 쓴다.

### 4.4 Knoben et al. (2019): KGE 의 기준선 [원문확인]

Knoben WJM, Freer JE, Woods RA (2019) "Technical note: Inherent benchmark or not? Comparing Nash-Sutcliffe and Kling-Gupta efficiency scores" HESS 23: 4323-4331. https://hess.copernicus.org/articles/23/4323/2019/
관측 평균 유량을 예측값으로 쓰면 KGE = 1 - √2 ≈ -0.41 이다(NSE 는 0). NSE 와 KGE 의 관계는 관측의 변동계수에 따라 달라 **직접 비교할 수 없다.** KGE 를 쓸 때는 NSE 의 감각을 옮기지 말고, 어떤 기준 모형과 비교하는지 명시하고 연구 목적에 따라 정당화하라고 권고한다.

지침 반영 [추정]: "KGE > 0 이면 평균보다 낫다" 는 서술을 금지하고, KGE 를 보고할 때 세 성분(r, α, β)과 기준선(-0.41 또는 명시한 기준 모형)을 함께 적는다.

### 4.5 Klemeš (1986): 분할 표본 계층 시험 [원문확인 초록 + 2차]

Klemeš V (1986) "Operational testing of hydrological simulation models" Hydrol. Sci. J. 31(1): 13-24. https://doi.org/10.1080/02626668609491024
초록 [원문확인]: 모형 과제의 난이도에 시험의 성격을 맞추는 계층적 체계를 제안한다. 목적은 실제 쓰일 상황에 최대한 가까운 조건에서 성능을 보는 "운영상 적정성" 평가이며, 모의와 관측의 일치는 모형 적정성의 필요조건일 뿐 충분조건이 아니다.
네 시험의 이름(split-sample, differential split-sample, proxy-basin, proxy-basin differential split-sample)은 본문을 열지 못해 [2차]로 남긴다(T&F PDF 403). 확인 방법: 도서관 경유로 p.13-24 를 연다.

지침 반영 [추정]: 보정 사상과 검증 사상을 나눈 기준(기간 · 강우 규모 · 선행 건기 등)을 방법 절에 명시한다. 강우 규모가 다른 사상으로 검증하면 differential split-sample 의 취지에 가깝다.

### 4.6 SWMM 전용: Niazi et al. (2017) [원문확인]

Niazi M, Nietch C, Maghrebi M, Jackson N, Bennett BR, Tryby M, Massoudieh A (2017) "Storm Water Management Model: Performance review and gap analysis" J. Sustainable Water Built Environ. 3(2): 04017002. DOI 10.1061/JSWBAY.0000817. https://swmm5.org/wp-content/uploads/2017/07/swmmreview.pdf
p.04017002-1: SWMM 보고서 다수가 동료 심사를 거치지 않아 성능의 신뢰성을 가늠하기 어렵다는 문제의식. p.04017002-22: 검증은 보정과 다른 기간으로 하며 59 개 연구가 검증을 수행했다. 같은 지표로 보정과 검증을 모두 보고한 연구들을 비교하면 **검증 성능이 보정보다 약한 경우가 더 많아** 외삽 능력의 신뢰가 낮으므로 검증 수행이 필요하다. 역방향 불확도 분석 방법으로 MCMC(베이즈), GLUE, 국소 민감도 기반을 분류한다. p.04017002-24: **SWMM 적용에서 순방향 · 역방향 불확도 분석은 드물게 수행되었다.** p.04017002-20-21: 민감도 분석 사례 정리.

SWMM 에 특화된 학회 차원의 "보고 표준" 문서는 찾지 못했다 [미확인].

### 4.7 불확도 보고: Pappenberger & Beven (2006) [2차]

Pappenberger F, Beven KJ (2006) "Ignorance is bliss: Or seven reasons not to use uncertainty analysis" WRR 42: W05302. https://doi.org/10.1029/2005WR004820 . 불확도 분석을 하지 않는 일곱 가지 흔한 이유(물리적으로 현실적인 모형이면 불필요, 가설 검정에 못 씀, 정책가가 이해 못 함, 의사결정에 못 넣음, 너무 주관적, 너무 어려움, 최종 결정에 영향 없음)를 반박한다. 검색 요약으로만 확인. Beven 의 등결과성(equifinality) 논문(Beven 2006 J. Hydrol. 320: 18-36)은 이번에 열지 않음 [미확인].

### 4.8 재현성: Hutton et al. (2016) [원문확인]

WRR 52(10): 7548-7555. https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2016wr019285
초록: 전산 수문학에서 결과를 만든 코드와 자료가 공개되지 않아 재현 · 검증이 어렵다. 결과를 모호함 없이 재현하는 재사용 가능한 코드와 형식화된 워크플로를 자료와 함께 공개하라고 권고한다. 본문: 최소 기준으로 코드에 예제 워크플로를 붙이고, 코드는 함수 · 클래스로 모듈화하며, 주석은 코드를 되풀이하지 말고 상위 수준에서 무엇을 하려는지 설명한다. 코드와 워크플로는 **사용한 정확한 버전에 해당하는 DOI** 로 인용한다.

지침 반영 [추정]: SWMM .inp 원본, 보정 스크립트, 강우 · 유량 자료(공개 가능 범위)를 버전 DOI(Zenodo 등)로 올리고 AGU Open Research · HESS Code/Data availability · J. Hydrol. Data statement 에 적는다. 발주처 자료처럼 공개가 불가하면 이유를 구체적으로 쓴다(Copernicus 규정). 단, 전역 규칙상 공개 업로드는 사용자 승인 사항이다.

### 4.9 통계 보고: ASA p-value 성명 [2차]

Wasserstein RL, Lazar NA (2016) "The ASA's statement on p-values: Context, process, and purpose" The American Statistician 70(2): 129-133. https://doi.org/10.1080/00031305.2016.1154108 . 여섯 원칙 가운데 원칙 3: 과학적 결론과 정책 결정은 p 값이 특정 문턱을 넘었는지만으로 내리지 말 것. p 값은 가설이 참일 확률이 아니며, 효과의 크기나 중요성을 재지 않는다. 검색 요약으로 확인(원문 PDF https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf 미열람).

지침 반영 [추정]: "n, 검정통계량, p" 에 **효과 크기, 신뢰구간(또는 불확도 구간), 정확한 p 값(p < 0.05 식 표기 대신)** 을 더한다. 모형 성능 지표에도 가능하면 부트스트랩 구간을 붙인다.

---

## 5. 국내 학술지와 학위논문

### 5.1 한국수자원학회논문집 투고지침 [원문확인, 웹 요약 도구 경유]

https://www.kwra.or.kr/staticdata/static/publish/sbumission-rule/ (2021-03-10 편집위원회 의결 · 시행)
구성: 제목(국문 · 영문), 저자명(국문 · 영문), 요지(국문 · 영문과 핵심용어), 본문, 감사의 글, References, 기호, 부록. 본문은 서론 · 본론 · 결론. 분량: 일반 논문 인쇄 8 쪽 이하(그림 · 표 · 사진 포함), 기술 · 정책 노트 6 쪽. 요지: 영문과 국문 각 200 단어 이내, **영문요지 다음 국문요지**, 내용 일치, 각 한 문단, 표 · 식 · 인용 없음. 원고는 국문 또는 영문, "국문으로 작성 시 명확한 뜻의 전달이 필요한 경우에 한하여 괄호 안에 한자 또는 영자를 사용할 수 있다." SI 단위. "수학기호나 함수를 제외한 기호는 이탤릭체로 표기함을 원칙으로 한다." "그림, 사진, 표는 제목과 내용을 영문으로 표기한다." "모든 참고문헌은 영문표기를 원칙으로 하며 알파벳순으로 정리한다." 본문 인용은 성만, 3 인 이상은 "Wood et al.". "결론에서는 가장 주목할 만한 연구결과를 정리하고, 해당 연구 분야 및 유사한 분야에 대한 기여도를 제시한다."
주의: 이 쪽은 WebFetch 요약 모형이 인용한 문장이다. 조항 번호는 받지 못함 [미확인]. 확인 방법: 학회 누리집 투고지침 원문에서 조항 번호를 붙여 옮긴다.

### 5.2 한국물환경학회지 논문투고규정 [원문확인]

https://www.kswe.org/download/pages_jkswe/regulation/rule_03.pdf (PDF 에 적힌 최종 개정 2018-09-01; 학회 투고안내 페이지 https://www.kswe.org/pages_jkswe/jkswe_outline.vm 는 2024-11-25 기준으로 표시되어 PDF 와 최신판이 같은지 [미확인])
p.1 제4조 1항: 국문 또는 영문, A4, 글자 11, 행간 160 %. p.2 제4조 3항 ③: Abstract 는 영문, **200-250 단어 한 문단**, Key words 는 알파벳순 4-6 개. 심사용 논문파일 순서(국문 논문): Abstract(영문), Key words(영문), Introduction, Materials and Methods, Results and Discussion, Conclusion, References(영문), Table(영문), Figure(영문). 제4조 4항: 본문은 서론, 연구방법, 결과 및 고찰, 결론 순서, 아라비아 숫자 번호. 5항: 약어는 처음에 완전한 이름과 괄호 약어. 6항: 그림 · 사진 · 표의 제목과 내용은 모두 영문, 첫 자만 대문자, 그림 제목은 아래, 표 제목은 위. 7항: 모든 참고문헌은 영문으로 쓰고, 영어 이외 문헌은 공식 영문 표기를 쓰고 말미에 문헌 언어를 대괄호로 표시. p.3: 학술지 논문 형식 "저자. (출판년도). 논문제목, 학술지명, 권(호), 인용페이지." 학회 투고안내 페이지: 제목 · 저자 · 소속 · 초록 · 주제어 · 참고문헌 · 표와 그림은 반드시 영문.

### 5.3 국문 문체: 번역투와 한자어 [2차]

국립국어원 공공언어 자료: "개정 한눈에 알아보는 공공언어 바로 쓰기"(2020-03-17 등록) https://korean.go.kr/front/etcData/etcDataView.do?mn_id=&etc_seq=647&pageIndex=1 . 부록에 "다듬어 쓸 행정용어 100", "피해야 할 일본어 투 표현 50" 이 있다고 소개 페이지에 적혀 있음 [원문확인 소개 페이지, 본문 PDF 미열람]. "(무엇)을 필요로 하다" 를 영어 번역 투로 보고 "필요한" 으로 다듬는 예는 검색 요약으로만 확인 [2차]. "쉬운 공문서 쓰기 길잡이"(2022) https://www.korean.go.kr/front/etcData/etcDataView.do?mn_id=&etc_seq=700&pageIndex=1 [미확인].
한국수자원학회 지침이 한자 · 영자 병기를 "명확한 뜻 전달이 필요한 경우에 한하여" 허용하는 것(5.1 절)은 한자 병기를 절제하라는 근거로 쓸 수 있다.
개조식 금지: 학술 논문 본문을 개조식으로 쓰지 말라는 학회 규정 문장은 찾지 못했다 [미확인]. 국내 학술지 투고규정들이 본문 형식을 산문 절 구성(서론-방법-결과-결론)으로 정하고 있으므로 개조식은 관행상 맞지 않는다고 보는 것이 합리적이다 [추정].

국문 논문의 주어 [추정]: 한국어 학술문에서 "우리는" 은 드물고 "본 연구에서는" 이 관행이다. 따라서 "This study 주어, we 회피" 규칙은 **국문 원고에 한해 유지**하고, 영문 원고에는 we 와 능동태를 허용하도록 둘을 갈라 적는다. 다만 영문에서도 "This study" 를 행위 주체로 쓰는 것("This study calibrated ...")은 무생물 주어가 행위를 하는 구조라 어색하다는 비판이 있다(APA 의 3인칭 자기지칭 모호성 논지와 같은 방향) [추정].

### 5.4 학위논문 지침 [2차 또는 원문확인 표시]

서울대학교 암연구소 대학원 학위논문 작성 지침 https://cri.snu.ac.kr/graduate/academics/paper/guide [원문확인, 웹 요약 도구 경유]: "논문은 국문 또는 외국어로 작성할 수 있다. 단, 초록은 국문, 외국어 두 가지 모두 작성하여야 한다." 초록 1-2 쪽(목적 · 방법 · 결과 요약 · 결론). 판형 4×6 배판(19 × 26 cm). 참고문헌은 해당 분야 학술지에서 널리 쓰는 방식 하나를 골라 일관되게. 본 과업자의 소속 대학 · 학과 규정은 별도로 확인해야 한다 [미확인].
KAIST 학위논문 작성요령: 한글 초록 500 자 이내, 영문 초록 300 낱말 이내라는 검색 요약 [2차]. 원문 https://ee.kaist.ac.kr/ 의 "석박사학위논문 작성 및 제출요령_2022년.pdf" 미열람.

---

## 6. 작성 과정, 생산성, 공저

### 6.1 일정 글쓰기: Silvia "How to Write a Lot" [2차]

Silvia PJ (2007; 2판 2019) How to Write a Lot: A Practical Guide to Productive Academic Writing. APA LifeTools. 쪽 번호 [미확인]. 서평 https://muratbuffalo.blogspot.com/2018/04/book-review-how-to-write-lot-practical.html 과 Baylor 대학원 글쓰기센터 서평 https://blogs.baylor.edu/gwc/2020/06/30/book-review-how-to-write-a-lot-by-paul-j-silvia/ 에 따르면: 생산적인 저자는 일정을 정하고 지킨다. 몰아 쓰기(binge writing)를 배격한다. 목표를 정하고 날마다 진척을 기록한다. 초고 생성과 수정을 분리한다. 책이 인용하는 Boice 의 실험(1990 년 전후 [미확인])에서 일정 강제 조건은 자발적 조건보다 약 3.5 배, 금지 조건보다 약 16 배 많은 쪽수를 썼고, 새 착상도 더 자주 떠올랐다(서평 수치, [2차]).

### 6.2 거친 초고: Lamott "Shitty First Drafts" [2차]

Lamott A (1994) Bird by Bird: Some Instructions on Writing and Life. Pantheon. 해당 장 사본 https://wrd.as.uky.edu/sites/default/files/1-Shitty%20First%20Drafts.pdf (미열람). 첫 초고는 아무도 보지 않을 "아이의 초고" 로 다 쏟아내고 나중에 다듬는다는 취지. 과학 논문 문헌은 아니지만 Silvia 의 "생성과 수정 분리" 와 같은 방향이다.

### 6.3 지도교수 피드백 주기 [원문확인]

Whitesides p.1376: 학생이 개요(자료 · 그림 · 표 포함)를 내면 교수가 의견을 달아 돌려주고, 합의까지 보통 4-5 회(추가 실험 포함) 반복한 뒤 본문을 쓴다. Mensh & Kording 규칙 10: 동료 피드백으로 이야기의 약점을 찾고, 부분 편집보다 재구성을 택한다. Zhang 규칙 9 "Test the Water in Your Own Backyard", 규칙 10 "Build a Virtual Team of Collaborators" 도 내부 검토를 권한다 [원문확인 제목].

지침 반영 [추정]: 지도교수에게 본문이 아니라 "한 문단 한 문장 개요 + 그림 초안" 을 먼저 보낸다. 본문 교정은 개요 합의 후.

### 6.4 공저 기여: CRediT [원문확인 일부]

CRediT(Contributor Roles Taxonomy)는 ANSI/NISO Z39.104-2022 표준(2022-02-08 공표), 14 개 역할. https://credit.niso.org/ , https://www.niso.org/publications/z39104-2022-credit [2차: 14 역할 목록은 이번에 원문으로 옮기지 않음]. J. Hydrol.(필수), AGU(제출 시스템에서 표시), HESS(권장)가 채택 [원문확인, 3 장]. 역할 이름(Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Resources, Software, Supervision, Validation, Visualization, Writing: original draft, Writing: review and editing)은 조사자 기억에 의존하므로 [미확인]; 투고 전 credit.niso.org 에서 대조한다.

### 6.5 심사 대응: Noble (2017) [원문확인]

Noble WS (2017) "Ten simple rules for writing a response to reviewers" PLOS Comput Biol 13(10): e1005730. https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005730
1 개요를 먼저 쓰고 심사평 전체를 인용한다. 2 모든 심사자에게 정중하게. 3 불명확했다면 탓을 받아들이고 고친다. 4 바뀐 문장을 줄 번호와 함께 응답서에 직접 인용해 자족적으로 만든다. 5 모든 지적에 응답하고, 한 항목에 여러 지적이 있으면 쪼갠다. 6 심사평 · 응답 · 수정문을 서체로 구분한다. 7 가능하면 각 응답을 직답(예/아니오)으로 시작한다. 8 가능하면 요청대로 한다(요청 분석은 수행해 결과를 보고한 뒤 우려를 설명). 9 이전 판과 무엇이 바뀌었는지 분명히 한다. 10 필요하면 응답서를 두 번 쓴다(감정 정리용 초안과 제출본).

판정 [추정]: 현행 "3 범주" 분류(예: 수용 · 부분 수용 · 반론)는 Noble 규칙과 충돌하지 않는다. 다만 범주 분류보다 "모든 지적 응답, 직답 먼저, 수정문 인용과 쪽 · 줄" 이 더 직접적인 근거가 있으므로 이 형식을 필수로 올리고 3 범주는 내부 관리용 태그로 두는 편이 낫다.

---

## 7. 지침 개정 문안(초안) [추정: 위 근거를 조합한 제안]

영문 원고 문체. 능동태를 기본으로 하고 공저 논문에서는 we 를 쓴다(Nature; APA 7 4.16; AGU 는 APA 를 따름; Whitesides p.1377). 수동태는 행위자가 중요하지 않거나 문장의 이야기 주체가 대상일 때 쓴다(Gopen & Swan 재인쇄본 p.8). 방법 절의 보정 절차 서술은 수동태가 자연스러울 수 있다. "It was found that" 처럼 주어와 동사를 떨어뜨리는 구문은 피한다. 문장은 한 주장씩 짧고 직접적으로 쓴다(Nature; Plavén-Sigray et al. 2017). 무생물 "This study" 를 행위 주체로 되풀이하지 않는다.

국문 원고 문체. "본 연구에서는" 을 주어로 쓰는 관행을 유지한다. 번역투(이중피동, "(무엇)을 필요로 하다", "(무엇)에 있어서")를 피하고, 한자 · 영자 병기는 뜻 전달에 꼭 필요할 때만 괄호로 한다(한국수자원학회 투고지침).

구조. 하나의 중심 기여를 정하고 제목에 담는다(Mensh & Kording 규칙 1). 모든 문단과 절은 맥락-내용-결론 순서로 쓴다(규칙 3). 결과 소제목과 문단 첫 문장은 결과를 말하는 선언문으로 쓴다(규칙 7; Whitesides p.1376).

작성 순서. 개요(한 문단 한 문장, 그림 · 표 초안 포함)를 지도교수와 합의한 뒤(Whitesides p.1376) 결과 · 방법, 토의 · 결론, 서론, 초록 · 제목 순으로 쓴다. 초안 완성 후 역개요로 흐름을 점검한다(Caltech).

모형 성능 보고. 보정 · 검증 사상 분할 기준을 밝힌다(Klemeš 1986). NSE, PBIAS, RSR 과 수문곡선 · 산점도 그래프를 함께 보고한다(Moriasi et al. 2007 p.885). Moriasi 등급은 일 · 월 단위 유역 모형 기준임을 밝히고 사상 기반 SWMM 에 쓸 때 한계를 적는다(Moriasi et al. 2015 p.1763, p.1772). KGE 는 성분과 기준선(-0.41 또는 명시한 기준 모형)을 함께 적고 NSE 와 직접 비교하지 않는다(Knoben et al. 2019). 검증 성능이 보정보다 낮은 것은 흔하므로 숨기지 말고 보고한다(Niazi et al. 2017 p.04017002-22). 불확도 분석 방법과 범위를 명시한다.

통계. n, 검정통계량, 자유도, 정확한 p, 효과 크기, 신뢰구간을 함께 적고 p 문턱만으로 결론 내리지 않는다(ASA 2016).

부속물. 학술지별 필수 항목(3 장)을 투고 전 점검표로 둔다: J. Hydrol. Highlights · Data statement · CRediT · 생성형 AI 진술; AGU Key Points · Open Research · (권장) PLS; HESS Code/Data availability · Author contribution. 코드와 워크플로는 버전 DOI 로 인용한다(Hutton et al. 2016). 공개 업로드는 사전 승인.

심사 대응. 모든 지적에 응답하고, 직답으로 시작하며, 바뀐 문장을 쪽 · 줄과 함께 인용한다(Noble 2017).

---

## 8. 확인하지 못한 것과 확인 방법

APA 7 원문(apastyle.apa.org 봇 차단): 1인칭 4.16 절, 태 4.13 절, 시제 관례. 확인: 매뉴얼 실물 또는 브라우저에서 직접 열람.
Science, AGU Grammar and Style Guide 전문, PNAS 2024 1인칭 연구, ACS 지침: 403 차단. 확인: 기관 네트워크에서 브라우저 열람.
Klemeš (1986) 본문의 네 시험 이름과 쪽: 확인은 T&F 도서관 경유.
Schimel (2012) 원서 쪽 번호: 도서 실물.
Silvia 책 쪽 번호와 Boice 원 연구 서지: 도서 실물과 Boice(1990) Professors as Writers.
Gopen & Swan 원 학술지 쪽(550-558 안의 위치): JSTOR https://www.jstor.org/stable/29774235 .
J. Hydrol. Research Article 단어 제한: Guide for authors 의 Article types 절 전문.
한국수자원학회 투고지침 조항 번호: 학회 누리집 원문.
한국물환경학회지 규정 PDF(2018-09-01)와 2024-11-25 투고안내의 일치 여부: 학회 문의 또는 최신 서식 파일 대조.
CRediT 14 역할 정식 명칭: credit.niso.org 대조.
"방법 · 결과 먼저 쓴다" 는 작성 순서의 1 차 근거.
"심사 대응 3 범주" 의 문헌 근거.
SWMM 전용 보고 표준(학회 · 기관 문서).

---

## 9. 출처 목록

Mensh & Kording 2017, PLOS Comput Biol 13(9) e1005619: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619
Whitesides 2004, Adv Mater 16(15) 1375-1377: https://mason.gmu.edu/%7Ehjing2/advice%20for%20phd%20students/Writing%20a%20paper-George%20Whiteside.pdf
Gopen & Swan 1990, Am Sci 78(6) 550-558: https://www.usenix.org/sites/default/files/gopen_and_swan_science_of_scientific_writing.pdf
Schimel 2012 (2차 슬라이드): https://yncenter.sites.yale.edu/sites/default/files/xiao_wei_jun_2012.pdf
Nature summary paragraph: https://www.nature.com/documents/nature-summary-paragraph.pdf
Nature Portfolio "How to write your paper": https://www.nature.com/nature-portfolio/for-authors/write
Zhang 2014, PLOS Comput Biol 10(1) e1003453: https://pmc.ncbi.nlm.nih.gov/articles/PMC3907284/
Caltech reverse outlining: https://writing.caltech.edu/documents/24103/ReverseOutliningScientificWriting.pdf
APA first-person (2차): https://apastyle.apa.org/style-grammar-guidelines/grammar/first-person-pronouns
AGU Grammar and Style Guide: https://www.agu.org/publications/authors/journals/grammar-style-guide
AGU 구판 문법 지침: https://web.mst.edu/%7Esgao/research/resources/agu_grammar_style.pdf
AGU Text & Graphics Requirements: https://www.agu.org/publications/authors/journals/text-graphics-requirements
AGU Plain Language Summary: https://www.agu.org/publications/authors/journals/plain-language-summary
Copernicus Manuscript preparation: https://publications.copernicus.org/for_authors/manuscript_preparation.html
J. Hydrology Guide for authors: https://www.sciencedirect.com/journal/journal-of-hydrology/publish/guide-for-authors
Plavén-Sigray et al. 2017, eLife 6 e27725: https://elifesciences.org/articles/27725
Moriasi et al. 2007, Trans ASABE 50(3) 885-900: https://swat.tamu.edu/media/90109/moriasimodeleval.pdf
Moriasi et al. 2015, Trans ASABE 58(6) 1763-1785: https://web.ics.purdue.edu/%7Emgitau/pdf/Moriasi%20et%20al%202015.pdf
Gupta et al. 2009, J Hydrol 377 80-91 (투고본): https://ntrs.nasa.gov/api/citations/20090027858/downloads/20090027858.pdf
Knoben et al. 2019, HESS 23 4323-4331: https://hess.copernicus.org/articles/23/4323/2019/
Klemeš 1986, Hydrol Sci J 31(1) 13-24: https://doi.org/10.1080/02626668609491024
Niazi et al. 2017, J Sustain Water Built Environ 3(2) 04017002: https://swmm5.org/wp-content/uploads/2017/07/swmmreview.pdf
Pappenberger & Beven 2006, WRR 42 W05302: https://doi.org/10.1029/2005WR004820
Hutton et al. 2016, WRR 52(10) 7548-7555: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2016wr019285
Wasserstein & Lazar 2016, Am Stat 70(2) 129-133: https://doi.org/10.1080/00031305.2016.1154108
Noble 2017, PLOS Comput Biol 13(10) e1005730: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005730
CRediT: https://credit.niso.org/
한국수자원학회 국문논문 투고지침: https://www.kwra.or.kr/staticdata/static/publish/sbumission-rule/
한국물환경학회지 논문투고규정: https://www.kswe.org/download/pages_jkswe/regulation/rule_03.pdf
한국물환경학회지 투고안내: https://www.kswe.org/pages_jkswe/jkswe_outline.vm
국립국어원 공공언어 바로 쓰기: https://korean.go.kr/front/etcData/etcDataView.do?mn_id=&etc_seq=647&pageIndex=1
서울대 암연구소 학위논문 작성 지침: https://cri.snu.ac.kr/graduate/academics/paper/guide
Silvia 서평: https://muratbuffalo.blogspot.com/2018/04/book-review-how-to-write-lot-practical.html
Lamott 장 사본: https://wrd.as.uky.edu/sites/default/files/1-Shitty%20First%20Drafts.pdf
