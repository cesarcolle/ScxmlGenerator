####  Generator class will generate via Cheetah template some files .
from scxml.node import Transition

from scxmlProcessor.FamillyManager import FamillyManager
from scxmlProcessor.Loader import Loader
from templateGenerator.TemplateProvider import TemplateProvider
from templateGenerator.TransitionManager import TransitionManager

import os

templatesFiles = {"state_source": "state_generic_template.tmpl", \
                  "event": "event_template.tmpl", \
                  "state_header": "state_generic_header_state.tmpl", \
                  "main": "mainSmProcessus.tmpl", \
                  "sharedStruture": "sharedStructure.tmpl"}


class Generator:
    def __init__(self, path):
        self.loader = Loader(path)
        self.data = dict()
        self.parent = dict()
        print(self.loader.machine.doc.rootState.initial)
        self.ancestor = self.loader.machine.doc.rootState.initial[0]
        self.generateTransition()
        self.familly = FamillyManager(self.loader.machine.doc.stateDict)
        self.tmpl = TemplateProvider()
        self.events = set()

    # write the template content into a filename.
    def generateOutputFile(self, fileName, template, option='w'):
        try:
            outputFile = open(fileName, option)
            outputFile.write(str(template))
            outputFile.close()
        except IOError:
            print("erreur opening file")

    def generateTransition(self):
        # recover transition from the initial state.
        # His job is to inialize the value of all data.
        self.t = Transition(self.loader.machine.doc.rootState)
        del self.loader.machine.doc.stateDict["__main__"]
        # we recovering all transition
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
        allNameState = list()
        templates = ""
        statement = {"statement" : []}
        for state in self.data:
            name = directory + "SM_" + state
            v = ""
            if self.data[state]:
                v = self.data[state]
            # recover all data from one state
            # here all names
            allNameState += [state]

            source_state = dict()
            # label of the state
            source_state["nom"] = state
            # transition of the state
            source_state["transition"] = TransitionManager().generateIfTransition(v, self.parent[state])
            # parents or the state
            source_state["parent"] = self.familly.takeFather(state)

            # create the source code to import dependancies
            source_state["dependancies"] = TransitionManager().generateDependance(v)

            statement["statement"] += [source_state]
            #templates += str(self.tmpl.provideTemplate(templatesFiles["state_source"], source_state))
            #                                                                 source_state)
            # self.generateOutputFile(directory + state + ".py", )

            self.generateEvents(self.data[state])
        # Generate the event enum
        self.generateOutputFile(directory + "event.py", self.tmpl.provideTemplate(templatesFiles["event"],
                                                                                  {"events": self.events}))

        self.generateOutputFile(directory + "sharedStruture.py",
                                self.tmpl.provideTemplate(templatesFiles["sharedStruture"], \
                                                          {"fathers": self.familly.takeAllFather()}))
        self.generateOutputFile(directory + "fsm.py", templates)

        self.generateOutputFile(directory + "fsm.py", self.tmpl.provideTemplate(templatesFiles["state_source"], statement))
        mainValue = self.tmpl.provideTemplate(templatesFiles["main"],
                                  {"states": allNameState,
                                   "ancestor": self.ancestor})
        self.generateOutputFile(directory + "fsm.py", mainValue, option='a')

    def generateHierarchy(self):
        pass


if __name__ == '__main__':
    os.system("cd ../Test/ressource && rm *.py")
    generator = Generator("../very_simpl.scxml").generateSources("../Test/ressource/")
