from {{ cookiecutter.project_slug }}.base.loaders import BaseLoader
from .models import User


class UserByIDLoader(BaseLoader):
    """
    Loads users by their User-ID.
    """

    context_key = "users_by_id"

    def batch_load_fn(self, keys):
        users = User.query.filter(User.id.in_(keys))
        return map(lambda user_id: users.get(user_id), keys)


class UserByUsernameLoader(BaseLoader):
    """
    Loads users by their username.
    """

    context_key = "users_by_username"

    def batch_load_fn(self, keys):
        users = User.query.filter(User.username.in_(keys))
        return map(lambda username: users.get(username), keys)
