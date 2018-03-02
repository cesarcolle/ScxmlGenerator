import os
from multiprocessing import Queue

from collections import defaultdict

from scxmlProcessor import Loader


class FamillyManager:
    def __init__(self, dictData):
        self.data = dictData
        self.familly = dict()
        self.fathers = list()
        self.path = dict()
        self.toTheEnd = list()
        self.fatherFamilly = dict()
        self.makeFamilly()

    # make familly will fill dictionary to report who is a father, and for one child who is his father.
    # we need it for the compounded state.
    def makeFamilly(self):
        # Init the list value of the dictionary key
        for state in self.data:
            self.familly[state] = list()
            self.fatherFamilly[state] = list()
        for state in self.data:
            # check if he is a father
            if self.data[state].state:
                self.fathers += [state]
            # add child
            self.path[state] = self.data[state].initial
            for child in self.data[state].state:
                self.fatherFamilly[state] += [child.id]
                self.familly[child.id] += [state]

    def pathToAncestor(self, departure):
        if departure:
            return departure + self.pathToAncestor(self.familly[departure[0]])
        else:
            return list()

    def nodeIntersection(self, begin, path):
        if begin and not begin in path:
            self.nodeIntersection(self.familly[begin[0]])
        else:
            return begin

    def bromance(self, state1, state2):
        if not (state1 and state2):
            return
        # state1 => check if state1's father have same father that state's 2 father
        # if false => recursion with father's state
        # else retourn children
        # print("father familly : ", self.fatherFamilly[state1[0]])
        if self.fatherFamilly[state1[0]] != self.fatherFamilly[state2[0]]:
            self.bromance(self.familly[state1[0]], self.familly[state2[0]])
        else:
            return state1, state2

    def isComponed(self, state):
        return

    def brothers(self, lookingBrothers):
        d = defaultdict(list)
        s = self.familly.items()
        for k, v in s:
            if v:
                d[v.pop()].append(k)

    # return the father of one state
    def takeFather(self, key):
        return self.familly[key]

    def takeChild(self, key):
        return self.path[key]

    # return all father
    def takeAllFather(self):
        return self.fathers


if __name__ == "__main__":
    l = Loader.Loader("../Test/ressource/test_bromance.scxml")
    f = FamillyManager(l.machine.doc.stateDict)
    # f.brothers(list())
    print("familly : ", f.familly)
    print("fathers : ", f.fathers)

    print("child : ", f.path)
    print("childOfFather  : ", f.fatherFamilly)
    print("La Bromance de a1 et b1 : ", f.bromance(["a1"], ["b1"]))
    print("hh")
    print("ho ho : ", f.pathToAncestor(["b1"]))
    print("path to follow : ", f.nodeIntersection(["b1"], f.pathToAncestor(["a1"])))
