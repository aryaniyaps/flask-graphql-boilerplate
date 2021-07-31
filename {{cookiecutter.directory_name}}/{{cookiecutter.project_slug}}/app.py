from datetime import datetime

from flask import Flask
from flask_uploads import configure_uploads
from strawberry.flask.views import GraphQLView

from {{ cookiecutter.project_slug }} import schema
from {{ cookiecutter.project_slug }} import extensions
from {{ cookiecutter.project_slug }} import upload_sets
from {{ cookiecutter.project_slug }} import users


def create_app(config="{{ cookiecutter.project_slug }}.settings"):
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

    register_extensions(app)
    register_context_processors(app)
    register_shell_context(app)

    configure_upload_sets(app)
    return app


def register_extensions(app):
    """
    registers extensions for the server.
    """
    extensions.mail.init_app(app)
    extensions.db.init_app(app)
    extensions.bcrypt.init_app(app)

def configure_upload_sets(app):
    """
    configures upload sets for the server.
    """
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
