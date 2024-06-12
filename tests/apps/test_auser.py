from apps.core.config import settings
from apps.user.schema import UserCreateSchema

blog_prefix = "user/"

def test_create_user(test_app):
    resp = test_app.post(url="/"+ settings.API_VERSION + blog_prefix + "create-user",
                         json=UserCreateSchema(
                             email="test_user@test.com",
                             password="test_passsword",
                             is_active=True
                         ).dict())
    assert isinstance(resp.json(), dict)
    assert UserCreateSchema(**resp.json())