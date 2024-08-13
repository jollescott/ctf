from django.apps import apps


def fetch_ctf_modules(additional_flag=None):
    """Fetches all django apps with modules installed within them."""

    def check(config):
        try:
            return config.has_tasks and (
                True if additional_flag is None else config.additional_flag
            )
        except AttributeError:
            return False

    mods = [c for c in apps.get_app_configs() if check(c)]
    return mods
