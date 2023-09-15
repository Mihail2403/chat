import json

from asgiref.sync import async_to_sync
from channels.auth import login
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils.html import escape


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "room"
        self.room_group_name = f"chat_{self.room_name}"
        self.user = self.scope["user"]
        # if self.user == 'AnonymousUser'
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.accept()
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "add.or.dis.to.chat.message", "message": f"{self.user} присоединился к чату"}
        )

    async def disconnect(self, code):

        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = {
            "message": escape(text_data_json["message"]),
            "sender": str(self.scope["user"])
        }

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({"message": event["message"]}))

    async def add_or_dis_to_chat_message(self, event):
        message = {"message": f'{event["message"]:.^100}'}
        await self.send(text_data=json.dumps({"message": message}))
