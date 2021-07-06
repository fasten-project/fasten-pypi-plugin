import re
import json

class ReadRequirementsFile:

    def __init__(self, pathToFile):
        self.pathToFile = pathToFile

    def readFile(self):

        with open(self.pathToFile, "r") as requirements:

            pkgs = { }
            for x in requirements:
                name = "".join(re.findall(r".+(?===)", x))
                version = "".join(re.findall(r"(?<===).+", x))
                pkgs[name] = version

            pkgs = json.dumps(pkgs)

            return pkgs
