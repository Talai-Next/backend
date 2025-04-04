from django.apps import AppConfig
import logging
import os
import sys

logger = logging.getLogger(__name__)


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        if os.environ.get("RUN_MAIN") != "true":
            return

        if "runserver" in sys.argv:
            logger.info("Starting bus thread...")
            from api.services import start_update_bus_data, start_update_bus_locations
            start_update_bus_data()
            start_update_bus_locations()
