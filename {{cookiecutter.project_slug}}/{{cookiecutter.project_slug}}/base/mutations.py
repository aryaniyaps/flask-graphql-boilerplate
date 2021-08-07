from cerberus import Validator
from graphene import Boolean, List
from graphene.relay import ClientIDMutation

from .types import ErrorType


validator = Validator()


class BaseMutation(ClientIDMutation):
    success = Boolean(
        required=True,
        description="Whether the operation was successful."
    )
    errors = List(
        required=True,
        default_value=[],
        of_type=ErrorType,
        description="Client side errors of the operation."
    )

    class Meta:
        abstract = True
