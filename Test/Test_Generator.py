from unittest import TestCase


## Mok classe
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
             's4': state("s4", [state("s5", [])]),
             's5': state("s5", [])}


class Test_Generator(TestCase):
    def test_GenerateTransition(self):
        pass
