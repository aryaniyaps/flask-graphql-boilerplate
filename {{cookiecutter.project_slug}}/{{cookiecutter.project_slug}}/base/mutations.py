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
        required=True
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
        except ValidationError as exc:
            return cls.handle_errors(exc)
    
    @classmethod
    def perform_mutate(cls, root, info, **data):
        """
        Executes the mutation and returns the payload.
        """
        raise NotImplementedError
    
    @classmethod
    def handle_errors(cls, exception):
        """
        Returns a formatted array of errors.
        """
        errors = []
        for field, message in exception.errors.items():
            errors.append(ErrorType(
                field=field,
                message=str(message)
            ))
        return cls(
            success=False, 
            errors=errors
        )
