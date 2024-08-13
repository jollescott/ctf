import functools

MODULE_TASKS = {}


def define_task(title):
    def decorator(func):
        functools.wraps(func)
        key = func.__module__.split(".")[0]
        tup = (func, title)

        if key not in MODULE_TASKS:
            MODULE_TASKS[key] = [tup]
        else:
            MODULE_TASKS[key].append(tup)

        return func

    return decorator
