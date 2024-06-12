from fastapi import FastAPI
from apps.core.config import settings
from apps.user.routers import router as user_router
from apps.blogs.routers import router as blog_router
from apps.core.utils import generate_api_prefix

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)


app.router.include_router(user_router, prefix=generate_api_prefix('user'), tags=['User'])
app.router.include_router(blog_router, prefix=generate_api_prefix('blogs'), tags=['Blogs'])