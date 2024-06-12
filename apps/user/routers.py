from fastapi import APIRouter, Depends, status
from .schema import UserCreateSchema, UserCreateResponseSchema
from apps.user.service import UserService

router = APIRouter()

@router.post("/create-user", response_model=UserCreateResponseSchema,
             status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreateSchema, user_service = Depends(UserService)):
    return user_service.create_user1(payload)
