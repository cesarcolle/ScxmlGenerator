import os
from multiprocessing import Queue

from scxmlProcessor import Loader


class FamillyManager:
    def __init__(self, dictData):
        print(dictData)
        self.data = dictData
        self.familly = dict()
        self.fathers = list()
        self.path = dict()
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

            self.path[state] = self.data[state].initial

            for child in self.data[state].state:
                self.familly[child.id] += [state]

    # return the father of one state
    def takeFather(self, key):
        return self.familly[key]

    def takeChild(self, key):
        return self.path[key]

    # return all father
    def takeAllFather(self):
        return self.fathers


if __name__ == "__main__":
    l = Loader.Loader("../Test/bigHierarchy.scxml")
    f = FamillyManager(l.machine.doc.stateDict)
    print(f.familly)
    print(f.fathers)
    print("child : ", f.path)
