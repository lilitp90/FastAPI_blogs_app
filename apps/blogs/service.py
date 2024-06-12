from fastapi import Depends, HTTPException, status

from apps.blogs.model import Blog
from apps.blogs.repository import BlogRepository
from apps.blogs.schema import BlogCreateSchema


class BlogService:

    def __init__(self, blog_repo: BlogRepository=Depends(BlogRepository)):
        self.blog_repo = blog_repo

    def create_blog(self, data: BlogCreateSchema):
        return self.blog_repo.create(data)

    def get_blog(self, id: int):
        blog = self.blog_repo.get_blog_by_id(id)
        if not blog:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with id {id} does not exist")
        return blog

    def get_active_blogs(self) -> list[Blog]:
        return self.blog_repo.get_user_blogs()

    def update_blog(self, id: int, blog_schema: BlogCreateSchema):
        blog_obj = self.blog_repo.get_blog_by_id(id)
        if not blog_obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with id {id} does not exist")
        return self.blog_repo.update_blog(id=id, blog_obj=blog_obj,
                                          blog_schema=blog_schema)


    def delete_blog(self, id:int):
        blog = self.blog_repo.get_blog_by_id(id)
        if not blog:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} does not exist")
        self.blog_repo.delete_blog(id, blog)