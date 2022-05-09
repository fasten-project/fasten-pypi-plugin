import argparse
from readRequirementsFile import ReadRequirementsFile
from checkPackageAvailability import CheckPackageAvailability
from createCallGraph import CreateCallGraph
from requestFasten import RequestFasten
from stitchCallGraph import StitchCallGraph


class Main:

    parser = argparse.ArgumentParser()
    parser.add_argument("--product", type=str, help="Package name")
    parser.add_argument("--pkg_name", type=str, help="Package containing the code to be analyzed")
    parser.add_argument("--project_path", type=str, help="Path to package to be analyzed")
    parser.add_argument("--timestamp", type=int, help="Timestamp of the package's version")
    parser.add_argument("--version", type=str, help="Version of the product")
    parser.add_argument("--requirements", type=str, help="Path to the requirements file")
    parser.add_argument("--cg_path", type=str, help="Path to the Call Graphs to be stored")
    parser.add_argument("--scg_path", type=str, help="Path to the Stitched Call Graph to be stored")
    args = parser.parse_args()

    url = 'https://api.fasten-project.eu/api/pypi/' # URL to the FASTEN API
    forge = "local" # Source the product was downloaded from
    max_iter = -1 # Maximum number of iterations through source code (from pycg).
    operation = "call-graph" # or key-error for key error detection on dictionaries (from pycg).
    call_graphs = []
    vulnerabilities = []

    pkgs = ReadRequirementsFile.readFile(args.requirements) # Read requirements.txt
    pkgs, unknown_pkgs = CheckPackageAvailability.checkPackageAvailability(pkgs, url) # Check if packages are known by FASTEN


    call_graphs = RequestFasten.requestFasten(pkgs, url, "rcg")
    call_graphs = CreateCallGraph().createCallGraph(args, forge, max_iter, operation, call_graphs)
    vulnerabilities = RequestFasten.requestFasten(pkgs, url, "vulnerabilities")

#    pathsToCallGraphs = parser.parse_args(call_graphs)

    stitched_call_graph = StitchCallGraph().stitchCallGraph(args, call_graphs)
