from typing import Any
from django.core.management.base import BaseCommand
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from django.db.utils import IntegrityError
from django.utils.text import slugify

from main.models import TaskModule, Task
from main.decorators import MODULE_TASKS
from main.common import fetch_ctf_modules


class Command(BaseCommand):
    help = "Register all modules within the database"

    def handle(self, *args: Any, **options: Any) -> str | None:
        mods = fetch_ctf_modules()

        for mod in mods:
            module = TaskModule()
            module.name = mod.name
            module.title = mod.display_name

            try:
                module.save()
            except IntegrityError:
                print(
                    f'Module "{mod.display_name}" has already been added, skipping...'
                )
                continue

            key = mod.__module__.split(".")[0]
            module_tasks = MODULE_TASKS[key]

            for module_task in module_tasks:
                name = module_task[0]

                task = Task()
                task.name = name
                task.slug = module_task[1]
                task.module = module
                task.points = 10

                try:
                    task.url = reverse(name)
                except NoReverseMatch:
                    print("[ERROR] Mismatch between task view name and function name!")
                    continue

                task.save()
