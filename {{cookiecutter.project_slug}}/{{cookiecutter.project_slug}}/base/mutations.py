from graphene import Boolean, List
from graphene.relay import ClientIDMutation
from mongoengine.errors import ValidationError

from .types import ErrorType


class BaseMutation(ClientIDMutation):
    """
    An abstract mutation which executes input
    validation, permission checking and more.
    """
    success = Boolean(
        required=True, 
        default_value=True
    )
    errors = List(
        required=True,
        of_type=ErrorType
    )

    class Meta:
        abstract = True
    
    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        """
        Performs the mutation after checking permissions.
        Also handles validation errors.
        """
        try:
            return cls.perform_mutate(root, info, **data)
        except ValidationError as err:
            return cls.handle_error(err)
    
    @classmethod
    def perform_mutate(cls, root, info, **data):
        """
        Executes the mutation and returns the payload.
        """
        raise NotImplementedError
    
    @classmethod
    def handle_error(cls, error):
        """
        Returns a formatted array of errors.
        """
        formatted_errors = [
            ErrorType(
                field=error.field_name, 
                messages=error.errors
            )
        ]
        return cls(
            success=False, 
            errors=formatted_errors
        )
