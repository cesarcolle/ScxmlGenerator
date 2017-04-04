tab = "    "


class TransitionManager:
    def createIf(self, v1, returnedValue):
        return "if (event == " + "\"" + v1 + "\"" + "):\n" + tab * 3 + "return " + "statesItem[\"" + str(
            returnedValue) + "\"]" + '\n'

    def generateIfTransition(self, data, pere=""):
        value = ""
        if not data:
            return ""
        for transition in data:
            flatList = reduce(lambda l: [item for sublist in l for item in sublist], transition["event"])
            value += self.createIf(flatList[0], transition["target"][0])
        return value

    def generateDependance(self, data):
        value = ""
        for transition in data:
            value += "import SM_" + str(transition["target"][0])
        return value
