#  state_init
#  author @cesarColle
from threading import Thread
from event import *
from SM_State_5 import *



class SM_init:
    def __init__(self):
        pass

    def start(self):
        self.onentry()

    def onentry(self):
        pass

    def transition(self, event):
        pass
        if (event == event["truc"]):
            return State_5()

