# 📘 Assignment: Python Text Processing

## 🎯 Objective

문자열 처리와 파일 I/O를 사용하여 텍스트 데이터를 읽고, 분석하고, 변형하는 기본 파이썬 프로그램을 작성합니다.

## 📝 Tasks

### 🛠️ Text Analysis Utilities

#### Description
로컬 텍스트 파일을 읽어 단어 수, 줄 수, 빈도 상위 단어를 계산하고 간단한 텍스트 변환(예: 특정 단어 치환)을 수행하는 유틸리티를 구현합니다.

#### Requirements
Completed program should:

- 파일 경로를 입력으로 받아 파일이 존재하지 않으면 적절한 오류 메시지를 출력한다.
- 전체 단어 수와 줄 수를 정확히 계산한다.
- 단어 빈도 수를 계산하고 상위 N개 단어를 반환한다.
- 특정 단어를 다른 단어로 교체한 결과를 새 파일로 저장하는 기능을 제공한다.
- 입력 검증과 예외 처리를 포함한다.
- 기능을 분리한 함수들과 `main()` 진입점을 사용한다.

## 🔧 Starter

이 폴더의 `starter-code.py`를 사용하세요. 예시 파일 `sample.txt`가 제공됩니다. 실행 예:

```bash
python assignments/python-text-processing/starter-code.py sample.txt --top 5
```

## 📚 Learning outcomes

- 파일 입출력과 텍스트 인코딩 처리
- 문자열 메서드와 정규 표현식 기본
- 데이터 집계(단어 빈도) 및 간단한 변환 파이프라인 설계
