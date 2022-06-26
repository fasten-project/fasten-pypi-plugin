# Enrich the Optimized Stitched Call Graph with metadata information from FASTEN.

import re
import json

class EnrichOSCG:

    @staticmethod
    def enrichOSCG(args, oscg, callables):
        """
        Enrich the Optimized Stitched Call Graph
        with metadata information from FASTEN.
        """

        print("Enrich Optimized Stitched Call Graph...")

        with open(callables[0], "r") as callables_file:
            callables = json.load(callables_file)

        for node in oscg["nodes"]:
            oscg_uri = "".join(re.findall(rf"(?<={args.version}).+",
                               oscg["nodes"][node]["URI"]))
            for callable in callables:
                if callable["fasten_uri"] == oscg_uri:
                    if callable["metadata"]:
                        oscg["nodes"][node]["metadata"] = callable["metadata"]

        with open(args.scg_path + "enrichedCallGraph.json", "w+") as ecg_file:
            ecg_file.write(json.dumps(oscg))
