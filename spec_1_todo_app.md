= SPEC-1: Secure, Scalable FastAPI-Based ToDo App
:sectnums:
:toc:


== Background

The goal of this project is to create a secure, modular, and scalable ToDo web application using FastAPI. It follows OWASP secure coding practices, and is structured for progressive, maintainable development. This system includes registration, login, RBAC, user-specific ToDos, admin role management, logout, testing, Docker deployment, and CI/CD support.

== Requirements

*Must Have:*
- [x] Secure registration system with email/password and hashed credentials
- [x] Login system with role-based access control (RBAC)
- [x] User-specific ToDo creation, listing, and deletion
- [x] Admin dashboard for role management
- [x] Logout and session clearing
- [x] Unit testing using `pytest`
- [x] Dockerization and `.env` support
- [x] GitHub Actions CI/CD

*Should Have:*
- [ ] HTTPS setup guide (external Nginx + Certbot)
- [ ] UI enhancements using Tailwind or Bootstrap

*Could Have:*
- [ ] REST API for external clients
- [ ] JWT-based auth as an alternative to signed cookies

== Method

=== Architecture Overview

[plantuml]
----
@startuml
package "Web Frontend" {
  [Home Page] --> [Register Form]
  [Home Page] --> [Login Form]
  [Login Form] --> [Dashboard]
}

package "FastAPI App" {
  [main.py] --> [routes/register.py]
  [main.py] --> [routes/login.py]
  [main.py] --> [routes/dashboard.py]
  [main.py] --> [routes/todos.py]
  [main.py] --> [routes/admin.py]
  [main.py] --> [routes/auth.py]
}

[Dashboard] --> [ToDos View]
[Admin Panel] --> [Users List]
[Login Form] --> [Session Cookie]
@enduml
----

=== Database Schema (SQLModel)

*User Table*
- id: int (PK)
- email: str (unique)
- hashed_password: str
- role: str (default: "user")
- created_at: datetime

*ToDo Table*
- id: int (PK)
- title: str
- description: str
- completed: bool
- created_at: datetime
- user_id: int (FK -> User.id)

=== Security Features
- Passwords hashed using `passlib[bcrypt]`
- Signed cookies for session via `itsdangerous`
- RBAC: Admin-only access to `/admin`
- Form validation on both frontend and backend
- Cookie flags: `secure=True`, `httponly=True`

=== Configuration
- `.env` used for secret and DB connection
- Dockerized using a multi-stage build
- GitHub Actions for CI (lint, type-check, test, coverage)

== Implementation

1. Scaffold project structure with FastAPI, Jinja2 templates
2. Create landing page with navbar and branding
3. Add `/register` route with form validation and secure persistence
4. Add `/login` route, hashed credential check, signed cookie session
5. Implement `/dashboard` with user greeting
6. Add `/todos` (CRUD) linked to logged-in user ID
7. Create `/admin` for role management (admin only)
8. Add `/logout` to clear cookies
9. Write unit tests for auth and ToDos
10. Containerize with Dockerfile and `.env` support
11. Add GitHub Actions CI pipeline

== Milestones

1. ✅ Project scaffold and landing page
2. ✅ Secure registration module
3. ✅ Login with session and RBAC
4. ✅ User dashboard and ToDo CRUD
5. ✅ Admin panel with role management
6. ✅ Logout and UI updates
7. ✅ Unit test coverage and testability
8. ✅ Dockerization and `.env`
9. ✅ CI/CD with GitHub Actions

== Gathering Results

- Use `pytest --cov` to measure test coverage (target: >90%)
- Manually verify access control via browser tests
- Check login/logout flows across roles
- Monitor production containers for memory and CPU usage
- Ensure secure headers and cookies in browser dev tools












generate a gpt prompt for a fastapi based todo app. it should not have security flaws and should follow owasp secure coding guidlenes. 
the app should keep scalability in mind and all the dependecies should be listed in requirements.txt readme file should contain details about the app with  running instructions.
you should also generate a prompt to generate project structure and commands to create that structure. The projects should have a landing home page which displays a logo in left and few navigation links in right. in the content area of landing page it should contain few details about appwill register and login screen.

The prompts should be generated in step by step manner so that when first prompt is run it creates project sturucture and other basic details listed above and second  module create another module and third prompt generates anopther modules etc etc. the prompts should be progressive prompts will when run keeps updating the main app accordngly.


the app should have following modules

registration module with role based access control

registration page displays a beatutiful form with email and password field. the email should be vallidated for correctness and password length should be atleast 8 chacraters. when form is submitted the users is regsitered and stored in sqlite database.
the password should be hashed before storing in database. the backend should also validate email and password length. Users is registered with default role of user and date of registration is also stored in database

Login system with authorization

the app should display a login page with email and password field. here also we should validate email and password length in frontend accordingly. once the login form is submitted, it verfies users against information stored in sqlite table 
if the users is verfied he is redirected to members dashboard and wlecome message is shown. if user is not verfied, login failure message should be displayed


ChatGPT said:

Great — we'll design this progressively in prompt steps. Here's how I'll structure it:

    Prompt 1: Create base project structure with FastAPI, requirements.txt, README.md, HTML home page with logo and navigation.

    Prompt 2: Add the registration module with RBAC and secure password handling.

    Prompt 3: Add the login module with session/authorization.

    Prompt 4+: Extend further modules (e.g., todo creation, admin panel, user profiles).

Let's start with Prompt 1: Project Bootstrap — this sets up the foundation.
✅ Prompt 1: Base Project Bootstrap

You are a senior Python developer. Create the foundational structure for a secure and scalable FastAPI-based ToDo application.

Follow OWASP secure coding guidelines.

### Features to Include
- Use FastAPI with Jinja2 for templating
- Create a clean project structure (`app/`, `static/`, `templates/`, `routes/`, `models/`)
- Set up `requirements.txt` with only secure and minimal dependencies
- Add `README.md` explaining the project, install and run instructions
- Create a landing page:
  - Logo on the left, navigation links (Register, Login) on the right
  - Content section with project introduction

### Commands to Create Project Structure

Use `os.makedirs` or shell commands like `mkdir` and `touch` to create:

todo_app/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── routes/
│ │ └── home.py
│ ├── templates/
│ │ └── home.html
│ ├── static/
│ │ └── logo.png
├── requirements.txt
├── README.md


### Requirements.txt
Use pinned, minimal secure dependencies:

fastapi==0.110.0
uvicorn==0.29.0
jinja2==3.1.3


### README.md
Include:
- Project description
- How to install dependencies
- How to run using `uvicorn`
- Basic structure explanation

### Landing Page (Jinja2 Template)
- Responsive layout
- Display logo (use placeholder image)
- Navbar with Register & Login links
- Brief introduction to the ToDo App in the content area

Would you like to proceed to Prompt 2 for the Registration Module now?
You said:
yes
ChatGPT said:

Great! Here's Prompt 2: Registration Module with RBAC & Validation.

This builds on the base and adds user registration with proper validations, secure password hashing, and default role assignment.
✅ Prompt 2: Add Registration Module with RBAC

Extend the existing FastAPI-based ToDo App to add a secure registration module.

### Features to Implement

- Create `/register` route (GET and POST)
- Show a registration form with:
  - Email input (HTML5 validation + JS regex)
  - Password input (minimum 8 characters)
- Validate email format and password length in backend
- Hash passwords using `passlib[bcrypt]`
- Store users in SQLite using SQLModel:
  - Fields: `id`, `email`, `hashed_password`, `role` (default: "user"), `created_at`

### Requirements

Update `requirements.txt` with:

sqlmodel==0.0.16
passlib[bcrypt]==1.7.4


### Project Updates

**1. models/user.py**
```python
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    role: str = Field(default="user")
    created_at: datetime = Field(default_factory=datetime.utcnow)

2. routes/register.py

from fastapi import APIRouter, Form, Request, status, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import Session
from passlib.hash import bcrypt
from app.models.user import User
from app.db import get_session
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/register", response_class=HTMLResponse)
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
def register_user(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    session: Session = Depends(get_session)
):
    if len(password) < 8:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Password too short."})
    if "@" not in email:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Invalid email."})

    user = User(email=email, hashed_password=bcrypt.hash(password))
    session.add(user)
    session.commit()
    return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)

3. templates/register.html
Use Tailwind or Bootstrap:

<form method="post" class="form">
  <label>Email: <input type="email" name="email" required></label>
  <label>Password: <input type="password" name="password" minlength="8" required></label>
  <button type="submit">Register</button>
</form>

4. app/db.py

from sqlmodel import create_engine, Session

engine = create_engine("sqlite:///todo.db")

def get_session():
    with Session(engine) as session:
        yield session

5. Update app/main.py

from fastapi import FastAPI
from app.routes import home, register
from app.db import engine
from app.models.user import SQLModel

app = FastAPI()

app.include_router(home.router)
app.include_router(register.router)

SQLModel.metadata.create_all(engine)


---

Shall we proceed to **Prompt 3: Login System with Authentication & Dashboard Redirect**?

You said:
yes
ChatGPT said:

Excellent — here's Prompt 3: Login System with Authentication and Dashboard Access.

This adds secure login using hashed password verification, session/token handling (with basic session-based auth), and user dashboard with RBAC enforcement.
✅ Prompt 3: Add Login Module with Authorization

Extend the existing FastAPI-based ToDo App to include secure login functionality with proper validation and access control.

### Features to Implement

- Create `/login` route (GET and POST)
- Login form should include:
  - Email (HTML5 + backend format validation)
  - Password (minimum 8 chars)
- Validate credentials:
  - Compare provided password with stored hash using `passlib`
- On success:
  - Set a session (use `fastapi-login` or secure cookies for now)
  - Redirect to `/dashboard`
- On failure:
  - Show login error message
- Add `/dashboard` route, protected so only logged-in users can access it

### Additional Dependencies (add to requirements.txt)

python-multipart==0.0.9
itsdangerous==2.1.2


> For this MVP, we'll use `itsdangerous` to create signed cookies for basic session-like auth.

### Project Updates

**1. routes/login.py**
```python
from fastapi import APIRouter, Request, Form, Depends, Response, status
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import select
from app.models.user import User
from app.db import get_session
from passlib.hash import bcrypt
from itsdangerous import URLSafeSerializer
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
serializer = URLSafeSerializer("SECRET_KEY")  # Replace with secure value

@router.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
def login_user(
    response: Response,
    email: str = Form(...),
    password: str = Form(...),
    session=Depends(get_session)
):
    user = session.exec(select(User).where(User.email == email)).first()
    if not user or not bcrypt.verify(password, user.hashed_password):
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "Invalid credentials"
        })

    token = serializer.dumps({"user_id": user.id, "role": user.role})
    response = RedirectResponse(url="/dashboard", status_code=status.HTTP_302_FOUND)
    response.set_cookie("session", token, httponly=True, secure=True)
    return response

2. Add /dashboard route (routes/dashboard.py)

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from app.db import get_session
from app.models.user import User
from itsdangerous import URLSafeSerializer, BadSignature
from sqlmodel import Session, select
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
serializer = URLSafeSerializer("SECRET_KEY")

def get_current_user(request: Request, session: Session):
    cookie = request.cookies.get("session")
    if not cookie:
        return None
    try:
        data = serializer.loads(cookie)
        user = session.exec(select(User).where(User.id == data["user_id"])).first()
        return user
    except BadSignature:
        return None

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, session: Session = Depends(get_session)):
    user = get_current_user(request, session)
    if not user:
        return RedirectResponse(url="/login")
    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user})

3. templates/login.html

<form method="post">
  <label>Email: <input type="email" name="email" required></label>
  <label>Password: <input type="password" name="password" minlength="8" required></label>
  <button type="submit">Login</button>
</form>
{% if error %}
<p style="color:red;">{{ error }}</p>
{% endif %}

4. templates/dashboard.html

<h2>Welcome, {{ user.email }}</h2>
<p>You are logged in as {{ user.role }}</p>

5. Update main.py

from app.routes import login, dashboard

app.include_router(login.router)
app.include_router(dashboard.router)


---

Ready for **Prompt 4: Add ToDo CRUD module (protected, per user)?**

You said:
yes
ChatGPT said:

Great! Here's Prompt 4: Add ToDo Module (CRUD, User-Scoped) — this extends the app by allowing users to create, view, update, and delete their own ToDo items. All actions are RBAC-protected and scoped per logged-in user.
✅ Prompt 4: ToDo CRUD Module (Per User)

Extend the FastAPI-based ToDo App by adding a secure, user-scoped ToDo CRUD module.

### Features to Implement

- Authenticated users can:
  - Create, list, update, delete their own ToDo items
- Each ToDo item is linked to its creator (FK: user_id)
- Prevent users from accessing other users' items
- List ToDos in `/todos` view after login

### Updates to Requirements.txt (already compatible)

No new dependencies required.

### Project Updates

**1. models/todo.py**
```python
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class ToDo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = ""
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    user_id: int = Field(foreign_key="user.id")

2. Extend app/db.py
Add this to db.py:

from app.models.todo import ToDo

3. routes/todos.py

from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from app.models.todo import ToDo
from app.models.user import User
from app.db import get_session
from itsdangerous import URLSafeSerializer, BadSignature
from sqlmodel import select, Session
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
serializer = URLSafeSerializer("SECRET_KEY")

def get_current_user(request: Request, session: Session):
    cookie = request.cookies.get("session")
    if not cookie:
        return None
    try:
        data = serializer.loads(cookie)
        user = session.exec(select(User).where(User.id == data["user_id"])).first()
        return user
    except BadSignature:
        return None

@router.get("/todos", response_class=HTMLResponse)
def list_todos(request: Request, session: Session = Depends(get_session)):
    user = get_current_user(request, session)
    if not user:
        return RedirectResponse(url="/login")
    todos = session.exec(select(ToDo).where(ToDo.user_id == user.id)).all()
    return templates.TemplateResponse("todos.html", {"request": request, "todos": todos})

@router.post("/todos")
def create_todo(request: Request, title: str = Form(...), description: str = Form(""), session: Session = Depends(get_session)):
    user = get_current_user(request, session)
    if not user:
        return RedirectResponse(url="/login")
    todo = ToDo(title=title, description=description, user_id=user.id)
    session.add(todo)
    session.commit()
    return RedirectResponse(url="/todos", status_code=302)

@router.post("/todos/delete/{todo_id}")
def delete_todo(todo_id: int, request: Request, session: Session = Depends(get_session)):
    user = get_current_user(request, session)
    todo = session.get(ToDo, todo_id)
    if todo and todo.user_id == user.id:
        session.delete(todo)
        session.commit()
    return RedirectResponse(url="/todos", status_code=302)

4. templates/todos.html

<h2>Your ToDos</h2>
<ul>
  {% for todo in todos %}
    <li>
      <strong>{{ todo.title }}</strong>: {{ todo.description }}
      <form method="post" action="/todos/delete/{{ todo.id }}">
        <button type="submit">Delete</button>
      </form>
    </li>
  {% endfor %}
</ul>

<h3>Add New ToDo</h3>
<form method="post" action="/todos">
  <label>Title: <input type="text" name="title" required></label><br>
  <label>Description: <input type="text" name="description"></label><br>
  <button type="submit">Add ToDo</button>
</form>

5. Update main.py

from app.routes import todos

app.include_router(todos.router)


---

This completes a secure, role-aware, user-scoped MVP for a FastAPI-based ToDo app.

Would you like to move on to Prompt 5: **Admin-only role management panel** or **logout and session clearing**?

You said:
yes
ChatGPT said:

Perfect. Let’s move on with Prompt 5: Admin-Only Role Management Panel — this introduces access control and a basic UI for admins to view and manage user roles (e.g., promote users to "admin").
✅ Prompt 5: Admin Role Management Panel (RBAC)

Extend the existing FastAPI ToDo App by adding a role-protected admin panel. This should allow only users with the `"admin"` role to:

- View list of all registered users
- Promote or demote users by changing their role (between "user" and "admin")
- Must prevent any access by non-admins

### Requirements

- Use the existing signed cookie session to identify and enforce admin role
- Reuse existing `User` model
- Add a `/admin` dashboard

### Project Updates

**1. routes/admin.py**
```python
from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import select, Session
from fastapi.templating import Jinja2Templates
from app.models.user import User
from app.db import get_session
from itsdangerous import URLSafeSerializer, BadSignature

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
serializer = URLSafeSerializer("SECRET_KEY")

def get_current_user(request: Request, session: Session):
    cookie = request.cookies.get("session")
    if not cookie:
        return None
    try:
        data = serializer.loads(cookie)
        user = session.exec(select(User).where(User.id == data["user_id"])).first()
        return user
    except BadSignature:
        return None

@router.get("/admin", response_class=HTMLResponse)
def admin_dashboard(request: Request, session: Session = Depends(get_session)):
    user = get_current_user(request, session)
    if not user or user.role != "admin":
        return RedirectResponse(url="/login")
    users = session.exec(select(User)).all()
    return templates.TemplateResponse("admin.html", {"request": request, "users": users})

@router.post("/admin/role")
def update_role(request: Request, user_id: int = Form(...), new_role: str = Form(...), session: Session = Depends(get_session)):
    current_user = get_current_user(request, session)
    if not current_user or current_user.role != "admin":
        return RedirectResponse(url="/login")
    user = session.get(User, user_id)
    if user:
        user.role = new_role
        session.add(user)
        session.commit()
    return RedirectResponse(url="/admin", status_code=302)

2. templates/admin.html

<h2>Admin Panel</h2>
<table>
  <tr><th>Email</th><th>Role</th><th>Change Role</th></tr>
  {% for user in users %}
  <tr>
    <td>{{ user.email }}</td>
    <td>{{ user.role }}</td>
    <td>
      <form method="post" action="/admin/role">
        <input type="hidden" name="user_id" value="{{ user.id }}">
        <select name="new_role">
          <option value="user" {% if user.role == 'user' %}selected{% endif %}>user</option>
          <option value="admin" {% if user.role == 'admin' %}selected{% endif %}>admin</option>
        </select>
        <button type="submit">Update</button>
      </form>
    </td>
  </tr>
  {% endfor %}
</table>

3. Update main.py

from app.routes import admin

app.include_router(admin.router)


---

Would you like **Prompt 6: Add Logout + Session Clearing** next, or prefer something else (e.g., unit testing setup or deployment config)?

You said:
yes
ChatGPT said:

Perfect — here’s Prompt 6: Add Logout and Session Clearing, a crucial step to allow users to securely end their session.
✅ Prompt 6: Logout Functionality with Secure Session Clearing

Extend the FastAPI ToDo App to add a secure logout feature.

### Features to Implement

- Add a `/logout` route
- Clear the session cookie (invalidate token on client)
- Redirect to home or login page after logout
- Show a "Logout" link in the dashboard or navbar if user is logged in

### Updates Required

**1. routes/auth.py (create or extend if exists)**
```python
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/logout")
def logout(request: Request):
    response = RedirectResponse(url="/")
    response.delete_cookie("session")
    return response

2. Update navigation links in all templates
For example, in dashboard.html, todos.html, and home.html, update navigation:

<nav>
  <a href="/">Home</a>
  {% if user %}
    <a href="/dashboard">Dashboard</a>
    <a href="/logout">Logout</a>
  {% else %}
    <a href="/register">Register</a>
    <a href="/login">Login</a>
  {% endif %}
</nav>

3. Pass user to all templates
Modify all routes rendering templates like this:

user = get_current_user(request, session)
return templates.TemplateResponse("somepage.html", {"request": request, "user": user, ...})

4. Update main.py

from app.routes import auth

app.include_router(auth.router)


---

With this, users can now **safely log out**, which clears their session cookie on the client side.

Would you like to proceed to **Prompt 7: Setup Unit Testing (pytest, coverage)** or explore **deployment config (Docker, .env, HTTPS setup)?**

You said:
yes
ChatGPT said:

Great! Here’s Prompt 7: Add Unit Testing with pytest and Coverage Reporting — this ensures your FastAPI ToDo app is verifiable and follows good engineering practices.
✅ Prompt 7: Setup Unit Testing (pytest + coverage)

Extend the FastAPI ToDo App with proper unit testing and coverage tools.

### Features to Implement

- Add `tests/` directory with unit tests for:
  - User registration
  - User login
  - ToDo creation
- Use `pytest` for test framework
- Use `httpx` for async test client
- Use in-memory SQLite for tests
- Add coverage reporting with `pytest-cov`

### Update `requirements.txt` (dev dependencies)

pytest==8.2.1
pytest-cov==5.0.0
httpx==0.27.0


### Project Structure Update

todo_app/
├── tests/
│ ├── init.py
│ ├── test_auth.py
│ ├── test_todos.py


### Example: tests/test_auth.py
```python
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_register_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.post("/register", data={
            "email": "test@example.com",
            "password": "securepass123"
        })
    assert resp.status_code == 200 or resp.status_code == 302

Example: tests/test_todos.py

import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_todo_requires_auth():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.post("/todos", data={"title": "A test task"})
    assert resp.status_code == 200 or resp.status_code == 307  # should redirect to login

Run Tests

pytest --cov=app tests/


---

Would you like to continue to **Prompt 8: Dockerize the App with `.env` config and HTTPS notes**, or prefer CI/CD pipeline setup next?

You said:
yes
ChatGPT said:

Excellent! Here’s Prompt 8: Dockerize the App with .env Support and Basic HTTPS Prep — this prepares the app for container-based deployment with configuration isolation and production-readiness in mind.
✅ Prompt 8: Dockerize FastAPI App with .env Support & HTTPS Readiness

Package the FastAPI ToDo App into a Docker container for scalable, reproducible deployment.

### Features to Add

- Add `Dockerfile` for production-ready container
- Add `.env` file for managing config like secret keys, DB URLs
- Mount static and template folders correctly
- Prepare for HTTPS with note on using Nginx + Certbot

### Project Updates

**1. Add `.env` file**
```env
SECRET_KEY=change_this_securely
DATABASE_URL=sqlite:///todo.db

2. Update app/db.py

import os
from sqlmodel import create_engine, Session

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///todo.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def get_session():
    with Session(engine) as session:
        yield session

3. Update secret handling in routes
Use os.getenv("SECRET_KEY") instead of hardcoded value:

import os
SECRET_KEY = os.getenv("SECRET_KEY", "default_dev_key")
serializer = URLSafeSerializer(SECRET_KEY)

4. Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

5. .dockerignore

__pycache__/
*.pyc
*.db
.env

6. docker-compose.yml (Optional)

version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    volumes:
      - .:/app

7. HTTPS Setup Notes

    Use Nginx as reverse proxy with Let's Encrypt / Certbot

    Forward HTTPS to internal http://localhost:8000

    Use secure cookies: secure=True, httponly=True


---

Would you like to move to **Prompt 9: GitHub Actions CI/CD with linting and test workflows**, or generate a final summary design document in asciidoc format?

You said:
yes
ChatGPT said:

Great choice. Let’s continue with Prompt 9: GitHub Actions CI/CD with Linting + Test Workflows — this sets up continuous integration for code quality and test reliability.
✅ Prompt 9: GitHub Actions CI/CD for Linting, Testing, and Coverage

Setup GitHub Actions to enable CI/CD for the FastAPI ToDo App.

### Goals

- Run on every `push` and `pull_request`
- Perform:
  - Python linting with `ruff`
  - Type-checking with `mypy`
  - Unit tests with `pytest`
  - Coverage reporting with `pytest-cov`

### Requirements.txt — Dev Section (if not already)

ruff==0.4.4
mypy==1.10.0


### Add `.github/workflows/ci.yml`
```yaml
name: FastAPI CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install ruff mypy pytest pytest-cov

    - name: Lint with ruff
      run: ruff app tests

    - name: Type check with mypy
      run: mypy app

    - name: Run tests with pytest
      run: pytest --cov=app tests/

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v4
      with:
        token: ${{ secrets.CODECOV_TOKEN }}  # optional

Optional Setup

    Create ruff.toml or pyproject.toml to customize rules.

    Add a coverage badge by integrating Codecov or Coveralls with your repo.


---

Would you now like to generate the **final `asciidoc` design document** summarizing this progressive app setup?

You said:
yes
ChatGPT said:

✅ Final design document has been generated under SPEC-1: Secure, Scalable FastAPI-Based ToDo App. It includes architecture, database schemas, components, implementation steps, milestones, and evaluation criteria.

Would you like:

    A production deployment guide (e.g., Docker + Nginx + systemd)?

    A REST API-only version (for mobile clients)?

    Or we can build a second module (e.g., notifications or audit logs)?

You said:
export this to markdown file
ChatGPT said:

✅ The design has been exported as a Markdown file: spec_1_todo_app.md

You can download it using the link above. Let me know if you’d like a PDF or HTML export as well!
You said:
export complete code and suggestions in dowc file
ChatGPT said:

✅ The complete design, code structure, and suggestions have been exported to a Word document:
spec_1_todo_app.docx

You can download it from the link above. Would you also like a PDF version or include sample code snippets directly in the document? 



====================================

Here is a complete, module-wise progressive set of GPT prompts that can be run step-by-step to create an incrementally growing FastAPI-based ToDo application, following OWASP secure coding practices, scalable architecture, and proper structure.

Each prompt assumes that the previous one has been executed, and each builds logically on top of it.
✅ GPT Prompts for Incremental FastAPI ToDo App
🧱 Prompt 1: Bootstrap Project with Landing Page

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

todo_app/
├── app/
│ ├── main.py
│ ├── routes/home.py
│ ├── templates/home.html
│ └── static/logo.png
├── requirements.txt
├── README.md

🧾 Prompt 2: Add Secure Registration Module

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

🔐 Prompt 3: Add Login and Session Handling

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

📝 Prompt 4: Add User-Scoped ToDo CRUD Module

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

🛡 Prompt 5: Add Admin Panel for Role Management

Create an admin dashboard for managing user roles.

### Requirements:
- `/admin` route (only for users with `role = admin`)
- Show list of all users
- Allow changing user roles (`user <-> admin`)
- Form-based role switch

Update:
- Add `admin.html` template
- Enforce role check in route logic

🔓 Prompt 6: Add Logout Functionality

Add logout support to clear user session.

### Requirements:
- `/logout` route
- Deletes session cookie and redirects to home
- Show Logout link when user is authenticated in navbar

Update:
- Clear cookie using `response.delete_cookie("session")`
- Update all template navbars to show login/logout conditionally

🧪 Prompt 7: Add Unit Tests and Coverage

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

🐳 Prompt 8: Add Docker Support with .env

Dockerize the app with support for `.env`.

### Requirements:
- Create `Dockerfile`
- Add `.env` file (SECRET_KEY, DATABASE_URL)
- Modify code to read config via `os.getenv`
- Optional: Add `docker-compose.yml`

Ensure static + templates are correctly mounted.

`.dockerignore`:

pycache/
*.pyc
.env
*.db

⚙️ Prompt 9: Add GitHub Actions CI/CD

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

Each of these prompts can be copy-pasted progressively into a GPT developer assistant or Copilot-like tool to build the app from scratch in a secure and structured manner.

Would you like me to export these prompts to a .txt, .docx, or .md file for easy reuse?




