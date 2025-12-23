"""
The flask application package.
"""

import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# Logging configuration for Task #6
if not app.debug:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s : %(message)s",
    )
    app.logger.setLevel(logging.INFO)
    app.logger.info("Flask application startup")
else:
    app.logger.setLevel(logging.DEBUG)

# Extensions
Session(app)
db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = "login"

# Import views
import FlaskWebProject.views  # noqa