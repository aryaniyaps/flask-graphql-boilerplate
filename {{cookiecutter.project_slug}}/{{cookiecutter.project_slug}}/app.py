from datetime import datetime

from flask import Flask
from flask_graphql import GraphQLView

from {{ cookiecutter.project_slug }} import schema, commands
from {{ cookiecutter.project_slug }}.extensions import migrate, db, cors
from {{ cookiecutter.project_slug }}.extensions import login_manager, mail
from {{ cookiecutter.project_slug }}.users.models import User

__all__ = ("create_app",)


def create_app(config="{{ cookiecutter.project_slug }}.settings") -> Flask:
    """
    Initializes and returns an app.
    """
    app = Flask(__name__)
    app.config.from_object(config)

    configure_url_rules(app)
    configure_extensions(app)
    configure_commands(app)
    configure_context_processors(app)
    configure_shell_context(app)

    return app


def configure_url_rules(app: Flask) -> None:
    """
    Configures URL rules for the server.
    """
    app.add_url_rule(
        rule="/graphql",
        view_func=GraphQLView.as_view(
            name="graphql",
            schema=schema.schema,
            graphiql=app.config.get("DEBUG")
        )
    )

    # batch querying support.
    app.add_url_rule(
        rule="/graphql/batch",
        view_func=GraphQLView.as_view(
            name="graphql-batch",
            schema=schema.schema,
            batch=True
        )
    )


def configure_extensions(app: Flask) -> None:
    """
    Configures extensions for the server.
    """
    db.init_app(app)
    mail.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        """
        Looks up an user with the given
        user ID from the database.
        """
        return User.query.get(id=user_id)


def configure_commands(app: Flask) -> None:
    """
    Configures commands for the server.
    """
    app.cli.add_command(commands.test)


def configure_shell_context(app: Flask) -> None:
    """
    Configures shell context processors for the server.
    """

    app.shell_context_processor(
        lambda: {
            'db': db,
            'User': User
        }
    )


def configure_context_processors(app: Flask) -> None:
    """
    Configures context processors which
    inject values into templates.
    """

    # injects the current UTC date-time instance
    # (for use with email templates).
    app.context_processor(lambda: {"now": datetime.utcnow()})
