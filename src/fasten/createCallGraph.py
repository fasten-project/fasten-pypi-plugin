import json
from pathlib import Path
from pycg.pycg import CallGraphGenerator
from pycg import formats

class CreateCallGraph:

    @staticmethod
    def createCallGraph(pkg_name, product, forge, version, timestamp):

        entry_point = [] # List of python files related to the current project

        for file_path in Path("./fasten-pypi-plugin").glob("**/*.py"): # Path needs to be changed
            entry_point.append(str(file_path))

        cg = CallGraphGenerator(entry_point, pkg_name)
        cg.analyze()
        formatter = formats.Fasten(cg, pkg_name, product, forge, version, timestamp)

        print(formatter.generate())

        with open("CallGraph.json", "w+") as f:
            f.write(json.dumps(formatter.generate()))
