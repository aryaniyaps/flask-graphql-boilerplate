from datetime import datetime

from {{ cookiecutter.project_slug }}.extensions import db


class BaseDocument(db.Document):
    """
    An abstract document which provides
    a set of base fields. Every document
    created must subclass this class.
    """

    created_at = db.DateTimeField(
        required=True,
        default=datetime.now()
    )
    updated_at = db.DateTimeField(
        required=True,
        default=datetime.now()
    )

    meta = {
        "abstract": True
    }

    def save(self, *args, **kwargs):
        """
        keeps track of the `created_at` and
        `updated_at` fields for the document.
        """
        if not self.created_at:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super(BaseDocument, self).save(*args, **kwargs)
