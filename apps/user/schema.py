from pydantic import BaseModel, EmailStr, Field

class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=4)
    is_active: bool


class UserCreateResponseSchema(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    # class Config:
    #     orm_mode = True
