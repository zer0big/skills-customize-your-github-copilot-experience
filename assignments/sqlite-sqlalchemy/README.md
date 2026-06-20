# 📘 Assignment: Persistent Data with SQLite & SQLAlchemy

## 🎯 Objective

SQLite와 SQLAlchemy를 사용해 데이터를 영구 저장하고 Python으로 CRUD를 구현합니다. 학생은 관계형 데이터 모델링과 ORM 사용법을 배우게 됩니다.

## 📝 Tasks

### 🛠️ Build the Items Storage

#### Description
SQLAlchemy ORM으로 `Item` 모델을 정의하고, SQLite 데이터베이스에 대해 생성(Create), 조회(Read), 수정(Update), 삭제(Delete) 작업을 수행하는 유틸리티를 구현합니다. 옵션으로 FastAPI와 연동하는 간단한 API 엔드포인트를 추가할 수 있습니다.

#### Requirements
Completed program should:

- SQLAlchemy `declarative` 방식으로 `Item` 모델을 정의 (`id`, `name`, `description` 등).
- 로컬 SQLite 데이터베이스 파일을 생성하고 연결한다.
- CRUD 함수들을 구현: `create_item`, `get_item`, `update_item`, `delete_item`, `list_items`.
- 입력 검증과 예외 처리를 포함한다.
- 예제 실행 스크립트(`starter_code.py`)가 있어 기본 사용법을 보여준다.
- (선택 사항) FastAPI와 연결해 REST API 엔드포인트로 노출하면 추가 점수를 준다.

## 🔧 Starter

이 폴더의 `starter_code.py`는 SQLAlchemy로 작은 DB를 초기화하고 기본 CRUD를 실행하는 예시를 포함합니다. 의존성을 설치하려면:

```bash
pip install -r assignments/sqlite-sqlalchemy/requirements.txt
python assignments/sqlite-sqlalchemy/starter_code.py
```

## 📚 Learning outcomes

- SQLAlchemy ORM 기초와 데이터 모델링
- SQLite를 사용한 로컬 퍼시스턴스 관리
- 트랜잭션, 세션 사용법과 예외 처리
