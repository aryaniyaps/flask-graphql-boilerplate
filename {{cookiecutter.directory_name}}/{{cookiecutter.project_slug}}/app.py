from datetime import datetime

from flask import Flask
from flask_uploads import configure_uploads, patch_request_class
from strawberry.flask.views import GraphQLView

from {{ cookiecutter.project_slug }} import schema
from {{ cookiecutter.project_slug }} import extensions
from {{ cookiecutter.project_slug }} import upload_sets
from {{ cookiecutter.project_slug }} import users


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
    register_context_processors(app)
    register_shell_context(app)

    return app


def register_extensions(app):
    """
    registers extensions for the server.
    """
    extensions.mail.init_app(app)
    extensions.db.init_app(app)
    extensions.bcrypt.init_app(app)

def add_upload_sets(app):
    """
    adds upload sets for the server.
    """
    # sets the maximum upload size (defaults to 16MB).
    patch_request_class(app)
    configure_uploads(app, upload_sets.avatar_set)


def register_shell_context(app):
    """
    registers the shell context for the server.
    """

    def shell_context():
        return {
            'db': extensions.db,
            'User': users.models.User
        }

    app.shell_context_processor(shell_context)


def register_context_processors(app):
    """
    registers context processors which
    inject values into templates.
    """

    # injects the current UTC date-time instance
    # (for use with email templates).
    app.context_processor(lambda: {"now": datetime.utcnow()})
