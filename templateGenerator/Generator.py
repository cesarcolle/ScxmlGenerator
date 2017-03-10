####  Generator class will generate via Cheetah template some files .

from scxmlProcessor.Loader import Loader
from TemplateProvider import TemplateProvider
import os
templatesFiles = {"state" : "state_generic_template.tmpl", "event" : "event_template.tmpl"}

class Generator:
    def __init__(self, path):
        self.loader = Loader(path)
        self.loader.generateTransition()
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
    def generateEvents(self, stateData):
        for data in stateData:
            flatList = reduce(lambda l: [item for sublist in l for item in sublist], data["event"])
            #using set because we don't want twice similiar value into our event
            self.events.add(flatList[0])




    def generateSources(self):
        del self.loader.data["__main__"]
        for state in self.loader.data:
            v = ""
            if self.loader.data[state]:
                v = self.loader.data[state][0]
            self.generateOutputFile(state + ".cpp", self.tmpl.provideTemplate(templatesFiles["state"], \
                                                                               {"nom" : state, "params": v}))

            # take the information provided by the state for loop. update the Set event into our object
            self.generateEvents(self.loader.data[state])
        lastEvent = ""
        if self.events:
            lastEvent = self.events.pop()

        self.generateOutputFile("event.h", self.tmpl.provideTemplate(templatesFiles["event"],
                                                                     {"events": list(self.events), "final" : lastEvent}))


if __name__ == '__main__':
    generator = Generator("../test.xml").generateSources()
    #os.system("rm *.cpp")