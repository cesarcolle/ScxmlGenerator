class TransitionManager:
    def generateIfTransition(self, data, pere=""):
        value = ""
        if not data:
            return ""
        for transition in data :
            flatList = reduce(lambda l: [item for sublist in l for item in sublist], transition["event"])
            value += "if (event == " + flatList[0] + ") :\n\t\t\treturn " + str(transition["target"][0]) + '()\n'

        return value
