from StringIO import StringIO
import xml.etree.ElementTree as ET

### The onentry / onexit isn't handled by scxml in order to provide code.
### We have to parse scxml as a xml to catch these data


actionsTook = ["onentry", "onexit"]

class Action:
    def __init__(self,  pathToScxml):
        it = ET.iterparse(StringIO(str(open(pathToScxml).read())))
        for _, el in it:
            if '}' in el.tag:
                el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
        self.root = it.root
        self.actions = dict()
        for ac in actionsTook:
            self.initAction(ac)

    def sendEvent(self, sendAttrib):
        pass

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
                    if a.tag in ["raise", "send"]:
                        action[i.get("id")][a.tag] += [a.attrib["event"]]
        self.actions[keyAction] = action

    def getOnentryAction(self, actions, key ):
        print(self.actions)
        return self.actions[actions][key]




if __name__ == '__main__':
    a = Action("../Test/send_event.scxml")
    print(a.actions)