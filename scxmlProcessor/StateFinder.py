from scxmlProcessor import Loader
from scxmlProcessor.Generator import Generator


class StateFinder():
    def __init__(self, statedict):
        self.stateDict = statedict
        self.hierarchy = dict()
        self.hierarchy["Initial"] = list()

    def findHierachy(self):
        tmp = self.stateDict
        self.stateDict = self.stateDict.stateDict
        self.findFirstState(tmp.rootState)

    def findFirstState(self, rootstate):
        #print (rootstate.initial)
        if rootstate.initial == None:
            return rootstate
        else:
            tmp = self.findFirstState(self.stateDict[rootstate.initial[0]])
            if  tmp != None:
                self.hierarchy["Initial"] += tmp







if __name__ == "__main__":
    l = Generator("../initialTest.scxml")
    s = StateFinder(l.loader.machine.doc)
    s.findHierachy()
    print (s.hierarchy)