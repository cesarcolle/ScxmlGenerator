####  Generator class will generate via Cheetah template some files .

from scxmlProcessor.Loader import Loader
from Cheetah.Template import Template


class Generator:
    def __init__(self, path):
        self.loader = Loader(path)

    def generateChart(self, stateChartXML, fileName, template):
        template.state = stateChartXML
        self.generateOutputFile(fileName, template)

    def generateOutputFile(self, fileName, template):
        print template
        outputFile = open(fileName, 'w')
        try:
            outputFile.write(str(template))
        finally:
            outputFile.close()

    def generateSources(self):
        self.loader.generateTransition()
        value = ""
        try:
            f = open("state_generic_template.tmpl", "r")
            value = f.read()
            f.close()
        except IOError:
            print "eerror opening the file"

        for state in self.loader.data:
            v = ""
            print self.loader.data[state]
            if len(self.loader.data[state]) > 0:
                v = self.loader.data[state][0]
            temp = Template(value, searchList={"nom": state, "params" : v})
            self.generateOutputFile(state + ".cpp", temp)

            print "writting"


if __name__ == '__main__':
    generator = Generator("../test.xml").generateSources()