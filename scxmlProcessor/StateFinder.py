from scxmlProcessor import Loader
from scxmlProcessor.Generator import Generator


class StateFinder:
    def __init__(self, statedict):
        self.stateDict = statedict
        self.hierarchy = dict()
        self.hierarchy["Initial"] = list()

    def findHierachy(self):
        tmp = self.stateDict
        self.stateDict = self.stateDict.stateDict

if __name__ == "__main__":
    l = Generator("../bigTest2.scxml")
    s = StateFinder(l.loader.machine.doc)
    s.findHierachy()
    print (s.hierarchy)