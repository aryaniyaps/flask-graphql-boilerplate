from flask_login import login_user
from graphene import String, Boolean, Field
from marshmallow import Schema, fields, validate

from {{ cookiecutter.project_slug }}.base.mutations import BaseMutation
from {{ cookiecutter.project_slug }}.users.models import User
from {{ cookiecutter.project_slug }}.users.types import UserType


class UserCreateSchema(Schema):
    email = fields.Email(
        required=True
    )
    password = fields.String(
        required=True, 
        validate=(
            validate.Length(min=8),
            validate.Regexp(
                regex=r"[A-Za-z0-9@#$%^&+=]"
            )
        )
    )
    username = fields.String(
        required=True, 
        validate=validate.Length(
            min=2, 
            max=32
        )
    )
    remember = fields.Boolean(
        default=True
    )


class UserCreate(BaseMutation):
    """
    Creates an user instance.
    """

    class Input:
        email = String(
            required=True,
            description="The email of the user."
        )
        username = String(
            required=True,
            description="The username of the user."
        )
        password = String(
            required=True,
            description="The password of the user."
        )
        remember = Boolean(
            default_value=True,
            description="Remembers the user after session expires."
        )

    user = Field(
        type=UserType,
        description="The created user instance."
    )

    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        errors = UserCreateSchema().validate(data)
        if errors:
            # handle errors here
            print(errors) 
            
        if User.objects(email=data.get("email")):
            return cls(
                success=False,
                user_errors=(
                    dict(
                        field="email",
                        message="Email already exists."
                    ),
                )
            )
        
        if User.objects(username=data.get("username")):
            return cls(
                success=False,
                user_errors=(
                    dict(
                        field="username",
                        message="Username already exists."
                    ),
                )
            )
        
        user = User(
            email=data.get("email"), 
            username=data.get("username")
        )
        # hash the user's password.
        user.set_password(data.get("password"))
        user.save()

        login_user(
            user=user, 
            remember=data.get("remember")
        )

        return cls(
            success=True,
            user=user
        )
