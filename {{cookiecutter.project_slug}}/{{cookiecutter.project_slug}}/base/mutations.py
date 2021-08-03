from graphene.relay import ClientIDMutation


class BaseMutation(ClientIDMutation):
    """
    an abstract mutation which executes input
    validation, permission checking and more.
    Subclasses `ClientIDMutation` to keep track
    of client mutation IDs.
    """
    class Meta:
        abstract = True
    
    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        """
        performs the mutation after checking permissions.
        Also handles validation errors.
        """
        raise NotImplementedError
