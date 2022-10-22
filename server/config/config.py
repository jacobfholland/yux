import os
import platform
import requests
from dotenv import load_dotenv, find_dotenv


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PLATFORM_NAME = os.name
    PLATFORM_SYSTEM = platform.system(),
    PLATFORM_RELEASE = platform.release(),
    PLATFORM_MACHINE = platform.machine(),
    IP_ADDRESS = requests.get('https://checkip.amazonaws.com').text.strip(),
    PORT = os.environ.get("PORT")
    ROOT = os.environ.get("ROOT")

    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    TMDB_KEY = os.environ.get("TMDB_KEY")

    def __init__(self) -> None:
        load_dotenv(find_dotenv())
