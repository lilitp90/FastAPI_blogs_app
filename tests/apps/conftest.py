import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, drop_database, database_exists

from apps.core.config import settings
from apps.core.utils import common_parameters
from main import app
from apps.core.db import Base
from apps.core.db_utils import get_db


@pytest.fixture(scope="session")
def create_test_db():
    engine = create_engine(settings.TEST_DATABASE_URL)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db_session = TestingSessionLocal()

    if not database_exists(engine.url):
        create_database(engine.url)
        print(engine.url, 'engineeeee')
        Base.metadata.create_all(engine)
    yield db_session

    # finally:
    #     drop_database(engine.url)


@pytest.fixture(scope="session")
def test_app(create_test_db):
    app.dependency_overrides[get_db] = lambda: create_test_db
    return TestClient(app)
