from argon2 import PasswordHasher
from argon2.exceptions import VerificationError
from flask_login import UserMixin

from {{ cookiecutter.project_slug }}.base.models import BaseDocument
from {{ cookiecutter.project_slug }}.extensions import db


password_hasher = PasswordHasher()


class User(BaseDocument, UserMixin):
    meta = {
        "collection": "users"
    }
    email = db.EmailField(
        unique=True,
        required=True,
    )
    username = db.StringField(
        min_length=2,
        max_length=32,
        required=True,
        unique=True,
    )
    password = db.StringField(
        min_length=8,
        regex=r"[A-Za-z0-9@#$%^&+=]",
        required=True,
    )
    avatar = db.StringField(
        default="default.jpg",
        required=True
    )
    is_active = db.BooleanField(
        default=True,
        required=True
    )

    def set_password(self, password: str):
        """
        sets a hashed version of the provided
        password on the user instance.
        """
        self.password = password_hasher.hash(password)

    def check_password(self, password: str) -> bool:
        """
        returns whether the provided password
        matches the user's password hash.
        """
        try:
            return password_hasher.verify(
                hash=self.password, 
                password=password
            )
        except VerificationError:
            return False

    def has_stale_password(self) -> bool:
        """
        returns whether the current user's password
        hash is stale and needs to be recalculated.
        """
        return password_hasher.check_needs_rehash(self.password)
