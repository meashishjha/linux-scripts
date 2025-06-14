# GPT Prompts: FastAPI-Based Secure, Scalable ToDo App (Module-Wise Progressive Setup)

---

## 🧱 Prompt 1: Bootstrap Project with Landing Page

Create the foundational structure for a FastAPI-based secure ToDo web app.

### Requirements:
- Set up a clean project structure:
  - `app/`, `routes/`, `templates/`, `static/`, `models/`
- Create `main.py`, and a basic home page using Jinja2
- Show a top navbar with a logo (left) and Register/Login links (right)
- Add `requirements.txt` with pinned minimal dependencies
- Create `README.md` with app description and run instructions

### Tech Stack:
- FastAPI
- Jinja2
- HTML5 + CSS

Project layout:
```
todo_app/
├── app/
│   ├── main.py
│   ├── routes/home.py
│   ├── templates/home.html
│   └── static/logo.png
├── requirements.txt
├── README.md
```

---

## 🧾 Prompt 2: Add Secure Registration Module

Add a registration module to the FastAPI ToDo App.

### Requirements:
- `/register` (GET/POST) route
- Registration form with:
  - Email (validated on front/back)
  - Password (min 8 characters)
- Backend:
  - Hash password using `passlib[bcrypt]`
  - Save user in SQLite using `sqlmodel`
  - Default role = `user`, with created timestamp

Update:
- Add `User` model
- Add `register.html` template
- Update `requirements.txt`: `passlib[bcrypt]`, `sqlmodel`

---

## 🔐 Prompt 3: Add Login and Session Handling

Add login functionality with secure session handling.

### Requirements:
- `/login` route (GET/POST)
- Login form: email + password
- Validate credentials (check hash)
- On success: set secure cookie using `itsdangerous`
- On failure: show error
- Add `/dashboard` page (visible only if logged in)

Update:
- Add `login.html`, `dashboard.html`
- Use cookie-based session with signed token (`itsdangerous`)

---

## 📝 Prompt 4: Add User-Scoped ToDo CRUD Module

Add ToDo functionality to allow logged-in users to manage their tasks.

### Requirements:
- `/todos` route
- Show all user's ToDos
- Allow creation, deletion (POST)
- Store each ToDo with FK to user ID

Update:
- Create `ToDo` model
- Create `todos.html` for display + form
- Protect with auth (same session token)

---

## 🛡 Prompt 5: Add Admin Panel for Role Management

Create an admin dashboard for managing user roles.

### Requirements:
- `/admin` route (only for users with `role = admin`)
- Show list of all users
- Allow changing user roles (`user <-> admin`)
- Form-based role switch

Update:
- Add `admin.html` template
- Enforce role check in route logic

---

## 🔓 Prompt 6: Add Logout Functionality

Add logout support to clear user session.

### Requirements:
- `/logout` route
- Deletes session cookie and redirects to home
- Show Logout link when user is authenticated in navbar

Update:
- Clear cookie using `response.delete_cookie("session")`
- Update all template navbars to show login/logout conditionally

---

## 🧪 Prompt 7: Add Unit Tests and Coverage

Add unit tests to the FastAPI ToDo App using `pytest`.

### Requirements:
- Add `tests/` folder
- Write tests for:
  - Registration
  - Login
  - ToDo creation
- Use `httpx.AsyncClient` for test calls
- Use in-memory SQLite

Dev dependencies:
- `pytest`, `pytest-cov`, `httpx`, `mypy`, `ruff`

Commands:
- `pytest --cov=app tests/`

---

## 🐳 Prompt 8: Add Docker Support with .env

Dockerize the app with support for `.env`.

### Requirements:
- Create `Dockerfile`
- Add `.env` file (SECRET_KEY, DATABASE_URL)
- Modify code to read config via `os.getenv`
- Optional: Add `docker-compose.yml`

Ensure static + templates are correctly mounted.

`.dockerignore`:
```
__pycache__/
*.pyc
.env
*.db
```

---

## ⚙️ Prompt 9: Add GitHub Actions CI/CD

Add GitHub Actions CI pipeline for FastAPI ToDo App.

### Requirements:
- Lint code with `ruff`
- Type-check with `mypy`
- Run tests with `pytest`
- Upload coverage using `codecov` action

File: `.github/workflows/ci.yml`

Triggers:
- `push`
- `pull_request`

Ensure setup installs dev dependencies.
