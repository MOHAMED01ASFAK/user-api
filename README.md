# User Management REST API (FastAPI)

A high-performance, production-ready REST API built with **FastAPI**, demonstrating core backend engineering concepts such as RESTful routing, request validation, schema modeling, error handling, and interactive API documentation.  
This project is designed for interviews, practical learning, and real-world backend development.

---

## 🚀 Features

- Complete **CRUD** operations for User resource  
- **Pydantic models** for request validation  
- **Email validation** using `EmailStr`  
- Clean and structured API routing  
- Professional **HTTP status codes & error handling**  
- Auto-generated interactive documentation:
  - Swagger UI → `/docs`
  - ReDoc → `/redoc`

---

## 🛠 Tech Stack

| Component     | Technology |
|---------------|------------|
| Language      | Python 3.10+ |
| Framework     | FastAPI |
| Server        | Uvicorn |
| Validation    | Pydantic |
| Documentation | Swagger / ReDoc |

---

## 📂 Project Structure

```
user-api/
│── main.py
│── requirements.txt
│── .gitignore
└── README.md
```

---

## 📌 API Endpoints

### Health Check
```
GET /health
```

### Get All Users
```
GET /users
```

### Get User by ID
```
GET /users/{user_id}
```

### Create User
```
POST /users
```
Request Body:
```json
{
  "name": "John Doe",
  "age": 25,
  "email": "john@example.com"
}
```

### Update User
```
PUT /users/{user_id}
```

### Delete User
```
DELETE /users/{user_id}
```

---

## ▶️ Running the Project

### 1. Create and activate virtual environment
```
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.\.venv\Scripts\activate    # Windows
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Start the server
```
uvicorn main:app --reload --port 8000
```

Server runs at:
```
http://127.0.0.1:8000
```

---

## 📘 API Documentation

FastAPI automatically generates interactive docs:

- Swagger UI → http://127.0.0.1:8000/docs  
- ReDoc → http://127.0.0.1:8000/redoc  

These tools allow you to test the API directly from your browser.

---

## 🧪 Example Request (cURL)

### Create a new user
```
curl -X POST "http://127.0.0.1:8000/users" \
-H "Content-Type: application/json" \
-d "{\"name\":\"Ashfag\",\"age\":23,\"email\":\"ashfag@example.com\"}"
```

---

## 📦 Dependencies

```
fastapi
uvicorn
pydantic
email-validator
```

---

## 🔮 Future Enhancements (Roadmap)

- Migrate from in-memory storage → **SQLite + SQLModel**  
- Add **JWT Authentication** (Login / Register)  
- Add **User Roles** (Admin / Standard User)  
- Containerize with **Docker**  
- Deploy to **Render / Railway / AWS**  
- Add unit tests using **pytest + httpx**

---

## 👨‍💻 Author

**Mohamed Ashfag**  
Backend Developer | Python | FastAPI | SQL  

GitHub: https://github.com/MOHAMED01ASFAK  

---

## ⭐ Show Your Support  
If you find this project useful, don't forget to **star the repository**!

