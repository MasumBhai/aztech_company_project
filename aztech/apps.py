from django.apps import AppConfig

VERBOSE_APP_NAME = 'Aztech Valley'

class AztechConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aztech'
    verbose_name = VERBOSE_APP_NAME