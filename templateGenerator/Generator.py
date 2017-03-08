####  Generator class will generate via Cheetah template some files .

from statechart_debugout import statechart_debugout
from scxmlProcessor.Loader import Loader


class Generator:


    def generateChart(self, stateChartXML, fileName, template):
        template.stateChartXML = stateChartXML
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
    template = statechart_debugout()
    generator = Generator()
    generator.generateChart(loader.data,
                            './test.out',
                            template)
