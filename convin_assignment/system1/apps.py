from django.apps import AppConfig


class System1Config(AppConfig):
    name = 'system1'

    def ready(self):
        import system1.signals
