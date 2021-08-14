from flask_login import current_user
from graphene import String, Field
from graphene_file_upload.scalars import Upload

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation
from {{ cookiecutter.project_slug }}.extensions import db
from {{ cookiecutter.project_slug }}.users.types import UserType


class UserUpdate(BaseMutation):
    """
    Updates the current user instance.
    """

    class Input:
        avatar = Upload(
            description="The user's new avatar file."
        )
        username = String(
            description="The user's new username."
        )
    
    user = Field(
        type=UserType,
        description="The updated user instance."
    )

    @classmethod
    def mutate_and_get_payload(cls, root, info, avatar=None, username=None):
        if username is not None:
            # TODO: validate the username.
            current_user.username = username
            db.session.commit()

        if avatar is not None:
            # TODO: save the user's new avatar.
            pass

        return cls(
            success=True,
            user=current_user
        )
