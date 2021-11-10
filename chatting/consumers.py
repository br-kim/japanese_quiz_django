import json
import os

import aioredis

from channels.generic.websocket import AsyncWebsocketConsumer
from aioredis import Redis


class ChatConsumer(AsyncWebsocketConsumer):

    @property
    async def get_connection(self):
        return await Redis(await aioredis.create_connection(os.environ.get("REDIS_URL")))

    async def connect(self):
        self.room_group_name = 'chat_room'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print("connected")
        user_id = self.scope.get('user').username

        connection = await self.get_connection
        await connection.lpush('users_list', user_id)

        result = await connection.lrange('users_list', 0, -1)
        print(result)
        await self.accept()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': "chat_message",
                'message': {
                    'type': 'list',
                    'message': [i.decode() for i in result],
                },
            }
        )
        print("send1")
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': "chat_message",
                'message': {'type': 'alert', 'detail': 'enter', 'sender': user_id,
                            'message': "enter the chatting room."}
            }
        )
        print("send2")

        await self.send(json.dumps({'type': 'user_id', 'message': user_id}))
        connection.close()

    async def disconnect(self, code):
        print("disconnected")
        user_id = self.scope.get('user').username
        connection = await self.get_connection
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': "chat_message",
                'message': {'type': 'alert', 'detail': 'leave', 'sender': user_id,
                            'message': "leave the chatting room."}
            }
        )
        await connection.lrem('users_list', 1, user_id)
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        connection.close()

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')
        if message:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': "chat_message",
                    'message': text_data_json,
                }
            )

    async def chat_message(self, event):
        message = event.get("message")
        await self.send(text_data=json.dumps(message))
