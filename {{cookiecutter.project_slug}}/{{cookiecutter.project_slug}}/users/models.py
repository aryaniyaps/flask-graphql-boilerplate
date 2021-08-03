from {{ cookiecutter.project_slug }}.base.models import BaseModel
from {{ cookiecutter.project_slug }}.extensions import db, bcrypt


class User(BaseModel):
    __tablename__ = "users"

    email = db.Column(
        db.String(255),
        unique=True,
        nullable=False,
        index=True
    )
    username = db.Column(
        db.String(32),
        unique=True,
        nullable=False,
        index=True
    )
    password = db.Column(
        db.String(255),
        nullable=False
    )
    avatar = db.Column(
        db.String(255),
        default="default.jpg",
        nullable=False
    )
    is_active = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )
    is_staff = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    def __repr__(self):
        return "<User %s>" % self.id


    def set_password(self, password: str):
        """
        sets a hashed version of the provided
        password on the user instance.
        """
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password: str):
        """
        returns whether the provided password
        matches the user's password hash.
        """
        return bcrypt.check_password_hash(
            password=password,
            pw_hash=self.password
        )
