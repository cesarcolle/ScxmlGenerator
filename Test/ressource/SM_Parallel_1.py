#  state_Parallel_1
#  author @cesarColle
from threading import Thread
from event import *
from SM_State_4 import *



class SM_Parallel_1:
    def __init__(self):
        pass

    def start(self):
        self.onentry()

    def onentry(self):
        pass

    def transition(self, event):
        pass
        if (event == event["machin"]):
            return State_4()

