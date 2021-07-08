# Stitch Call Graphs togehter

import json
from stitcher.stitcher import Stitcher

class StitchCallGraph:

    @staticmethod
    def stitchCallGraph(call_graphs):

        print("Stitch Call Graphs")

        stitcher = Stitcher(call_graphs)
        stitcher.stitch()
        output = json.dumps(stitcher.output())
        print(output)
