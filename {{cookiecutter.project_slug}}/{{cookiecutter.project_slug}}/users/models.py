from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from flask_login import UserMixin

from {{ cookiecutter.project_slug }}.base.models import BaseModel
from {{ cookiecutter.project_slug }}.extensions import db


password_hasher = PasswordHasher()


class User(BaseModel, UserMixin):
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

    def __repr__(self):
        return "<User %s>" % self.id

    def set_password(self, password: str):
        """
        Sets a hashed version of the provided
        password on the user instance.
        """
        self.password = password_hasher.hash(password)

    def check_password(self, password: str) -> bool:
        """
        Returns whether the provided password
        matches the user's password hash.
        """
        try:
            return password_hasher.verify(
                hash=self.password, 
                password=password
            )
        except VerifyMismatchError:
            return False

    def has_stale_password(self) -> bool:
        """
        Returns whether the user's password
        hash is stale and needs to be recalculated.
        """
        return password_hasher.check_needs_rehash(self.password)
