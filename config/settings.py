from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Параметры HTTP-сервера CherryPy."""
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    HOST: str = "127.0.0.1"
    PORT: int = 8080


@lru_cache
def get_settings() -> Settings:
    """
    Читает окружение и возвращает настройки.

    Returns:
        Экземпляр `Settings`.
    """
    load_dotenv()
    return Settings()
