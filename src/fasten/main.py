import argparse
import sys
from readRequirementsFile import ReadRequirementsFile
from createCallGraph import CreateCallGraph
from sendPackages import SendPackages
from stitchCallGraph import StitchCallGraph
from fasten import FastenPackage


class Main:

    parser = argparse.ArgumentParser()
    parser.add_argument("call_graph", nargs="*",help="Some path")
    url = 'http://127.0.0.1:9002'
#    forge = sys.argv[1] # mvn
#    pkg_name = sys.argv[2] # namesss
#    pkg_version = sys.argv[3] # 0.1.0
    product = "fasten-pypi-plugin" # Package name
    forge = "local" # Source the product was downloaded from
    pkg_name = "fasten-pypi-plugin" # Package containing the code to be analyzed
    version = "1.0" # Version of the product
    timestamp = "42" # Timestamp of the package's version
    pathToFile = '../../requirements.txt' # 'fasten-pypi-plugin/requirements.txt'
    packages = ReadRequirementsFile(pathToFile)
    pkgs= packages.readFile() # read requirements.txt
#    package = FastenPackage(url, forge, pkg_name, pkg_version)
#    result = package.get_pkg_metadata()
#    print(result)
    call_graphs = SendPackages.sendPackages(pkgs, url)
    pathsToCallGraphs = parser.parse_args(call_graphs)

    print(pathsToCallGraphs)

    CreateCallGraph().createCallGraph(pkg_name, product, forge, version, timestamp)

    StitchCallGraph().stitchCallGraph(pathsToCallGraphs.call_graph)
