from multiprocessing import Queue

from scxmlProcessor import Loader


class FamillyManager:
    def __init__(self, dictData):
        self.data = dictData
        #del self.data["__main__"]
        self.familly = dict()
        self.fathers = list()
        self.makeFamilly()
        pass
    def makeFamilly(self):

        # Init the list value
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


if __name__ == "__main__":
    l = Loader.Loader("../paralele2.scxml")
    f = FamillyManager(l.machine.doc.stateDict)
    f.makeFamilly()
    print f.familly
    print f.fathers