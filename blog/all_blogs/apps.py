from django.apps import AppConfig


class AllBlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'all_blogs'

    def ready(self):
        import all_blogs.signals
