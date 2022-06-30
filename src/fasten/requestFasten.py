# Send package name and version to FASTEN and receive a Call Graph or metadata information for it.

import json
import time
import requests

class RequestFasten:

    @staticmethod
    def requestFasten(args, pkgs, url, path):

        if path == "rcg":
            print("Receive Call Graph from FASTEN:")
        if path == "vulnerabilities":
            print("Receive vulnerabilities from FASTEN:")

        pkgs = json.loads(pkgs)
        metadata_JSON_File_Locations = [] # Call Graphs and metadata file location
        cg_pkgs = { }
        vul_pkgs = { }

        for package in pkgs:

            URL = url + "packages/" + package + "/" + pkgs[package] + "/" + path

            try:
                response = requests.get(url=URL) # get Call Graph or metadata for specified package

                if response.status_code == 200:

                    metadata_JSON = response.json() # save in JSON format

                    if metadata_JSON:
                        if path == "rcg":
                            cg_pkgs[package] = pkgs[package]
                        if path == "vulnerabilities":
                            vul_pkgs[package] = pkgs[package]

                        with open(args.fasten_data + package + "." + path + ".json", "w") as f:
                            f.write(json.dumps(metadata_JSON)) # save Call Graph or metadata in a file

                        metadata_JSON_File_Locations.append(args.fasten_data + package + "." + path + ".json") # append Call Graph or metadata file location to a list

                        print(package + ":" + pkgs[package] + ": " + path + " received.")

#                    else:
#                        print("Vulnerabilities are empty!")

                elif response.status_code == 500:
                    print(package + ":" + pkgs[package] + ": " + path + " not available!")
                else:
                    print("Something went wrong for the package " + package + ":" + pkgs[package] + " on the server side!")

            except requests.exceptions.ReadTimeout:
                print('Connection timeout: ReadTimeout')
            except requests.exceptions.ConnectTimeout:
                print('Connection timeout: ConnectTimeout')
            except requests.exceptions.ConnectionError:
                print('Connection timeout: ConnectError')

        if path == "rcg":
            return metadata_JSON_File_Locations, cg_pkgs
        if path == "vulnerabilities":
            return metadata_JSON_File_Locations, vul_pkgs
