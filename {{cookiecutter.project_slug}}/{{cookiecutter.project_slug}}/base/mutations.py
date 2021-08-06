from cerberus import Validator
from graphene import Boolean, List
from graphene.relay import ClientIDMutation
from mongoengine.errors import ValidationError

from .types import ErrorType


validator = Validator()


class BaseMutation(ClientIDMutation):
    """
    An abstract mutation which executes input
    validation, permission checking and more.
    """

    schema = None

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
    
    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        """
        Performs the mutation after checking permissions.
        Also handles validation errors.
        """
        if cls.schema is not None and not validator.validate(data, cls.schema):
            return cls.handle_errors(validator.errors)

        return cls.perform_mutate(root, info, **data)
    
    @classmethod
    def perform_mutate(cls, root, info, **data):
        """
        Executes the mutation and returns the payload.
        """
        raise NotImplementedError
    
    @classmethod
    def handle_errors(cls, errors):
        """
        Returns a formatted array of errors.
        """
        for field, messages in errors.items():
            errors.append(ErrorType(
                field=field,
                messages=messages
            ))
        return cls(
            success=False, 
            errors=errors
        )
