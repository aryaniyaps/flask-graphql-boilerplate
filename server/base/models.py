from datetime import datetime

from server.extensions import db


class BaseDocument(db.Document):
    """
    an abstract document which provides
    a set of base fields. Every document
    created must subclass this class.
    """
    meta = {
        "abstract": True
    }

    created_at = db.DateTimeField(
        required=True,
        default=datetime.now()
    )
    updated_at = db.DateTimeField(
        required=True,
        default=datetime.now()
    )

    def save(self, **kwargs):
        """
        keeps track of the `created_at` and
        `updated_at` fields for the document.
        """
        if not self.created_at:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super(BaseDocument, self).save(**kwargs)
