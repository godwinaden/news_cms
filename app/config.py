import logging
import os
import pathlib

from pathlib import Path
from datetime import datetime
from functools import lru_cache
from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app_environ: str = os.environ["APP_ENV"]
app_space: str = os.environ["SPACE"]


class Settings(BaseSettings):
    """	Settings """
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')
    base_dir: Path = Path(__file__).resolve().parent
    db_client_key: str = Field(..., alias="API_KEY")
    db_client_domain: str = Field(..., alias="AUTH_DOMAIN")
    db_client_id: str = Field(..., alias="PROJECT_ID")
    db_client_app: str = Field(..., alias="APP_ID")
    db_client_push: str = Field(..., alias="MESSAGING_SENDER_ID")
    db_client_store: str = Field(..., alias="STORAGE_BUCKET")
    db_client_measure: str = Field(..., alias="MEASUREMENT_ID")
    db_user: str = Field(..., alias="EMAIL")
    db_user_pass: str = Field(..., alias="FIREBASE_PASS")
    environment: str = app_environ
    space: str = app_space
    logger: logging.Logger | logging.RootLogger = logging.getLogger()
    log_file: str = ""
    db_session: Any = None
    db: Any = None


@lru_cache
def get_settings():
    """	Settings """
    return Settings()


@lru_cache
def set_logger():
    """	logging messages """
    file_name = datetime.now().strftime("%d-%m-%Y.log")
    base_dir = pathlib.Path(__file__).resolve().parent
    log_path = base_dir / "logs" / file_name
    settings = get_settings()
    settings.logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    fh = logging.FileHandler(log_path)
    fh.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    sh = logging.StreamHandler()
    sh.setLevel(logging.ERROR)

    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add the handlers to logger
    settings.logger.addHandler(sh)
    settings.logger.addHandler(fh)
    settings.log_file = log_path
