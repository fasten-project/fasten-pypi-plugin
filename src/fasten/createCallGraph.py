import json
from pathlib import Path
from pycg.pycg import CallGraphGenerator
from pycg import formats

class CreateCallGraph:

    @staticmethod
    def createCallGraph(args, forge, max_iter, operation, call_graphs):

        entry_point = [] # List of python files related to the current project

        for file_path in Path(args.project_path).glob("**/*.py"):
            entry_point.append(str(file_path))

        cg = CallGraphGenerator(entry_point, args.pkg_name, max_iter, operation)
        cg.analyze()
        formatter = formats.Fasten(cg, args.pkg_name, args.product, forge, args.version, args.timestamp)

        print(formatter.generate())

        with open("callGraphs/" + args.pkg_name + ".json", "w+") as f:
            f.write(json.dumps(formatter.generate()))

        call_graphs.append("callGraphs/" + args.pkg_name + ".json") # Append path to locally created Call Graph to list of paths

        return call_graphs
