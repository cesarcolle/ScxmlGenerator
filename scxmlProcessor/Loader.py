from __future__ import print_function

from scxml.pyscxml import StateMachine

## The loader class allow us to load a SCXML file.
## The loader will provide the tree containing all the data needed by our generator.

informations = dict()


class Loader:
    def __init__(self, path):
        self.machine = StateMachine(path)
        self.data = dict()
        self.parent = dict()


if __name__ == "__main__":
    l = Loader("../Test/ressource/send_event.scxml")
