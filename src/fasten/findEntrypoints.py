# Find the entrypoints of local project in Stitched Call Graph for the project.

import re
import json

class FindEntrypoints:

    @staticmethod
    def findEntrypoints(args, stitched_call_graph):
        """Find the entry points of a local project in the Stitched Call Graph of this project
           and save them in a list called 'entry_points'."""

        print("Find entrypoints in Stitched Call Graph for local project.")
        entry_points = [ ]

        with open(stitched_call_graph, "r") as scg_file:
            scg = json.load(scg_file)

        for node in scg["nodes"]:

            product = "".join(re.findall(rf"\!({args.product})\$", scg["nodes"][node]["URI"]))
            if product == args.product:
                entry_points.append(node)

        return entry_points
