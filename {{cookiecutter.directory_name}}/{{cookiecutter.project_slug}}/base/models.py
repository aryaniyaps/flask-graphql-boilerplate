from datetime import datetime

from {{ cookiecutter.project_slug }}.extensions import db


class BaseModel(db.Model):
    """
    an abstract model which provides
    a set of base fields. Every model
    created must subclass this class.
    """
    __abstract__ = True

    id = db.Column(
        "id",
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    created_at = db.Column(
        "created_at",
        db.DateTime,
        nullable=False,
        default=db.func.now()
    )
    updated_at = db.Column(
        "updated_at",
        db.DateTime,
        nullable=False,
        onupdate=db.func.now(),
        default=db.func.now()
    )
