# Secure Task Management API

A RESTful backend API built with FastAPI that enables multi-user task management with JWT-based authentication and user-scoped authorization. The system supports secure login, protected CRUD operations, and paginated task retrieval. Deployed on Render.

Live Demo:
https://secure-task-api-t99d.onrender.com/docs

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- passlib (bcrypt)
- Uvicorn
- pytest (automated testing)
- Render (deployment)

## Module Responsibilities

- **main.py** — Defines API endpoints and integrates dependencies.
- **models.py** — Defines relational database structure using SQLAlchemy.
- **schemas.py** — Defines request validation and response serialization models.
- **auth.py** — Handles JWT token creation and validation.
- **security.py** — Encapsulates password hashing and verification logic.
- **database.py** — Configures database engine and session management.

This modular structure ensures separation of concerns and maintainable backend architecture.

## Testing

Automated API tests implemented using pytest.

- **test_auth.py** - Tests user registration and JWT login flow.
- **test_tasks.py** - Tests protected routes, authorization enforcement, task creation, and pagination behavior.

## Local Setup

### 1. Clone Repository

```bash
git clone https://github.com/saadsajid-dev/secure-task-api.git
cd secure-task-api
```

### 2. Create Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Secret Key

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 5. Create .env File in your root folder, and write:

```ini
SECRET_KEY=your_generated_secret_key
```

### 6. Run Server

```bash
uvicorn app.main:app --reload
```

### 7. Test on your local server

Visit:
http://127.0.0.1:8000/docs