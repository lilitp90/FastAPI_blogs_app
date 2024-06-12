from apps.core.db_utils import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from apps.user.model import User
from apps.user.schema import UserCreateSchema


class UserRepository:

    def __init__(self, db: Session=Depends(get_db)):
        self.db = db


    def create_user(self, user: UserCreateSchema):
        user = User(**user.model_dump())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user(self, email):
        return self.db.query(User).filter(User.email==email).first()
