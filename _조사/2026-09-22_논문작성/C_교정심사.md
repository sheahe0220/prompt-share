# 논문 교정 · 심사 대응 · 심사하기 조사 (지침 갱신용)

조사일 2026-09-22. 대상은 SWMM 모의 · 보정을 다루는 수문 연구자가 쓰는 영문 SCI 논문(Journal of Hydrology, WRR, HESS)과 국문 KCI 논문, 학위논문이다.

표기 규약. `[원문확인]` 은 이번 조사에서 원문(웹 페이지 또는 PDF 본문)을 직접 열어 해당 문장을 확인한 것, `[2차]` 는 검색 요약 · 2차 문헌에만 근거한 것, `[추정]` 은 조사자의 추론, `[미확인]` 은 확인하지 못한 것이다. 쪽 번호는 PDF 본문에서 확인한 경우에만 적는다. 웹 페이지는 쪽 번호가 없으므로 절 이름을 적는다.

결론을 먼저 적는다. 수문 분야 편집자들이 공동사설에서 반복해 지적한 것은 (1) 한 유역에 국한되어 일반화가 어려운 결과, (2) 혁신이 적은 모형 적용 논문의 범람, (3) 재현할 수 없는 계산(자료 · 코드 미공개), (4) 쪼개기 출판과 수정 없이 다른 학술지에 재투고하는 관행이다. Journal of Hydrology 는 2026 년 현행 투고 규정에서 "local or site-specific context" 에만 머무는 기술노트를 명시적으로 배제한다. 심사 대응 서식은 HESS 가 "(1) 심사 의견, (2) 저자 응답, (3) 원고 변경" 순서와 쪽 · 행 번호, 변경 표시본(track changes 또는 latexdiff) 제출을 요구한다. 심사를 맡았을 때 원고를 생성형 AI 에 올리는 것은 Elsevier 와 AGU 모두 금지한다. 학위논문을 학술지 논문으로 내는 것은 출처를 밝히면 중복게재가 아니라는 것이 연구윤리정보센터 FAQ 와 Elsevier · AGU 정책의 공통 입장이나, AGU 는 "어떤 언어로든" 먼저 출판된 논문을 다시 내는 것을 이중출판으로 본다. 국문 KCI 논문을 영문으로 옮겨 WRR 에 내는 길은 막혀 있다는 뜻이다.

---

## 1. 자기교정(self-editing) 방법

### 1.1 거꾸로 개요 짜기(reverse outlining)

완성된 원고를 문단 단위로 읽으며 각 문단의 요지를 한 줄로 적어 개요를 역으로 만든다. Oregon State University Writing Center 는 절차를 "Identify the thesis and topic", "Read one paragraph at a time", "Write the main point or idea of each paragraph", 그리고 완성된 개요에서 각 문단 요지의 관련성 · 순서 · 빈틈을 평가하는 4 단계로 제시한다. [원문확인] https://writingcenter.oregonstate.edu/reverse-outlining

같은 기법을 여러 대학 글쓰기센터가 안내한다. 한 방법은 문단마다 "무엇에 관한 문단인가(subject)" 와 "무슨 일을 하는 문단인가(function)" 두 문장을 적는 것이다. [2차] https://www.ou.edu/content/dam/writingcenter/docs/writing-guides/reverse_outline_handout.pdf , https://gcwritingcenter.commons.gc.cuny.edu/reverse-outlining/

[추정] SWMM 논문에 적용하면, 서론의 각 문단 요지만 이어 읽었을 때 "기존 보정 연구의 한계 → 본 연구의 질문 → 기여" 가 한 줄로 이어지는지, 결과 절의 문단 요지가 연구 질문의 순서와 같은지를 보는 점검이 된다.

### 1.2 편집 단계 나누기와 교정 기법

UNC Writing Center 는 편집을 내용(Content), 전체 구조(Overall Structure), 문단 구조(Paragraph Structure: "Does each paragraph have a clear topic sentence? Does each paragraph stick to one main idea?"), 명료성(Clarity), 문체(Style), 인용(Citations)의 층위로 나눈다. 교정 기법으로 소리 내어 읽기("forces you to say each word and also lets you hear how the words sound together"), 거꾸로 읽기, 시간 간격 두기("Put the paper aside for a few hours, days, or weeks"), 한 번에 한 종류의 오류만 찾기("Proofread for only one kind of error at a time")를 권한다. [원문확인] https://writingcenter.unc.edu/tips-and-tools/editing-and-proofreading/

[추정] 지침에는 "구조 → 문단 → 문장 → 단어 → 일관성" 순서의 5 회 통과를 두고, 뒤 단계에서 앞 단계 문제가 보이면 앞 단계로 돌아가는 규칙을 두는 것이 위 권고와 맞다.

### 1.3 Gopen & Swan: 독자 기대 원리(주제 위치 · 강세 위치)

출처: Gopen, G. D., & Swan, J. A. (1990). The Science of Scientific Writing. American Scientist, 78(6), 550-558. [원문확인] 재수록본 PDF https://www.usenix.org/sites/default/files/gopen_and_swan_science_of_scientific_writing.pdf (재수록 PDF 16 쪽 중 15 쪽에 요약 원칙). 원 게재 쪽수 550-558 은 검색 요약에서 확인했다. [2차] https://www.georgegopen.com/american-scientist-articles.html

재수록본 15 쪽의 7 원칙(원문 그대로):

1. Follow a grammatical subject as soon as possible with its verb.
2. Place in the stress position the "new information" you want the reader to emphasize.
3. Place the person or thing whose "story" a sentence is telling at the beginning of the sentence, in the topic position.
4. Place appropriate "old information" (material already stated in the discourse) in the topic position for linkage backward and contextualization forward.
5. Articulate the action of every clause or sentence in its verb.
6. In general, provide context for your reader before asking that reader to consider anything new.
7. In general, try to ensure that the relative emphases of the substance coincide with the relative expectations for emphasis raised by the structure.

저자들은 같은 쪽에서 이것들이 "rules" 가 아니며 기계적으로 따르면 수동태 회피 규칙을 맹종하는 것과 다를 바 없다고 적는다. 또 강세 위치는 문장 끝이며, 세미콜론으로 두 번째 강세 위치를 만들 수 있다고 설명한다(재수록본 5-6 쪽). [원문확인]

[추정] 수문 논문 예시. "NSE of 0.82 was obtained for the validation period by the calibrated model" 보다 "The calibrated model reproduced validation-period flows with an NSE of 0.82" 가 주어(모형)와 동사(reproduced)를 붙이고, 새 정보(0.82)를 강세 위치에 둔다.

### 1.4 단어 줄이기: Zinsser 와 Sword 의 "zombie nouns"

Zinsser 의 On Writing Well 에 "Clutter is the disease of American writing. We are a society strangling in unnecessary words, circular constructions, pompous frills and meaningless jargon." 이라는 문장이 있다. [2차] (책 원문 쪽 번호 [미확인]) https://www.publicationcoach.com/william-zinsser/ , http://sites.gatech.edu/higinbotham/wp-content/uploads/sites/359/2016/06/Zinsser.pdf

Helen Sword, "Zombie Nouns", New York Times Opinionator, 2012-07-23. 형용사나 동사에 "ity, tion or ism" 같은 접미사를 붙여 만든 명사화를 "zombie nouns" 라 부르고, 이것들이 "cannibalize active verbs, suck the lifeblood from adjectives" 한다고 쓴다. 예시로 든 동사가 calibrate → calibration 이다. 같은 글에서 명사화는 "At their best ... help us express complex ideas" 이지만 최악의 경우 소통을 방해한다고 적어 전면 금지가 아님을 밝힌다. [원문확인] https://www.lsu.edu/hss/english/files/university_writing_files/item51054.pdf (재수록 PDF 1 쪽)

Sword 의 단행본 Stylish Academic Writing (Harvard University Press) 의 출간연도는 검색 결과에서 2016 과 2012 가 엇갈린다. [미확인] 확인 방법: 출판사 서지 페이지.

[추정] SWMM 원고에서 자주 생기는 형태: "the calibration of the model was performed" → "we calibrated the model"; "an improvement in the reduction of peak flow" → "reduced peak flow further". 단 "calibration", "validation" 은 절 제목과 용어로는 정착된 명사이므로 문장 주어로 반복될 때만 동사로 되돌린다.

### 1.5 명사 연쇄(noun strings)

미국 CDC 의 쓰기 요령은 명사 연쇄를 "Seven Deadly Sins" 의 하나로 다룬다. [2차] https://www.cdc.gov/nceh/clearwriting/writing-tips/pdfs/2024/writing-tip-wed-03-06-2024-H.pdf . 연방 Plain Language 지침도 명사 연쇄를 피하라고 한다. [2차] https://webarchive.library.unt.edu/web/20170118202111mp_/http:/www.plainlanguage.gov/howto/guidelines/FederalPLGuidelines/writeNoNounStrings.cfm . 3-4 개 이하로 제한하고 전치사로 관계를 드러내라는 권고는 편집업체 블로그 수준의 출처다. [2차] https://www.aje.com/arc/editing-tip-avoiding-noun-string-overuse

[추정] 예: "LID facility runoff reduction performance evaluation method" 는 "a method for evaluating how much LID facilities reduce runoff" 로 푼다.

### 1.6 일관성 점검(용어 · 약어 · 수치 · 단위 · 그림표 번호 · 인용)

Copernicus(HESS 발행사) 원고 작성 지침 [원문확인] https://publications.copernicus.org/for_authors/manuscript_preparation.html :
- 약어는 제목에서 피하고, 초록에서 정의한 뒤 본문 첫 등장 때 다시 정의한다("defined in the abstract and then again at the first instance in the rest of the text").
- SI 단위, 분모의 단위는 음의 지수("10 km h-1 instead of 10 km/h", 원문은 위첨자).
- 10 미만 기수는 단어, 10 이상은 숫자.
- 그림 · 표는 아라비아 숫자로 순서대로 번호를 붙이고 본문에서는 "Fig." 을 쓴다(문장 첫머리 제외).
- 영국식 · 미국식 철자 중 하나로 통일.
- 행 번호 필수, Data availability 절 필수.

HESS 심사 기준 12 번 문항도 "Are mathematical formulae, symbols, abbreviations, and units correctly defined and used?" 이다. [원문확인] https://www.hydrology-and-earth-system-sciences.net/peer_review/review_criteria.html

AGU(WRR 발행) 는 문법 · 구두점 · 표 · 인용에서 APA 양식을 따른다고 밝힌다. [원문확인] https://www.agu.org/publications/authors/journals/grammar-style-guide

Journal of Hydrology 현행 투고 규정 [원문확인, 2026-09-22 열람] https://www.sciencedirect.com/journal/journal-of-hydrology/publish/guide-for-authors : 초록 250 단어 이하, 키워드 1-7 개, Highlights 3-5 개 · 각 85 자(공백 포함) 이하, 학술지명 약어는 LTWA, 프리프린트는 "preprint" 또는 서버명과 DOI 를 표시.

[추정] 참고문헌 교차 대조(본문 인용 ↔ 참고문헌 목록), 그림 번호 순서, 약어 정의 1 회, 단위 표기를 스크립트로 검사하는 것이 사람이 훑는 것보다 확실하다. 이것은 기존 `std-check` 의 점검.py 확장 후보다.

---

## 2. 논문이 거절되는 이유

### 2.1 출판사 · 편집자의 일반 진술

Elsevier Connect (Eleanne van Vliet, Tyrone Zhang, 2023-10-02) 는 데스크 리젝트의 흔한 원인을 "out of scope; problems with the manuscript's language or structure; failure to adhere to the guide for authors; lack of perceived novelty or impact; and/or ethical issues" 로 적는다. 수치 통계는 이 글에 없다. [원문확인] https://www.elsevier.com/connect/manuscript-rejected-five-insider-tips-to-see-you-to-success

데스크 리젝트 비율, "51.8 % 가 새로움 부족" 같은 수치는 검색 결과에서 편집업체 · 블로그만 제시했고 1 차 출처를 찾지 못했다. [미확인] 지침에 수치로 싣지 않는다. Nature 의 데스크 리젝트 비율도 2 차 사이트마다 값이 달라 [미확인].

Journal of Hydrology 의 게시 지표(2026-09-22 열람): 투고부터 첫 결정까지 10 일, 심사 후 결정까지 69 일, 게재 승인까지 159 일. [원문확인] https://www.sciencedirect.com/journal/journal-of-hydrology/about/insights . [추정] 첫 결정 중앙값이 10 일이라는 것은 상당수 원고가 외부 심사 없이 편집자 단계에서 결정된다는 뜻으로 읽을 수 있으나 채택률 · 데스크 리젝트율은 게시되어 있지 않다.

### 2.2 Journal of Hydrology 투고 규정의 명시 기준 [원문확인]

https://www.sciencedirect.com/journal/journal-of-hydrology/publish/guide-for-authors (2026-09-22 열람)
- Research Article: "should make a clear and substantive contribution to the hydrological sciences, advancing understanding through new data, methods, modelling approaches, or theoretical insights." 결론은 "Conclusions that reflect the scope of the evidence presented".
- Technical Note: "Be relevant to the broader hydrology community, not solely to a local or site-specific context", 그리고 "not simply a description of an application of existing methods".
- 심사는 단일 익명, 편집자 1 차 평가 후 적합하면 최소 2 인 심사.

[추정] SWMM 을 한 배수구역에 적용한 연구는 이 두 문장에 정면으로 걸린다. 서론과 결론에서 "다른 도시 유역으로 옮길 수 있는 무엇" 을 명시해야 한다.

Journal of Hydrology: Regional Studies 가 지역 사례 연구의 통로라는 설명은 검색 요약 수준이다. 창간 사설 PDF 는 열지 못했다. [2차] https://media.journals.elsevier.com/content/files/editorialhydrologyregionalstudies-18134837.pdf

### 2.3 수문 학술지 편집자 공동사설 [원문확인]

(a) Blöschl, G., Bárdossy, A., Koutsoyiannis, D., Kundzewicz, Z. W., Littlewood, I., Montanari, A., & Savenije, H. (2014). Joint Editorial "On the future of journal publications in hydrology". Hydrol. Earth Syst. Sci., 18, 2433-2435. https://hess.copernicus.org/articles/18/2433/2014/hess-18-2433-2014.pdf . HSJ, HESS, Hydrology Research, Journal of Hydrology, WRR 에 함께 실렸다(2433 쪽).
- 2433 쪽: 2013 년 한 해 5 개 학술지가 약 5000 편을 투고받아 약 2000 편을 게재.
- 2434 쪽: "Often, research papers in the field of hydrology focus on a particular catchment. Results are sometimes of local interest only and difficult to generalise." 이어서 Blöschl et al. (2013, p. 386) 을 인용해 결과가 독자에게 쓸모 있으려면 일반화할 수 있어야 한다고 적는다.
- 2434 쪽: 모형이 복잡해져 모형 구조 · 매개변수 · 입력자료가 논문에 실리지 않아 "The analyses presented in many papers can therefore no longer be repeated by other scientists." 자료와 코드 공개를 권장.
- 2434 쪽: 심사 부담에 관해, 논문당 2-3 건의 심사가 보통이면 저자도 자기 투고 수의 2-3 배 심사를 맡아야 한다.
- 2434 쪽: 최신 수문 문헌을 통합해 인용하라는 권고(오래된 문헌 위주의 인용 관행 지적).
- 2435 쪽: 자기 자료를 재활용해 새 연구처럼 내는 것은 비윤리. 방법 절의 작은 중복은 일부 학술지가 허용할 수 있고, 학위논문 · 보고서 · 학술대회 발표문 등 미심사 자료와의 중복은 "generally acceptable".
- 2435 쪽: 한 학술지에서 거절된 원고를 수정 없이 다른 학술지에 내면 같은 심사자에게 가는 일이 잦다. "Authors of rejected papers are therefore advised to take the suggestions of the referees very seriously and not to submit their papers to another journal without significant improvement." 최소 출판 단위(least publishable unit) 쪼개기 출판도 반대.

(b) Quinn, N., Blöschl, G., Bárdossy, A., et al. (2018). Joint editorial: Invigorating hydrological research through journal publications. Hydrol. Earth Syst. Sci., 22, 5735-5739. https://hess.copernicus.org/articles/22/5735/2018/hess-22-5735-2018.pdf (14 개 학술지 편집자 21 명, 2017-04 비엔나 회의)
- 5737 쪽: "salami publishing", 기여가 "incremental rather than significant" 인 조기 출판, 자기 작업을 최소 확장해 재포장하는 "recycling", 동시 다중 투고, 거절 원고를 심사 의견 반영 없이 즉시 재투고하는 관행, 심사자 · 편집자의 인용 강요(citation coercion)를 우려 사항으로 열거. 다저자 논문에 기여 진술을 넣으라고 권고.
- 5738 쪽: "submissions on climate impact studies, often with little novelty or innovation, have become something of a cottage industry. Equally disappointing is the proliferation of model applications with marginal innovation and/or little generality."
- 5738 쪽: 풀어야 할 문제는 관측 현상과 그 원인에 관한 것이고 "universal (i.e. not only apply to one catchment or region)" 이어야 한다.
- 같은 사설에서 14 개 학술지가 2017 년 46000 쪽을 게재(10 년 전 26000 쪽). (쪽 번호는 WebFetch 요약에서 확인, PDF 에서 쪽 재확인은 [미확인])

[추정] 두 사설을 SWMM 보정 논문의 거절 위험으로 번역하면: 한 유역 적용에 그침, 기존 보정 기법(수동 · PEST · SCE-UA 등)의 단순 적용, 코드 · 입력 파일 미공개로 재현 불가, 한 과업에서 여러 편을 쪼갬.

### 2.4 모형 논문에 대한 방법론적 비판 축 (심사자 지적의 근거 문헌)

- 성능지표 남용. Clark, M. P., Vogel, R. M., Lamontagne, J. R., et al. (2021). The Abuse of Popular Performance Metrics in Hydrologic Modeling. Water Resources Research, 57, e2020WR029001. https://doi.org/10.1029/2020WR029001 . 요지: "It is essential to quantify the sampling uncertainty in performance metrics when justifying the use of a model for a specific purpose and when comparing the performance of competing models." (1 쪽 Abstract), 결론에서 많은 연구의 결론이 NSE · KGE 의 불확실성 범위 안에 드는 값에 기대고 있어 "Such conclusions may thus not be justified." (11 쪽). 8-9 쪽은 하한 · 상한 기준(benchmark)과 함께 지표를 해석하라고 한다. [원문확인] 저자 공개본 https://bpb-us-e1.wpmucdn.com/sites.tufts.edu/dist/a/4406/files/2021/08/wrcr25486.pdf
- 동등결과성(equifinality). Beven, K. (2006). A manifesto for the equifinality thesis. Journal of Hydrology, 320(1-2), 18-36. https://doi.org/10.1016/j.jhydrol.2005.07.007 . 보정자료에 대해 받아들일 수 있는 모형이 여럿이라는 점을 더 진지하게 고려하라는 주장. [2차] (초록 요약만 확인)
- 다중 작업가설. Clark, M. P., Kavetski, D., & Fenicia, F. (2011). Pursuing the method of multiple working hypotheses for hydrological modeling. Water Resources Research, 47, W09301. https://doi.org/10.1029/2010WR009827 [2차]
- 재현성. Hutton, C., Wagener, T., Freer, J., Han, D., Duffy, C., & Arheimer, B. (2016). Most computational hydrology is not reproducible, so is it really science? Water Resources Research, 52(10), 7548-7555. https://doi.org/10.1002/2016WR019285 [2차]

[추정] 심사자가 SWMM 보정 논문에 흔히 던질 질문 목록(위 문헌에서 유도): 보정 · 검증 사상의 독립성, 매개변수 수 대비 사상 수, 동등결과 매개변수 세트의 존재 여부, NSE · KGE 의 표본 불확실성과 비교 기준, 입력 강우 불확실성, 결과의 전이 가능성. 이 목록은 문헌 요지에서 추론한 것이며 편집자가 직접 "SWMM" 을 거론한 원문은 찾지 못했다. [미확인]

### 2.5 WRR · HESS 의 평가 기준

HESS 심사 기준 [원문확인] https://www.hydrology-and-earth-system-sciences.net/peer_review/review_criteria.html
- 3 대 기준: Scientific significance("substantial contribution to scientific progress"), Scientific quality("Are the scientific approach and applied methods valid? Are the results discussed in an appropriate and balanced way?"), Presentation quality. 각 1(Excellent)-4(Poor).
- 15 개 세부 문항 중 저자 자기점검에 직결되는 것: 새 개념 · 도구 · 자료를 제시하는가(2), 결과가 해석 · 결론을 충분히 뒷받침하는가(5), 재현 가능한 수준으로 기술했는가(6), 선행연구에 정당한 공을 돌리고 자신의 기여를 밝혔는가(7), 제목 · 초록(8, 9), 줄이거나 합치거나 뺄 부분(13).

WRR 은 새로움 · 정확성 · 중요성 · 파급을 평가한다는 설명이 검색 요약에 있으나 Wiley 의 Aims and Scope 페이지는 접근 차단(403, 브라우저 접속 시 AGU 문체 지침으로 이동)으로 원문을 열지 못했다. [2차] https://agupubs.onlinelibrary.wiley.com/hub/journal/19447973/aims-and-scope/read-full-aims-and-scope

---

## 3. 심사 의견 대응

### 3.1 Noble (2017) 의 10 가지 규칙 [원문확인]

Noble, W. S. (2017). Ten simple rules for writing a response to reviewers. PLOS Computational Biology, 13(10), e1005730. https://doi.org/10.1371/journal.pcbi.1005730 (온라인 논문이라 쪽 번호 없음. 권호 중 호수 10 은 [2차])

1. 개요를 먼저 쓰고 심사 의견 전문을 인용한다. 여러 심사자의 공통 지적은 따로 묶는다.
2. 모든 심사자에게 정중하게.
3. 책임을 받아들인다. 오해는 내 글이 불분명했던 탓으로 본다.
4. 응답서만 읽어도 이해되게(self-contained). 바뀐 원고 문장을 행 번호와 함께 응답서에 인용한다.
5. 모든 지적에 응답한다. 한 항목에 여러 지적이 섞였으면 쪼갠다.
6. 서체 · 색 · 들여쓰기로 심사 의견, 응답, 원고 변경을 구분한다.
7. 응답을 직답(yes / no)으로 시작한다.
8. 가능하면 요청대로 한다. 회의적이어도 분석을 해 보고, 원고에 넣지 않을 이유는 그 결과 뒤에 설명한다.
9. 이전 판과 무엇이 달라졌는지 분명히 한다.
10. 필요하면 두 번 쓴다. 감정을 푸는 초안을 먼저 쓰고 며칠 뒤 제출용을 따로 쓴다.

또 심사자의 편향이 의심되면 응답서에서 따지지 말고 편집자에게 따로 알리라고 권한다. [원문확인]

### 3.2 학술지가 요구하는 서식

HESS [원문확인]
- 공개 토론(약 6 주, 보통 심사 의견 최소 2 건) 뒤, 토론 중에 응답하지 않았으면 4 주 안에 모든 의견에 대한 최종 응답을 낸다. https://www.hydrology-and-earth-system-sciences.net/peer_review/interactive_review_process.html
- 저자 응답은 "(1) comments from referees/community, (2) author's response, and (3) author's changes in manuscript" 순서. 같은 페이지.
- 수정본 제출 시 응답서를 하나의 PDF 로, 쪽 · 행 번호를 적고, 별도로 변경 표시본(Word track changes 또는 LaTeX latexdiff) PDF 를 낸다. https://www.hydrology-and-earth-system-sciences.net/submission.html
- 초기 심사(access review) 단계에서 편집자는 오탈자 · 그림 명료화 같은 기술적 수정만 요구할 수 있다. [원문확인]

[추정] HESS 는 심사 의견과 저자 응답이 EGUsphere 에 공개되므로 응답의 어조가 공개 기록으로 남는다. 다른 두 학술지보다 어조 관리가 더 중요하다.

Journal of Hydrology, WRR 의 응답서 서식 요구는 이번 조사에서 원문 문장을 확인하지 못했다. [미확인] 확인 방법: 수정 요청 메일의 지시문과 Editorial Manager 제출 화면.

### 3.3 어조와 이견 처리

Wiley 편집자 조언: "answer politely", "answer completely", "answer with evidence" (Williams 2004 를 인용). "where you disagree with a reviewer you must support that with evidence". 도발적 의견에 "do not 'rise to the bait'". [원문확인] https://www.wiley.com/en-us/publish/editor-insights/how-to-deal-with-reviewer-comments/ . 인용된 Williams (2004) 원문의 서지는 [미확인].

### 3.4 상충하는 심사 의견

원 출판사 문서에서 저자용 명시 지침은 찾지 못했다. Elsevier Connect 의 "It's a tie" 글(Tancock, 2019)은 편집자용이다. [원문확인] https://www.elsevier.com/en-au/connect/its-a-tie-how-to-deal-with-conflicting-recommendations-from-reviewers . 상충 사항을 목록으로 만들어 편집자에게 어떻게 할지 묻는다, 중간 타협을 시도하지 않는다는 권고는 편집업체 · 커뮤니티 글 수준이다. [2차] https://www.editage.com/insights/how-to-deal-with-conflicting-reviewer-comments-a-case-study

[추정] 실무 권고: 편집자 결정문이 우선순위를 주었으면 그것을 따르고, 응답서 첫머리 개요에 "Reviewers 1 and 2 made opposing suggestions on X; we followed Reviewer 1 because ..." 식으로 한 번 밝히고 양쪽 항목에서 서로 참조한다. Noble 규칙 1(공통 지적 묶기)과 규칙 4(자기완결)와 모순되지 않는다.

### 3.5 거절 이의신청(appeal)

Elsevier 편집 결정 이의신청 정책 [원문확인] https://www.elsevier.com/about/policies-and-standards/editorial-decision-appeals-policy
- 교신저자가 내고 모든 저자가 동의해야 함, 결정 통보 후 1 개월 안.
- "Only one appeal per submission will be considered and the appeal decision will be final."
- 외부 심사를 거친 원고만 대상, 데스크 리젝트는 제외.
- 학술지 정책 불이행으로 거절된 경우, 원고의 "interest, novelty, or suitability" 에 대한 견해 차이인 경우는 받아들이지 않음.
- 편집자 · 심사자 의견에 항목별 응답과 근거를 붙여야 함.

Elsevier Researcher Academy 는 "most appeals are not successful unless invited" 라고 적는다. [원문확인] https://researcheracademy.elsevier.com/publication-process/finding-right-journal/appealing-rejection-think-twice

AGU 이의신청 절차: 학술지 수신함에 원고 번호와 이의 내용을 보내면 Program Manager 가 편집자 · 부편집자 · 편집장에게 넘기고, 불복 시 정식 민원(Ethics Manager, VP Publications, Publications Committee 순). [원문확인] https://www.agu.org/publications/reviewers/policies (AGU Ethics and Appeals Procedures 절)

[추정] 새로움에 대한 견해 차이로 거절됐다면 Elsevier 에서는 이의신청 대상이 아니므로, 2014 공동사설 2435 쪽의 권고대로 심사 의견을 반영해 크게 고친 뒤 다른 학술지로 가는 것이 기본 경로다.

### 3.6 투고 서신(cover letter)

Springer Nature 지원 페이지 [원문확인] https://support.springernature.com/en/support/solutions/articles/6000245674-cover-letter
- 1 문단: 제목, 논문 유형, 배경과 연구 질문, 이유.
- 2 문단: 한 일, 주요 결과, 중요성.
- 3 문단: 학술지 독자가 관심을 가질 이유, aims and scope 와의 부합.
- 맺음: 교신저자, 학술지별 요구사항(윤리 기준 등).
- 필수 문장: "We confirm that this manuscript has not been published elsewhere and is not under consideration by another journal. All authors have approved the manuscript and agree with its submission to [journal]."

[추정] Journal of Hydrology 에 낼 때는 2.2 절의 문장("broader hydrology community, not solely ... local")에 대응하는 한 문장을 3 문단에 넣는다. 학위논문 기반이면 그 사실을 서신에 밝힌다(6.3 절).

---

## 4. 심사를 맡았을 때

### 4.1 Elsevier 심사자 지침 [원문확인]

https://www.elsevier.com/reviewers/how-to-review
- 원고 절(제목, 초록, 방법, 결과, 고찰, 참고문헌)별로 짧은 문단으로 정리. 내용 이해를 보여 주는 요약 문단, 새로움 · 영향에 대한 주요 인상, 구체적이고 사실에 근거한 개선 제안을 포함.
- 모든 자료를 기밀로 다루고 편집자 · 저자의 사전 허락 없이 공유하지 않으며, 이 의무는 출판 뒤에도 유지.

Elsevier 생성형 AI 정책(최종 갱신 2026-06 으로 표시) [원문확인] https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals
- 심사자: "Reviewers should not upload a submitted manuscript or any part of it into an AI tool as this may violate the authors' confidentiality and proprietary rights".
- 편집자도 같은 문장.
- 저자: AI 사용을 별도 선언문으로 밝힘. 기본 문법 · 철자 검사는 선언 불필요.

Journal of Hydrology 투고 규정도 같은 취지("does not currently allow academic editors and reviewers to upload an unpublished manuscript into a generative AI tool")를 적고, 심사 보고서 자체의 구조 · 언어 다듬기나 배경 문헌 검색에는 AI 를 보조로 쓸 수 있다고 한다. [원문확인] https://www.sciencedirect.com/journal/journal-of-hydrology/publish/guide-for-authors

주의: Elsevier 의 "How to review" 페이지 요약에는 "private AI tools" 사용과 선언문 서식이 언급되고, 정책 페이지는 "even 'private' tools" 도 경계한다는 취지로 요약되었다. 두 페이지의 표현이 완전히 같지 않을 수 있다. [판정보류] 확인 방법: 두 페이지 원문을 나란히 열어 비교. 보수적으로 "원고 어느 부분도 AI 에 넣지 않는다" 로 지침을 쓴다.

### 4.2 AGU 심사자 정책 (WRR) [원문확인]

https://www.agu.org/publications/reviewers/policies (Peer Review Policy, Reviewers: Ethical Obligations 절)
- "Large Language Models (LLMs) and other generative Artificial Intelligence (AI) tools cannot be used to review a manuscript on behalf of the invited reviewer."
- "Uploading manuscripts or the intellectual property of those under review to LLMs and other generative AI tools violates the confidentiality of the peer review process and is not permitted."
- 언어 다듬기 · 참고문헌 확인에 쓰더라도 심사자 자신의 글에 한정하고 원고 문장에는 쓰지 않으며, 사용 사실을 편집자에게 밝혀야 함.
- 원고는 기밀 문서로 다루고 남과 공유 · 논의하지 않음. 예외는 공식 공동심사(co-review) 로, 대학원생 · 박사후연구원 1-2 명이 참여하고 심사 양식에 이름을 올림.
- 이해충돌이 있으면 심사 수락 전에 알림. 인신공격 금지, 비판은 건설적이고 명확하게. AGU 는 "Reviewer Tone Table" 을 제공.
- WRR 등 AGU 학술지는 단일 익명 심사.

[추정] 사용자 규칙과의 연결: 전역 규칙의 "과업 자료를 공개 URL 로 올리지 마라" 와 같은 방향이다. 심사 원고는 Claude 를 포함한 어떤 생성형 AI 에도 넣지 않는다는 금지 조항을 지침에 명시해야 한다. 심사 보고서 초안을 사람이 쓴 뒤 그 초안의 영어만 다듬는 것도 AGU 는 허용하되 공개(disclosure) 를 요구한다.

### 4.3 HESS 심사

HESS 는 3.2 절의 15 문항과 3 대 기준을 심사자 양식으로 쓴다. 공개 토론에 심사 의견이 게시된다. [원문확인] (2.5 절 URL)

2014 공동사설 2434 쪽: 자기 투고 수의 2-3 배 심사를 맡으라는 권고. [원문확인]

---

## 5. 비원어민(한국어 화자) 영어와 국문 원고

### 5.1 한국 이공계의 영문 논문 쓰기 부담

Cho, D. (2009). Science journal paper writing in an EFL context: The case of Korea. English for Specific Purposes, 28(4), 230-239. 한국 이공계 대학원생 · 교수 설문에서 언어적 요소가 가장 문제로 인식되었고, 전체 구조와 문단 전개 같은 메타언어적 특징이 가장 중요하다고 인식되었다. 대학원생 74 % 가 언어 문제로 영문 학술지 쓰기 · 출판에 어려움을 겪었다는 수치는 검색 요약에서만 확인했다. [2차] https://www.sciencedirect.com/science/article/abs/pii/S0889490609000404 (403 으로 원문 미열람)

2014 공동사설 2434 쪽은 지역별로 투고 수와 "the quality of presentation" 이 크게 다르며 일부 지역의 출판 문화를 강화하는 공동 노력이 필요하다고 적는다. [원문확인]

### 5.2 관사 · 전치사

Kojima, T., & Popiel, H. A. (2023). Correct Use of Articles and Prepositions in Academic Writing: Advice for Non-Native English-Speaking Researchers. Journal of Korean Medical Science, 38(48), e417. https://doi.org/10.3346/jkms.2023.38.e417 . 특정 · 기언급 명사에 the, 불특정 가산 단수에 a/an(자음 · 모음 소리 기준), 일반화 · 불가산 명사에 무관사, in/into, in/at, at/on, between/among 구분을 다룬다. 관사 체계가 없는 언어 화자에게 어렵다고 설명. [원문확인] https://jkms.org/search.php?where=aview&id=10.3346/jkms.2023.38.e417&code=0063JKMS&vmode=FULL

### 5.3 "In this study" 반복 · 콩글리시

한국인 저자의 "In this study" 반복, 콩글리시 목록을 다룬 권위 있는 1 차 출처는 찾지 못했다. [미확인] 지침에는 경험 규칙으로 [추정] 표시를 달아 싣는다. [추정] 예: 한 문단에 "In this study" 가 두 번 이상이면 "We" 또는 "Here" 로 바꾼다. "hand phone", "fighting" 같은 일상 콩글리시보다 논문에서 실제로 문제 되는 것은 "rainfall intensity was strong" (→ high), "discharge amount" (→ discharge), "data was" (분야 관례에 따라 were) 같은 연어 · 수 일치 오류라고 본다. [추정]

### 5.4 참고 자원

Academic Phrasebank (University of Manchester, John Morley). 논문 구성(도입, 출처 언급, 방법, 결과, 고찰, 결론)과 기능(신중하게 말하기, 비판, 비교, 추세 기술, 인과 설명 등)별 표현 모음. 사이트는 항목이 "mostly content neutral and generic" 이라 그대로 써도 표절이 아니라고 밝힌다. [원문확인] https://www.phrasebank.manchester.ac.uk/

[추정] 교정업체 이용 시 고려: (1) 업체가 원고를 생성형 AI 에 넣는지 계약에서 확인(Elsevier 저자 정책상 AI 사용은 선언 대상), (2) 과업 발주처 자료가 섞였으면 전역 규칙에 따라 사전 승인, (3) 교정 후 용어 통일표(1.6 절)로 재점검. 업체 선택 기준에 관한 학술지 공식 문서는 이번에 찾지 않았다. [미확인]

### 5.5 국문(KCI) 원고 관례

한국수자원학회논문집 국문논문 투고지침 [원문확인] https://www.kwra.or.kr/staticdata/static/publish/sbumission-rule/
- 영문 초록 200 단어 이내.
- 키워드는 국문 · 영문으로 쓰고 "용어의 뜻과 나열순서가 서로 일치하여야 한다".
- 논문 · 총설 8 쪽, 기술 · 정책노트 6 쪽, 토의 · 답변 2 쪽 이내(인쇄 지면 기준, 그림 · 표 포함).
- SI 단위, 영문 단위는 관행적 대문자 외 소문자.
- "그림, 사진, 표는 제목과 내용을 영문으로 표기한다".
- 참고문헌은 저자 성의 알파벳순.
투고지침 전문은 논문집 52 권 1 호(2019-01) 1-11 쪽에 실렸다고 안내된다. [원문확인] https://www.kwra.or.kr/staticdata/static/publish/submission-guide/

번역투 · 문장 길이에 관한 국립국어원의 구체 조항은 이번에 원문으로 확인하지 못했다. 「한눈에 알아보는 공공언어 바로 쓰기(개정판)」가 관련 자료로 검색된다. [미확인] https://www.korean.go.kr/front/etcData/etcDataView.do?mn_id=&etc_seq=699&pageIndex=1 . 사용자 전역 규칙(이중피동, "에 있어서", "을 필요로 한다" 금지)이 이미 이 역할을 한다.

[추정] 국문 논문의 영문 초록은 본문 번역이 아니라 영문 독자가 초록만 읽고 판단할 수 있게 목적 · 방법 · 수치 결과 · 함의를 담는다. 그림 · 표가 영문이므로 본문 용어(국문)와 그림 용어(영문)의 대응표를 원고 작성 초기에 만든다.

---

## 6. 학위논문

### 6.1 연구부정행위 정의 (교육부)

「연구윤리 확보를 위한 지침」 제12조(연구부정행위의 범위). 2018 판(교육부훈령 제263호, 2018-07-17 시행) 본문 [원문확인] https://www.konkuk.ac.kr/sites/research/down/%EA%B5%90%EC%9C%A1%EB%B6%80%20%EC%97%B0%EA%B5%AC%EC%9C%A4%EB%A6%AC%20%ED%99%95%EB%B3%B4%EB%A5%BC%20%EC%9C%84%ED%95%9C%20%EC%A7%80%EC%B9%A8.pdf
- 표절: 타인의 독창적 아이디어나 창작물을 적절한 출처표시 없이 활용해 자신의 것처럼 인식하게 하는 행위. 타인 저작물을 번역해 출처 없이 쓰는 경우 포함(라목).
- 부당한 저자 표시: "지도학생의 학위논문을 학술지 등에 지도교수의 단독 명의로 게재·발표하는 경우" 포함(다목).
- 부당한 중복게재: "자신의 이전 연구결과와 동일 또는 실질적으로 유사한 저작물을 출처표시 없이 게재한 후, 연구비를 수령하거나 별도의 연구업적으로 인정받는 경우 등 부당한 이익을 얻는 행위".

현행판은 교육부훈령 제449호(2023-07-17 시행, 전부개정)로 안내된다. [2차] https://research.uos.ac.kr/node/4179 . 현행판의 조문 번호와 문구가 위와 같은지는 [판정보류]. 확인 방법: 국가법령정보센터 행정규칙 https://www.law.go.kr/LSW//admRulLsInfoP.do?admRulId=44335&efYd=0 에서 현행 조문을 연다.

### 6.2 표절검사 도구와 기준

- KCI 문헌 유사도 검사 서비스: KCI 또는 JAMS 계정으로 로그인, 비교 범위 선택, 인용 · 출처 표시 문장 포함 여부와 유사도 처리 기준 설정, 파일당 40 MB. [2차] https://check.kci.go.kr/ , 이용자 매뉴얼 https://check.kci.go.kr/common/KCI_User_Manual.pdf (PDF 미열람)
- 계명대 도서관 LibGuide: "유사도에 절대적인 % 기준은 없습니다", 유사도가 낮아도 출처 없이 쓰면 표절로 간주될 수 있음. 국내 문헌은 CopyKiller, 해외 문헌은 Turnitin 을 권함. [원문확인] https://kmu-kr.libguides.com/c.php?g=918453&p=6898458
- 대학원별 기준: 동서대 일반대학원 공지 등에서 20 % 초과 시 지도교수 검토의견을 받아 제출, 예비심사 · 본심사에 각 1 회 제출 사례가 검색된다. [2차] https://uni.dongseo.ac.kr/graduategeneral/index.php?pCode=MN8000063&mode=view&idx=1171 . 대학마다 다르므로 [추정] 소속 대학원 공지를 1 차 출처로 삼는다. 수원대 공지는 본문을 열지 못했다. [미확인]

### 6.3 학위논문 → 학술지 논문의 자기표절 · 중복게재

한국연구재단 지정 연구윤리정보센터 발췌 「학위논문의 연구윤리 FAQ」 [원문확인] https://kuccs.korea.ac.kr/bbs/cuhc/503/174743/download.do
- 문항 1(1 쪽): 국내 인문사회 · 이공계에서 학위논문과 학술지 논문 간 재출판 · 재사용은 중복게재나 자기표절로 판단하지 않는다. 다만 선행 출판관계를 후속 논문에 반드시 밝히고 인용해야 한다.
- 문항 2(1 쪽): 학위논문을 학술지 논문으로 내는 것은 "매우 장려되어야" 하나 후속 논문에 학위논문 출처를 밝혀야 하고, 일부 분야는 "본 논문은 OOO의 학위논문을 바탕으로 작성되었다" 는 명기를 요구한다. 투고 전 학술지 가이드라인 확인.
- 문항 5(3 쪽): 학위논문 출처를 밝히고 이를 인지한 상태에서 심사 · 편집인이 게재를 승인했다면 중복게재가 아니다. 활용 부분의 출처를 표시하고 출판 관계자에게 미리 알리는 것이 중요.
- 3 쪽 참조로 한국학술단체총연합회 「연구윤리 지침」(2010) 의 중복게재 예외 유형(두 학술지 편집인 동의로 다른 독자군에 출처를 밝혀 게재 등)을 싣는다.

국제 학술지 정책
- Elsevier: 초록, 공개 강연, "academic thesis", 전자 프리프린트 형태의 선행 공개는 선행 출판으로 보지 않는다. 동시 투고는 비윤리. 번역 등 일부 이중 게재는 조건을 갖추면 정당화될 수 있다. [원문확인] https://www.elsevier.com/about/policies-and-standards/publishing-ethics
- AGU(WRR): 구두 · 포스터 발표, 학회 초록, 공저자의 학위논문은 선행 출판이 아니다("student theses/dissertations of any co-authors"). 그러나 "Publication of an article in any language prior to submission to an AGU journal constitutes dual publication." [원문확인] https://www.agu.org/publications/reviewers/policies (Dual Publication Policy 절)
- 2014 수문 공동사설 2435 쪽: 학위논문 · 보고서 · 학술대회 발표문 같은 미심사 자료와의 중복은 "generally acceptable", 5 개 학술지 정책이 조금씩 다르다. [원문확인]

[추정] 실무 결론: (1) 학위논문 기반 SCI 투고는 허용되며, 서신과 감사의 글 또는 각주에 학위논문을 밝힌다. (2) 이미 KCI 에 국문으로 게재한 내용을 영문으로 옮겨 WRR 에 내는 것은 AGU 기준으로 이중출판이다. Journal of Hydrology 는 Elsevier 의 번역 게재 조건을 따로 확인해야 한다. (3) 학위논문에서 여러 편을 낼 때는 2018 공동사설 5737 쪽의 "salami publishing" 비판을 의식해 각 편이 독립된 질문과 결론을 갖게 한다. (4) 유사도 검사에서 자기 학위논문과의 중복이 높게 나오는 것은 예상되는 일이므로 서신에서 미리 밝힌다.

### 6.4 학위논문 구조 · 인준

대학별 학위논문 작성 지침(구조, 인준지 양식)은 이번 조사 범위에서 원문을 확인하지 못했다. [미확인] 확인 방법: 소속 대학원 "학위청구논문 작성 요령" 공지.

---

## 7. 지침 반영 제안 (모두 [추정])

아래는 위 근거를 사용자 지침(`13_논문.md` 등)에 옮길 때의 초안이다. 근거가 [원문확인] 인 항목을 괄호로 붙였다.

1. 교정 5 회 통과: 구조(거꾸로 개요) → 문단(주제문 1 개, UNC) → 문장(Gopen & Swan 7 원칙) → 단어(명사화 · 명사 연쇄) → 일관성(약어 1 회 정의, 단위 음의 지수, 그림표 순서, 인용 대조; Copernicus). 마지막에 소리 내어 읽기.
2. 투고 전 자기심사: HESS 15 문항을 그대로 체크리스트로 쓴다. 특히 2(새로움), 5(결론 뒷받침), 6(재현성), 7(기여 구분).
3. SWMM 논문 거절 위험 점검: 한 유역에 그치는가(JoH 기술노트 규정, 2014 · 2018 공동사설), 기존 방법 단순 적용인가(JoH), 성능지표의 표본 불확실성과 기준을 보였는가(Clark 2021), 재현 가능한가(자료 · 코드 공개; 2014 공동사설 2434 쪽).
4. 응답서: Noble 10 규칙 + HESS 3 단 서식(의견 · 응답 · 변경, 쪽 · 행 번호, 변경 표시본). 감정 초안과 제출본 분리.
5. 이의신청: Elsevier 는 1 회, 1 개월, 새로움 견해 차이는 대상 아님. 기본 경로는 수정 후 다른 학술지.
6. 심사 수락 시: 원고를 어떤 생성형 AI 에도 넣지 않는다(Elsevier, AGU). 자기 심사문 다듬기에 쓰면 편집자에게 밝힌다(AGU). 이해충돌은 수락 전에 알린다.
7. 학위논문 → 논문: 학위논문 출처 명기, 서신에 밝힘. KCI 국문 게재분의 영문 재게재 금지(AGU). 대학원 유사도 기준은 소속 대학 공지 확인.

---

## 8. 한계와 확인하지 못한 것

- 데스크 리젝트율과 거절 사유별 비율의 1 차 통계를 찾지 못했다. 블로그 수치(51.8 %, 30-85 % 등)는 싣지 않았다. [미확인]
- WRR Aims and Scope, AGU 심사 기준(review-criteria) 페이지, Journal of Hydrology: Regional Studies 창간 사설은 접근이 막혀 원문을 열지 못했다.
- Journal of Hydrology · WRR 의 응답서 서식 요구는 확인하지 못했다.
- Beven (2006), Clark et al. (2011), Hutton et al. (2016), Cho (2009) 는 서지와 초록 요약만 확인했다.
- 교육부 지침은 2018 판 본문만 열었다. 2023 전부개정판 조문은 [판정보류].
- 한국인 저자 특유 오류("In this study" 반복, 콩글리시)의 권위 있는 출처, 국립국어원 번역투 조항은 찾지 못했다.
- Elsevier 심사자 페이지와 AI 정책 페이지의 "private AI tools" 관련 표현 차이는 [판정보류].

---

## 9. 출처 목록 (확인 수준)

| 출처 | URL | 수준 |
|---|---|---|
| Noble 2017, PLOS Comput Biol 13 e1005730 | https://doi.org/10.1371/journal.pcbi.1005730 | 원문확인 |
| Gopen & Swan 1990, Am Sci 78:550-558 (재수록 PDF) | https://www.usenix.org/sites/default/files/gopen_and_swan_science_of_scientific_writing.pdf | 원문확인 |
| Sword 2012 NYT "Zombie Nouns" (재수록) | https://www.lsu.edu/hss/english/files/university_writing_files/item51054.pdf | 원문확인 |
| Zinsser, On Writing Well | https://www.publicationcoach.com/william-zinsser/ | 2차 |
| UNC Writing Center, Editing and Proofreading | https://writingcenter.unc.edu/tips-and-tools/editing-and-proofreading/ | 원문확인 |
| Oregon State, Reverse Outlining | https://writingcenter.oregonstate.edu/reverse-outlining | 원문확인 |
| CDC noun strings | https://www.cdc.gov/nceh/clearwriting/writing-tips/pdfs/2024/writing-tip-wed-03-06-2024-H.pdf | 2차 |
| Copernicus manuscript preparation | https://publications.copernicus.org/for_authors/manuscript_preparation.html | 원문확인 |
| HESS review criteria | https://www.hydrology-and-earth-system-sciences.net/peer_review/review_criteria.html | 원문확인 |
| HESS interactive review | https://www.hydrology-and-earth-system-sciences.net/peer_review/interactive_review_process.html | 원문확인 |
| HESS submission | https://www.hydrology-and-earth-system-sciences.net/submission.html | 원문확인 |
| Journal of Hydrology guide for authors (2026-09-22) | https://www.sciencedirect.com/journal/journal-of-hydrology/publish/guide-for-authors | 원문확인 |
| Journal of Hydrology insights | https://www.sciencedirect.com/journal/journal-of-hydrology/about/insights | 원문확인 |
| Blöschl et al. 2014, HESS 18:2433-2435 | https://hess.copernicus.org/articles/18/2433/2014/hess-18-2433-2014.pdf | 원문확인 |
| Quinn et al. 2018, HESS 22:5735-5739 | https://hess.copernicus.org/articles/22/5735/2018/hess-22-5735-2018.pdf | 원문확인 |
| Clark et al. 2021, WRR 57 e2020WR029001 | https://bpb-us-e1.wpmucdn.com/sites.tufts.edu/dist/a/4406/files/2021/08/wrcr25486.pdf | 원문확인 |
| Beven 2006, J Hydrol 320:18-36 | https://doi.org/10.1016/j.jhydrol.2005.07.007 | 2차 |
| Clark, Kavetski, Fenicia 2011, WRR 47 W09301 | https://doi.org/10.1029/2010WR009827 | 2차 |
| Hutton et al. 2016, WRR 52:7548-7555 | https://doi.org/10.1002/2016WR019285 | 2차 |
| Elsevier Connect 2023-10-02 rejection tips | https://www.elsevier.com/connect/manuscript-rejected-five-insider-tips-to-see-you-to-success | 원문확인 |
| Elsevier How to review | https://www.elsevier.com/reviewers/how-to-review | 원문확인 |
| Elsevier GenAI policies (2026-06 갱신 표시) | https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals | 원문확인 |
| Elsevier publishing ethics | https://www.elsevier.com/about/policies-and-standards/publishing-ethics | 원문확인 |
| Elsevier appeals policy | https://www.elsevier.com/about/policies-and-standards/editorial-decision-appeals-policy | 원문확인 |
| Elsevier Researcher Academy, appeals | https://researcheracademy.elsevier.com/publication-process/finding-right-journal/appealing-rejection-think-twice | 원문확인 |
| AGU publications and ethics policies | https://www.agu.org/publications/reviewers/policies | 원문확인 |
| AGU grammar and style guide | https://www.agu.org/publications/authors/journals/grammar-style-guide | 원문확인 |
| Wiley, How to deal with reviewer comments | https://www.wiley.com/en-us/publish/editor-insights/how-to-deal-with-reviewer-comments/ | 원문확인 |
| Springer Nature cover letter | https://support.springernature.com/en/support/solutions/articles/6000245674-cover-letter | 원문확인 |
| Academic Phrasebank | https://www.phrasebank.manchester.ac.uk/ | 원문확인 |
| Kojima & Popiel 2023, JKMS 38 e417 | https://doi.org/10.3346/jkms.2023.38.e417 | 원문확인 |
| Cho 2009, ESP 28(4):230-239 | https://www.sciencedirect.com/science/article/abs/pii/S0889490609000404 | 2차 |
| 한국수자원학회 국문논문 투고지침 | https://www.kwra.or.kr/staticdata/static/publish/sbumission-rule/ | 원문확인 |
| 교육부 연구윤리 확보를 위한 지침(2018 판) | https://www.konkuk.ac.kr/sites/research/down/%EA%B5%90%EC%9C%A1%EB%B6%80%20%EC%97%B0%EA%B5%AC%EC%9C%A4%EB%A6%AC%20%ED%99%95%EB%B3%B4%EB%A5%BC%20%EC%9C%84%ED%95%9C%20%EC%A7%80%EC%B9%A8.pdf | 원문확인 |
| 교육부 지침 2023 전부개정 안내 | https://research.uos.ac.kr/node/4179 | 2차 |
| 학위논문의 연구윤리 FAQ(연구윤리정보센터 발췌) | https://kuccs.korea.ac.kr/bbs/cuhc/503/174743/download.do | 원문확인 |
| 계명대 LibGuide 유사도검사 | https://kmu-kr.libguides.com/c.php?g=918453&p=6898458 | 원문확인 |
| 동서대 일반대학원 유사도 공지 | https://uni.dongseo.ac.kr/graduategeneral/index.php?pCode=MN8000063&mode=view&idx=1171 | 2차 |
| KCI 문헌 유사도 검사 | https://check.kci.go.kr/ | 2차 |
