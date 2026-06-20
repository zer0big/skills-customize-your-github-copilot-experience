# 📘 Assignment: FastAPI REST API — Simple Items Service

## 🎯 Objective

FastAPI를 사용하여 간단한 RESTful API를 구현합니다. 학생은 기본 CRUD 엔드포인트와 Pydantic 모델을 사용한 입력 검증을 배우게 됩니다.

## 📝 Tasks

### 🛠️ Build the Items API

#### Description
간단한 아이템 관리 API를 구현합니다. 아이템은 메모리 저장소에 보관하며, 클라이언트는 아이템을 생성, 조회, 수정, 삭제할 수 있습니다.

#### Requirements
Completed program should:

- `GET /items` — 모든 아이템 목록을 반환한다.
- `GET /items/{id}` — 특정 아이템을 반환한다 (존재하지 않으면 404).
- `POST /items` — 새 아이템을 생성한다 (요청 바디는 JSON, `name` 필수).
- `PUT /items/{id}` — 기존 아이템을 수정한다 (존재하지 않으면 404).
- `DELETE /items/{id}` — 아이템을 삭제한다 (존재하지 않으면 404).
- Pydantic 모델을 사용하여 입력을 검증한다.
- 적절한 HTTP 상태 코드와 명확한 에러 메시지를 반환한다.
- 데이터베이스는 필요하지 않으며, 간단한 in-memory 저장소(예: dict)를 사용한다.

## 🔧 Starter

이 폴더의 `starter_code.py`를 사용하세요. 로컬에서 실행하려면 `requirements.txt`를 설치한 후 아래 명령을 사용합니다:

```bash
pip install -r assignments/fastapi_rest_api/requirements.txt
uvicorn assignments.fastapi_rest_api.starter_code:app --reload --port 8000
```

## 📚 Learning outcomes

- FastAPI 기본 구조와 라우팅 이해
- Pydantic을 이용한 데이터 검증
- RESTful API 설계(HTTP 메서드, 상태 코드)
