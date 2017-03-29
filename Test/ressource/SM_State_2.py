#  state_State_2
#  author @cesarColle
from threading import Thread
from event import *
from SM_State_3 import *



class SM_State_2:
    def __init__(self):
        pass

    def start(self):
        self.onentry()

    def onentry(self):
        pass

    def transition(self, event):
        pass
        if (event == event["truc"]):
            return State_3()

