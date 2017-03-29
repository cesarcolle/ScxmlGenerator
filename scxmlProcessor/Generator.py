####  Generator class will generate via Cheetah template some files .
from scxml.node import Transition

from scxmlProcessor.Loader import Loader
from templateGenerator.TemplateProvider import TemplateProvider
from templateGenerator.TransitionManager import TransitionManager

import os

templatesFiles = {"state_source": "state_generic_template.tmpl", \
                  "event": "event_template.tmpl", \
                  "state_header": "state_generic_header_state.tmpl"}


class Generator:
    def __init__(self, path):
        self.loader = Loader(path)
        self.data = dict()
        self.parent = dict()
        self.generateTransition()
        self.tmpl = TemplateProvider()
        self.events = set()

    # write the template content into a filename.
    def generateOutputFile(self, fileName, template):
        try:
            outputFile = open(fileName, 'w')
            outputFile.write(str(template))
            outputFile.close()
        except IOError:
            print "erreur opening file"

            # generate the Events from the scxml machine

    def generateTransition(self):
        # recover transition from the initial state.
        self.t = Transition(self.loader.machine.doc.rootState)
        del self.loader.machine.doc.stateDict["__main__"]
        for key in self.loader.machine.doc.stateDict:
            tmp = Transition(self.loader.machine.doc.stateDict[key])
            self.parent[key] = self.loader.machine.doc.stateDict[key].parent
            self.data[key] = list()
            for transition in tmp.source.transition:
                self.data[key] += [{"event": transition.event, "target": transition.target}]

    def generateEvents(self, stateData):
        for data in stateData:
            flatList = reduce(lambda l: [item for sublist in l for item in sublist], data["event"])
            # using set because we don't want twice similiar value into our event
            self.events.add(flatList[0])

    def generateSources(self, directory):

        #   del self.loader.data["__main__"]
        for state in self.data:
            name = directory + "SM_" + state
            v = ""
            if self.data[state]:
                v = self.data[state]
            # create the cpp source
            source_state = dict()
            source_state["nom"] = state
            source_state["transition"] = TransitionManager().generateIfTransition(v, self.parent[state])
            source_state["parent"] = [x.id for x in self.parent[state]]
            source_state["dependancies"] = TransitionManager().generateDependance(v)
            # transition = TransitionManager().generateIfTransition(v, self.parent[state])
            self.generateOutputFile(name + ".py", self.tmpl.provideTemplate(templatesFiles["state_source"], \
                                                                            source_state))
            self.generateEvents(self.data[state])
        # Generate the event enum
        lastEvent = ""
        if self.events:
            lastEvent = self.events.pop()

        self.generateOutputFile(directory + "event.py", self.tmpl.provideTemplate(templatesFiles["event"],
                                                                                 source_state))

    def generateHierarchy(self):
        pass


if __name__ == '__main__':
    os.system("cd ../Test/ressource && rm *.py")

    generator = Generator("../parallel.scxml").generateSources("../Test/ressource/")
