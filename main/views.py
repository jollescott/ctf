from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout as logout_user

from .common import get_base_context
from .forms import EnterForm


# Create your views here.
def index(request: HttpRequest):
    context = get_base_context(request)

    if request.user.is_authenticated:
        return render(request, "main/index.html", context)
    else:
        return redirect("enter")


def enter(request: HttpRequest):
    if request.method == "POST":
        form = EnterForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data["username"])
            user.save()

            login(request, user)

            return HttpResponseRedirect("/")
    else:
        form = EnterForm()

    return render(request, "main/enter.html", {"form": form})


def logout(request: HttpRequest):
    logout_user(request)
    return HttpResponseRedirect("/enter")
