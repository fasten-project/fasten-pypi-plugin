# Analyze the Stitched Call Graph.

import json

class StitchedCallGraphAnalyzer:

    @staticmethod
    def analyzeStitchedCallGraph(stitched_call_graph):

        print("Analyze Stitched Call Graph")

        print(stitched_call_graph)
        with open(stitched_call_graph, "r") as f:

            scg = json.load(f)

            print(type(scg))
            print(scg['nodes']['0']['URI'])
