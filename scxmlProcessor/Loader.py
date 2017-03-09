from __future__ import print_function

import sets

from scxml.pyscxml import StateMachine
from scxml.interpreter import Transition
import re
from scxml.node import SCXMLNode
import json

## The loader class allow us to load a SCXML file.
## The loader will provide the tree containing all the data needed by our generator.

informations = dict()


class Loader:
    def __init__(self, path):
        self.machine = StateMachine(path)
        self.data = dict()

    def generateTransition(self):
        self.t = Transition(self.machine.doc.rootState)
        for key in self.machine.doc.stateDict:
            tmp = Transition(self.machine.doc.stateDict[key])
            self.data[key] = list()
            for transition in tmp.source.transition:
                self.data[key] += [{ "event" : transition.event, "target" : transition.target}]



    def __str__(self):
        l = ""
        for s in self.machine.doc.stateDict["Initial"].transition:
            informations[s] = {"parent": s.parent}
        return l


if __name__ == "__main__":
    l = Loader("../test.xml")
    l.generateTransition()
    print(l.data)