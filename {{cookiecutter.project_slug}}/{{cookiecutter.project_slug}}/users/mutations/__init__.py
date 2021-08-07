from graphene import ObjectType

from .login import Login
from .create_user import UserCreate
from .reset_password import PasswordReset
from .request_password_reset import PasswordResetRequest
from .update_current_user import CurrentUserUpdate
from .change_email_request import EmailChangeRequest
from .change_email import EmailChange
from .change_password import PasswordChange


class UserMutation(ObjectType):
    login = Login.Field()
    user_create = UserCreate.Field()
    password_reset = PasswordReset.Field()
    password_reset_request = PasswordResetRequest.Field()
    current_user_update = CurrentUserUpdate.Field()
    email_change_request = EmailChangeRequest.Field()
    email_change = EmailChange.Field()
    password_change = PasswordChange.Field()
