

from pydantic_settings import BaseSettings
from sqlalchemy.orm import declarative_base

DBBaseModel = declarative_base()

class Settings(BaseSettings):
    #configs gerais da aplicacao
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:DaniloMelo1302%40@localhost:5432/famp"

    model_config = {"case_sensitive": True}


settings = Settings()