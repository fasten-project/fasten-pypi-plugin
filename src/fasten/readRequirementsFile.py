import re
import json

class ReadRequirementsFile:

    def __init__(self, pathToFile):
        self.pathToFile = pathToFile

    def readFile(self):

        with open(self.pathToFile, "r") as requirements:

            pkgs_list = ""
            for x in requirements:
                name = "".join(re.findall(r".+(?===)", x))
                version = "".join(re.findall(r"(?<===).+", x))
                pkg = {
                    "name": name,
                    "version": version,
                    "forge": "pypi"
                }

                pkgs_list += json.dumps(pkg) + "\n"

            print(pkgs_list)
