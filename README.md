# 🛒 FastAPI E-commerce Backend

A modern, secure, and lightweight **E-commerce Backend API** built with **FastAPI**. This project demonstrates industry-standard practices like **JWT authentication**, **modular routing**, **ORM with SQLAlchemy**, and **schema validation using Pydantic** — making it ideal for **learning, showcasing, or extending into a full-stack application**.

---

## 🚀 Features

- ✅ **User Registration & Login** with hashed passwords
- 🔐 **JWT-based Authentication** with token expiry
- 🧾 **Product Management** (Create and View Products)
- 🔒 **Protected Routes** using OAuth2 and bearer tokens
- 🛠️ **Data Validation** using Pydantic schemas
- 📦 **Modular Folder Structure** following FastAPI best practices
- 🧪 API ready for testing with Swagger UI

---

## 🧱 Tech Stack

| Tool            | Purpose                            |
|-----------------|------------------------------------|
| **FastAPI**     | High-performance Python web framework |
| **Uvicorn**     | ASGI server to serve FastAPI apps  |
| **SQLAlchemy**  | ORM for defining and querying models |
| **SQLite**      | Lightweight file-based database     |
| **Pydantic**    | Schema validation and type hints    |
| **Passlib**     | Password hashing (bcrypt)           |
| **Python-Jose** | JWT creation and verification       |

---

## 🔐 Authentication Flow

1. **POST `/signup`** – Create a new user with `username`, `email`, and `password`.
2. **POST `/login`** – Authenticate and receive a JWT access token.
3. **GET `/protected`** – Access protected route with `Authorization: Bearer <token>`.

> 🔐 Swagger UI provides an **Authorize** button to test JWT-protected routes easily.

---

## 📮 Example Usage

### 📝 Register a New User

```json
POST /signup
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword"
}
