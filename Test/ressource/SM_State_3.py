#  state_State_3
#  author @cesarColle
from threading import Thread
from event import *
from SM_final import *



class SM_State_3:
    def __init__(self):
        pass

    def start(self):
        self.onentry()

    def onentry(self):
        pass

    def transition(self, event):
        pass
        if (event == event["bab"]):
            return final()

