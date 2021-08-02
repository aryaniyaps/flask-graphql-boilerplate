from datetime import datetime

from flask import Flask
from flask_uploads import configure_uploads
from flask_graphql import GraphQLView

from {{ cookiecutter.project_slug }} import schema
from {{ cookiecutter.project_slug }} import extensions
from {{ cookiecutter.project_slug }} import commands
from {{ cookiecutter.project_slug }} import uploads
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

    add_upload_sets(app)

    register_extensions(app)
    register_commands(app)
    register_context_processors(app)
    register_shell_context(app)

    return app


def register_extensions(app):
    """
    registers extensions for the server.
    """
    extensions.mail.init_app(app)
    extensions.db.init_app(app)
    extensions.migrate.init_app(app, extensions.db)
    extensions.admin.init_app(app)
    extensions.bcrypt.init_app(app)

def register_commands(app):
    """
    registers commands for the server.
    """
    app.cli.add_command(commands.test)


def add_upload_sets(app):
    """
    adds upload sets for the server.
    """
    configure_uploads(app, uploads.avatar_set)


def register_shell_context(app):
    """
    registers shell context processors for the server.
    """

    app.shell_context_processor(
        lambda: {
            'db': extensions.db,
            'User': User
        }
    )


def register_context_processors(app):
    """
    registers context processors which
    inject values into templates.
    """

    # injects the current UTC date-time instance
    # (for use with email templates).
    app.context_processor(lambda: {"now": datetime.utcnow()})
