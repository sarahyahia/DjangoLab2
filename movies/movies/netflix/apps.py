from django.apps import AppConfig


class NetflixConfig(AppConfig):
    name = 'netflix'


    def ready(self):
        from . import signals
