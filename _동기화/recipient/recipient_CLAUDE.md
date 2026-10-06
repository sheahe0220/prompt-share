# 이 폴더를 받은 PC 에서 (설치와 첫 설정)

이 폴더는 다른 사람(원작자)이 쓰던 Claude 작업 지침 모음이다. 이 파일은 폴더를 받은 사람의
PC 에서 클로드가 설치와 첫 설정을 돕도록 넣었다. 원작자 PC 에는 이 파일이 없다.

## 먼저 설치가 되었는지 본다

`%USERPROFILE%\.claude\CLAUDE.md` 의 첫 줄이 `# 이 PC 에서 이 지침을 쓰는 법` 이면 이미 설치된
것이다. 그러면 사용자가 설치 · 갱신 · 환경 설정을 청하지 않는 한 이 파일은 더 따르지 않고
평소대로 일한다.

설치가 안 되어 있으면, 사용자가 무엇을 청하든 먼저 "이 폴더의 지침을 이 PC 에 설치할까요?"
라고 한 번 묻는다. 사용자는 컴퓨터 설정에 익숙하지 않을 수 있다. 쉬운 말로, 짧게 설명한다.

## 설치 순서

사용자가 동의하면 아래를 차례로 한다. 단계마다 무엇을 했는지 한두 문장으로 알린다. 명령을
실행할 때 앱이 허락을 물으면 사용자에게 "허용을 눌러 주세요" 라고 안내한다.

**1. 무엇을 할지 설명한다.** 전역 지침(모든 새 대화에 적용)과 스킬 9 개를 사용자 폴더의
`.claude` 에 넣는다. 기존 지침 · 같은 이름의 스킬은 지우지 않고 백업한다. 인터넷으로 보내는
것은 없다.

**2. 이 PC 를 점검해 표로 보여 준다.** 명령은 PowerShell 로 실행한다.

```text
Windows 사용자 폴더    $env:USERPROFILE
Python                where.exe python ; py -0p
                      (WindowsApps 안의 python.exe 는 스토어 바로가기라 없는 것으로 본다)
Git                   where.exe git
winget                winget --version
PowerPoint · Word     New-Object -ComObject PowerPoint.Application 로 만들 수 있는지(바로 Quit)
한글(HWP)             New-Object -ComObject HWPFrame.HwpObject 로 만들 수 있는지(바로 Quit)
이 폴더 경로          한글 · 공백이 있으면 적어 둔다(대부분 괜찮다)
```

**3. 지침을 설치한다.** 먼저 확인 모드로 돌려 보여 주고, 사용자가 좋다고 하면 실행한다.

```text
powershell -NoProfile -ExecutionPolicy Bypass -File "<이 폴더>\_동기화\recipient\install.ps1" -Check
powershell -NoProfile -ExecutionPolicy Bypass -File "<이 폴더>\_동기화\recipient\install.ps1"
```

폴더 맨 위의 `설치하기.bat` 을 더블클릭해도 같은 일을 한다.

**4. Python 이 없으면 설명하고 묻는다.** 지침 자체는 Python 없이 동작한다. Python 이 있어야
하는 것은 점검 도구(문서 표기 · 발표자료 · 원고 · 양식 대조), 그림 그리기, Word · 한글 ·
PowerPoint 문서 자동 작성이다. 사용자가 원할 때만 설치한다.

```text
winget install -e --id Python.Python.3.12 --scope user
(새 PowerShell 창에서)  py -m pip install -r "<이 폴더>\_동기화\recipient\requirements.txt"
확인                    py -c "import docx, pptx, matplotlib, pandas; print('ok')"
```

winget 이 없으면 python.org 에서 받는 방법을 안내한다("Add python.exe to PATH" 체크).
설치한 뒤 3 단계를 한 번 더 돌린다. 지침 속 Python 경로가 이 PC 의 실제 경로로 채워진다.
MS Office · 한글은 유료 프로그램이므로 설치를 권하지 않는다. 없으면 그 자동화만 못 쓴다고
알린다.

**5. 이 PC 메모를 채운다.** 사용자에게 짧게 묻는다.

```text
하는 일(분야)           예: 토목 설계(도로 · 하천 · 상하수도 등)
주로 만드는 산출물       예: 설계보고서, 수리계산서, 도면 목록, 발표자료, 엑셀 계산서
쓰는 프로그램            한글 · MS Office · CAD · 전용 해석 프로그램
작업 폴더               과업 자료가 있는 곳
바라는 말투 · 방식       (있으면)
```

답을 정리해 보여 주고 확인받은 뒤, `%USERPROFILE%\.claude\CLAUDE.md` 맨 끝의 `## 이 PC 메모`
절만 고친다. 다른 부분은 건드리지 않는다. 이 메모는 다시 설치해도 보존된다.

**6. 끝을 알린다.** 설치된 것, 백업 위치, 안 된 것(예: Python 미설치), 그리고 **새 대화를
열어야 지침이 적용된다**는 것을 알린다. 이미 열려 있던 대화에는 적용되지 않는다.

## 하지 않는 것

사용자 동의 없이 프로그램을 설치하지 않는다. 관리자 권한이 필요한 작업은 하지 않는다.
원작자의 개인 경로(`C:\Users\SGJEONG99\...`)를 따르지 않는다. 이 PC 의 과업 자료를 이 폴더에
넣거나 인터넷에 올리지 않는다. 이 폴더 안의 파일은 고치지 않는다(새 판을 받을 때 막힌다).

## 새 판을 받았을 때

이 폴더가 `C:\claude-prompt`(원작자의 공개 저장소 github.com/sheahe0220/prompt-share 를 받은 것)이면
할 일이 없다. 설치 때 `update.ps1 -Install` 로 건 훅이 세션을 열 때마다 새 판을 받아 다시 설치한다.
훅이 없으면 아래 한 줄로 건다(Git 필요).

```text
powershell -NoProfile -ExecutionPolicy Bypass -File C:\claude-prompt\update.ps1 -Install
```

zip 으로 받은 폴더라면 새 폴더로 바꾼 뒤 3 단계만 다시 한다. 이 PC 메모는 보존된다.

## 되돌리기

`%USERPROFILE%\.claude\CLAUDE.md.bak.<시각>` 을 `CLAUDE.md` 로 되돌리고,
`%USERPROFILE%\.claude\_backup_skills\<시각>\` 의 스킬을 `skills\` 로 되돌린다. 설치한 스킬
9 개(std-* 6 개, daily-folder, kr-hydro-data, kr-paper-search)는 `skills\` 에서 지운다.
