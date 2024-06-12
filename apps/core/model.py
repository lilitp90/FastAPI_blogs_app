from sqlalchemy import Column, Integer

class BaseModelMixin:
    id = Column(Integer, primary_key=True, index=True)