
import subprocess

class TestLoader :
    def __init__(self):
        self.file = subprocess.call(["ls", "./Test/ressource/*.scxml"])