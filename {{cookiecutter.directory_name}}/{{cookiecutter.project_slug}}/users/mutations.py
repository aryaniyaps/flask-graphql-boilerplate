import strawberry

from {{ cookiecutter.project_slug }}.base.permissions import IsAuthenticated
from .types import RegisterInput, LoginInput, UpdateUserInput
from .types import ResetPasswordInput, RequestResetInput
from .types import ChangeEmailInput, RequestEmailChangeInput


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

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    def update_current_user(self, input: UpdateUserInput) -> bool:
        """
        updates the current user instance.
        """
        return True

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    def request_email_change(self, input: RequestEmailChangeInput) -> bool:
        """
        sends a email change link to the
        provided email address.
        """
        return True

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    def change_email(self, input: ChangeEmailInput) -> bool:
        """
        changes the email for the user account
        associated with the given email address.
        """
        return True
