# main.py
import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from db import SessionLocal, Base, engine  # assuming your code is in db.py

# Load environment variables
load_dotenv()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(title="Agent-Based AI System")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root route to check deployment
@app.get("/")
def root():
    return {"message": "API is running"}

# Example route to test database
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    # Example query (replace with your actual models)
    return {"users": db.query(Base).all()}  # placeholder

# Optional: add more endpoints here
