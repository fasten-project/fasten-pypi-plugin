from gitHubAndPyPIParsingUtils import *

'''
* SPDX-FileCopyrightText: 2022 Michele Scarlato <michele.scarlato@endocode.com>
*
* SPDX-License-Identifier: Apache-2.0
'''

class ReceiveLocallyLicensesInformation:

    @staticmethod
    # add the source (e.g. GitHub or PyPI) to the dict!
    def receiveLocallyLicensesInformation(package_list, LCVurl, i):
#        print("Retrieval of license information:")
        licenses = {}
        for package in package_list:
            licenses[i] = {}
            licenses[i]['packageName'] = package['name']
            licenses[i]['packageVersion'] = package['version']
            if package['name'] and package['version'] is not None:
                PyPILicense, PyPILicenseSPDX, jsonResponse = retrieveLicenseInformationFromPyPI(package['name'], package['version'], LCVurl)
                if len(PyPILicense) > 0:
                    licenses[i]['PyPILicense'] = PyPILicense
                if len(PyPILicenseSPDX) > 0:
                    licenses[i]['PyPILicenseSPDX'] = PyPILicenseSPDX
                print(package['name'])
                print(package['version'])
                GitHubURL = retrieveGitHubUrl(jsonResponse, package['name'])
                if GitHubURL is not None:
                    if len(GitHubURL) > 0:
                        GitHubAPIurl = RetrieveGitHubAPIurl(GitHubURL)
                        if len(GitHubAPIurl) > 0:
        #                    print(GitHubAPIurl)
                            GitHubLicense, GitHubLicenseSPDX = RetrieveLicenseFromGitHub(GitHubAPIurl, LCVurl)
                            if GitHubLicense != "":
                                if GitHubLicense is not None:
                                    licenses[i]['GitHubLicense'] = GitHubLicense
                            if GitHubLicenseSPDX != "":
                                if GitHubLicenseSPDX is not None:
                                    licenses[i]['GitHubLicenseSPDX'] = GitHubLicenseSPDX
            i += 1
        return licenses
