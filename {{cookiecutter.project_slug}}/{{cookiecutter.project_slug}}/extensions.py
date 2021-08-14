from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS

__all__ = (
    "mail", 
    "db",
    "migrate",
    "cors",
    "login_manager"
)

mail = Mail()
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
cors = CORS()
