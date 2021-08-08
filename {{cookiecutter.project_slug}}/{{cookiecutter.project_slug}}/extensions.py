from flask_mail import Mail
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_cors import CORS

__all__ = (
    "mail", 
    "db", 
    "cors",
    "login_manager"
)

mail = Mail()
db = MongoEngine()
login_manager = LoginManager()
cors = CORS()
