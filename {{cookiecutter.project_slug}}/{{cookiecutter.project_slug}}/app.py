from datetime import datetime

from flask import Flask
from flask_graphql import GraphQLView

from {{ cookiecutter.project_slug }} import schema, commands
from {{ cookiecutter.project_slug }}.extensions import mail, db, cors
from {{ cookiecutter.project_slug }}.extensions import login_manager
from {{ cookiecutter.project_slug }}.users.loaders import UserByIdLoader
from {{ cookiecutter.project_slug }}.users.loaders import UserByUsernameLoader
from {{ cookiecutter.project_slug }}.users.models import User


def create_app(config="{{ cookiecutter.project_slug }}.settings"):
    """
    initializes and returns an app.
    """
    app = Flask(__name__)
    app.config.from_object(config)

    app.add_url_rule(
        rule="/graphql",
        view_func=GraphQLView.as_view(
            name="graphql",
            schema=schema.schema,
            graphiql=app.config.get("DEBUG"),
            context={
                "loaders": {
                    "user_by_id": UserByIdLoader(),
                    "user_by_username": UserByUsernameLoader()
                }
            }
        )
    )

    configure_extensions(app)
    configure_commands(app)
    configure_context_processors(app)
    configure_shell_context(app)

    return app


def configure_extensions(app):
    """
    configures extensions for the server.
    """
    db.init_app(app)
    mail.init_app(app)
    cors.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        """
        Looks up an user with the given
        user ID from the database.
        """
        return User.objects(id=user_id).first()


def configure_commands(app):
    """
    configures commands for the server.
    """
    app.cli.add_command(commands.test)


def configure_shell_context(app):
    """
    configures shell context processors for the server.
    """

    app.shell_context_processor(
        lambda: {
            'db': db,
            'User': User
        }
    )


def configure_context_processors(app):
    """
    configures context processors which
    inject values into templates.
    """

    # injects the current UTC date-time instance
    # (for use with email templates).
    app.context_processor(lambda: {"now": datetime.utcnow()})
