from pycg_producer.producer import CallGraphGenerator
import time
import os.path
import shutil

def deleteCallGraphsDir(CallGraphsDirLocal):
    if os.path.exists(CallGraphsDirLocal):
        shutil.rmtree(CallGraphsDirLocal)
        print("The directory " + CallGraphsDirLocal + " has been deleted successfully")
        time.sleep(10)
    else:
        print("The directory " + CallGraphsDirLocal + " does not exist!")

def executeCallGraphGenerator(unknown_call_graphs):
    CallGraphsDirLocal = "directoryName"
    for key in unknown_call_graphs:
        print(key, unknown_call_graphs[key])
        packageName = key
        packageVersion = unknown_call_graphs[key]

        coord = { "product": ""+packageName+"",
              "version": ""+packageVersion+"",
              "version_timestamp": "2000",
              "requires_dist": []}

        CallGraphPathLocal = CallGraphsDirLocal + "/" + "callgraphs"+ "/" + packageName[0] + "/" + packageName + "/" + packageVersion + "/" + "cg.json"
        executeSingleCallGraphGeneration(coord, packageName, packageVersion, CallGraphsDirLocal, CallGraphPathLocal)



def executeSingleCallGraphGeneration(coord, packageName, packageVersion, directoryName, CallGraphPathLocal):

    generator = CallGraphGenerator(directoryName, coord)
    print(generator.generate())
    # wait for the call graph to be generated
    print("Waiting for call graph generation at: ")
    print(CallGraphPathLocal)
    while not os.path.exists(CallGraphPathLocal):
        time.sleep(1)
    if os.path.isfile(CallGraphPathLocal):
        print("Call graph generated at: "+CallGraphPathLocal)
        pass
    else:
        raise ValueError("%s isn't a file!" % CallGraphPathLocal)
    #time.sleep(300)

