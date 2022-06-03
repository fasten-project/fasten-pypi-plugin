# Stitch Call Graphs together.

import json
from stitcher.stitcher import Stitcher

class StitchCallGraphs:

    @staticmethod
    def stitchCallGraphs(args, call_graphs):

        print("Stitch Call Graphs")

        stitcher = Stitcher(call_graphs, False)
        stitcher.stitch()
        output = json.dumps(stitcher.output(), indent=2)
        stitched_call_graph = args.scg_path + args.product + ".json"

        with open(args.scg_path + args.product + ".json", "w+") as f:
            f.write(output)
        print('Saved Stitched Call Graph in: ' + args.scg_path + args.product + ".json")

        return stitched_call_graph
