import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")

engine = create_engine(f"postgresql+psycopg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db_service:5432/{POSTGRES_DB}")

def get_session():
    with Session(engine) as session:
        yield session


# with engine.connect() as conn:
#     result = conn.execute(text("SELECT 'Hello World'"))
#     print(result.all())