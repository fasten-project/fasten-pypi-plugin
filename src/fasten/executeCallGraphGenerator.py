from pycg_producer.producer import CallGraphGenerator
import time
import os.path
import shutil

'''
* SPDX-FileCopyrightText: 2022 Michele Scarlato <michele.scarlato@endocode.com>
*
* SPDX-License-Identifier: Apache-2.0
'''

def deleteCallGraphsDir(CallGraphsDirLocal):
    if os.path.exists(CallGraphsDirLocal):
        shutil.rmtree(CallGraphsDirLocal)
        print("The directory " + CallGraphsDirLocal + " has been deleted successfully")
        time.sleep(10)
    else:
        print("The directory " + CallGraphsDirLocal + " does not exist!")

def executeCallGraphGenerator(unknown_call_graphs, callGraphFastenPath):
    CallGraphsDirLocal = "cg_sources_dir"

    isExist = os.path.exists(CallGraphsDirLocal)
    if isExist:
        shutil.rmtree(CallGraphsDirLocal)

    global CallGraphPaths
    CallGraphPaths = []
    for key in unknown_call_graphs:
        #print(key, unknown_call_graphs[key])
        packageName = key
        packageVersion = unknown_call_graphs[key]

        coord = { "product": ""+packageName+"",
              "version": ""+packageVersion+"",
              "version_timestamp": "2000",
              "requires_dist": []}

        CallGraphPathLocal = CallGraphsDirLocal + "/" + "callgraphs"+ "/" + packageName[0] + "/" + packageName + "/" + packageVersion + "/" + "cg.json"
        executeSingleCallGraphGeneration(coord, packageName, packageVersion, CallGraphsDirLocal, CallGraphPathLocal, callGraphFastenPath)
    return CallGraphPaths


def executeSingleCallGraphGeneration(coord, packageName, packageVersion, directoryName, CallGraphPathLocal,callGraphFastenPath):

    generator = CallGraphGenerator(directoryName, coord)
    # wait for the call graph to be generated
    #print("Waiting for call graph generation at: ")
    #print(CallGraphPathLocal)
    timer = 1
    global CallGraphPaths
    CallGraphPaths = []
    while not os.path.exists(CallGraphPathLocal):
        time.sleep(1)
        timer += 1
        if timer > 60:
            print("" + str(timer) + " seconds without call graph generation passed.")
            # print the status
            dict = generator.generate()
            print(dict.get("Status"))
            #print(dict)
            #print(generator.generate())
            break
    if os.path.isfile(CallGraphPathLocal):
        print("Call graph generated at: "+CallGraphPathLocal)
        CallGraphPathLocalRenamed = CallGraphPathLocal.replace("cg.json", packageName+"-"+packageVersion+".json")
        os.rename(CallGraphPathLocal, CallGraphPathLocalRenamed)
        shutil.copy(CallGraphPathLocalRenamed, callGraphFastenPath )
        CallGraphPaths.append(callGraphFastenPath+"/"+packageName+"-"+packageVersion+".json")
        pass
    else:
        print("%s has not been generated!" % CallGraphPathLocal)