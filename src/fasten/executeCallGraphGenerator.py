import os.path
from pycg_producer.producer import CallGraphGenerator

'''
* SPDX-FileCopyrightText: 2022 Michele Scarlato <michele.scarlato@endocode.com>
*
* SPDX-License-Identifier: Apache-2.0
'''

def executeCallGraphGenerator(args, package_list):
    """Create dictonary necessary for 'CallGraphGenerator'."""

    for pkg in package_list:

        if pkg["cg_file"] is None:
            coord = { "product": ""+pkg["name"]+"",
                      "version": ""+pkg["version"]+"",
                      "version_timestamp": "2000",
                      "requires_dist": [] }
            cg_path = args.fasten_data + "callgraphs"+ "/" + pkg["name"][0] + "/" + pkg["name"] + "/" + pkg["version"] + "/cg.json"
            pkg["cg_file"] = executeSingleCallGraphGeneration(args.fasten_data, coord, cg_path)

    return package_list


def executeSingleCallGraphGeneration(fasten_data, coord, cg_path):
    """Create Call Graph for a single package."""

    generator = CallGraphGenerator(fasten_data, coord)
    generator.generate()

    if os.path.isfile(cg_path):
        print(f"Call graph generated at: {cg_path}")
        return cg_path
    else:
        print(f"{cg_path} has not been generated!")
        return None
