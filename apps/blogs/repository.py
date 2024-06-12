from apps.blogs.schema import BlogCreateSchema
from sqlalchemy.orm import Session
from fastapi import Depends
from apps.core.db_utils import get_db
from apps.blogs.model import Blog


class BlogRepository:

    def __init__(self, db:Session=Depends(get_db)):
        self.db = db

    def create(self, data: BlogCreateSchema):
        blog = Blog(**data.model_dump())
        # blog.author_id = 1
        self.db.add(blog)
        self.db.commit()
        self.db.refresh(blog)
        return blog

    def get_blog_by_id(self, id: int):
        blog = self.db.query(Blog).get(id)
        return blog

    def get_user_blogs(self) -> list[Blog]:
        return self.db.query(Blog).filter(Blog.author_id==1, Blog.is_active==True).all()

    def update_blog(self, id: int, blog_obj: Blog, blog_schema: BlogCreateSchema):
        blog_obj.title=blog_schema.title
        blog_obj.slug=blog_schema.slug
        blog_obj.content=blog_schema.content
        #TODO to understand why we don't need db.add here before commiting
        self.db.commit()
        self.db.refresh(blog_obj)
        return blog_obj


    def delete_blog(self, id:int, blog_obj):
        self.db.delete(blog_obj)
        self.db.commit()

