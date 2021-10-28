from django.urls import path

from chatting import consumers

websocket_urlpatterns = [
    path('ws/chatting/room', consumers.ChatConsumer.as_asgi()),
]
