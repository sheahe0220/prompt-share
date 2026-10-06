# 논문 작성 · 수정 · 심사에서의 AI 활용: 정책 · 실무 · 도구 · 검증 API · 보안

조사일 2026-09-22. 조사자 Claude(서브에이전트). 대상 독자는 SCI(Journal of Hydrology 등)와 KCI 논문을 쓰는 수문 연구자.

표지 규칙: [원문확인] 은 이번 조사에서 1차 출처 페이지를 직접 받아 문구를 확인한 것, [2차] 는 언론 · 요약 · 검색결과 발췌로만 확인한 것, [추정] 은 조사자 판단, [미확인] 은 찾지 못한 것이다. 확인 방법은 curl 로 페이지를 받아 본문을 추출하거나(2026-09-22), WebFetch, `gh api`, arXiv export API 를 썼다.

## 0. 결론 요약

첫째, 주요 출판사는 모두 AI 를 저자로 인정하지 않고, 저자가 책임을 지며, 심사자가 미공개 원고를 공개형 AI 에 올리는 것을 금지한다. 차이는 공개 위치와 면제 범위다. Elsevier(Journal of Hydrology)는 참고문헌 앞의 별도 선언 절, AGU 와 COPE 는 Materials and Methods, IEEE 는 Acknowledgments, HESS(Copernicus)는 Methods 또는 Acknowledgements 다. 2026 년 들어 Elsevier 와 Springer Nature 가 "심사자는 private AI 만 보조적으로 쓸 수 있다"는 쪽으로 문구를 바꿨다. 한국은 2026-09-20 과기정통부가 「국가연구개발 AI 연구윤리 가이드」를 확정했다고 보도됐다[2차].

둘째, 가장 큰 실패는 허위 참고문헌이다. 2023 년 연구에서 GPT-3.5 인용의 55 %, GPT-4 인용의 18 % 가 존재하지 않았고, 2025 년 NeurIPS 채택 논문 약 1 % 에서 허위 인용이 발견됐다. 사람의 동료심사는 이를 거의 걸러내지 못했다.

셋째, 참고문헌 검증은 무료 API 로 자동화할 수 있다. Crossref 로 시험한 결과 실재 논문은 score 82.95 로 1 위에 정확히 잡히고, 지어낸 서지는 score 약 40 의 엉뚱한 논문이 돌아온다. 즉 "결과가 나왔다"가 아니라 "제목 · 저자 · 연도가 일치하는가"로 판정해야 한다.

넷째, Claude Code 로 원고를 다루는 것 자체가 Anthropic 서버로의 전송이다. 소비자 요금제는 학습 사용 설정을 확인해야 하며, 심사 원고는 넣지 않는다.

## 1. 학술지 · 출판사 AI 정책

### 1.1 Elsevier (Journal of Hydrology 포함) [원문확인]

출처: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals (curl · WebFetch 2026-09-22). WebFetch 요약은 최종 갱신을 "June 2026" 으로 보고했으나 HTML 원문에서 날짜 문자열은 직접 확인하지 못했다[판정보류: 페이지 하단 "Last updated" 를 브라우저로 확인].

공개 위치와 문안. 원문: "Authors should disclose the use of AI tools for manuscript preparation in a separate AI declaration statement included in their manuscript upon submission. This statement will appear in the published article". 권장 절 제목은 "Declaration of generative AI and AI-assisted technologies in the manuscript preparation process", 권장 문안은 "During the preparation of this work, the author(s) used [NAME OF TOOL / SERVICE] in order to [REASON]. After using this tool/service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the published article." 도구명, 목적, 감독 정도를 기록하라고 한다. WebFetch 요약은 이 절이 참고문헌 앞에 놓인다고 전했다.

면제. "Basic checks of grammar, spelling and punctuation do not need a declaration statement. However, when an AI tool makes substantive changes to sentence structure or organization of a part of the text, this should be disclosed." 장애 보조기술과 참고문헌 관리자의 기본 기능도 면제다. 따라서 Claude 로 문단 구조를 고쳤다면 선언 대상이다.

저자. "Authors should not list AI tools as an author or co-author, nor cite AI tools as an author."

그림. 흐름도 · 개념도 같은 설명용 그림은 허용(공개 필요). 자료 시각화는 "only when the visual output is directly derived from underlying data" 이고 Methods 에 모델 · 버전 · 개발사를 적는다. 1 차 관측 영상(현미경, 영상의학 등)의 생성 · 변형은 금지. "General-purpose generative AI image tools must not be used to create graphical abstracts." 표지 그림은 사전 허가.

심사자. "Reviewers should not upload a submitted manuscript or any part of it into an AI tool". 동시에 "reviewers should only use private AI tools to assist in the review process" 이고, 심사보고서에 AI 사용을 공개해야 한다. "private" 의 정의는 입력을 보존 · 재사용 · 공유 · 학습하지 않는 도구이며, 무료 도구는 기본값이 private 이 아닌 경우가 많으니 유료 · 기관판 · 로컬 모델을 우선하라고 권한다. [추정] 원고 업로드 금지와 private 도구 허용이 함께 있으므로, 안전한 해석은 "원고 본문은 어떤 AI 에도 넣지 않고, 자신이 쓴 심사 의견의 문장 다듬기에만 private 도구를 쓴다"이다.

### 1.2 Springer Nature (Nature Portfolio) [원문확인]

출처: https://www.nature.com/nature-portfolio/editorial-policies/ai (curl 2026-09-22, 페이지에 날짜 표기 없음).

현행 페이지는 도구가 아니라 위험 수준으로 판단하는 신호등 체계다. Green(허용, 공개 권장)에는 "Using an LLM to polish or refine the language", "Suggesting structure or formatting of manuscript sections" 가 있다. Amber(주의, 인간 감독 · 검증 · 공개 조건 허용)에는 "Extensive copy editing or writing support", "Explaining outputs from statistical models in plain language", "Recommending statistical tests or modelling approaches" 가 있다. Red(불허)에는 "Generating hypotheses, analyses or conclusions and presenting them as human-derived", "Assigning authorship or accountability to AI systems or tools", "Creating photorealistic images (deepfakes)" 가 있다. 공통 원칙은 "Manuscripts, peer review reports, and sensitive data must not be shared with unsecured or public AI systems." 심사자는 "May use AI to support peer review but must not upload manuscript content to unsecured or public AI tools" 이고 "Must not delegate critique or judgement to AI systems".

이전 문구(LLM 사용은 Methods 절에 기록, "AI assisted copy editing" 은 공개 불요)는 검색 결과와 Nature 2025-05-14 기사에서 확인된다[2차: https://www.nature.com/articles/d41586-025-01463-8]. 현행 페이지에는 공개 위치가 명시돼 있지 않으므로, Springer 계열 학술지(예: Water Resources Management, Stochastic Environmental Research and Risk Assessment)는 개별 학술지 투고규정을 확인해야 한다[추정].

### 1.3 Wiley 와 AGU (Water Resources Research 등) [원문확인]

Wiley 출처: https://www.wiley.com/en-us/publish/article/ai-guidelines/ (curl 2026-09-22). "Authors must disclose the use of AI Technologies when submitting their Material to a Wiley-published journal." 목적, 핵심 논지나 결론에 영향을 줬는지, 어떻게 검증했는지를 기록해 두라고 한다. 또 AI 제공자가 입력을 학습하는 권리를 얻지 않는지 약관을 확인하라고 한다("including the right to ingest or 'train'"). 미공개 내용은 "appropriate privacy controls" 가 있는 도구를 쓰라고 한다. Wiley 가 심사에서 제한적 사용을 공개 조건으로 허용한다는 내용은 Nature 2025-05-14 기사에서만 확인했다[2차].

AGU 출처: https://www.agu.org/publications/authors/policies (curl 2026-09-22). 저자는 AI 를 원고 작성, 그림 제작, 자료 수집 · 분석에 쓴 경우 "which AI tool was used and how it was used, in the Materials and Methods (or similar section)" 을 공개한다. 심사자는 "Uploading manuscripts or the intellectual property of those under review to LLMs and other generative AI tools violates the confidentiality of the peer review process and is not permitted." 언어 다듬기나 참고문헌 점검은 "limited to the reviewer's own text, not the text of the manuscript" 로 한정한다.

### 1.4 Copernicus / HESS [원문확인]

출처: https://www.hydrology-and-earth-system-sciences.net/policies/ai_policy.html (curl 2026-09-22, 날짜 표기 미확인).

가장 엄격한 편이다. 문법 · 가독성 보조는 공개 불요다. 그 이상은 "generative" 로 보고 공개하며 "This can be done either in the Methods or in the Acknowledgements sections". 핵심 제한은 "Generative AI must not be used for text or interpretations" 이다. 삽화 · 개념도 생성은 도구를 인용하면 허용된다. 투고 등록 시 공개 여부를 인증해야 한다. 심사자와 편집자는 원고와 심사보고서를 AI 에 올리면 안 되고("may not provide appropriate attribution to the authors as required by the CC BY distribution licence"), "It is prohibited to use AI tools to generate referee comments or reports."

[추정] HESS 에 낼 원고에서는 Claude 로 문단을 새로 쓰게 하는 사용이 정책 위반 소지가 있다. 저자가 쓴 문장의 교정 수준에 머물러야 한다.

### 1.5 Taylor & Francis [원문확인]

출처: https://taylorandfrancis.com/our-policies/ai-policy/ (curl 2026-09-22). 공개문에 "the full name of the tool used (with version number), how it was used and the reason for use" 를 요구하고, 논문은 "a specific statement of AI usage disclosure" 를 넣는다. 저자 불가. 자료 시각화와 개념도는 허용, 연구 결과 영상의 생성 · 조작은 금지. 심사자와 편집자는 "must not upload files, images, or information from unpublished manuscripts into Generative AI tools", 심사보고서 생성도 금지, 심사 문장 다듬기만 허용.

### 1.6 IEEE [원문확인]

출처: https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/ (curl 2026-09-22). AI 생성 콘텐츠(글, 그림, 코드)는 "shall be disclosed in the acknowledgments section", 해당 절과 사용 정도를 밝힌다. 편집 · 문법 보조는 "disclosure as noted above is not required, but recommended." 실무 팁도 있다: "If using an AI system for editing and grammar, exclude the reference section; otherwise, the tool may make unwanted changes." 심사 원고는 "shall not be processed through a public platform".

### 1.7 ICMJE 와 COPE

ICMJE [원문확인]: https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html (WebFetch 2026-09-22, 개정일 미표기). 공개는 "in both the cover letter and the submitted work in the appropriate section". 챗봇은 저자 불가. "Referencing AI-generated material as the primary source is not acceptable." "Nondisclosure of AI use may require corrective action and may be construed as misconduct in some circumstances." 심사자 페이지(https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-reviewers.html): 기밀을 보장할 수 없는 AI 에 원고를 올리는 것은 "unless such use of AI is explicitly permitted by journals" 금지될 수 있다.

COPE [2차]: https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools 는 Cloudflare 차단(403)으로 직접 받지 못했다. 다만 AGU 정책이 COPE 문구를 그대로 인용한다: AI 는 책임을 질 수 없어 저자가 될 수 없고, 사용 시 Materials and Methods(또는 유사 절)에 공개하며, AI 생성 부분까지 저자가 책임진다.

### 1.8 정책 대조표

| 기관 | 공개 위치 | 교정 면제 | 심사자 원고 업로드 |
|---|---|---|---|
| Elsevier | 별도 선언 절 | 문법 · 철자만 | 금지, private 도구만 보조 |
| Springer Nature | 현행 미명시(구: Methods) | 구 정책상 면제 | 공개형 · 비보안 도구 금지 |
| AGU / Wiley | Materials and Methods | [미확인] | 금지 |
| HESS | Methods 또는 Acknowledgements | 면제, 단 생성형 글쓰기 금지 | 금지, 보고서 생성도 금지 |
| T&F | 별도 공개문(버전 포함) | [미확인] | 금지 |
| IEEE | Acknowledgments | 면제(공개 권장) | 공개 플랫폼 금지 |
| ICMJE | 커버레터 + 본문 | 해당 조항 미확인 | 학술지 허용 없으면 금지 |

### 1.9 한국

한국연구재단 권고사항(2024-03) [원문확인, 일부]: 웹진 https://webzine.nrf.re.kr/magazine/2403/sub_1_01.php 에 「한국연구재단, 생성형 인공지능(AI) 도구의 책임 있는 사용을 위한 권고사항」이 실려 있다. 받은 본문에서 확인한 것은 평가위원이 ChatGPT 등에 과제 정보를 업로드하는 행위에 대한 경고, 연구개발계획서와 보고서 작성에 생성형 AI 를 쓴 경우의 조치 조항 머리, 향후 수정 · 보완 예정 문구다. 조항 전문은 이미지로 되어 있어 추출하지 못했다[판정보류: 웹진 페이지를 브라우저로 열어 확인].

「대학 연구자를 위한 생성형 AI 연구윤리 가이드」(한국연구재단) [2차]: 서울대 학과 공지들(https://ie.snu.ac.kr/notice/?mod=document&uid=6291 등)이 발간을 안내하며, 연구 설계 · 수행 · 보고 단계별 활용, AI 활용 후 인용, 체크리스트를 담고 연구윤리정보포털(cre.nrf.re.kr) CRE발간물에서 열람한다고 적었다. 발간일은 [미확인].

과기정통부 「국가연구개발 AI 연구윤리 가이드」 [2차]: 교수신문 2026-09-21 기사(https://www.kyosu.net/news/articleView.html?idxno=210621)에 따르면 국가과학기술자문회의 운영위원회 심의를 거쳐 확정됐다(기사 표현 "지난 20일", 즉 2026-09-20). AI 는 "도구"이고 저자 · 발명자 지위를 가질 수 없으며, 모델 · 버전 · 시기 · 목적을 보고서나 논문에 공개하도록 권고하고 "AI 활용 여부 공개 서식"을 담았다. 평가위원 · 심사위원이 원고를 외부 AI 에 입력하는 행위는 제한되고, 은닉 프롬프트는 연구부정행위에 해당할 수 있다고 명시했다. 자가진단표에 허위 참고문헌, 미발표 자료와 특허 예정 기술의 상용 AI 입력 여부가 들어 있다. 원문은 msit.go.kr 과 kistep.re.kr 에 있다고 한다[판정보류: 원문 PDF 를 받아 쪽 번호와 함께 인용할 것].

한국수자원학회: 투고지침 페이지 https://www.kwra.or.kr/staticdata/static/publish/sbumission-rule/ 를 curl 로 받아(2026-09-22) "AI · 인공지능 · 생성형 · ChatGPT · LLM" 을 검색한 결과 해당 조항은 0 건이었다[원문확인]. 별도 연구윤리규정에 있는지는 [미확인]. KCI 차원의 생성형 AI 지침도 [미확인]. 따라서 KCI 투고 시에는 NRF · 과기정통부 지침에 맞춰 사사 또는 연구방법 절에 사용 내역을 적는 것이 안전하다[추정].

## 2. 실무 흐름과 실패 유형

### 2.1 연구자가 실제로 쓰는 방식

Nature 설문(2025-05-14, 응답 5,229 명, 2025 년 3 월 조사) [원문확인: https://www.nature.com/articles/d41586-025-01463-8]. 90 % 이상이 편집 · 번역에 AI 를 쓰는 것을 수용 가능하다고 봤고, 원고 전부 또는 일부 작성은 65 % 가 수용 가능, 약 1/3 이 반대했다. 초기 심사보고서 생성은 60 % 이상이 부적절하다고 했으나, 원고에 대한 질문에 AI 가 답하게 하는 심사 보조는 57 % 가 수용했다. 실제 사용은 적었다. 자기 논문 편집에 써 봤다는 응답이 약 28 %, 초고 작성 · 번역 · 심사 보조는 약 8 % 였고, 약 65 % 는 제시된 어떤 상황에서도 써 본 적이 없었다. 사용자는 대체로 공개하지 않았다고 답했다. 영어가 모국어가 아닌 나라의 응답자가 더 많이 썼다. 같은 기사에 인용된 Wiley 설문(약 5,000 명)에서는 번역 40 %, 교정 · 편집 38 % 였다.

Gruda 의 Nature Careers 칼럼(2024-04-08) [원문확인: https://www.nature.com/articles/d41586-024-01042-3]. 거의 매일 문장 다듬기와 심사 · 편집 보조에 쓴다고 밝혔다. 핵심은 맥락 제공이며 예시 지시문은 "I'm writing a paper on [topic] for a leading [discipline] academic journal. What I tried to say in the following section is [specific point]. Please rephrase it for clarity, coherence and conciseness, ensuring each paragraph flows into the next. Remove jargon. Use a professional tone." 심사에서는 원고를 넣지 않고 자신의 요약만 넣어 의견 정리를 돕게 한다("without directly inputting or uploading the manuscript's text"). 같은 방법을 심사 답변서 문장 정리에도 쓴다고 했다. 이 칼럼에 대한 독자 투고(2024-07-16, https://www.nature.com/articles/d41586-024-02319-3)는 문체 균질화와 저자 목소리 상실을 경고했다.

LLM 의 원고 피드백 품질. Liang et al.(arXiv 2310.01783, 2023-10-03) [원문확인]: GPT-4 의 지적과 인간 심사자 지적의 겹침은 Nature 계열 30.85 %, ICLR 39.23 % 로 인간 심사자 둘 사이의 겹침(28.58 %, 35.25 %)과 비슷했다. 약한 논문일수록 겹침이 컸다. 즉 "비판적 심사자 역할" 로 초안을 점검시키는 용도는 근거가 있으나 대체물은 아니다.

[추정] 수문 연구자에게 맞는 단계별 사용법(조사자 제안):
1. 개요 · 논리 점검: 자신이 쓴 요점 목록을 주고 "이 논지의 빈틈과 반론"을 묻는다. 결론은 사람이 정한다(Springer Nature Red 조항).
2. 영문 교정: 문단 단위로 넣고 "의미를 바꾸지 말고 문법 · 간결성만" 을 지시한다. 참고문헌 목록은 넣지 않는다(IEEE 팁). HESS 는 이 수준을 넘지 않는다.
3. 비판적 심사 모의: "Journal of Hydrology 심사자로서 주요 · 부차 지적을 나눠라" 식으로 자기 원고에만 쓴다.
4. 일관성 점검: 본문 수치와 표 · 그림 수치의 대조, 기호 정의 누락, 약어 첫 정의, 그림 번호 순서처럼 기계적 검사는 Python 스크립트와 LLM 을 함께 쓴다.
5. 심사 답변서: 심사 의견 번호별 표를 만들고 초안을 받되 수정 위치(쪽 · 행)는 사람이 확인한다.
6. 참고문헌 검증: 4 절의 API 로 모든 항목을 자동 대조한다.
7. 공개문: 1.8 표에 맞춰 학술지별 위치에 도구명 · 버전 · 목적을 적는다.

### 2.2 실패 유형과 정량 근거

허위 참고문헌.
- Walters & Wilder, Scientific Reports 2023-09-07 [2차: https://www.nature.com/articles/s41598-023-41032-5 검색 발췌]: 42 개 주제 문헌고찰 84 편, 인용 636 건. 허위 인용 GPT-3.5 55 %, GPT-4 18 %. 실재 인용 중 실질 오류 GPT-3.5 43 %, GPT-4 24 %.
- Chelli et al., JMIR 2024;26:e53164 [2차: https://www.jmir.org/2024/1/e53164 검색 발췌]: 체계적 문헌고찰 11 편 기준 참고문헌 471 건. 환각률 GPT-3.5 39.6 %(55/139), GPT-4 28.6 %(34/119), Bard 91.4 %(95/104).
- Ansari, arXiv 2602.05930(2026-02-05) [원문확인]: NeurIPS 2025 채택 논문의 허위 인용 100 건이 53 편(채택 논문의 약 1 %)에 있었다. 유형은 완전 날조 66 %, 일부 속성 변조 27 %, 식별자 도용 4 %. 모든 사례가 복합 유형이었고 3-5 명 심사를 통과했다. 원자료는 GPTZero 발표(https://gptzero.me/news/neurips/, 4,841 편 검사, 51 편 100 건) [2차, 업체 발표].
- GPTZero ICLR 2026 [2차, 업체 발표: https://gptzero.me/news/iclr-2026/]: 심사 중 300 편 표본에서 50 편이 허위 인용을 1 건 이상 포함.
- Sakai et al., arXiv 2601.18724(2026-01-26) [원문확인]: ACL · NAACL · EMNLP 2024-2025 전체에서 약 300 편이 허위 인용을 포함했고 대부분 2025 년, 절반이 EMNLP 2025.
- 검증 도구 자신도 틀린다. PHY041/claude-skill-citation-checker README 는 "NeurIPS 2025 accepted papers contained 100+ fake refs" 의 출처로 arXiv 2501.04181 을 달았으나, arXiv API 로 조회하면 그 ID 는 소아 교모세포종 단일세포 논문(2025-01-07)이다 [원문확인 2026-09-22]. 남의 README 수치도 원문을 열어 확인해야 한다는 사례다.

AI 문체 확산과 사용률 추정.
- Kobak et al., arXiv 2406.07016 [원문확인]: PubMed 초록 1,500 만 건 이상에서 "delve" 류 스타일 단어의 초과 빈도를 분석해 2024 년 초록의 최소 13.5 % 가 LLM 을 거쳤다고 추정했다. 일부 하위 집단은 40 %.
- Liang et al., arXiv 2404.01268 [원문확인]: 2020-01 에서 2024-02 사이 논문 950,965 편. LLM 수정 비율은 컴퓨터과학에서 최대 17.5 %, 수학과 Nature 계열은 최대 6.3 %.
- Holzwarth, González-Márquez & Kobak, arXiv 2608.10715(2026-08-11) [원문확인]: PubMed Central 전문 기준 2025 년 말 89 % 가 LLM 관련 어휘 초과를 보였다. Discussion 문단 68 %, Methods 문단 32 %. Nature 뉴스(2026-08-20, https://www.nature.com/articles/d41586-026-02551-z) [원문확인]는 2025 년 전체 77 %, 2024 년 52 %, 새 방법으로 2024 년 초록 추정이 13.5 % 에서 31 % 로 올랐다고 전했다. 또 비영어권 저자에서 사용이 더 많았고, 현재 탐지법은 문법 교정과 생성을 구분하지 못한다는 Andrew Gray 의 지적을 실었다.
- 심사보고서: Liang et al., arXiv 2403.07183 [원문확인]: ICLR 2024 · NeurIPS 2023 · CoRL 2023 · EMNLP 2023 심사문의 6.5-16.9 % 가 LLM 으로 상당히 수정됐을 것으로 추정. 마감 직전, 확신도 낮은 심사일수록 높았다.

탐지의 문제. Liang et al., arXiv 2304.02819(Patterns 게재) [원문확인]: GPT 탐지기는 비원어민 영어 글을 일관되게 AI 생성으로 오분류하고, 간단한 프롬프트로 우회된다. 비원어민 연구자는 탐지기 결과를 근거로 불이익을 받을 위험이 있으므로 공개문을 정확히 쓰는 편이 방어에 유리하다[추정].

은닉 프롬프트. Lin, arXiv 2507.06185(2025-07-08) [원문확인]: 2025 년 7 월 arXiv 원고 18 편에 흰 글씨 · 극소 글꼴로 심사용 AI 를 조작하는 지시문이 숨겨져 있었다. 과기정통부 가이드는 이를 연구부정행위로 규정했다고 보도됐다[2차].

완전 자동 논문. Sakana AI Scientist(arXiv 2408.06292) [원문확인]은 논문당 15 달러 미만으로 전 과정을 자동화했다고 주장하고, v2(arXiv 2504.08066) [원문확인]는 ICLR 워크숍에 낸 3 편 중 1 편이 평균 채택선을 넘었다고 보고했다. 모든 주요 출판사 정책에서 이런 사용은 Red 영역(판단 위임, 저자 책임 불가)에 해당한다[추정].

## 3. GitHub · Hugging Face 도구

별 수와 최근 푸시는 `gh api repos/OWNER/NAME` 로 2026-09-22 에 받았다 [원문확인].

| 저장소 | 별 | 최근 푸시 | 라이선스 | 용도 · 비고 |
|---|---|---|---|---|
| anthropics/skills | 177,501 | 2026-09-10 | 표기 없음 | 공식 스킬. 학술 글쓰기 전용 스킬은 없음, doc-coauthoring · docx · pdf 등 |
| K-Dense-AI/scientific-agent-skills (구 claude-scientific-skills, 이름 바뀜) | 45,965 | 2026-09-21 | MIT | skills 166 개. scientific-writing, peer-review, citation-management, literature-review 포함 |
| Imbad0202/academic-research-skills | 49,025 | 2026-09-21 | CC BY-NC 4.0 | research, write, review, revise, finalize 파이프라인 플러그인. 한국어 README 있음 |
| K-Dense-AI/claude-scientific-writer | 2,378 | 2026-08-19 | MIT | 문헌 조회 후 집필. 외부 API 필요 |
| SakanaAI/AI-Scientist | 14,595 | 2025-12-19 | NOASSERTION | 완전 자동 연구 · 논문 |
| SakanaAI/AI-Scientist-v2 | 7,196 | 2025-12-19 | NOASSERTION | 동 v2 |
| stanford-oval/storm | 31,455 | 2025-09-30 | MIT | 위키식 조사 보고서 생성 |
| Future-House/paper-qa | 9,232 | 2026-09-21 | Apache-2.0 | 논문 PDF 기반 질의응답 |
| blader/humanizer | 51,112 | 2026-09-06 | MIT | AI 문체 제거. 탐지 회피 목적 사용은 공개 의무 위반 소지[추정] |
| bahayonghang/academic-writing-skills | 478 | 2026-09-20 | 표기 없음 | 사후 점검(형식, 문법 · 문체) |
| WenyuChiou/academic-writing-skills | 62 | 2026-09-18 | MIT | 분야 무관 집필 · 수정 · 제출 스킬 |
| Hylouis233/bibverify | 99 | 2026-09-17 | MIT | BibTeX 검증 CLI · Python · MCP. Crossref, OpenAlex, S2, PubMed, DBLP 등 |
| se-uhd/hallucite | 15 | 2026-09-18 | MIT | PDF 참고문헌 허위 탐지. DBLP 오프라인 미러 후 Crossref 등. 분류 단계만 LLM(로컬 가능) |
| tingrui-huang/veracite | 3 | 2026-05-24 | MIT | .bib 를 arXiv · Crossref · OpenAlex · S2 와 대조, 키 불필요 |
| PHY041/claude-skill-citation-checker | 32 | 2026-03-22 | 표기 없음 | .bib 검증 스킬. README 인용 오류 있음(2.2 참조) |
| JeonKH81/claude-cove-reference-verifier | 5 | 2026-07-19 | MIT | PubMed 기반 CoVe 검증. 수문 분야는 PubMed 미수록이 많아 부적합[추정] |
| parkjui92/paper-proofread | 6 | 2026-07-20 | MIT | 한국어 논문 교정 스킬(표기 · 문장 · 논리 · 인용, 서지 실재 확인) |
| poldrack/ai-peer-review | 154 | 2026-07-05 | MIT | 여러 LLM 으로 메타 심사. OpenAI · Anthropic · Google API 로 원고 전송 |
| AlexWortega/ai-peer-review-skill | 64 | 2026-05-08 | MIT | 위 도구를 Claude Code 스킬로 이식 |
| retorquere/zotero-better-bibtex | 7,145 | 2026-09-21 | MIT | Zotero 에서 안정적 BibTeX 키 |
| jgm/pandoc | 46,370 | 2026-09-21 | GPL-2.0 | Markdown, LaTeX, docx 변환 |

`gh search repos` 로 "claude code academic writing", "latex claude code", "bibtex check doi" 는 결과가 0 이거나 별 3 개 이하 저장소뿐이었다 [원문확인]. 즉 이 영역은 소수 대형 묶음과 다수의 소형 스킬로 나뉘어 있다.

사용자 PC 에 이미 있는 scientific-writing 스킬은 K-Dense 판 v2.1 과 설명문이 같다. 원문 SKILL.md 는 "Bundled tools are offline and require no API keys" 이고 미공개 원고의 외부 전송을 권한 있는 승인 없이는 금지한다 [원문확인]. peer-review 스킬도 기밀 원고를 공개 모델 · 인용 서비스 · 문법 도구에 올리지 말라고 명시한다 [원문확인].

Hugging Face Papers(hf_fs 검색 2026-09-22) 관련 논문: CiteAudit 2602.23452(추천 18), CiteCheck 2605.27700, CiteTracer 2605.08583, "The 17% Gap" 2601.17431, LLM 심사 개관 2606.25057, 자동 심사의 한계 2512.22145 · 2509.19326, 논문 수정용 XtraGPT 2505.11336. 제목과 요약만 확인했다 [2차: HF 요약].

## 4. 참고문헌 검증용 무료 API

### 4.1 Crossref REST API

속도 제한(2025-12-01 시행, 블로그 2025-11-05) [원문확인: https://www.crossref.org/blog/announcing-changes-to-rest-api-rate-limits/]. 공개 풀은 단건 5 req/s · 동시 1, 목록 질의 1 req/s · 동시 1. polite 풀은 단건 10 req/s · 동시 3, 목록 질의 3 req/s · 동시 3. polite 풀은 `mailto` 매개변수로 들어간다. 이번 시험의 응답 헤더도 `x-rate-limit-limit: 10`, `x-rate-limit-interval: 1s`, `x-concurrency-limit: 3`, `x-api-pool: polite-single` 이었다 [원문확인]. 문서는 결과 캐시를 권하고 대량 작업에는 연간 공개 데이터 파일을 권한다(https://www.crossref.org/documentation/retrieve-metadata/rest-api/tips-for-using-the-crossref-rest-api/).

시험 1, DOI 조회: `GET https://api.crossref.org/works/10.1016/j.jhydrol.2009.08.003?mailto=...` 결과 status "ok". message 의 키 전체: DOI, ISSN, URL, alternative-id, assertion, author, container-title, content-domain, created, deposited, indexed, is-referenced-by-count, issn-type, issue, issued, journal-issue, language, license, link, member, original-title, page, prefix, published, published-print, publisher, reference, reference-count, references-count, relation, resource, score, short-container-title, short-title, source, subject, subtitle, title, type, update-policy, volume. 값: title "Decomposition of the mean squared error and NSE performance criteria: Implications for improving hydrological modelling", author Gupta(Hoshin V.), Kling(Harald), Yilmaz(Koray K.), Martinez(Guillermo F.), container-title "Journal of Hydrology", volume 377, issue "1-2", page "80-91", issued 2009-10, type journal-article, publisher "Elsevier BV", is-referenced-by-count 5385, references-count 47.

시험 2, 서지 질의: `GET /works?query.bibliographic=Gupta Kling Yilmaz Martinez 2009 Decomposition of the mean squared error and NSE performance criteria&rows=3&select=DOI,title,score,author,issued,container-title` 결과 total-results 113,997, 1 위 10.1016/j.jhydrol.2009.08.003(score 82.95), 2 위 10.1029/2011wr010962(score 39.23). 응답 message 키는 facets, items, items-per-page, query, total-results.

시험 3, 지어낸 서지: "Kim Park 2021 Deep learning prediction of combined sewer overflow in Seoul using SWMM Journal of Hydrology" 로 질의하자 1 위가 10.1007/s42452-026-09452-w(Discover Applied Sciences 2026, score 40.69)였다. Crossref 는 없는 논문에도 비슷한 논문을 돌려주므로, 판정은 score 절대값이 아니라 제목 유사도 · 첫 저자 성 · 연도 · 학술지 일치로 해야 한다. 이번 표본에서 실재 1 위와 2 위의 score 차는 약 2 배였다[추정: 표본 1 건, 임계값은 자체 시험으로 정할 것].

시험 4, 없는 DOI: `/works/10.1016/j.jhydrol.2099.99.999` 는 HTTP 404.

### 4.2 OpenAlex

[원문확인: https://help.openalex.org/api/authentication/ (2026-08-19 갱신), https://help.openalex.org/access/example-costs/ (2026-08-09 갱신)]. 사용량 과금 체계로 바뀌었다. 키 없이는 하루 0.10 달러, 무료 키는 하루 1 달러 예산이다. 단건 조회는 무료, 목록 · 필터 1,000 건당 0.10 달러, 검색 1,000 건당 1 달러. 초당 100 요청을 넘거나 일일 예산을 넘으면 429. 키는 openalex.org/settings/api 에서 무료 발급. 전체 자료는 CC0 스냅샷으로 받을 수 있다[2차: 검색 발췌]. 이번 시험에서 키 없이 DOI 단건 조회가 성공했고(W2138763184, cited_by_count 6992) 응답 헤더는 `X-RateLimit-Cost-USD: 0`, `X-RateLimit-Limit-USD: 0.1` 이었다 [원문확인]. 2026 년 2 월 키 의무화 공지(https://groups.google.com/g/openalex-users/c/rI1GIAySpVQ)는 [2차].

### 4.3 Semantic Scholar

[원문확인: https://www.semanticscholar.org/product/api (WebFetch 2026-09-22)]. 비인증은 "1000 requests per second shared among all unauthenticated users", API 키는 "introductory rate limit ... 1 RPS on all endpoints". 키는 신청 양식으로 받는다. Ai2 의 이용약관과 API License Agreement 를 따른다. 시험: `/graph/v1/paper/DOI:10.1016/j.jhydrol.2009.08.003?fields=title,year,citationCount,externalIds` 는 citationCount 5588, CorpusId 12741747 을 돌려줬다 [원문확인]. 같은 논문의 피인용 수가 Crossref 5385, OpenAlex 6992, S2 5588 로 서로 다르므로 논문에 피인용 수를 적을 때는 출처를 병기한다.

### 4.4 권장 검증 순서 [추정]

DOI 가 있으면 Crossref 단건 조회로 제목 · 첫 저자 · 연도 · 권 · 쪽을 대조하고, DOI 가 없거나 404 면 Crossref query.bibliographic 과 OpenAlex 검색으로 후보를 받아 제목 유사도(예: 0.9 이상)로 판정하고, 둘 다 실패하면 "확인 불가"로 사람이 본다. KCI 논문은 Crossref 에 DOI 가 없는 경우가 있어 kr-paper-search 스킬(KCI Open API)을 함께 쓴다. 이 순서는 bibverify · veracite 의 설계와 같다. 전송되는 것은 서지 정보뿐이라 원고 유출 위험이 낮다.

## 5. 보안: 원고를 외부로 보내는 도구

원칙: 미발표 결과, 발주처 자료, 심사 중 원고는 공개형 · 학습 사용 서비스에 올리지 않는다. 모든 출판사가 심사 원고 업로드를 금지하고(1 절), Elsevier 와 Wiley 는 저자에게도 입력을 학습에 쓰지 않는 도구를 쓰라고 한다.

Claude Code 자체. Claude Code 는 원고를 Anthropic API 로 보낸다. Anthropic 은 2025-08-28 소비자 약관을 바꿔 Free · Pro · Max 사용자의 대화와 코딩 세션을 학습에 쓸 수 있게 했고(거부 가능), 학습 허용 시 보존 기간은 최대 5 년, 거부 시 30 일이라고 보도됐다. 상업 약관(Claude for Work, API 등)에는 적용되지 않는다 [2차: https://www.anthropic.com/news/updates-to-our-consumer-terms 를 인용한 검색 발췌, 원문 페이지 직접 확인은 못 함]. 조치: claude.ai 개인정보 설정에서 학습 사용을 끄고, 심사 원고는 어떤 경우에도 넣지 않는다. Elsevier 의 "private AI" 정의(입력을 보존 · 재사용 · 학습하지 않음)에 30 일 보존이 부합하는지는 [판정보류: 학술지나 기관에 문의].

외부로 원고 본문을 보내는 도구(주의):
- poldrack/ai-peer-review, AlexWortega/ai-peer-review-skill: 원고를 OpenAI · Anthropic · Google API 로 보낸다(README). 남의 원고 심사에는 쓰면 안 되고, 자기 원고에만 약관 확인 후 쓴다.
- K-Dense-AI/claude-scientific-writer: ANTHROPIC_API_KEY 필수, Parallel 검색 API, 선택적으로 OpenRouter(그림 생성) 사용(README).
- GPTZero Hallucination Check 등 웹 업로드형 검사기: PDF 를 업체 서버에 올린다[추정: 서비스 형태로 판단, 약관 미확인].
- federicodeponte/opendraft(19 개 에이전트가 2 만 단어 논문을 씀): 외부 LLM 사용[추정: README 미정독]. 정책상 Red 영역.
- Imbad0202/academic-research-skills: 설치 시 SessionStart 훅과 Write · Edit · Bash 에 걸리는 PreToolUse 훅을 심는다(hooks/hooks.json 원문 확인). 훅 자체는 쓰기 범위 감시 목적으로 보이나, 전역 규칙(남의 스킬은 훅을 확인)에 따라 설치 전 scripts 를 정독해야 한다. 라이선스가 CC BY-NC 4.0 이라 상업 과업에 쓰기 곤란할 수 있다.

서지 정보만 보내는 도구(상대적으로 안전): bibverify, veracite, hallucite(`--offline` 이면 DBLP 로컬만, LLM 분류는 로컬 모델 가능), PHY041 citation-checker. 단 hallucite 는 PDF 에서 참고문헌을 뽑는 분류 단계에 클라우드 LLM 을 설정하면 일부 본문이 나갈 수 있다(README).

## 6. 다음에 정할 것

첫째, 과기정통부 가이드 원문 PDF 와 NRF 가이드 원문을 받아 쪽 번호로 인용할지. 둘째, Journal of Hydrology 투고 시 선언 절 문안을 표준화할지(Elsevier 권장 문안을 그대로 쓰되 도구명에 "Claude (Anthropic), Claude Code" 와 버전을 적는 방식). 셋째, 4.4 순서대로 `.bib` 또는 docx 참고문헌 검증 스크립트를 로컬 Python 으로 만들지(외부 도구 도입 대신). 넷째, HESS 처럼 생성형 글쓰기를 금지하는 학술지 목록을 투고 후보마다 관리할지.
