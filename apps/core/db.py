from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declarative_base
from typing import Generator

from apps.core.config import settings
from sqlalchemy_utils import create_database

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print('runnningdd?????')

Base = declarative_base()

from apps.user.model import User
from apps.blogs.model import Blog


