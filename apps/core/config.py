import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_TITLE : str = 'Blog'
    PROJECT_VERSION: str = '0.1.0'
    API_VERSION: str = 'api/v1/'

    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT')
    POSTGRES_DB_NAME: str = os.getenv('POSTGRES_DB')

    @property
    def DATABASE_URL(self) -> str:
        return f'postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}' \
               f'@{self.POSTGRES_HOST}/{self.POSTGRES_DB_NAME}'


    @property
    def TEST_DATABASE_URL(self) -> str:
        return f'postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}' \
               f'@{self.POSTGRES_HOST}/test_{self.POSTGRES_DB_NAME}'

settings = Settings()