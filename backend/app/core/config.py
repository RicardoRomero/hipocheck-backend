# from typing import List
# from pydantic_settings import BaseSettings
# from pydantic import AnyHttpUrl
# import os

# class Settings(BaseSettings):
#     API_V1_STR: str = "/api/v1"
#     JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
#     JWT_REFRESH_SECRET_KEY: str = os.getenv("JWT_REFRESH_SECRET_KEY")
#     ALGORITHM: str = 'HS256'
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
#     REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
#     BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
#     PROJECT_NAME: str = "HIPOCHECK"
#     MONGO_CONNECTION_STRING: str = os.getenv("MONGO_CONNECTION_STRING")
#     MONGO_DB: str = os.getenv("MONGO_DB")


#     class Config:
#         env_file = "app/.env"

# # Crear una instancia de la clase Settings para acceder a las variables
# settings = Settings()

from typing import List
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str
    JWT_REFRESH_SECRET_KEY: str
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 5
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 días
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "HIPOCHECK"
    MONGO_CONNECTION_STRING: str
    MONGO_DB: str

    class Config:
        env_file = "app/.env"

settings = Settings()
