from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import Dict

app = FastAPI(title="User Management API", version="1.0")

# In-memory "database"
users: Dict[int, dict] = {}

class User(BaseModel):
    name: str
    age: int
    email: EmailStr

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "ok"}

@app.get("/users", status_code=status.HTTP_200_OK)
def get_users():
    return users

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return users[user_id]

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    user_id = max(users.keys(), default=0) + 1
    users[user_id] = user.dict()
    return {"message": "User created", "id": user_id}

@app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: User):
    if user_id not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    users[user_id] = user.dict()
    return {"message": "User updated", "id": user_id}

@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    del users[user_id]
    return {"message": "User deleted"}
