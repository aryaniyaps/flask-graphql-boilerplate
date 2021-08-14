from {{ cookiecutter.project_slug }}.extensions import db


class BaseModel(db.Model):
    """
    An abstract document which provides
    a set of base fields. Every document
    created must subclass this class.
    """
    __abstract__ = True

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        onupdate=db.func.now(),
        default=db.func.now()
    )
