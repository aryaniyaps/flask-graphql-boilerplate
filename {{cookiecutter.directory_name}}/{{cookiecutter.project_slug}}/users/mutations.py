from graphene import Mutation

from .types import RegisterInput, LoginInput, UpdateUserInput
from .types import ResetPasswordInput, RequestResetInput
from .types import ChangeEmailInput, RequestEmailChangeInput


class Register(Mutation):
    """
    creates an user instance.
    """
    class Arguments:
        input = RegisterInput(required=True)
    
    def mutate(root, info, input):
        return Register()


class Login(Mutation):
    """
    logs the user associated with the provided
    credentials in, if they were correct.
    """
    class Arguments:
        input = LoginInput(required=True)

    def mutate(root, info, input):
        return Login()


class ResetPassword(Mutation):
    """
    resets the password for the user account
    associated with the given email address.
    """
    class Arguments:
        input = ResetPasswordInput(required=True)

    def mutate(root, info, input):
        return ResetPassword()


class RequestReset(Mutation):
    """
    sends a password reset link to the
    provided email address.
    """
    class Arguments:
        input = RequestResetInput(required=True)
    
    def mutate(root, info, input):
        return RequestReset()


class UpdateCurrentUser(Mutation):
    """
    updates the current user instance.
    """
    class Arguments:
        input = UpdateUserInput(required=True)

    def mutate(root, info, input):
        return UpdateCurrentUser()


class RequestEmailChange(Mutation):
    """
    sends a email change link to the
    provided email address.
    """
    class Arguments:
        input = RequestEmailChangeInput(required=True)
    
    def mutate(root, info, input):
        return RequestEmailChange()


class ChangeEmail(Mutation):
    """
    changes the email for the user account
    associated with the given email address.
    """
    class Arguments:
        input = ChangeEmailInput(required=True)

    def mutate(root, info, input):
        return RequestEmailChange()


class UserMutation:
    register = Register.Field()
    login = Login.Field()
    reset_password = ResetPassword.Field()
    request_reset = RequestReset.Field()
    update_current_user = UpdateCurrentUser.Field()
    request_email_change = RequestEmailChange.Field()
    change_email = ChangeEmail.Field()
