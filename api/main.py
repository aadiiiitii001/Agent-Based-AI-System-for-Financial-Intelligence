from fastapi import FastAPI
from api.routes import router
from api.auth import create_access_token
from api.models import LoginRequest

app = FastAPI(title="Enterprise Agent-Based Financial AI")

@app.post("/login")
def login(data: LoginRequest):
    # Mock auth (replace with DB later)
    if data.username == "admin" and data.password == "admin":
        token = create_access_token({"sub": data.username, "role": "admin"})
        return {"access_token": token, "token_type": "bearer"}

    return {"error": "Invalid credentials"}

app.include_router(router)
