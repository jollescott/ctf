import functools
from django.utils.text import slugify

from .common import task_view_wrapper

MODULE_TASKS = {}


def define_task(name):
    def decorator(view):
        functools.wraps(view)
        key = view.__module__.split(".")[0]
        slug = slugify(name)

        wrapped_view = task_view_wrapper(view, slug)

        tup = (name, slug, wrapped_view)

        if key not in MODULE_TASKS:
            MODULE_TASKS[key] = [tup]
        else:
            MODULE_TASKS[key].append(tup)

        return wrapped_view

    return decorator
