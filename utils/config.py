from configparser import ConfigParser
from typing import Dict, Any

from auto_configparser import AutoConfig
from pydantic import BaseModel


class BotConfig(BaseModel):
    token: str = None

    api_server: str = 'n'
    is_api_local: bool = False


class DatabaseConfig(BaseModel):
    username: str = None
    password: str = None
    ip: str = "localhost"
    port: int = 3306
    db: str = "MessageLogBot"


class Config(AutoConfig):
    DATABASE: DatabaseConfig = DatabaseConfig()
    BOT: BotConfig = BotConfig()


config = Config().load()
