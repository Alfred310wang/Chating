import sys
import re
import requests
from bs4 import BeautifulSoup
from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_video_message


url = "https://www.youtube.com/feed/trending"
res = requests.get(url, verify=False)
soup = BeautifulSoup(res.text,'html.parser')
last = None
list=[]

for entry in soup.select('a'):
    m = re.search("v=(.*)",entry['href'])
    if m:
        target = m.group(1)
        if target == last:
            continue
        if re.search("list",target):
            continue
        last = target
        list.append(target)

class TocMachine(GraphMachine):
    
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'top video'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'hello'
        return False
    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state3'
        return False
    def is_going_to_state3_1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state3_1'
        return False


    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_video_message(sender_id,"https://www.youtube.com/watch?v="+list[0])
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Hi,Dear")
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')
    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state3")
#       self.go_back()

    def on_enter_state3_1(self, event):
        print("I'm entering state3_1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state3_1")
        self.go_back()

    def on_exit_state3_1(self):
        print('Leaving state3_1')

