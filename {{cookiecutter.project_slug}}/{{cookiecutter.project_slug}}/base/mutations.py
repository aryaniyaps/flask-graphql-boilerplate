from graphene import Boolean, List
from graphene.relay import ClientIDMutation

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
        cls.validate_input(cls, root, info, **data)
        return cls.perform_mutate(root, info, **data)
    
    @classmethod
    def perform_mutate(cls, root, info, **data):
        """
        Executes the mutation and returns the payload.
        """
        raise NotImplementedError

    @classmethod
    def validate_input(cls, root, info, **data):
        """
        Performs validation on the mutation's input.
        """
        raise NotImplementedError
    
    @classmethod
    def handle_errors(cls, errors):
        """
        Returns a formatted array of errors.
        """
        pass
