import os
import sys
import logging
from urllib.parse import urlparse


def configure_database_settings(BASE_DIR):
    """
    Configure database settings for a Django application.

    Returns:
        dict: Django DATABASES setting with either PostgreSQL (via Neon) or local SQLite.
    """
    # Use SQLite for tests
    if sys.argv[1:2] == ['test']:
        logging.debug("Running tests using SQLite database.")
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }

    database_url = os.getenv("DATABASE_URL")
    if database_url:
        try:
            parsed_url = urlparse(database_url)
            logging.info("Using PostgreSQL configuration from DATABASE_URL.")
            return {
                'default': {
                    'ENGINE': 'django.db.backends.postgresql',
                    'NAME': parsed_url.path.lstrip('/'),
                    'USER': parsed_url.username,
                    'PASSWORD': parsed_url.password,
                    'HOST': parsed_url.hostname,
                    'PORT': parsed_url.port or 5432,
                }
            }
        except Exception as e:
            logging.warning(f"Failed to parse DATABASE_URL: {e}. Falling back to SQLite.")

    logging.info("DATABASE_URL not found. Using local SQLite database.")
    return {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
