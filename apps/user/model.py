from apps.core.db import Base
from apps.core.model import BaseModelMixin
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

class User(Base, BaseModelMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    blogs = relationship("Blog", back_populates="authors", lazy=True)
