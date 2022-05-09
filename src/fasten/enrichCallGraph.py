# Enrich the Stitched Call Graph with metadata information.

import json

class EnrichCallGraph:

    @staticmethod
    def enrichCallGraph(pkgs, stitched_call_graph):

        print("Enrich Stitched Call Graph")
        pkgs = json.loads(pkgs)
        print(pkgs)

        #TODO: Read in the callable information and send it to FASTEN to receive metadata for each.

        for package in pkgs:

            print(package)
            with open("fastenData/" + package +  ".vulnerabilities" + ".json", "r") as f:
                pkgs_vul = json.loads(f.read()) # read in the package vulnerability

                #TODO: Find a way to store the vulnerability information in the Stitched Call Graph.
