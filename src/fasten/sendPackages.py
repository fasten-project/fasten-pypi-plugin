# Send package name and version to FASTEN and receive Call Graph for it

import json
import time
import requests

class SendPackages:

    @staticmethod
    def sendPackages(pkgs, url):

        print("In function sendPackages:")
        pkgs = json.loads(pkgs)

        for package in pkgs:

            URL = url + "/mvn/packages/" + package + "/" + pkgs[package] + "/callgraph"

            try:
                response = requests.get(url=URL) # Get Call Graph for specified package
                cg = response.json() # save Call Graph as JSON format

                print(cg)

                if response.status_code == 500:
                    print("Call Graph for package " + package + " not available!")
                elif response.status_code != 200:
                    print("Something went wrong")

            except requests.exceptions.ReadTimeout:
                print('Connection timeout: ReadTimeout')
            except requests.exceptions.ConnectTimeout:
                print('Connection timeout: ConnectTimeout')
            except requests.exceptions.ConnectionError:
                print('Connection timeout: ConnectError')
                time.sleep(30)
