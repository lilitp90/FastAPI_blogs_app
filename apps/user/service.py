from apps.user.schema import UserCreateSchema
from apps.user.repository import UserRepository
from apps.user.model import User
from apps.core.db_utils import get_db
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .password_utils import PasswordHasher

class UserService:

    def __init__(self, user_repo=Depends(UserRepository)):
        self.user_repo = user_repo


    def create_user1(self, user: UserCreateSchema):
        user_with_same_email = self.user_repo.get_user(email=user.email)
        if user_with_same_email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="User already exists")
        hashed_password = PasswordHasher.get_password_hash(user.password)
        user = UserCreateSchema(
            email=user.email,
            password = hashed_password,
            is_active=user.is_active
        )
        return self.user_repo.create_user(user=user)