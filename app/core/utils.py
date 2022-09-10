import os
from pathlib import Path
from typing import Tuple
from dotenv import load_dotenv


def is_data_empty(data: Tuple) -> bool:
    filtered = tuple(filter(lambda x: x is not None, data))
    return len(filtered) == 0


def get_project_root():
    return Path(__file__).parent.parent.parent


def get_env_path():
    return os.path.join(get_project_root(), '.env')


def load_env():
    load_dotenv(get_env_path())


load_env()


def get_telegram_token():
    return os.environ.get("TELEGRAM_TOKEN")
