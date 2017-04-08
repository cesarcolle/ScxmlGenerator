from unittest import TestCase

# mok Loader
from scxmlProcessor.Generator import Generator


class Test_Generator(TestCase):
    def test_GenerateEventsSimple(self):
        g = Generator("./Test/simple1.scxml")
        for d in g.data:
            g.generateEvents(g.data[d])
        self.assertListEqual(["Transition_1", "Transition_2"], list(g.events))

    def test_GenerateEventExtended(self):
        g = Generator("./Test/simple2.scxml")
        for d in g.data:
            g.generateEvents(g.data[d])
        self.assertListEqual(["Transition_1", "Transition_2"], list(g.events))

    def test_GenerateEventComplete(self):
        g = Generator("./Test/simple3.scxml")
        for d in g.data:
            g.generateEvents(g.data[d])
        self.assertListEqual(["Transition_1", "Transition_2", "Transition_3", "Transition_4"],
                             list(g.events))

    def test_GenerateTransitionSimple(self):
        g = Generator("./Test/simple1.scxml")
        self.assertDictEqual(g.data, {"State_1" : [{"event" : [["Transition_1"]], "target" : ["State_2"]},
                                                   {"event" : [["Transition_2"]], "target" : ["State_3"]}],
                                      "State_2" : [],
                                      "State_3" : []})
        
    def test_GenerateTransitionExtended(self):
        g = Generator("./Test/simple2.scxml")
        self.assertDictEqual(g.data, {"State_1" : [{"event" : [["Transition_1"]], "target" : ["State_2"]},
                                                   ],
                                      "State_2" : [{"event" : [["Transition_2"]], "target" : ["State_3"]}],
                                      "State_3" : []})