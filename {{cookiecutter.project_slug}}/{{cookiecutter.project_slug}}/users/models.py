from {{ cookiecutter.project_slug }}.base.models import BaseDocument
from {{ cookiecutter.project_slug }}.extensions import db


class User(BaseDocument):
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
    is_staff = db.BooleanField(
        default=False,
        required=True
    )
