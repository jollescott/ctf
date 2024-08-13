from django.http import HttpRequest
from django.shortcuts import render, redirect

from .common import get_base_context


# Create your views here.
def index(request: HttpRequest):
    context = get_base_context()

    if request.user.is_authenticated:
        return render(request, "main/index.html", context)
    else:
        return redirect("enter")
