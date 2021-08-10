from graphene import ObjectType

from .authenticate import Authenticate
from .unauthenticate import Unauthenticate
from .user_create import UserCreate
from .user_update import UserUpdate
from .user_inactivate import UserInactivate
from .avatar_remove import AvatarRemove
from .password_reset import PasswordReset
from .password_forgot import PasswordForgot
from .email_change_request import EmailChangeRequest
from .email_change import EmailChange
from .password_change import PasswordChange


__all__ = (
    "UserMutation",
)


class UserMutation(ObjectType):
    authenticate = Authenticate.Field()
    unauthenticate = Unauthenticate.Field()
    user_create = UserCreate.Field()
    user_update = UserUpdate.Field()
    user_inactivate = UserInactivate.Field()
    avatar_remove = AvatarRemove.Field()
    password_reset = PasswordReset.Field()
    password_forgot = PasswordForgot.Field()
    email_change_request = EmailChangeRequest.Field()
    email_change = EmailChange.Field()
    password_change = PasswordChange.Field()
