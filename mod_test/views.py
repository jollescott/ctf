from django.shortcuts import render
from django.http import HttpRequest

from main.decorators import define_task
from main.common import get_base_context


# Create your views here.
@define_task(title="Test Task")
def test_task(request: HttpRequest):
    context = get_base_context(request)
    return render(request, "mod_test/index.html", context)
