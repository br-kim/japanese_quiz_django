import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope
        self.room_group_name = 'chat_room'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': "chat_message",
                'message': message,
            }
        )
        # self.send(text_data=json.dumps({
        #     'message': message,
        # }))

    def chat_message(self, event):
        message = event.get("message")
