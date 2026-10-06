---
name: kr-paper-search
description: "국내 학술 논문 검색. KCI 와 DBpia 의 공식 Open API 만 불러 제목 · 저자 · 학술지 · 연도 · DOI · URL 을 CSV 로 모은다. 다음 상황에서 사용할 것: \"국내 논문\", \"KCI\", \"DBpia\", \"선행연구\", \"한국 논문 찾아\", \"학술지 검색\", \"참고문헌 찾아\", \"국내 연구 동향\". 키가 없으면 무엇이 없는지 알리고 멈춘다. 외국 논문은 alphaXiv · Consensus · Scholar Gateway 를 쓴다."
---

<!-- 원본: C:\Users\SGJEONG99\Desktop\Prompt\_도구\skills\kr-paper-search\
     ~/.claude/skills/kr-paper-search 는 정션이다. 원본을 고친다. -->

# 국내 논문 검색

```text
python.exe -X utf8 scripts/kr_papers.py "초기 우수 비점오염" --src kci dbpia --n 20 --out 결과.csv
python.exe -X utf8 scripts/kr_papers.py "대심도 터널" --src kci --from 2015 --to 2026
```

파이썬은 `C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe` 를 쓴다.

## 키

```text
환경변수   KCI_API_KEY · DBPIA_API_KEY
또는 파일   %USERPROFILE%\.claude\keys\kr_papers.env   (git 에 올리지 않는다)
             KCI_API_KEY=...
             DBPIA_API_KEY=...
발급       KCI    https://www.kci.go.kr > Open API 신청
           DBpia  https://api.dbpia.co.kr > 키 발급
```

**키를 채팅에 적게 하지 마라.** 사용자가 직접 파일에 넣게 한다.

## 결과를 쓰는 법

**검색 결과는 인용 근거가 아니다.** 목록일 뿐이다. 인용하려면 원문을 열어 쪽 번호를
확인한다. `13_논문.md` 의 인용 규칙과 `20_자료조사.md` 를 따른다.

찾은 목록은 과업의 `09_원자료\00_원자료_색인.md` 옆에 CSV 로 남긴다. 무엇을 어떤
검색어로 언제 찾았는지가 남아야 선행연구 절을 다시 짤 수 있다.

## 확인한 것과 못 한 것 (2026-09-20)

```text
KCI    주소 · 인자 · 응답 필드   공식 명세서에서 확인. 오류 응답은 실제 서버로 확인
DBpia  주소 · 인자 · 응답 필드   공식 안내에서 확인. http 는 https 로 옮겨진다(실측)
       결과 한 건을 감싸는 태그   item 으로 [추정]. 안내에 없다
RISS   넣지 않음                공식 명세를 확인하지 못했다 [판정보류]
성공 응답                        키가 없어 실제로는 못 봤다
```

**키를 넣고 처음 돌렸을 때 DBpia 가 0 건이면** 결과 묶음 태그가 `item` 이 아닌 것이다.
응답 XML 을 파일로 떠서 태그 이름을 보고 `parse_dbpia` 를 고친다.

## 함정

```text
증상  DBpia 시험용 키(DBPIA_DEMO_APIKEY)로 부르면 결과가 없다
원인  시험용 키가 더는 듣지 않는다. <Code>E0001</Code> 을 돌려준다 (실측)
대처  실제 키를 받는다
```

```text
증상  http 주소로 부르면 빈 응답이다
원인  301 로 https 로 옮겨졌다
대처  https 주소를 쓴다. 코드는 이미 https 다
```
