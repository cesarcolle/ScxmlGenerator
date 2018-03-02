from scxmlProcessor.Generator import Generator
from scxmlProcessor.Loader import Loader

if __name__ == "__main__":
    l = Generator("./Test/ressource/raise_test.scxml")
    l.generateSources("./output/")
