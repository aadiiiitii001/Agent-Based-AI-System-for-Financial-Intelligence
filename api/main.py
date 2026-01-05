# main.py
import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv

# Import your DB setup and models
from db import SessionLocal, Base, engine
from models import User  # example model, adjust to your actual models
from api.routes import router
from api.auth import create_access_token
from api.models import LoginRequest

# Load environment variables
load_dotenv()

# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(title="Enterprise Agent-Based Financial AI")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root route for health check / deployment confirmation
@app.get("/")
def root():
    return {"message": "Enterprise Agent-Based Financial AI is running"}

# Login endpoint
@app.post("/login")
def login(data: LoginRequest):
    # Mock authentication; replace with actual DB logic later
    if data.username == "admin" and data.password == "admin":
        token = create_access_token({"sub": data.username, "role": "admin"})
        return {"access_token": token, "token_type": "bearer"}

    return {"error": "Invalid credentials"}

# Include your API router(s)
app.include_router(router)
