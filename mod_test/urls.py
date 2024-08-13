from django.urls import path

from . import views

urlpatterns = [
    path("", views.test_task, name='test_task')
]