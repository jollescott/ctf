from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path("ws/terminal/(?P<task_id>\w+)/$", consumers.TerminalConsumer.as_asgi())
]
