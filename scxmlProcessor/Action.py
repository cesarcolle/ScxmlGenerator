from StringIO import StringIO
import xml.etree.ElementTree as ET

### The onentry / onexit isn't handled by scxml in order to provide code.
### We have to parse scxml as a xml to catch these data


actionsTook = ["onentry", "onexit"]

class Action:

    # There is a problem with the Pyscxml library. we juste have function pointer of onentry
    # onexit relation, so we have to catch these data with the python library etree.
    # but etree is old. So tu handle xml namespace, the best way stay to remove namespace call.


    def __init__(self,  pathToScxml):
        value = ""
        try:
            value = str(open(pathToScxml).read())
        except IOError:
            print("error openning file in action = " + pathToScxml)
        # parse XML
        it = ET.iterparse(StringIO(value))
        # remove namespace call
        for _, el in it:
            if '}' in el.tag:
                el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
        self.root = it.root
        self.actions = dict()
        for ac in actionsTook:
            self.initAction(ac)

    def sendEvent(self, sendAttrib):
        pass

    # catch all onentry / onexit actions from the xml given.
    def initAction(self, keyAction):
        self.actions[keyAction] = dict()
        action = self.actions[keyAction]
        for i in self.root.iter("state"):
            action[i.get("id")] = dict()
            action[i.get("id")]["send"] = list()
            action[i.get("id")]["raise"] = list()
            o = i.find(keyAction)
            if o != None:
                for a in o:
                    if a.tag in ["raise", "send"] and a.attrib:
                        action[i.get("id")][a.tag] += [a.attrib["event"]]
        self.actions[keyAction] = action

    def getOnentryAction(self, actions, key ):
        return self.actions[actions][key]




if __name__ == '__main__':
    a = Action("../Test/goal.scxml")
    print(a.actions)