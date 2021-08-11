from {{ cookiecutter.project_slug }}.users.models import User


def validate_unique_email(field, value, error):
    if User.objects(email=value):
        error(field, "Email already exists.")
