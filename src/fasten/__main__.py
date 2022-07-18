import argparse
import os, shutil
import json
from fasten.executePypiResolver import ExecutePypiResolver
from fasten.readRequirementsFile import ReadRequirementsFile
from fasten.checkPackageAvailability import CheckPackageAvailability
from fasten.createCallGraph import CreateCallGraph
from fasten.requestFasten import RequestFasten
from fasten.stitchCallGraphs import StitchCallGraphs
from fasten.findEntrypoints import FindEntrypoints
from fasten.createAdjacencyList import CreateAdjacencyList
from fasten.depthFirstSearch import DepthFirstSearch
from fasten.optimizeStitchedCallGraph import OptimizeStitchedCallGraph
from fasten.stitchedCallGraphAnalyzer import StitchedCallGraphAnalyzer
from fasten.createDirectories import CreateDirectories
from fasten.enrichOSCG import EnrichOSCG
from fasten.collectingGeneratedAndRetrievedCallGraphs import collectingGeneratedAndRetrievedCallGraphs


def main():

    parser = argparse.ArgumentParser(prog='PyPI-plugin')
    parser.add_argument("--product", type=str, help="Package name") # pypiPlugin-test-online
    parser.add_argument("--pkg_name", type=str, help="Package containing the code to be analyzed") # pypiPlugin-test-online
    parser.add_argument("--project_path", type=str, help="Path to package to be analyzed") # /mnt/stuff/projects/work/pypi-plugin/src/fasten/
    parser.add_argument("--timestamp", type=int, help="Timestamp of the package's version") # 42
    parser.add_argument("--version", type=str, help="Version of the product") # 1.0
    parser.add_argument("--requirements", type=str, help="Path to the requirements file") # /mnt/stuff/projects/work/pypi-plugin/requirements.txt
    parser.add_argument("--fasten_data", type=str, help="Path to the folder where the received FASTEN data will be stored")
    parser.add_argument("--scg_path", type=str, help="Path to the folder where the Stitched Call Graph will be stored")
    args = parser.parse_args()

    url = 'https://api.fasten-project.eu/api/pypi/' # URL to the FASTEN API
    forge = "local" # Source the product was downloaded from
    max_iter = -1 # Maximum number of iterations through source code (from pycg).
    operation = "call-graph" # or key-error for key error detection on dictionaries (from pycg).
    local_package = {args.product: args.version}
    local_package = json.dumps(local_package)
    call_graphs = []
    vulnerabilities = []

    dirs_to_delete = [args.fasten_data, args.scg_path ]
    for dir in dirs_to_delete :
        isExist = os.path.exists(dir)
        if isExist:
            print("removing: " + dir)
            shutil.rmtree(dir)

    CreateDirectories.DirectoryCheck(args.fasten_data, args.scg_path) # Create directories to store the Call Graphs and the Stitched Call Graph
    DependenciesTree = ExecutePypiResolver.executePypiResolver(args.requirements)
    all_pkgs = ReadRequirementsFile.readFile(DependenciesTree) # Read requirements.txt
    pkgs, unknown_pkgs = CheckPackageAvailability.checkPackageAvailability(all_pkgs, url) # Check if packages are known by FASTEN
    call_graphs, cg_pkgs, unknown_pkgs = RequestFasten.requestFasten(args, unknown_pkgs, url, "rcg")


    ################################ CALL GRAPHS - Michele - Retrieve and Generation in one function ##################
    call_graphs = collectingGeneratedAndRetrievedCallGraphs(args, unknown_pkgs, url)
    #print("call_graphs")
    #print(call_graphs)


    #call_graphs, cg_pkgs, unknown_pkgs = RequestFasten.requestFasten(args, pkgs, url, "rcg")
    #call_graphs = CreateCallGraph().createCallGraph(args, forge, max_iter, operation, call_graphs)
    vulnerabilities, vul_pkgs, unknown_pkgs = RequestFasten.requestFasten(args, pkgs, url, "vulnerabilities")

#    pathsToCallGraphs = parser.parse_args(call_graphs)

    stitched_call_graph = StitchCallGraphs().stitchCallGraphs(args, call_graphs)
    entry_points = FindEntrypoints.findEntrypoints(args, stitched_call_graph)

    adjList = CreateAdjacencyList
    adjList.createAdjacencyList(stitched_call_graph)
    list_of_nodes = [False] * adjList.getNodes()

    # Run a depth first search for each entry point to create a list of all called nodes.
    for x in entry_points:
        list_of_nodes = DepthFirstSearch.depthFirstSearch(adjList, int(x), list_of_nodes)


    oscg = OptimizeStitchedCallGraph.optimizeStitchedCallGraph(args, stitched_call_graph, list_of_nodes)
    callables, callable_pkgs , unknown_pkgs = RequestFasten.requestFasten(args, local_package, url, "callables?limit=1000000")
    EnrichOSCG.enrichOSCG(args, oscg, callables)

#    StitchedCallGraphAnalyzer.analyzeStitchedCallGraph(stitched_call_graph)

    for package in vul_pkgs:
        print("The package " + package + ":" + vul_pkgs[package] + " is vulnerable!")
        print("Vulnerabilities can be found in " + args.fasten_data + package + "." + "vulnerabilities.json")

if __name__ == "__main__":
    main()
