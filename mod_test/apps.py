from django.apps import AppConfig


class ModTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mod_test'
    has_tasks = True
    display_name = 'WIP CTF Problems'
    makefile = True
