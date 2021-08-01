import strawberry

from .types import RegisterInput, LoginInput
from .types import ResetPasswordInput, RequestResetInput


class UserMutation:
    @strawberry.mutation
    def login(self, input: LoginInput) -> bool:
        """
        logs the user associated with the provided
        credentials in, if they were correct.
        """
        return True
    
    @strawberry.mutation
    def register(self, input: RegisterInput) -> bool:
        """
        creates an user instance.
        """
        return True

    @strawberry.mutation
    def reset_password(self, input: ResetPasswordInput) -> bool:
        """
        resets the password for the user account
        associated with the given email address.
        """
        return True
    
    @strawberry.mutation
    def request_reset(self, input: RequestResetInput) -> bool:
        """
        sends a password reset link to the
        provided email address.
        """
        return True
