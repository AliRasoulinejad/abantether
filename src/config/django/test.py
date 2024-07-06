from config.env import env
from .base import *  # noqa

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("POSTGRES_TEST_NAME", "test_db"),
        "USER": env.str("POSTGRES_TEST_USER", "postgres"),
        "PASSWORD": env.str("POSTGRES_TEST_PASSWORD", "postgres"),
        "HOST": env.str("POSTGRES_TEST_HOST", "localhost"),
        "PORT": env.str("POSTGRES_TEST_PORT", 5432),
    }
}
