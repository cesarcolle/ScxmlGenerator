import subprocess
from subprocess import call
from unittest import TestCase
import os

from scxmlProcessor.Generator import Generator

import shlex, subprocess

testDirectory = "./Test/ressource/"

simpleParcours = {"simple3.scxml": ["t2", "t3"], "simple2.scxml": ["t2"], "simple1.scxml": [], \
                  "simple_hierarchie.scxml": []}


class Test_Integration(TestCase):
    # this integration test check if all the path given to our fsm reach the sucess
    # state. Allows us to know if we disturbed the code.
    def test_integration_simple(self):
        for file in os.listdir(testDirectory):
            if file.endswith("scxml"):
                g = Generator(testDirectory + file)
                g.generateSources("./output/")
                # simple as different value to put to reach succes.
                try:
                    f = open("./output/fsm.py", "a")
                    if file.startswith("simple"):
                        if file in simpleParcours:

                                for value in simpleParcours[file]:
                                    f.write("\n    stateMachine = stateMachine.sendEvent(" + "\"" + value + "\")")
                                f.write("\n    print(stateMachine)")
                                f.close()
                    else:
                        print("write print at the end : " + file)
                        f.write("\n    print(stateMachine)")
                        f.close()
                except IOError:
                    print('erreur generation de code')

                cmd = "python2 -d ./output/fsm.py"

                args = shlex.split(cmd)
                output, error = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
                print("retourne : ", output)
                self.assertTrue("succes" in str(output).split("\n")[-2], "probleme with : " + file)
