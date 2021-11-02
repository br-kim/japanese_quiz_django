import json
import os

import aioredis

# from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

# redis_db = await aioredis.from_url()

# redis_db = await aioredis.create_pool(os.environ.get("REDIS-DJANGO"))


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.room_name = self.scope
        self.room_group_name = 'chat_room'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')
        alert = text_data_json.get('alert')
        print(text_data_json)
        # print(redis_db.)
        if message:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': "chat_message",
                    'message': text_data_json,
                }
            )
        # if alert:
        #     async_to_sync(self.channel_layer.group_send)(
        #         self.room_group_name,
        #         {
        #             'type': "alert_message",
        #             'message': text_data_json,
        #         }
        #     )

    async def chat_message(self, event):
        message = event.get("message")
        await self.send(text_data=json.dumps(message))

    # def alert_message(self, event):
    #     message = event.get("message")
    #     self.send(text_data=json.dumps(message))
