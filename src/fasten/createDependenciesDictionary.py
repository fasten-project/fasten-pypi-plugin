import json
import requests


'''
* SPDX-FileCopyrightText: 2022 Michele Scarlato <michele.scarlato@endocode.com>
*
* SPDX-License-Identifier: Apache-2.0
'''

class CreateDependenciesDictionary:
    @staticmethod
    def createDependenciesDictionary(package_list):
        PyPIDependencyList = {}
        for package in package_list:
            packageName = package["name"]
            packageVersion = package["version"]
            URL = "https://pypi.org/" + "pypi/" + str(packageName) + "/" + str(packageVersion) + "/json"
            try:
                response = requests.get(url=URL)  # get Call Graph or metadata for specified package

                if response.status_code == 200:
                    jsonResponse = response.json()  # save in JSON format
                    PyPIDependencyList[packageName] = {}
                    PyPIDependencyList[packageName] = (jsonResponse["info"]["requires_dist"])
            except requests.exceptions.ReadTimeout:
                print('Connection timeout: ReadTimeout')
            except requests.exceptions.ConnectTimeout:
                print('Connection timeout: ConnectTimeout')
            except requests.exceptions.ConnectionError:
                print('Connection timeout: ConnectError')
        return PyPIDependencyList
