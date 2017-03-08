import sets

from scxml.pyscxml import StateMachine
from scxml.node import SCXMLNode

## The loader class allow us to load a SCXML file.
## The loader will provide the tree containing all the data needed by our generator.

informations = dict()

class Loader :
    def __init__(self, path):
        self.machine = StateMachine(path)
        self.data = self.machine.doc.stateDict["Initial"]
    def __str__(self):
        l = ""
        for s in self.machine.doc.stateDict["Initial"].transition:
            informations[s] = {"parent" : s.parent}
        return l