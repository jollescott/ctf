from channels.generic.websocket import WebsocketConsumer


class TerminalConsumer(WebsocketConsumer):

    def connect(self):
        self.task_id = self.scope["url_route"]["kwargs"]["task_id"]
        return super().connect()

    def disconnect(self, code):
        return super().disconnect(code)

    def receive(self, text_data=None, bytes_data=None):
        return super().receive(text_data, bytes_data)
