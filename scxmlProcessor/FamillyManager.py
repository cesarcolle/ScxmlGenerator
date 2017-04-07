import os
from multiprocessing import Queue

from scxmlProcessor import Loader


class FamillyManager:
    def __init__(self, dictData):
        self.data = dictData
        self.familly = dict()
        self.fathers = list()
        self.makeFamilly()
        pass

    def makeFamilly(self):
        # Init the list value of the dictionary key
        for state in self.data:
            self.familly[state] = list()

        for state in self.data:
            # check if he is a father

            if self.data[state].state:
                self.fathers += [state]
            # add child
            for child in self.data[state].state:
                self.familly[child.id] += [state]

    # return the father of one state
    def takeFather(self, key):
        return self.familly[key]

    # return all father
    def takeAllFather(self):
        return self.fathers

    # def initialOfFather(self):
    #     for father in self.fathers:
    #         stateFather = self.fathers[father]
    #         for state in stateFather.state:
    #



if __name__ == "__main__":
    l = Loader.Loader("../bigTest2.scxml")
    f = FamillyManager(l.machine.doc.stateDict)

