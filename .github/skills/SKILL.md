---
name: new-assignment
description: 머징턴 고등학교 학생을 위한 새 프로그래밍 숙제 과제를 만듭니다. 사용자가 새 과제, 연습 문제 또는 숙제를 만들기, 추가하기, 스캐폴딩하기, 생성하기를 원할 때마다 이 스킬을 사용하세요. 사용자가 “과제”라는 단어를 명시적으로 사용하지 않더라도 적용합니다.
---

# 새 프로그래밍 과제 만들기

과제는 `assignments/<id>/`에 저장되며, 웹사이트는 `config.json`을 읽어 과제를 표시합니다. 두 가지를 모두 만들려면 다음 단계를 따르세요.

## 1단계: 요구 사항 수집

사용자가 지정하지 않았다면 과제가 어떤 프로그래밍 개념을 다루어야 하는지 물어보세요.

> 📖 난이도, 범위, 시작 코드를 포함해야 하는 시점에 대한 지침은 [references/assignment-guide.md](references/assignment-guide.md)를 읽어 보세요.

## 2단계: 과제 만들기

1. [과제 템플릿](../../../templates/assignment-template.md)을 따라 `assignments/<kebab-case-id>/README.md`를 만듭니다.
2. (선택 사항) 시작 코드 또는 데이터 파일을 같은 디렉터리에 추가합니다.

## 3단계: 웹사이트에 등록

포함된 스크립트를 사용하세요. `config.json`을 수동으로 편집하지 마세요.

**과제 등록:**

    node .github/skills/new-assignment/scripts/update-config.js <id> "<title>" "<description>"

**각 파일을 첨부 파일로 등록**(시작 코드, 데이터 파일 등):

    node .github/skills/new-assignment/scripts/add-attachment.js <id> "<display-name>" <filename> <type>

일반적인 유형: `python`, `csv`, `json`, `txt`, `html`

## 4단계: 확인

과제가 올바르게 등록되었는지 확인합니다. `config.json`에 새 항목이 포함되어 있고, 생성된 모든 파일이 디스크에 존재하는지 확인하세요.