from django.apps import AppConfig


class TfaConfig(AppConfig):
    name = 'tfa'

    def ready(self):
        import  tfa.signals