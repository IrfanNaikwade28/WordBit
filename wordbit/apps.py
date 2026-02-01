# wordbit/apps.py
from django.apps import AppConfig

class WordbitConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wordbit"

    def ready(self):
        from .nlp import load_model
        load_model()
