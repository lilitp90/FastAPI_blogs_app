from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BlogCreateSchema(BaseModel):
    title: str
    slug: Optional[str] = None
    content: str

    # @model_validator(mode='after')
    # def generate_slug(self):
    #     if not self.slug:
    #         self.slug = self.title.replace(' ', '_').lower()
    #     return self


class BlogCreateResponseSchema(BaseModel):
    title: str
    content: str
    created_at: datetime
