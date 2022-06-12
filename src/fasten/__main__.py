import argparse
from fasten.readRequirementsFile import ReadRequirementsFile
from fasten.checkPackageAvailability import CheckPackageAvailability
from fasten.createCallGraph import CreateCallGraph
from fasten.requestFasten import RequestFasten
from fasten.stitchCallGraphs import StitchCallGraphs
from fasten.findEntrypoints import FindEntrypoints
from fasten.createAdjacencyList import CreateAdjacencyList
from fasten.depthFirstSearch import DepthFirstSearch
from fasten.optimizeStitchedCallGraph import OptimizeStitchedCallGraph
from fasten.enrichCallGraph import EnrichCallGraph
from fasten.stitchedCallGraphAnalyzer import StitchedCallGraphAnalyzer
from fasten.createDirectories import CreateDirectories


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
    call_graphs = []
    vulnerabilities = []

    CreateDirectories.DirectoryCheck(args.fasten_data, args.scg_path) # Create directories to store the Call Graphs and the Stitched Call Graph

    pkgs = ReadRequirementsFile.readFile(args.requirements) # Read requirements.txt
    pkgs, unknown_pkgs = CheckPackageAvailability.checkPackageAvailability(pkgs, url) # Check if packages are known by FASTEN


    call_graphs, cg_pkgs = RequestFasten.requestFasten(args, pkgs, url, "rcg")
    call_graphs = CreateCallGraph().createCallGraph(args, forge, max_iter, operation, call_graphs)
    vulnerabilities, vul_pkgs = RequestFasten.requestFasten(args, pkgs, url, "vulnerabilities")

#    pathsToCallGraphs = parser.parse_args(call_graphs)

    stitched_call_graph = StitchCallGraphs().stitchCallGraphs(args, call_graphs)
    entry_points = FindEntrypoints.findEntrypoints(args, stitched_call_graph)

    adjList = CreateAdjacencyList
    adjList.createAdjacencyList(stitched_call_graph)

    list_of_nodes = DepthFirstSearch.depthFirstSearch(adjList, 0)

    OptimizeStitchedCallGraph.optimizeStitchedCallGraph(args, stitched_call_graph, list_of_nodes)
#    StitchedCallGraphAnalyzer.analyzeStitchedCallGraph(stitched_call_graph)

    for package in vul_pkgs:
        print("The package " + package + ":" + vul_pkgs[package] + " is vulnerable!")
        print("Vulnerabilities can be found in " + args.fasten_data + package + "." + "vulnerabilities.json")

if __name__ == "__main__":
    main()
