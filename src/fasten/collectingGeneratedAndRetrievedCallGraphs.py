from executeCallGraphGenerator import executeCallGraphGenerator, deleteCallGraphsDir
from requestFastenKnownAndUnknownLists import RequestFastenKnownAndUnknownLists
from os import listdir
from os.path import isfile, join

'''
* SPDX-FileCopyrightText: 2022 Michele Scarlato <michele.scarlato@endocode.com>
*
* SPDX-License-Identifier: Apache-2.0
'''

def collectingGeneratedAndRetrievedCallGraphs(args, all_pkgs, url):

    CallGraphsDirLocal = "cg_producing"
    deleteCallGraphsDir(CallGraphsDirLocal)
    print("CALL GRAPHS Retrieval:")
    ReceivedCallGraphsLocation, known_call_graphs, unknown_call_graphs, call_graphs_connectivity_issues = RequestFastenKnownAndUnknownLists.requestFastenKnownAndUnknownLists(args, all_pkgs, url, "rcg")
    unknown_call_graphs_and_connectivity_issues = {**unknown_call_graphs, **call_graphs_connectivity_issues}
    GeneratedCallGraphPaths_broken = executeCallGraphGenerator(unknown_call_graphs_and_connectivity_issues, args.fasten_data)#,CallGraphsDirLocal)
    # merging lists of retrieved and generated call graphs location

    cg_path = args.fasten_data
    GeneratedCallGraphPaths = [f for f in listdir(cg_path) if isfile(join(cg_path, f))]
    GeneratedCallGraphPaths_mod = []
    for cg in GeneratedCallGraphPaths:
        cg = cg_path + "/" + cg
        GeneratedCallGraphPaths_mod.append(cg)
    CallGraphsList = GeneratedCallGraphPaths_mod + ReceivedCallGraphsLocation
    return CallGraphsList
