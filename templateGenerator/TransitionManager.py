

tab = "    "

class TransitionManager:
    def generateIfTransition(self, data, pere=""):
        value = ""
        if not data:
            return ""
        for transition in data:
            flatList = reduce(lambda l: [item for sublist in l for item in sublist], transition["event"])
            value +=  "if (event == event[" + "\"" + flatList[0] + "\"]" + "):\n" + tab + tab + tab + "return " + str(
                transition["target"][0]) + '()\n'
        return value

    def generateDependance(self, data):
        value = ""
        for transition in data:
            value += "from SM_" + str(transition["target"][0]) + " import *\n"
        return value
