from django.apps import AppConfig


class BmpappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bmpapp'


    # add this
    def ready(self):
        import  bmpapp.signals  # noqa