from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_mongoengine import MongoEngine
from flask_uploads import UploadSet, IMAGES

mail = Mail()
db = MongoEngine()
bcrypt = Bcrypt()
media = UploadSet("media", IMAGES)
