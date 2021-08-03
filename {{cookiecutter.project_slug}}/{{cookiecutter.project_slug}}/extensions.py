from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_migrate import Migrate
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

mail = Mail()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
admin = Admin(
    name="{{ cookiecutter.project_name }}",
    template_mode="bootstrap4"
)
