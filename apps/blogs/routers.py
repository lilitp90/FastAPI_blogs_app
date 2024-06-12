from fastapi import APIRouter, Depends, status
from apps.blogs.schema import BlogCreateSchema, BlogCreateResponseSchema
from apps.blogs.service import BlogService

router = APIRouter()

@router.post('', response_model=BlogCreateResponseSchema)
def create_blog(blog: BlogCreateSchema, blog_service:BlogService=Depends(BlogService)):
    print(blog, 'bloggggggsss')
    return blog_service.create_blog(blog)


@router.get('/{blog_id:int}', response_model=BlogCreateResponseSchema)
def get_blog(blog_id: int, blog_service: BlogService=Depends(BlogService)):
    return blog_service.get_blog(id=blog_id)


@router.get('', response_model=list[BlogCreateResponseSchema])
def get_active_blogs(blog_service: BlogService=Depends(BlogService)):
    return blog_service.get_active_blogs()


@router.put('/{blog_id:int}')
def update_blog(blog_id:int, blog_schema: BlogCreateSchema,
                blog_service: BlogService=Depends(BlogService)):
    return blog_service.update_blog(blog_id, blog_schema)


@router.delete('/{blog_id:int}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id:int, blog_service: BlogService=Depends(BlogService)):
    blog_service.delete_blog(id=blog_id)
