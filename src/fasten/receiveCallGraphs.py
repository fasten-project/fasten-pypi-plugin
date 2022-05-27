# Send package name and version to FASTEN and receive a Call Graph for it.

import re
import json
import time
import requests


class ReceiveCallGraphs:

    @staticmethod
    def receiveCallGraphs(pkgs, url):

        print("Read Call Graphs from FASTEN:")
        pkgs = json.loads(pkgs)
        call_graphs = []
        known_call_graphs = {}
        unknown_call_graphs = {}

        for package in pkgs:

            URL = url + "packages/" + package + "/" + pkgs[package] + "/rcg"
            print(URL)

            try:
                response = requests.get(url=URL)  # get Call Graph for specified package

                if response.status_code == 200:

                    call_graph = response.json()  # save Call Graph as JSON format
                    with open("callGraphs/" + package + ".json", "w") as f:
                        f.write(json.dumps(call_graph))  # save Call Graph in a file

                    call_graphs.append("callGraphs/" + package + ".json")  # append Call Graph file location to list

                    print(package + ":" + pkgs[package] + ": Call Graph received.")
                    known_call_graphs[package] = pkgs[package]

                #                    call_graphs.append(call_graph) # append Call Graph to list
                elif response.status_code == 500:
                    print(package + ":" + pkgs[package] + ": Call Graph not available!")
                    unknown_call_graphs[package] = pkgs[package]
                else:
                    print("something went wrong")

            except requests.exceptions.ReadTimeout:
                print('Connection timeout: ReadTimeout')
            except requests.exceptions.ConnectTimeout:
                print('Connection timeout: ConnectTimeout')
            except requests.exceptions.ConnectionError:
                print('Connection timeout: ConnectError')
                time.sleep(30)

        return call_graphs, known_call_graphs, unknown_call_graphs
