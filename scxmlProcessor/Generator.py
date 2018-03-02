####  Generator class will generate via Cheetah template some files .
import os
from scxml.node import Transition
from subprocess import call

from scxmlProcessor.Action import Action
from scxmlProcessor.FamillyManager import FamillyManager
from scxmlProcessor.Loader import Loader
from scxmlProcessor.TransitionManager import TransitionManager
from templateGenerator.TemplateProvider import TemplateProvider

templatesFiles = {"state_source": "./templateGenerator/state_generic_template.tmpl", \
                  "event": "./templateGenerator/event_template.tmpl", \
                  "state_header": "./templateGenerator/state_generic_header_state.tmpl", \
                  "main": "./templateGenerator/mainSmProcessus.tmpl", \
                  "sharedStruture": "./templateGenerator/sharedStructure.tmpl"}


class Generator:

    def __init__(self, path):
        self.loader = Loader(path)

        self.actions = Action(path)
        self.data = dict()
        self.parent = dict()
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
            print("erreur opening file Generator :" + fileName )

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

    def generateSources(self, directory, directoryTemplate = "./"):

        #   del self.loader.data["__main__"]
        allNameState = list()
        templates = ""
        statement = {"statement" : []}
        for state in self.data:
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
            source_state["onentry"] = self.actions.getOnentryAction("onentry", state)
            source_state["onexit"] = self.actions.getOnentryAction("onexit", state)
            # create the source code to import dependancies
            source_state["dependancies"] = TransitionManager().generateDependance(v)
            source_state["childToBegin"] = self.familly.takeChild(state)

            statement["statement"] += [source_state]
            self.generateEvents(self.data[state])
        # Generate the event enum
        self.generateOutputFile(directory + "event.py", self.tmpl.provideTemplate(templatesFiles["event"],
                                                                                  {"events": self.events}))

        self.generateOutputFile(directory + "sharedStruture.py",
                                self.tmpl.provideTemplate(templatesFiles["sharedStruture"], \
                                                          {"fathers": self.familly.takeAllFather()}))

        self.generateOutputFile(directory + "fsm.py", self.tmpl.provideTemplate(templatesFiles["state_source"],
                                                                                statement))
        mainValue = self.tmpl.provideTemplate(templatesFiles["main"],
                                  {"states": allNameState,
                                   "ancestor": self.ancestor})
        self.generateOutputFile(directory + "fsm.py", mainValue, option='a')


if __name__ == '__main__':
    os.system("cd ../output && rm *.py")
    Generator("../Test/ressource/raise_test.scxml").generateSources("../output/")
