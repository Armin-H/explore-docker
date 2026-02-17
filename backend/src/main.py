import os
from fastapi import FastAPI

app = FastAPI()

PORJECT_NAME = os.environ.get("PROJECT_NAME")
if not PORJECT_NAME:
    raise ValueError("PROJECT_NAME is not set")

@app.get("/")
def get_root():
    return {"message": f"Hello World, from backend, Project Name: {PORJECT_NAME}"}