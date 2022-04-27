# Stitch Call Graphs togehter

import json
from stitcher.stitcher import Stitcher

class StitchCallGraph:

    @staticmethod
    def stitchCallGraph(args, call_graphs):

        print("Stitch Call Graphs")

        stitcher = Stitcher(call_graphs)
        stitcher.stitch()
        output = json.dumps(stitcher.output())

        with open("StitchedCallGraph/" + args.product + ".json", "w+") as f:
            f.write(output)
        print('Saved Stiched Call Graph in: ' + "./StitchedCallGraph/" + args.product)
