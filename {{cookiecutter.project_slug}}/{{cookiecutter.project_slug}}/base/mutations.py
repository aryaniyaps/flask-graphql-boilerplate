from graphene import Boolean, List, NonNull
from graphene.relay import ClientIDMutation

from .types import ErrorType


class BaseMutation(ClientIDMutation):
    """
    an abstract mutation which executes input
    validation, permission checking and more.
    """
    success = Boolean(
        required=True, 
        default_value=True
    )
    errors = List(
        of_type=NonNull(
            of_type=ErrorType
        )
    )

    class Meta:
        abstract = True
    
    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        """
        performs the mutation after checking permissions.
        Also handles validation errors.
        """
        raise NotImplementedError
