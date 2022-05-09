# Stitch Call Graphs together.

import json
from stitcher.stitcher import Stitcher

class StitchCallGraph:

    @staticmethod
    def stitchCallGraph(args, call_graphs):

        print("Stitch Call Graphs")

        stitcher = Stitcher(call_graphs)
        stitcher.stitch()
        output = json.dumps(stitcher.output())
        stitched_call_graph = "StitchedCallGraph/" + args.product + ".json"

        with open("StitchedCallGraph/" + args.product + ".json", "w+") as f:
            f.write(output)
        print('Saved Stiched Call Graph in: ' + "./StitchedCallGraph/" + args.product)

        return stitched_call_graph
