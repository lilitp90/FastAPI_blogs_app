from apps.core.db import SessionLocal
from typing import Generator


def get_db():
    db = SessionLocal()
    print(type(db), 'typeeee')
    try:
        yield db
    finally:
        db.close()