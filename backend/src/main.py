import os
from fastapi import FastAPI, Depends
from sqlalchemy import text

from api.db import get_session
from sqlalchemy.orm import Session

app = FastAPI()

PORJECT_NAME = os.environ.get("PROJECT_NAME")
if not PORJECT_NAME:
    raise ValueError("PROJECT_NAME is not set")

@app.get("/")
def get_root(session: Session = Depends(get_session)):
    result = session.execute(text("SELECT 'Hello World FROM DB!'"))
    message = result.first()[0]
    return {"message": f"Hello World, from backend, Project Name: {PORJECT_NAME}, Message from DB: {message}"}