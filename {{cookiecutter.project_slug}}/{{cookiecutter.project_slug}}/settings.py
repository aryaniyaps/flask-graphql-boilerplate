from environs import Env

env = Env()
env.read_env()

# site branding configuration.
PUBLIC_SITE_URL = env.str("PUBLIC_SITE_URL")
PUBLIC_SITE_NAME = env.str("PUBLIC_SITE_NAME", default="{{ cookiecutter.project_name }}")

# flask core configuration.
ENV = env.str("FLASK_ENV", default="development")
SECRET_KEY = env.str("SECRET_KEY")

# flask-cors configuration.
CORS_ORIGINS = env.str("CORS_ORIGINS")
CORS_ALLOW_HEADERS = env.str("CORS_ALLOW_HEADERS")
CORS_SUPPORTS_CREDENTIALS = env.bool("CORS_SUPPORTS_CREDENTIALS")

# flask-sqlalchemy configuration.
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# flask-mail configuration.
MAIL_PORT = env.int("MAIl_PORT", default=465)
MAIL_USE_TLS = env.bool("MAIL_USE_TLS", default=True)
MAIL_SERVER = env.str("MAIL_SERVER")
MAIL_USERNAME = env.str("MAIL_USERNAME")
MAIL_PASSWORD = env.str("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = env.str("MAIL_DEFAULT_SENDER")
