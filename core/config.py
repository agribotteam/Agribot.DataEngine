from enum import Enum
from typing import List
from pydantic import BaseSettings


class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True


class Config(BaseConfig):
    DEBUG: int = 0
    DEFAULT_LOCALE: str = "en_US"
    ENVIRONMENT: str = EnvironmentType.DEVELOPMENT
    PORT: int = 8003
    ALLOW_ORIGINS: str = "*"
    
    # need to define the environment variables here and if we need we can give default values.
    
    @property
    def ALLOW_ORIGINS_LIST(self) -> List[str]:
        return [origin.strip() for origin in self.ALLOW_ORIGINS.split(',')]


config: Config = Config()
