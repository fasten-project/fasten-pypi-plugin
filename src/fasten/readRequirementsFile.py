# Retrieve package name and version from requirements.txt file.

import re
import json

class ReadRequirementsFile:

    @staticmethod
    def readFile(requirements_file):

        with open(requirements_file, "r") as requirements:

            pkgs = { }
            for x in requirements:
                name = "".join(re.findall(r".+(?===)", x))
                version = "".join(re.findall(r"(?<===).+", x))
                pkgs[name] = version

            pkgs = json.dumps(pkgs)

            return pkgs
