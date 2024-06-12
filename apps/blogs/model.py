from apps.core.db import Base
from apps.core.model import BaseModelMixin
from sqlalchemy import Integer, Column, String, Text, ForeignKey, DateTime, Boolean
from datetime import datetime
from sqlalchemy.orm import relationship


class Blog(Base, BaseModelMixin):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    author_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    authors = relationship("User", back_populates='blogs', lazy=True)
    created_at = Column(DateTime, default=datetime.now())
    is_active = Column(Boolean, default=False)