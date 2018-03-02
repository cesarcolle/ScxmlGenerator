from unittest import TestCase

# mok Loader
from scxmlProcessor.Generator import Generator


class Test_Generator(TestCase):
    def test_GenerateEventsSimple(self):
        g = Generator("./Test/ressource/simple1.scxml")
        for d in g.data:
            g.generateEvents(g.data[d])
        self.assertListEqual(["t2", "t1"], list(g.events))

    def test_GenerateEventExtended(self):
        g = Generator("./Test/ressource/simple2.scxml")
        for d in g.data:
            g.generateEvents(g.data[d])
        self.assertListEqual(["t2", "t1"], list(g.events))

    def test_GenerateEventComplete(self):
        g = Generator("./Test/ressource/simple3.scxml")
        for d in g.data:
            g.generateEvents(g.data[d])
        self.assertListEqual(["t2", "t3", "t1"],
                             list(g.events))

    def test_GenerateTransitionSimple(self):
        g = Generator("./Test/ressource/simple1.scxml")
        self.assertDictEqual(g.data, {"State_3" : [],
                                      "succes" : [],
                                      "faillure" : [{"event" : [["t1"]], "target" : ["succes"]}, {"event" : [["t2"]], "target" : ["State_3"]}]})

    def test_GenerateTransitionExtended(self):
        g = Generator("./Test/ressource/simple2.scxml")
        self.assertDictEqual(g.data, {"State_1" : [{"event" : [["t1"]], "target" : ["faillure"]}],
                                      "faillure" : [{"event" : [["t2"]], "target" : ["succes"]}],
                                      "succes" : []})