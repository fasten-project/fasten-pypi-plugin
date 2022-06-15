from executeCallGraphGenerator import executeCallGraphGenerator, deleteCallGraphsDir
from requestFastenKnownAndUnknownLists import RequestFastenKnownAndUnknownLists
def collectingGeneratedAndRetrievedCallGraphs(args, all_pkgs, url):

    CallGraphsDirLocal = "cg_producing"
    deleteCallGraphsDir(CallGraphsDirLocal)
    print("CALL GRAPHS Retrieval:")
    ReceivedCallGraphsLocation, known_call_graphs, unknown_call_graphs, call_graphs_connectivity_issues = RequestFastenKnownAndUnknownLists.requestFastenKnownAndUnknownLists(args, all_pkgs, url, "rcg")
    unknown_call_graphs_and_connectivity_issues = {**unknown_call_graphs, **call_graphs_connectivity_issues}
    GeneratedCallGraphPaths = executeCallGraphGenerator(unknown_call_graphs_and_connectivity_issues, args.fasten_data)#,CallGraphsDirLocal)
    # merging lists of retrieved and generated call graphs location
    CallGraphsList = GeneratedCallGraphPaths + ReceivedCallGraphsLocation
    return CallGraphsList
