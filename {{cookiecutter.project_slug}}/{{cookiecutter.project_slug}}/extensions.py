from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_mongoengine import MongoEngine

mail = Mail()
db = MongoEngine()
bcrypt = Bcrypt()
