

from pydantic import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    #configs gerais da aplicacao
    API_V1_STR = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:DaniloMelo1302@@localhost:5432/famp"
    DBBaseModel = declarative_base()

    class config:
        case_sensitive = True


settings = Settings()