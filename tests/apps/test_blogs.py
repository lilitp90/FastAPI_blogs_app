from sqlalchemy.orm import Session
from apps.core.config import settings
from apps.blogs.schema import BlogCreateSchema
blog_prefix = "blogs"

def test_create_blog(test_app):
    resp = test_app.post(url="/"+ settings.API_VERSION + blog_prefix,
                         json=BlogCreateSchema(
                            title= "test_title",
                            slug= "test_slug",
                            content= "test_content"
                                ).dict())
    assert isinstance(resp.json(), dict)
    assert bool(resp.json()["title"])
    assert BlogCreateSchema(**resp.json())
