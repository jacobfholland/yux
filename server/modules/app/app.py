from server.modules.log.models.log import log as LOG
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from server.config.config import Config
from flask_session import Session
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager
import coloredlogs
from server.config.blueprint import Blueprints


db = SQLAlchemy()
bcrypt = Bcrypt()
cors = CORS()
session = Session()
mail = Mail()
migrate = Migrate()
login_manager = LoginManager()

PACKAGES = [db, bcrypt, cors, session, mail, migrate, login_manager]


class Application():

    def create_app(self):
        app = Flask(__name__)
        app.config.from_object(Config)
        self.register_packages(app)
        Blueprints().app_register_blueprints(app)
        app.extensions["migrate"].db = db
        return app

    def register_packages(self, app):
        # TODO Add Try/Except blocks
        coloredlogs.install()
        LOG("info", "app", "install", "success",
            "Package ColoredLogs installed")
        for package in PACKAGES:
            self.register_package(package, app)

        return app

    def register_package(self, package, app):
        package.init_app(app)
        LOG("info", "app", "register", "success",
            f"Package {package.__class__.__name__} registered")
