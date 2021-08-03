from datetime import datetime

from flask import Flask
from flask_admin.contrib.sqla import ModelView
from flask_graphql import GraphQLView

from {{ cookiecutter.project_slug }} import schema
from {{ cookiecutter.project_slug }} import commands
from {{ cookiecutter.project_slug }}.extensions import db, migrate, admin
from {{ cookiecutter.project_slug }}.extensions import mail, bcrypt
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
            schema=schema,
            graphiql=app.config.get("DEBUG")
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
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)


    admin.init_app(app)
    admin.add_view(ModelView(User, db.session))

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
