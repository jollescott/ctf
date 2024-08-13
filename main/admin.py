from django.contrib import admin
from .models import TaskModule, Task

# Register your models here.
admin.site.register(TaskModule)
admin.site.register(Task)