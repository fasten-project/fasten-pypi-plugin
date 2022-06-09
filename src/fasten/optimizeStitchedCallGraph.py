# Create Optimized Stitched Call Graph.
import json

class OptimizeStitchedCallGraph:

    @staticmethod
    def optimizeStitchedCallGraph(args, stitched_call_graph, list_of_nodes):


        print("Optimize Stitched Call Graph:")
        print(stitched_call_graph)
        oscg = {

                "nodes":{}
        }

        i = 0

        for node in list_of_nodes:

            if node:

                node_number = {

                        str(i):{}
                }

                oscg["nodes"].update(node_number)

                with open(stitched_call_graph, "r") as scg_file:
                    scg = json.load(scg_file)

                oscg["nodes"][str(i)].update(scg["nodes"][str(i)])
                print(oscg)

                with open(args.scg_path + "oscg.json", "w") as oscg_file:
                    oscg_file.write(json.dumps(oscg))
            i=i+1

        print("Optimized Stitched Call Graph written in " + args.scg_path + "oscg.json")
