from pydantic_settings import BaseSettings

from lib_logging import EnvEnum


class Settings(BaseSettings):
    TOKEN: str | None = None
    HOST: str = '0.0.0.0'
    PORT: int = 8000
    ENVIRONMENT: EnvEnum = EnvEnum.STAGING

    class Config:
        env_file = '.env'


config = Settings()
