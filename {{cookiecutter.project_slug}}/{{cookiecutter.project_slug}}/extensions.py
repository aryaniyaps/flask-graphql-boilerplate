from flask_mail import Mail
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager

mail = Mail()
db = MongoEngine()
jwt = JWTManager()
