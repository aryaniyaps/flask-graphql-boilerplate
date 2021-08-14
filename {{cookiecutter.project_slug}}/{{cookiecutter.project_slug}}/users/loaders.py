from promise import Promise
from {{ cookiecutter.project_slug }}.base.loaders import BaseLoader
from .models import User


class UserByIDLoader(BaseLoader):
    """
    Loads users by their User-ID.
    """

    context_key = "users_by_id"

    def batch_load_fn(self, keys):
        users = User.query.filter(User.id.in_(keys))
        return Promise.resolve(list(users))


class UserByUsernameLoader(BaseLoader):
    """
    Loads users by their username.
    """

    context_key = "users_by_username"

    def batch_load_fn(self, keys):
        users = User.query.filter(User.username.in_(keys))
        return Promise.resolve(list(users))
