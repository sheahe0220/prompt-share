# Q1 수문학 학술지 저자들의 실제 서술 방식: 26 편 코퍼스 실측

작성일 2026-09-22. 대상은 SWMM 도시배수 보정 논문을 준비하는 석사과정생이다.
표기 약속: [원문확인] 은 내려받은 전문에서 스크립트 또는 직접 읽기로 센 값, [추정] 은 해석이나 키워드 휴리스틱에 기댄 값이다. [파생] 은 실측값에서 끌어낸 권고다.

## 0. 핵심 수치 한눈에

| 항목 | 중앙값 (범위) 또는 비율 | 근거 |
|---|---|---|
| 제목 길이 | 13 단어 (9-22), 콜론 4/26, 결과를 진술하는 제목 0/26 | [원문확인] |
| 초록 길이 | 243 단어 (149-581), 9 문장 (6-21) | [원문확인] |
| 초록에 정량 결과(소수 또는 %) | 11/26 (42 %) | [원문확인] |
| 본문 길이 | 6,628 단어 (3,720-11,534), 서론 1,091 단어, 결론 372 단어 | [원문확인] |
| 1 수준 장 수 | 5 (4-7) | [원문확인] |
| Results and Discussion 통합 / Discussion 분리 / 둘 다 아님 | 11 / 10 / 5 | [원문확인] |
| 데이터 · 코드 가용성 절 | 16/26 (62 %) | [원문확인] |
| we (1,000 단어당) | 0.70 (0-7.92) | [원문확인] |
| 수동태 근사 (1,000 단어당) | 20.7 (9.9-34.7) | [추정] 정규식 근사 |
| 그림 수 | 10 (5-19) | [원문확인] |
| 캡션 길이 | 23 단어 (사분위 12-46, 범위 2-177) | [원문확인] |
| 첫 그림 | 개념도 · 흐름도 12/26, 대상지 지도 11/26 | [추정] 분류기 정확도 약 80 % |
| 표 수 | 4 (0-9), 가장 흔한 표는 매개변수 · 범위 표 | [원문확인] 개수, [추정] 유형 |
| 본문 속 NSE · KGE · R2 값의 소수 자릿수 | 2 자리 59/92 값, 논문별 최빈 2 자리 10/15 편 | [원문확인] |
| 참고문헌 수 | 55 (34-89), Crossref 참고문헌 수와 26/26 일치 | [원문확인] |
| 최근 5 년 인용 비율 | 0.31 (0.11-0.64) | [원문확인] 정의는 11 절 |

## 1. 코퍼스와 측정 방법

### 1.1 수집 경로

OpenAlex 검색(17 개 질의, `is_oa:true`, 2015 년 이후, 논문 유형)으로 후보 382 행(중복 제거 228 편)을 모았다. 대상 학술지를 걸러낸 뒤 총설(review)과 의견(opinion) 논문은 빼고 연구 논문만 골랐다. 전문은 두 경로로 받았다.

HESS 12 편은 Copernicus JATS XML(`https://hess.copernicus.org/articles/<vol>/<page>/<year>/hess-<vol>-<page>-<year>.xml`)을 그대로 받았다. Wiley · Elsevier · IWA 14 편은 스크립트 요청이 403 으로 막혀서 Playwright 브라우저로 OA 전문 HTML 을 열고 저장했다. 처음 고른 hess-19-691-2015 와 hess-19-2409-2015 는 XML 에 본문이 없어(초록만 있는 약 2 만 바이트짜리 파일) 빼고, hess-25-5839-2021 과 hess-21-4895-2017 로 바꿨다.

모든 DOI 는 Crossref API 로 제목 · 학술지 · 연도를 대조했고, 내려받은 파일 안에 Crossref 제목 단어가 들어 있는지도 확인했다(26/26 일치). 참고문헌 수도 Crossref `reference-count` 와 26/26 일치해서 파싱 누락은 없다고 본다. [원문확인]

### 1.2 코퍼스 목록 (26 편, U = SWMM · 도시배수 17 편 65 %, R = 인접 수문모형 보정 · 대리모형 9 편 35 %)

| # | 학술지 | 연도 | DOI | 군 | 주제 요지 |
|---|---|---|---|---|---|
| 1 | HESS | 2020 | 10.5194/hess-24-869-2020 | U | 녹지 도시배수 모형 보정의 사상 선택, 2 단계 보정 |
| 2 | HESS | 2018 | 10.5194/hess-22-2615-2018 | U | SWMM 녹색기반시설 배수구역 구분 |
| 3 | HESS | 2017 | 10.5194/hess-21-1559-2017 | U | 강우 공간 · 기후 변동성의 분리, 도시배수 |
| 4 | HESS | 2021 | 10.5194/hess-25-5839-2021 | U | SuDS 수문응답, 설명 가능한 기계학습 |
| 5 | HESS | 2021 | 10.5194/hess-25-5493-2021 | U | 강우 시간분포 · 강도의 수문곡선 민감도 |
| 6 | HESS | 2015 | 10.5194/hess-19-4001-2015 | U | 우량계 기반 레이더 강우 보정, 도시 적용 |
| 7 | HESS | 2019 | 10.5194/hess-23-4293-2019 | U | SWMM-GIS 지하철 침수 분석 |
| 8 | HESS | 2017 | 10.5194/hess-21-4895-2017 | R | 수위 계급 자료의 보정 정보량 |
| 9 | HESS | 2020 | 10.5194/hess-24-4641-2020 | R | 기계학습 에뮬레이터와 허용한계 접근 |
| 10 | HESS | 2018 | 10.5194/hess-22-5021-2018 | R | GLUE 매개변수 불확실성 |
| 11 | HESS | 2017 | 10.5194/hess-21-393-2017 | R | 다중 매개변수 범위 선택으로 보정 개선 |
| 12 | HESS | 2017 | 10.5194/hess-21-6219-2017 | R | 모멘트 기반 전역 민감도 지표 |
| 13 | WRR | 2022 | 10.1029/2022wr032440 | U | 앙상블 평활기로 도시배수 모형 보정 |
| 14 | WRR | 2025 | 10.1029/2024wr039525 | R | AI 대표본 에뮬레이터로 보정 · 지역화 |
| 15 | WRR | 2016 | 10.1002/2015wr018230 | R | 다목적 적응형 대리모형 최적화 (MO-ASMO) |
| 16 | WRR | 2022 | 10.1029/2021wr030928 | U | 대리모형 전역최적화, LID 배치, 1D-2D 침수모형 |
| 17 | Hydrol. Process. | 2018 | 10.1002/hyp.13319 | R | 강우 불확실성이 물리기반 모형 성능에 주는 영향 |
| 18 | J. Hydrol. | 2020 | 10.1016/j.jhydrol.2019.124436 | U | OSTRICH-SWMM 자동보정 도구 |
| 19 | EMS | 2024 | 10.1016/j.envsoft.2024.106122 | U | Bayes_Opt-SWMM, GP 기반 베이지안 최적화 |
| 20 | J. Hydrol. | 2021 | 10.1016/j.jhydrol.2021.126525 | U | SWMM 투수성 포장 민감도 분석 |
| 21 | J. Hydrol. | 2023 | 10.1016/j.jhydrol.2023.129757 | U | SWMM 단순화 모형 |
| 22 | J. Hydrol. | 2024 | 10.1016/j.jhydrol.2024.131546 | U | 매개변수 불확실성 대 기후전망 편차 |
| 23 | EMS | 2022 | 10.1016/j.envsoft.2022.105341 | R | 전역-국소 혼합 최적화로 수문모형 보정 |
| 24 | J. Environ. Manage. | 2024 | 10.1016/j.jenvman.2024.121244 | U | SWMM 수질 보정 최적화 전략 |
| 25 | J. Hydroinform. | 2024 | 10.2166/hydro.2024.282 | U | 다목적 최적화 SWMM 자동보정 |
| 26 | J. Hydroinform. | 2026 | 10.2166/hydro.2026.064 | U | 열대 도시유역 SWMM 민감도 분석 |

학술지 분포는 HESS 12, WRR 4, J. Hydrol. 4, J. Hydroinform. 2, EMS 2, Hydrol. Process. 1, J. Environ. Manage. 1 이다. Water Research 와 Urban Water Journal 은 후보에는 있었으나 전문 확보 시간 안에 넣지 못했다(아래 13 절).

### 1.3 측정 도구

스크립트는 `corpus\` 에 있다. `s05_parse.py` 가 출판사 4 형식을 한 JSON 구조로 바꾸고, `s06_metrics.py` 가 지표를 계산한다. 그림 · 표 · 초록 단락 분류는 키워드 규칙이다. 그림 분류기는 무작위 30 개 캡션 두 벌을 직접 읽어 대조했고, 첫 벌은 22/30(73 %), 규칙을 고친 뒤 둘째 벌은 27/32(84 %)가 맞았다. 그래서 그림 유형 비율은 모두 [추정] 으로 적는다.

## 2. 제목

제목 길이는 중앙값 13 단어(9-22)다. 콜론이 있는 제목은 4/26(15 %)이고, 그중 2 편은 도구 이름을 앞에 둔 형식(`Bayes_Opt-SWMM: A Gaussian process-based ...`, `Balancing exploitation and exploration: A novel ...`)이며 2 편은 뒤에 사례지를 붙인 형식(`...: a case study in Shanghai`, `...: a case study of Udon Thani City, Thailand`)이다. [원문확인]

26 편 제목을 모두 직접 읽었을 때 결과를 문장으로 진술한 제목(예: "X improves Y")은 0 편이었다. 모두 주제 또는 방법을 명사구로 적었다. 자주 보인 틀은 다음과 같다. [원문확인]

```text
[방법/분석] of [대상] (in/for/using [모형])
  Sensitivity analysis of permeable pavement hydrological modelling in the Storm Water Management Model
  Parameter uncertainty analysis for an operational hydrological model using residual-based and limits of acceptability approaches
[A new / A simplified] [도구/접근] for [과업]
  A new tool for automatic calibration of the Storm Water Management Model (SWMM)
  A simplified approach for the hydrological simulation of urban drainage systems with SWMM
[동명사] [대상]
  Exploring the Performance of Ensemble Smoothers to Calibrate Urban Drainage Models
Effect/Impact of [요인] on [응답]
  Effect of rainfall uncertainty on the performance of physically based rainfall-runoff models
```

## 3. 초록

길이는 중앙값 243 단어(149-581), 9 문장(6-21)이다. 군별로는 도시배수 군 248 단어, 인접 군 199 단어다. [원문확인]

정량 결과(소수 또는 %)가 들어 있는 초록은 11/26(42 %)에 그쳤다. 한 초록당 정량 값 개수의 중앙값은 0 이고 최대 5 개다. 초록에 we 를 쓴 논문은 10/26(38 %), "Here we" 는 4/26(15 %), "this study/paper/work" 는 17/26(65 %)이다. 초록에서도 1 인칭보다 "This study ..." 가 흔하다. [원문확인]

단락(move) 존재율은 키워드 규칙으로 쟀다. [추정]

| 단락 | 있는 논문 | 판정 단서 |
|---|---|---|
| 배경 (첫 문장이 일반 진술) | 22/26 (85 %) | 첫 문장에 we/this study 없음 |
| 간극 | 17/26 (65 %) | however, remain, lack, limited, challenge 등 |
| 목적 | 22/26 (85 %) | this study, we propose, aims to 등 |
| 방법 | 26/26 (100 %) | using, applied, framework, calibrat 등 |
| 정량 결과 | 11/26 (42 %) | 소수 또는 % |
| 함의 · 활용 | 8/26 (31 %) | suggest, useful, recommend, decision 등 |

여섯 단락을 다 갖춘 초록은 2/26 뿐이다. 실제로 가장 흔한 뼈대는 "배경 1-2 문장, 목적, 방법, 정성적 결과, 도구 가치 한 문장" 이다. [추정]

초록 첫 문장 실례 [원문확인]:

- "The calibration of urban drainage models is typically performed based on a limited number of observed rainfall–runoff events, which may be selected from a larger dataset in different ways." (10.5194/hess-24-869-2020)
- "The USEPA (United States Environmental Protection Agency) Storm Water Management Model (SWMM) is one of the most widely used numerical models to simulate urban runoff and drainage." (10.1016/j.jhydrol.2019.124436)
- "Urban drainage models (UDMs) are often used to manage urban flooding." (10.1029/2022wr032440)

초록 마지막 문장 실례, 대체로 "도구 · 방법의 가치" 를 한 문장으로 닫는다 [원문확인]:

- "The results demonstrate that OSTRICH-SWMM is a promising tool for automatic calibration of SWMM models." (10.1016/j.jhydrol.2019.124436)
- "Overall, Bayes_Opt-SWMM emerges as a cost-effective and valuable tool for real-time flood modeling and monitoring, with significant potential for managing intelligent storm water systems in urban environments." (10.1016/j.envsoft.2024.106122)
- "The results show the importance of using multiple distributed rainfall realizations in urban hydrology studies to capture the total flow variability in the response of the urban drainage systems to heavy rainfall events." (10.5194/hess-21-1559-2017)

"Here we" 문장 실례 [원문확인]:

- "Here we compare the effects of parameter uncertainty in a hydrological model to inter-model spread from climate projections on hydrological projections of urban streamflow in response to climate change." (10.1016/j.jhydrol.2024.131546)
- "Here we present parameter uncertainty analysis of a recently released distributed conceptual hydrological model applied in the Nea catchment, Norway." (10.5194/hess-22-5021-2018)

## 4. 장 구성

1 수준 장 수는 중앙값 5(4-7)다. 서론은 26/26 모두 첫 장이다. 결과와 고찰의 배치는 세 갈래로 나뉜다. [원문확인]

| 배치 | 편수 | 예 |
|---|---|---|
| Results and Discussion 통합 | 11 (42 %) | hess-24-869-2020, jhydrol.2021.126525, 2022wr032440 |
| Results 와 Discussion 분리 | 10 (38 %) | hyp.13319, jhydrol.2024.131546, hydro.2026.064 |
| 둘 다 아님 (결과만, 또는 Discussion and Conclusions) | 5 (19 %) | 2015wr018230, jhydrol.2019.124436 |

대상지 · 사례를 별도 1 수준 장으로 둔 논문은 13 편이다. 그중 7 편은 방법 뒤에(Methodology, 다음에 Case study), 6 편은 방법 앞에 둔다. 방법 · 도구 개발 논문(OSTRICH-SWMM, Bayes_Opt-SWMM, MO-ASMO, 앙상블 평활기, DYCORS)은 모두 방법 뒤에 사례를 둔다. 사례 적용형 논문은 앞에 둔다. [원문확인 배치, 추정 해석]

실제 장 제목 목록 예 [원문확인]:

```text
1. Introduction | 2. Methodology | 3. Case study | 4. Results | 5. Conclusions            (10.1016/j.jhydrol.2019.124436)
1 Introduction | 2 Methodology | 3 Case Studies | 4 Results and Discussions | 5 Summary and Conclusions   (10.1029/2022wr032440)
1 INTRODUCTION | 2 STUDY SITE AND DATA | 3 METHODOLOGY | 4 RESULTS | 5 DISCUSSION | 6 CONCLUSIONS    (10.1002/hyp.13319)
```

분량 비율은 서론이 본문의 약 17.5 %(중앙값 1,091 단어), 결론이 약 5.5 %(중앙값 372 단어, 241-1,350)다. 결론을 번호 목록으로 쓴 논문은 4/26(15 %), 결론에 수치를 넣은 논문은 9/26(35 %), 결론에 향후 연구를 적은 논문은 8/26(31 %)이다. [원문확인 개수, 번호 목록 판정은 추정]

서론 끝에 "This paper is organized as follows" 형 안내 단락이 있는 논문은 6/26, 서론에서 목적을 (1)(2) 또는 (i)(ii) 번호로 나열한 논문은 7/26 이다. [원문확인]

데이터 · 코드 가용성 절은 16/26(62 %)에 있다. HESS 는 2017 년 이후 11 편 모두 있었다. 문구는 "available from the corresponding author upon request" 형이 가장 흔했고, 저장소 링크(GitHub, Zenodo, HydroShare)를 준 논문은 6 편 정도다(2021wr030928, 2022wr032440, 2024wr039525, envsoft.2024.106122, hess-25-5839-2021, jhydrol.2024.131546). [원문확인]

## 5. 태와 인칭

본문 1,000 단어당 빈도의 중앙값(범위)이다. [원문확인, 수동태만 추정]

| 표현 | 중앙값 | 범위 |
|---|---|---|
| we | 0.70 | 0-7.92 |
| our | 0.05 | 0-6.40 |
| this/the present study · paper · work | 1.70 | 0-5.85 |
| 수동태 근사 (be 동사 + 과거분사) | 20.7 | 9.9-34.7 |

we 를 한 번이라도 쓴 논문은 20/26 이지만 빈도는 낮다. 인접 군(R, 알고리즘 · 대리모형)은 we 중앙값 2.36, 도시배수 군(U)은 0.43 이다. HESS 는 0.42, 나머지 학술지는 1.11 이다. 도시배수 적용 논문은 수동태와 "this study" 로 서술하는 쪽이 우세하다. [원문확인 수치, 추정 해석]

"It is/was found/observed/seen/noted that" 류는 11/26 편에서 모두 51 회 나왔다. 한 편이 21 회를 차지하고 중앙값은 0 이다. 드물게 쓰는 표현이다. [원문확인]

## 6. 그림

### 6.1 개수와 순서

그림 수는 중앙값 10(5-19)이다. 도시배수 군은 9, 인접 군은 11 이다. [원문확인]

첫 그림은 개념도 · 흐름도 · 모형 구성도가 12/26, 대상지 지도가 11/26, 그 밖이 3/26 이다. 도시배수 군만 보면 개념도 9, 지도 7, 매개변수 1 이다. 첫 두 그림 안에 지도나 개념도가 있는 논문은 24/26(92 %)이고, 지도가 있는 논문은 13/26 이다. 지도를 어딘가에 쓴 논문은 19/26(73 %), 관측-모의 수문곡선 · 시계열을 쓴 논문은 16/26(62 %)이다. [추정]

그림 유형별 상대 위치(그림 번호 / 그림 수)의 중앙값으로 본 전형 순서는 다음과 같다. [추정]

```text
개념도·흐름도 (0.25, 23 편) -> 대상지 지도 (0.31, 19 편) -> 강우 입력 자료 (0.47, 6 편)
 -> 매개변수 분포·민감도·사후분포 (0.61, 20 편) -> 성능 비교 상자그림·파레토·CDF (0.69, 18 편)
 -> 수렴 곡선 (0.71, 6 편) -> 관측-모의 수문곡선·시계열 (0.73, 16 편)
```

마지막 그림은 수문곡선 · 시계열 8 편, 성능 비교 6 편, 매개변수 · 민감도 5 편이다. 관측 대 모의 산점도는 3 편에만 있었다. 이 분야 저자들은 적합도를 산점도보다 수문곡선 겹쳐 그리기와 지표 상자그림으로 보여 준다. [추정]

유형별 전체 그림 수(254 개)는 매개변수 · 민감도 50, 성능 비교 48, 개념도 46, 지도 34, 수문곡선 30, 수렴 14, 결과 공간분포 10, 강우 입력 8, 산점도 3, 기타 11 이다. [추정]

### 6.2 캡션 문체

캡션 길이는 중앙값 23 단어(사분위 12-46, 범위 2-177)이고, 논문별 캡션 중앙값의 중앙값은 28.5 단어(10-86)다. 두 문장 이상인 캡션은 35 % 다. 학술지 차이가 크다. J. Hydroinform. 과 WRR 의 MO-ASMO 논문은 10 단어 안팎의 제목형이고, HESS 의 hess-21-4895-2017 은 86 단어, jhydrol.2024.131546 은 79.5 단어의 설명형이다. [원문확인]

첫 문장이 결과를 진술하는 캡션은 휴리스틱으로 13/254(5 %)가 걸렸으나, 직접 읽어 보니 모두 "X is shown at ..." 같은 서술형 수동문이었다. 결과를 진술하는 캡션은 사실상 0 이다. 첫 문장은 명사구로 쓰는 것이 표준이다. [원문확인]

패널 (a)(b) 를 정의하는 캡션 34 %, 선 · 색 · 기호를 설명하는 캡션 22 %, 단위를 적은 캡션 12 % 다. [추정]

캡션 실례 [원문확인]:

- 짧은 명사구형: "Location of the study area." (10.5194/hess-21-393-2017), "OSTRICH-SWMM linkage." (10.1016/j.jhydrol.2019.124436), "Urban drainage model layouts of the three cases." (10.1029/2022wr032440)
- 명사구와 설명 문장: "Map of the studied catchment showing elements of the high-resolution rainfall–runoff model (see Sect. 2.2) and the distance of the catchment to the rain gauge (RG). The diameters of the pipes range from 400 mm for the main trunk where the flow sensor is located to 200 mm for the smaller branches." (10.5194/hess-24-869-2020)
- 패널 정의형: "Examples of hydrographs for events with high (a) and low (b) objective function (NSE) values; varobs denotes the variance of the observations." (10.5194/hess-24-869-2020)
- 패널과 기호 설명형: "Portobello catchment (a) general location; (b) sensor location, sewer network and radar grid over the catchment. Flow gauges FM 3, 10, 14 and 19 (the circled round markers in (b), respectively located at the up-, mid- and downstream parts of the catchment) are particularly selected for visual inspection in Sect. ." (10.5194/hess-19-4001-2015, 끝의 절 번호는 XML 교차참조라 텍스트에서 빠졌다)

## 7. 표

표 수는 중앙값 4(0-9)이고, 표가 없는 논문도 2 편 있다. 전체 표 103 개를 캡션 키워드로 나누면 매개변수 · 범위 40, 성능 지표 20, 사상 특성 12, 대상지 · 자료 특성 7, 방법 비교 6, 기타 18 이다. [원문확인 개수, 추정 유형]

성능 지표 표는 자동 분류에 오탐이 섞여 있어(예: "Metro-hydrological statistical data", 사후분포 요약) 직접 걸렀다. 실제 성능 지표 표가 있는 논문은 10/26 이다. 표 안 NSE · KGE 는 소수 2 자리가 8 편으로 가장 많고, 3 자리는 2 편(hess-24-4641-2020 일부, hess-25-5493-2021)이다. 최고값을 굵게 표시한 논문은 3 편이고, 캡션에 "Bold font indicates the best value in each column." 을 명시한 곳은 hess-24-869-2020 뿐이다. hess-21-4895-2017 은 굵은 글씨 대신 별표(`0.77*`)를 썼다. [원문확인]

## 8. 결과 서술

지표(NSE, KGE, RMSE, PBIAS, R2, MAE 등)와 수치가 한 문장에 함께 나온 문장은 26 편 중 18 편에서 모두 124 개였다. 8 편은 이런 문장이 하나도 없었다. 도구 개발(OSTRICH-SWMM)이나 민감도 분석 논문은 지표값 대신 파레토 전선이나 민감도 지수로 결과를 말한다. [원문확인]

124 개 문장 중 비교 표현(than, compared, outperform, from x to y, higher/lower)이 있는 문장은 36 %, 해석 표현(indicating, suggesting, due to, demonstrate)이 있는 문장은 18 % 다. 절반 넘는 문장은 값만 적는다. 값, 비교, 해석을 한 문장에 다 넣기보다 값 문장 다음에 해석 문장을 따로 두는 경우가 많다. [추정]

본문 속 NSE · KGE · R2 값 92 개의 소수 자릿수는 1 자리 21, 2 자리 59, 3 자리 10, 4 자리 2 다. 15 편 중 10 편의 최빈값이 2 자리다. [원문확인]

실제 문장 18 개 [원문확인]:

1. "At gauges USGS 02169505, USGS 02169506, and Olympia Park, the KGE values for the RTC scenario were 0.82, 0.57, and 0.64, respectively (Table 7)." (10.1016/j.envsoft.2024.106122)
2. "For the three storm events used for model calibration, the following mean performance statistics were obtained: Nash–Sutcliffe efficiency of 0.5782, root mean square error of 0.0373 m3 s-1, coefficient of determination (R2) of 0.7756 and regression coefficient (β), which provides a measurement of conditional bias, of 0.8826." (10.5194/hess-19-4001-2015)
3. "Low-flow volume errors (±5 %) and Nash–Sutcliffe efficiencies of > 0.8 for individual events, i.e., > 0.7 for longer periods, support the fact that the flow dynamics are reproduced adequately." (10.5194/hess-21-1559-2017)
4. "It is found that the minimum ENS, excepting extreme outliers, rises from 0.881 to 0.884 and the ENS concentrates at a higher value range, when the MINR is used instead of the initial range." (10.5194/hess-21-393-2017)
5. "The simulated hydrographs by the developed watershed-scale SWMM model were well matched with observed data over a 2-month continuous simulation (Nash–Sutcliffe coefficient = 0.852; R2=0.871) after minimal calibration effort." (10.5194/hess-22-2615-2018)
6. "In this study, NSE and LnNSE of 0.7 and 0.6, respectively, were considered as the threshold values for behavioral models." (10.5194/hess-22-5021-2018)
7. "During the calibration period, minimum NSE values of 0.81, 0.89, and 0.82 were, respectively, obtained for the models identified using RF, KNN, and NNET as emulators." (10.5194/hess-24-4641-2020)
8. "Using the HR model, there were four event characteristics (P_sum, PI_mean, QV_ppP and D_prec) for which the two-stage calibration performed better (up to 0.08 event mean NSE) than the single-stage calibration, while for Q_max the single-stage calibration performed better (0.03 event mean NSE)." (10.5194/hess-24-869-2020)
9. "For the two-stage calibration strategies, the individual stages also produced successful calibrations (stage 1 event mean NSE of 0.70–0.87; stage 2 event mean NSE of 0.78–0.87), except for the second stage in T32S_QV_ppP for the reasons explained above." (10.5194/hess-24-869-2020)
10. "The prediction accuracies of the XGBoost models, i.e., NSE>0.7 and R2>0.7, can be considered satisfactory, considering that they were relatively easy to set up and that it was impossible or very difficult to build process-based models for either site." (10.5194/hess-25-5839-2021)
11. "This is supported by a higher CE (0.74 against 0.70) and a lower RMSE (233.45 mg/L against 246.39 mg/L)." (10.1016/j.jenvman.2024.121244)
12. "For the validation phase, OF 1 Range 2 performed much better than OF 1 Range 3 with higher higher CE (0.7 against 0.47) and a lower RMSE (232.42 mg/L against 310.46 mg/L)." (10.1016/j.jenvman.2024.121244, "higher higher" 는 원문 그대로)
13. "For example, for Bellinge 5 (Fig. 5), with NSE = 0.89, the discharges of the first and the second peaks are underestimated by only 8.9%, and 11.8%, respectively, while the first peak time is anticipated by only 1 min, and the second peak time is perfectly predicted." (10.1016/j.jhydrol.2023.129757)
14. "After bias correction, MAE is reduced to 0.20–0.21 mm for precipitation and 0.1–0.2 °C for temperature." (10.1016/j.jhydrol.2024.131546)
15. "When the model was inputted with rainfall of other intensities (moderate rain and light rain), the M-NSE values for the J_44 water level process were all above 0.82, and the M-NSE values for the C_27 pipe flow process were also above 0.79, indicating excellent model verification results (the verification process is not detailed here because of space limitations)." (10.2166/hydro.2024.282)
16. "Figure 4 indicates that the 1D model tends to slightly overestimate baseflow, whereas it could produce close peak flows (with root mean square error = 0.06, and correlation coefficient r = 0.99 and 0.98 for the magnified two events, respectively) under intensive storm events." (10.1029/2021wr030928)
17. "More specifically, ES-ILU generally outperforms ES-MDA in terms of the estimation accuracy and the associated uncertainty (see the NSE mean and std values) while both the two methods can achieve highly accurate estimates for the observed states (all the NSE mean values above 0.98)." (10.1029/2022wr032440)
18. "For the SSE, the approach combining GPR and RF increases the mean CC from 0.79 to 0.83 and reduces the mean MAE from 0.057 to 0.051 compared to using GPR alone." (10.1029/2024wr039525)

관찰되는 틀 [추정]:

```text
A. 값 나열형      the KGE values ... were 0.82, 0.57, and 0.64, respectively (Table 7).          (1, 7)
B. 범위형         ... with an event mean NSE ... ranging from 0.68 to 0.85                        (9)
C. 비교형         A performed better (up to 0.08 event mean NSE) than B                           (8, 11, 12, 18)
                  increases the mean CC from 0.79 to 0.83 ... compared to using GPR alone
D. 판정형         ... NSE>0.7 and R2>0.7, can be considered satisfactory, considering that ...     (3, 10, 15)
E. 기준 선언형    NSE and LnNSE of 0.7 and 0.6 ... were considered as the threshold values         (6)
F. 물리량 해석형  with NSE = 0.89, the ... peaks are underestimated by only 8.9%, and 11.8%      (13)
```

## 9. 헤징과 주장 강도

본문 1,000 단어당 중앙값이다(범위는 CSV 에 있다). [원문확인]

| 동사 · 부사 | 중앙값 | | 동사 · 부사 | 중앙값 |
|---|---|---|---|---|
| show (shows/showed/shown) | 2.20 | | demonstrate | 0.21 |
| may | 1.04 | | might | 0.18 |
| indicate | 0.60 | | reveal | 0.08 |
| could | 0.46 | | likely | 0.06 |
| suggest | 0.35 | | appear | 0.00 |
| possible/possibly | 0.29 | | | |

주장 동사는 show 가 압도적이고 reveal 과 demonstrate 는 드물다. 완화 표현은 may 가 가장 흔하다. 문장 강도는 "show + may" 조합이 기본이다. [추정]

한계 서술은 약하다. 1 수준 또는 2 수준 제목에 limitation 이 들어간 논문은 3/26(envsoft.2022.105341 의 "3.4. Strengths and limitations", hess-21-4895-2017, hess-23-4293-2019 의 "Model evaluation and limitations")이다. Discussion 이나 결론에서 자기 연구의 한계를 명시적으로 말한 논문은 직접 읽어 보니 약 5 편, 향후 연구를 적은 논문은 12/26 이다. 본문 어디든 "limitation" 이 들어간 문장이 있는 논문은 19/26 이지만, 대부분 서론에서 기존 방법의 한계를 말하는 문장이다. [원문확인 개수, 약 5 편은 직접 판정]

자기 한계 문장 실례 [원문확인]:

- "This limitation highlights the need for future studies to incorporate observational data, where available, to enable formal validation and strengthen confidence in model predictions." (10.2166/hydro.2026.064)
- "Notwithstanding the difficulties with unique parameter identification, it should be noted that good state estimates can be achieved for the entire model while the parameter estimates are less accurate, as demonstrated in Section 4.2." (10.1029/2022wr032440)
- "The MLMs applied in this study and in other areas of application have both advantages and limitations." (10.5194/hess-24-4641-2020)

## 10. 서론의 간극 · 목적 문장

서론에서 간극 · 목적 패턴 문장은 135 개가 걸렸다. 유형별로는 However 계열(However, Nevertheless, Despite 등) 80, In this study/This paper 계열 31, "objective/aim of this study" 13, "few studies / has not been / remains" 10, "to our knowledge" 1 이다. 서론 1,000 단어당 However 는 중앙값 1.7 회다. [원문확인 개수, 유형 구분은 규칙]

실제 문장 12 개 [원문확인]:

1. "Thirdly, the possibility of using different (sets of) events to calibrate different (subsets of) parameters has not been investigated." (10.5194/hess-24-869-2020)
2. "Since then, while numerous LID/GI modeling studies have been introduced, best modeling practices for simulating GI in SWMM have received comparatively little attention in the literature (Niazi et al., 2017)." (10.5194/hess-22-2615-2018)
3. "Only few studies have examined the applicability of these adjustment techniques to urban-scale hydrological applications and concluded that they can effectively reduce rainfall bias, thus leading to improvements in the reproduction of hydrological outputs ." (10.5194/hess-19-4001-2015, 끝의 인용은 XML 변환에서 빠졌다)
4. "To our best knowledge, RF and KNN have not been used before as emulators of the MC simulation in parameter identification for hydrological models." (10.5194/hess-24-4641-2020)
5. "To the best of our knowledge, very few studies tried doing optimization analysis on 2D models or 1D-2D models for LID design." (10.1029/2021wr030928)
6. "In addition, few studies have focused specifically on tropical urban catchments, where high-intensity rainfall, rapid urbanization, and data scarcity intersect to complicate flood modeling." (10.2166/hydro.2026.064)
7. "There has been comparatively little work on uncertainty applied to understanding the hydrological impacts of climate change in urban catchments (Lai et al., 2022)." (10.1016/j.jhydrol.2024.131546)
8. "However, the limited interaction between the CLPSO and the local search during the optimization process suggests that there is still room for improvement, especially for unimodal problems." (10.1016/j.envsoft.2022.105341)
9. "Accordingly, the main objective of this study is to develop a RTC package employing real-time streamflow monitoring sensors for the SWMM model using Bayesian optimization with a GP-based surrogate model." (10.1016/j.envsoft.2024.106122)
10. "The main objective of this paper is to investigate the relative contribution of the spatial versus climatic rainfall variability for flow peaks at different locations in the drainage network and for different return periods." (10.5194/hess-21-1559-2017)
11. "This paper aims to address the above issues by introducing ensemble smoother (ES) methods to the UDM calibration." (10.1029/2022wr032440)
12. "In this paper, we look at the effect of rainfall uncertainty on the calibration and performance of two hydrological models: a fully distributed and a semidistributed one." (10.1002/hyp.13319)

번호 붙인 목적 나열 실례 [원문확인]: "Primary objectives of this study are to (1) examine how to configure HREs for GI modeling and (2) develop a methodology for parameterizing a SWMM model that reflects this configuration ..." (10.5194/hess-22-2615-2018)

## 11. 참고문헌

참고문헌 수는 중앙값 55(34-89)이고 Crossref 와 26/26 일치했다. 두 군 모두 중앙값 55 다. [원문확인]

최근 5 년 비율은 게재연도를 Y 라 할 때 Y-4 부터 Y+1 까지(Y+1 은 인쇄 중 문헌)의 인용 비율로 정의했다. 중앙값 0.31(0.11-0.64)이다. HESS 는 JATS `<year>` 요소를 썼고, 나머지는 참고문헌 문자열의 첫 연도를 썼다. 연도를 못 찾은 참고문헌은 1 건이었다. [원문확인]

## 12. 실무 지침 [파생]

아래 권고는 모두 위 실측값에서 끌어낸 것이다. 숫자는 이 26 편의 중앙값이지 학술지 규정이 아니다.

1. 제목은 12-14 단어 명사구로 쓴다. 결과를 진술하는 제목은 표본에 없었다(0/26). 콜론은 도구 이름("XXX-SWMM: ...")이나 사례지("...: a case study of ...")를 붙일 때만 쓴다(4/26).
2. 초록은 200-250 단어, 8-10 문장이다. 정량 결과를 넣은 초록은 42 % 에 그치므로, 핵심 NSE · KGE 값 한두 개를 넣으면 표본의 과반보다 구체적인 초록이 된다. 마지막 문장은 방법 · 도구의 적용 가치를 한 문장으로 닫는 틀이 가장 흔하다.
3. 인칭은 수동태와 "this study" 를 기본으로 하고 we 는 목적 · 제안 문장에만 드물게 쓴다(도시배수 군 we 0.43/1,000 단어, 수동태 약 21/1,000 단어). "It was found that" 은 쓰지 않아도 된다(중앙값 0).
4. 장 구성은 5 개 장(Introduction, Methods, Case study, Results (and Discussion), Conclusions)이 기본이다. 자동보정 · 대리모형 같은 방법 논문이면 "방법 다음 사례" 순서가 표본의 방법 논문과 같다. 석사 논문에서 고찰이 짧으면 Results and Discussion 통합(42 %)이 무난하다.
5. 서론은 본문의 약 17 %(약 1,000-1,100 단어), 결론은 약 5 %(약 370 단어)로 잡는다. 서론 끝에 목적을 (1)(2)로 번호 매기는 방식은 7/26 이 쓴다.
6. 그림은 8-11 장이다. 순서는 "방법 개념도 또는 대상지 지도 (1-2 번), 강우 입력, 민감도 · 매개변수 분포, 성능 비교(상자그림 · 파레토), 수렴, 관측-모의 수문곡선" 이 표본의 평균적 흐름이다. 첫 두 그림은 지도나 개념도로 채운다(24/26). 적합도는 산점도(3/26)보다 수문곡선 겹쳐 그리기(16/26)와 지표 상자그림으로 보인다.
7. 캡션은 명사구 첫 문장으로 시작하고(결과 진술 0 편), 20-30 단어 안팎에 (a)(b) 패널 정의를 넣는다. 선 · 색 설명(22 %)과 단위(12 %)는 드물게 넣으므로, 넣으면 독자에게 친절한 쪽에 속한다.
8. 표는 4 개 안팎이다. 매개변수 이름, 범위, 보정값 표를 반드시 두고(가장 흔한 유형), 성능 표는 NSE · KGE 를 소수 2 자리로 적는다(표 8/10 편, 본문 값 59/92). 최고값 굵게 표시는 캡션에 범례를 적는 hess-24-869-2020 방식이 명확하다.
9. 결과 문장은 "값 + 비교 대상 + 조건" 을 한 문장에 넣고, 해석은 다음 문장으로 넘긴다(비교 표현 36 %, 해석 표현 18 %). 8 절 틀 C(비교형)와 F(물리량 해석형)가 심사에서 가장 설득력 있게 읽힌다. 이 판단은 [추정] 이다.
10. 주장 동사는 show 를 기본으로 하고 demonstrate · reveal 은 아껴 쓴다. 완화는 may 로 한다.
11. 한계 단락은 표본에서 약하다(명시 약 5/26, 제목 3/26). 위성강우 · 레이더 강우 입력 불확실성이나 대리모형 오차처럼 자기 연구의 한계를 Discussion 끝에 한 단락으로 두면 표본보다 나은 쪽이 된다.
12. 데이터 · 코드 가용성 절은 넣는다(62 %, HESS 2017 년 이후 전부). 가능하면 "upon request" 보다 저장소 링크를 준다.
13. 참고문헌은 50-60 개, 그중 최근 5 년 문헌은 약 30 % 로 잡는다.

## 13. 측정하지 못한 것과 한계

Water Research 와 Urban Water Journal 논문은 코퍼스에 없다. 후보는 찾았으나 전문 확보까지 진행하지 않았다. 확인 방법: 같은 브라우저 저장 절차(`s03_receiver.py`)로 추가하면 된다. [판정보류]

Q1 여부는 이 작업에서 SJR 로 논문마다 대조하지 않았다. HESS, WRR, J. Hydrol., EMS, J. Environ. Manage. 는 수자원 범주 상위권 학술지로 알려져 있지만, J. Hydroinform. 과 Hydrol. Process. 의 연도별 사분위는 확인하지 않았다. 확인 방법: SCImago Journal Rank 의 Water Science and Technology 범주에서 게재연도별 사분위를 본다. [판정보류]

표본은 26 편이고 HESS 가 12 편(46 %)이라 HESS 문체(긴 캡션, 필수 데이터 가용성 절)로 기울어 있다. 학술지별 비교는 표본이 작아 하지 않았다.

그림 · 표 · 초록 단락 · 수동태는 키워드와 정규식 근사다. 그림 분류는 표본 대조 정확도가 약 73-84 % 다. 수동태는 "be + -ed" 형만 세므로 불규칙 과거분사 일부와 형용사적 분사가 섞인다.

그림 유형은 캡션 글로만 판정했고 이미지는 보지 않았다. 표의 굵은 글씨는 HTML · XML 태그로만 셌고, 출판사가 CSS 로 굵게 만든 경우는 놓쳤을 수 있다.

HESS XML 은 교차참조(그림 · 절 · 인용)를 텍스트에서 빼기 때문에 인용한 일부 문장에 "(see Table )" 같은 빈 괄호가 남는다. 해당 인용에는 표시를 달았다.

초록 첫 문장 · 마지막 문장의 "기능" 판정은 직접 읽은 인상이다. [추정]

## 14. 파일

모든 경로는 `C:\Users\SGJEONG99\AppData\Local\Temp\claude\c--Users-SGJEONG99-Desktop-Prompt\bcd23293-4bd2-40be-8a2f-142282b049b3\scratchpad\corpus\` 아래에 있다.

| 파일 | 내용 |
|---|---|
| `corpus_list.csv` | 26 편 목록, Crossref 대조 결과 |
| `metrics_per_paper.csv` | 논문별 지표 (제목 · 초록 · 장 · 태 · 헤징 · 그림 · 표 · 참고문헌) |
| `figures_per_caption.csv` | 캡션 254 개별 유형 · 문체 판정 |
| `tables_per_caption.csv` | 표 103 개별 유형 · 굵은 글씨 · 소수 자릿수 |
| `summary.json`, `extras.json`, `decimals.json`, `limits.json` | 집계값 |
| `examples.json` | 결과 문장 · 간극 문장 · 초록 첫/끝 문장 원문 (DOI 포함) |
| `raw\` | 원문 XML 12 개, HTML 14 개 (본문 없는 HESS XML 2 개도 남겨 둠) |
| `parsed\` | 통일 JSON 26 개 (`_excluded_stub_xml\` 에 제외 2 개) |
| `s01_search.py` 에서 `s09_limits.py` | 검색, 위치 조회, 수신기, 대조, 파싱, 지표, 추가 집계 스크립트 |

## 15. 정정: 학술지별로 갈라 보면 (2026-09-22 추가)

12 절의 실무 지침은 26 편을 합친 중앙값에서 끌어냈다. 26 편 중 12 편이 HESS 라, 합친 값을
"SCI 논문 일반" 으로 읽으면 안 된다(사용자 지적). `F_코퍼스\s11_journal_split.py` 로 학술지별로
가른 결과 차이가 컸다.

```text
                 we /1000 단어  초록 단어  초록에 수치  초록 this study  캡션 단어
HESS (12)        0.42           272        67 %         50 %             28
WRR (4)          5.36           220        25 %         100 %            35
J. Hydrology (4) 0.50           220        25 %         50 %             38
EMS (2)          2.19           194        0 %          50 %             24
J. Hydroinform.(2) 0.00         194        0 %          100 %            12
HESS 외 (14)     1.10           201        21 %         79 %             29
```

따라서 12 절 3 번("인칭은 수동태와 this study 를 기본")은 HESS · J. Hydrology 에 가까운 관행이고
WRR 에는 맞지 않는다. 12 절 2 번(초록 수치)도 HESS 쪽 값이다. 지침(`13_논문.md`)은 학술지별
수치와 "목표 학술지를 직접 잰다" 는 규칙으로 고쳤다. HESS 외 학술지는 2-4 편씩이라 학술지별
값도 방향만 본다.
