from django.apps import AppConfig
import threading
from channels import Group
from datetime import datetime
import time


class ChatConfig(AppConfig):
    name = 'chat'

    def ready(self):
        BroadCastTime().start()


class BroadCastTime(threading.Thread):
    def run(self):
        while True:
            time.sleep(5)
            print(datetime.now())
            Group('chat').send({'text': str(datetime.now())})