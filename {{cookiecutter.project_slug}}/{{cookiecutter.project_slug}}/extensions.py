from flask_mail import Mail
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_cors import CORS

mail = Mail()
db = MongoEngine()
cors = CORS()
jwt = JWTManager()
