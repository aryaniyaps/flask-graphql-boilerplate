from graphene import String
from graphene.relay import ClientIDMutation
from graphene_file_upload.scalars import Upload


class Register(ClientIDMutation):
    """
    creates an user instance.
    """
    class Input:
        email = String(required=True)
        username = String(required=True)
        password = String(required=True)
    
    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        return cls()


class Login(ClientIDMutation):
    """
    logs the user associated with the provided
    credentials in, if they were correct.
    """
    class Input:
        email = String(required=True)
        password = String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        return cls()


class ResetPassword(ClientIDMutation):
    """
    resets the password for the user account
    associated with the given email address.
    """
    class Input:
        password = String(required=True)
        reset_token = String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        return cls()


class RequestPasswordReset(ClientIDMutation):
    """
    sends a password reset link to the
    provided email address.
    """
    class Input:
        email = String(required=True)
    
    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        return cls()


class UpdateCurrentUser(ClientIDMutation):
    """
    updates the current user instance.
    """
    class Input:
        avatar = Upload()
        username = String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        return cls()


class RequestEmailChange(ClientIDMutation):
    """
    sends a email change link to the
    provided email address.
    """
    class Input:
        email = String(required=True)
    
    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        return cls()


class ChangeEmail(ClientIDMutation):
    """
    changes the email for the user account
    associated with the given email address.
    """
    class Input:
        email = String(required=True)
        change_code = String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        return cls()


class UserMutation:
    register = Register.Field()
    login = Login.Field()
    reset_password = ResetPassword.Field()
    request_password_reset = RequestPasswordReset.Field()
    update_current_user = UpdateCurrentUser.Field()
    request_email_change = RequestEmailChange.Field()
    change_email = ChangeEmail.Field()
