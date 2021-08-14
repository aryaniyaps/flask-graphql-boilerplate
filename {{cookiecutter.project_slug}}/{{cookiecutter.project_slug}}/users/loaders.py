from aiodataloader import DataLoader

from .models import User


class UserByIdLoader(DataLoader):
    """
    Loads users by their User-ID.
    """
    async def batch_load_fn(self, keys):
        users = User.query.filter(User.id.in_(keys))
        return [users.get(user_id) for user_id in keys]


class UserByUsernameLoader(DataLoader):
    """
    Loads users by their username.
    """
    async def batch_load_fn(self, keys):
        users = User.query.filter(User.username.in_(keys))
        return [users.get(username) for username in keys]
