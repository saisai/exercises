from django.apps import AppConfig


class CustomPkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_pk'
