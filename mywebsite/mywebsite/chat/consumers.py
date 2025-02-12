"""
consumers = versions of Django View
BUT they can not only respond to the requests (from the client)
they can also initiate request to the client (all while keeping open connection)
"""
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        """метод чтоб соединиться с клиентом"""
        # self.room_group_name = 'test'
        #
        # async_to_sync(self.channel_layer.group_add)(
        #     self.room_group_name,
        #     self.channel_name
        # )
        self.accept()

        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'You are now connected!'
        }))

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #
    #     async_to_sync(self.channel_layer.group_send)(
    #         self.room_group_name,
    #         {
    #             'type':'chat_message',
    #             'message':message
    #         }
    #     )
    #
    # def chat_message(self, event):
    #     message = event['message']
    #
    #     self.send(text_data=json.dumps({
    #         'type':'chat',
    #         'message':message
    #     }))

    # def receive(self, text_data=None, bytes_data=None):
    # """метод чтоб клиент мог соединиться с нами (сервером)"""
    #     pass
    #
    # def disconnect(self, code):
    # """тут что делать когда клиент сам отсоединился от соединения"""
    #     pass