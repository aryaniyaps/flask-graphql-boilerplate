from environs import Env

env = Env()
env.read_env()

SITE_NAME = env.str("PUBLIC_SITE_NAME")
SITE_URL = env.str("PUBLIC_SITE_URL")

ENV = env.str("FLASK_ENV", default="development")
SECRET_KEY = env.str("SECRET_KEY")
SECURITY_PASSWORD_SALT = env.str("SECURITY_PASSWORD_SALT")

MONGODB_SETTINGS = {
    "host": env.str("DATABASE_URL")
}

BCRYPT_LOG_ROUNDS = env.int("BCRYPT_LOG_ROUNDS", default=12)

MAIL_PORT = env.int("MAIl_PORT", default=465)
MAIL_USE_TLS = env.bool("MAIL_USE_TLS", default=True)
MAIL_SERVER = env.str("MAIL_SERVER")
MAIL_USERNAME = env.str("MAIL_USERNAME")
MAIL_PASSWORD = env.str("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = env.str("MAIL_DEFAULT_SENDER")