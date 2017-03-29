#  state_State_5
#  author @cesarColle
from threading import Thread
from event import *
from SM_final import *



class SM_State_5:
    def __init__(self):
        pass

    def start(self):
        self.onentry()

    def onentry(self):
        pass

    def transition(self, event):
        pass
        if (event == event["truc"]):
            return final()

