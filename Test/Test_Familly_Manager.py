from unittest import TestCase

from scxmlProcessor.FamillyManager import FamillyManager


class state:
    def __init__(self, id, state):
        self.id = id
        self.state = state


dataTest = {'s2': state("s2", [state("s3", [])]),
            's3': state("s3", [state("s1", [])]),
                        's1': state("s1", [])}

dataTest2 = {'s2': state("s2", [state("s3", [])]),
            's3': state("s3", [state("s1", [])]),
                        's1': state("s1", []),
            's4' : state("s4", [state("s5", [])]),
            's5' : state("s5", [])}


class Test_Familly_Manager(TestCase):
    def test_makeFamilly(self):
        f = FamillyManager(dataTest)
        self.assertDictEqual(f.familly, {"s2": [], "s3": ["s2"], "s1": ["s3"]})

    def test_makeFamillySeveralState(self):
        f = FamillyManager(dataTest2)
        self.assertDictEqual(f.familly, {"s2": [], "s3": ["s2"], "s1": ["s3"], "s5" : ["s4"], "s4" : []})

    def test_fathers(self):
        f = FamillyManager(dataTest)
        self.assertListEqual(f.fathers, ['s3', "s2"])

    def test_takeFather(self):
        f = FamillyManager(dataTest)
        self.assertDictEqual(f.familly, {"s2": [], "s3": ["s2"], "s1": ["s3"]})
