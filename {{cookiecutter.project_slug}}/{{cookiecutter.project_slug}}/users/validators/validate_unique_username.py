from {{ cookiecutter.project_slug }}.users.models import User


def validate_unique_username(field, value, error):
    if User.objects(username=value):
        error(field, "Username already exists.")
