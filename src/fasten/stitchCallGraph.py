# Stitch Call Graphs together.

import json
from stitcher.stitcher import Stitcher

class StitchCallGraph:

    @staticmethod
    def stitchCallGraph(args, call_graphs):

        print("Stitch Call Graphs")

        stitcher = Stitcher(call_graphs, "simple")
        stitcher.stitch()
        output = json.dumps(stitcher.output())
        stitched_call_graph = args.scg_path + args.product + ".json"

        with open(args.scg_path + args.product + ".json", "w+") as f:
            f.write(json.dumps(output))
        print('Saved Stiched Call Graph in: ' + args.scg_path + args.product)
