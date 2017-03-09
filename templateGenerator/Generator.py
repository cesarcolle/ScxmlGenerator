####  Generator class will generate via Cheetah template some files .

from state_generic_template import state_generic_template
from scxmlProcessor.Loader import Loader


class Generator:


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


if __name__ == '__main__':
    loader = Loader("../test.xml")
    template = state_generic_template()
    generator = Generator()

    generator.generateChart(loader.test,
                            './test.out',
                            template)
