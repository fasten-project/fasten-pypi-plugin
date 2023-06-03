import argparse
import os
import shutil
from createDirectory import CreateDirectory
from executePypiResolver import ExecutePypiResolver
from savePackageInformation import SavePackageInformation
from executeCallGraphGenerator import executeCallGraphGenerator
from createCallGraph import CreateCallGraph
from stitchCallGraphs import StitchCallGraphs
from findEntrypoints import FindEntrypoints
from createAdjacencyList import CreateAdjacencyList
from depthFirstSearch import DepthFirstSearch
from optimizeStitchedCallGraph import OptimizeStitchedCallGraph
from enrichOSCG import EnrichOSCG
from licensesAnalysis import licensesAnalysis
from vulnerabilityAnalysis import VulnerabilityAnalysis
from reportToPDF import ReportToPDF


def main():

    parser = argparse.ArgumentParser(prog='PyPI-plugin')
    parser.add_argument("--product", type=str, help="Package name")
    parser.add_argument("--pkg_name", type=str, help="Package containing the code to be analyzed")
    parser.add_argument("--project_path", type=str, help="Path to package to be analyzed")
    parser.add_argument("--timestamp", type=int, help="Timestamp of the package's version")
    parser.add_argument("--version", type=str, help="Version of the product")
    parser.add_argument("--requirements", type=str, help="Path to the requirements file")
    parser.add_argument("--fasten_data", type=str, help="Path to the folder where the received FASTEN data will be stored")
    parser.add_argument("--scg_path", type=str, help="Path to the folder where the Stitched Call Graph will be stored")
    parser.add_argument("--spdx_license", type=str, help="SPDX id of the license declared for this project")
    args = parser.parse_args()

    url = 'https://api.fasten-project.eu/api/pypi/' # URL to the FASTEN API
    LCVurl = 'http://0.0.0.0:3251/'#'https://lima.ewi.tudelft.nl/lcv/'
    package_list = [ ] # Storage for package dictionaries.
    cg_location_list = [ ] # Storage for the location of the Call Graphs.
    local_package = {   "name": args.product,
                        "version": args.version,
                        "cg_file": None,
                        "callables": None,
                        "metadata": None,
                        "vulnerabilities": None,
                        "license": args.spdx_license
                    }
    report = ""

    dirs_to_delete = [args.fasten_data, args.scg_path ]
    for dir in dirs_to_delete :
        isExist = os.path.exists(dir)
        if isExist:
            shutil.rmtree(dir)


#   Create directories to store the Call Graphs and the Stitched Call Graph
    CreateDirectory.createDirectory(args.fasten_data)
    CreateDirectory.createDirectory(args.scg_path)
    #cg_file = CreateCallGraph().createCallGraph(args)
    #local_package["cg_file"] = cg_file
    #cg_location_list.append(cg_file)
    package_list = ExecutePypiResolver.executePypiResolver(args.requirements, package_list)
    '''
    package_list = SavePackageInformation.savePackageInformation(args.fasten_data, url, package_list)
    
    package_list, cg_location_list = executeCallGraphGenerator(args, package_list, cg_location_list)
    stitched_call_graph = StitchCallGraphs().stitchCallGraphs(args, cg_location_list)

    entry_points = FindEntrypoints.findEntrypoints(args, stitched_call_graph)

    adjList = CreateAdjacencyList
    adjList.createAdjacencyList(stitched_call_graph)
    list_of_nodes = [False] * adjList.getNodes()

    # Run a depth first search for each entry point to create a list of all called nodes.
    for x in entry_points:
        list_of_nodes = DepthFirstSearch.depthFirstSearch(adjList, int(x), list_of_nodes)


    oscg = OptimizeStitchedCallGraph.optimizeStitchedCallGraph(args, stitched_call_graph, list_of_nodes)
    EnrichOSCG.enrichOSCG(args, oscg, package_list)
    '''
#   Create report
    #report = VulnerabilityAnalysis.vulnerabilityAnalysis(package_list)
    report = licensesAnalysis(args, package_list, url, LCVurl)#, oscg)
    print(report)
    ReportToPDF.reportToPDF(report,args.product)

if __name__ == "__main__":
    main()
