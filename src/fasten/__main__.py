import argparse

from readRequirementsFile import ReadRequirementsFile
from checkPackageAvailability import CheckPackageAvailability
from createCallGraph import CreateCallGraph
from receiveCallGraphs import ReceiveCallGraphs
from stitchCallGraph import StitchCallGraph


from fasten.readRequirementsFile import ReadRequirementsFile
from fasten.createCallGraph import CreateCallGraph
from fasten.receiveCallGraphs import ReceiveCallGraphs
from fasten.stitchCallGraph import StitchCallGraph



def main():

    parser = argparse.ArgumentParser(prog='PyPI-plugin')
    parser.add_argument("--product", type=str, help="Package name") # pypiPlugin-test-online
    parser.add_argument("--pkg_name", type=str, help="Package containing the code to be analyzed") # pypiPlugin-test-online
    parser.add_argument("--project_path", type=str, help="Path to package to be analyzed") # /mnt/stuff/projects/work/pypi-plugin/src/fasten/
    parser.add_argument("--timestamp", type=int, help="Timestamp of the package's version") # 42
    parser.add_argument("--version", type=str, help="Version of the product") # 1.0
    parser.add_argument("--requirements", type=str, help="Path to the requirements file") # /mnt/stuff/projects/work/pypi-plugin/requirements.txt
    parser.add_argument("--cg_path", type=str, help="Path where the Call Graphs will be stored")
    parser.add_argument("--scg_path", type=str, help="Path where the Stitched Call Graph will be stored")
    args = parser.parse_args()


    url = 'https://api.fasten-project.eu/api/pypi/' # URL to the FASTEN API
    forge = "local" # Source the product was downloaded from
    max_iter = -1 # Maximum number of iterations through source code (from pycg).
    operation = "call-graph" # or key-error for key error detection on dictionaries (from pycg).
    call_graphs = []

    pkgs = ReadRequirementsFile.readFile(args.requirements) # Read requirements.txt
    pkgs, unknown_pkgs = CheckPackageAvailability.checkPackageAvailability(pkgs, url) # Check if packages are known by FASTEN

# TODO: Enable plugin to receive Call Graphs and metadata information from FASTEN as soon as the pypi-API is ready
#    package = FastenPackage(url, forge, pkg_name, pkg_version)
#    result = package.get_pkg_metadata()
#    print(result)
    call_graphs = ReceiveCallGraphs.receiveCallGraphs(args, pkgs, url)

    call_graphs = CreateCallGraph().createCallGraph(args, forge, max_iter, operation, call_graphs)
#    pathsToCallGraphs = parser.parse_args(call_graphs)

    StitchCallGraph().stitchCallGraph(args, call_graphs)

if __name__ == "__main__":
    main()
