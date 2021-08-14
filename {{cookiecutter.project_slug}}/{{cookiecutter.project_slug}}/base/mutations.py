from graphene import Boolean, List
from graphene.relay import ClientIDMutation

from .types import ErrorType


class BaseMutation(ClientIDMutation):
    success = Boolean(
        required=True,
        description="Whether the operation was successful."
    )
    user_errors = List(
        required=True,
        default_value=[],
        of_type=ErrorType,
        description="User errors of the operation."
    )

    class Meta:
        abstract = True

    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        try:
            return cls.perform_mutate(root, info, **data)
        except Exception:
            # handle errors here
            pass

    @classmethod
    def perform_mutate(cls, root, info, **data):
        pass
