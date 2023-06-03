import json
from retrieveLicenseInformation import retrieveLicenseInformation
from retrieveLocallyLicensesInformation import ReceiveLocallyLicensesInformation
from licenseComplianceVerification import generateInboundLicenses, licenseComplianceVerification, parseLCVAssessmentResponse, transitiveLicenseComplianceVerification, parseLCVTransitiveAssessmentResponse, parseLicenseDeclared#, provideReport
from licensesApplicationToTheStitchedCallGraph import licensesAtThePackageLevelApplicationToTheStitchedCallGraph, licensesAtTheFileLevelApplicationToTheStitchedCallGraph, LCVAssessmentAtTheFileLevel, LCVAssessmentAtTheFileLevelGenerateReport, CompareLicensesAtThePackageLevelWithTheFileLevel
from createDependenciesDictionary import CreateDependenciesDictionary
'''
* SPDX-FileCopyrightText: 2022 Michele Scarlato <michele.scarlato@endocode.com>
*
* SPDX-License-Identifier: Apache-2.0
'''

def licensesAnalysis(args, package_list, url, LCVurl):#, oscg):

    print("Start license analysis...")
    #commented to skip FASTEN queries
    #licenses_retrieved_from_fasten, licenses_retrieved_locally, licenses_retrieved_at_the_file_level = retrieveLicenseInformation(args, package_list, url, LCVurl)

    # added to skip FASTEN queries
    index = 0

    licenses_retrieved = ReceiveLocallyLicensesInformation.receiveLocallyLicensesInformation(package_list,LCVurl, index)
    #licenses_retrieved = {**licenses_retrieved_from_fasten, **licenses_retrieved_locally}
    #print(licenses_retrieved)
    inbound_licenses = generateInboundLicenses(licenses_retrieved)
    outbound_license = args.spdx_license
    lcv_assessment_response = licenseComplianceVerification(inbound_licenses, outbound_license, LCVurl)
    lcv_transitive_assessment_response = transitiveLicenseComplianceVerification(inbound_licenses, LCVurl)
    #print("lcv_transitive_assessment_response")
    #print(lcv_transitive_assessment_response)
    transitive_license_report = parseLCVTransitiveAssessmentResponse(lcv_transitive_assessment_response, licenses_retrieved)
    #print(transitive_license_report)
    dependenciesDictionary = CreateDependenciesDictionary.createDependenciesDictionary(package_list)
    #print("dependenciesDictionary")
    #print(dependenciesDictionary)
    #print("\n\n")
    license_report = parseLCVAssessmentResponse(lcv_assessment_response, licenses_retrieved)

    #print("licenses_retrieved")
    # this list should be parsed against the supported licenses present in the Compatibility Matrix and provide the user with
    # this answer in the report.
    #print(licenses_retrieved)
    license_declared_report = parseLicenseDeclared(licenses_retrieved)

    full_report = "Report about licenses:\n"
    notCompatibleWithOutboundLicense = 0
    if len(license_report) > 0:
        #print("License violation found at the package level: " +str(len(license_report)) + " ." )
        for i in license_report:
            if "noLicensesIssues" in license_report[i]:
                notCompatibleWithOutboundLicense = 1
                full_report += license_report[i]["noLicensesIssues"]
            else:
                full_report += "\n\n############# - License violation against the declared Outbound license, number " + str(i + 1) + " #################\n" + "\n" + str(license_report[i]["packageInformation"]) + "\n" + str(license_report[i]["licenseViolation"]) + "\n"
    if len(transitive_license_report) > 0:
        #print("License violation found at the package level: " +str(len(license_report)) + " ." )
        '''
        if notCompatibleWithOutboundLicense > 0:
            full_report += "\n\n############# -Since the project has license violations, the possible alternative outbound licenses: #############\n"
        else:
            full_report += "\n\n############# -The project is license compliant, anyway, possible alternative outbound licenses are: #############\n"
        for i in transitive_license_report:
            full_report += i'''
    #if len(transitive_license_report) == 0:
        #full_report += "\n\n############# PyPI plugin couldn't detect any possible outbound license preventing the violation. #############\n"
    full_report += "\n\n############# - Licenses considered for the compliance verification: ############# \n"
    #print(license_declared_report)
    for i in license_declared_report:
        if "License declared" in license_declared_report[i]:
            full_report += license_declared_report[i]["License declared"]+"\n"

            #print(license_declared_report[i].get("License declared"))

    '''
    # commented to perform only license detection at the package level, without querying FASTEN KB 
    callablesEnrichedWithLicenseInformation = licensesAtThePackageLevelApplicationToTheStitchedCallGraph(oscg, licenses_retrieved)
    
    
    callablesEnrichedWithLicenseAtTheFileLevel = licensesAtTheFileLevelApplicationToTheStitchedCallGraph(licenses_retrieved_at_the_file_level, oscg)

    callablesWithLicenseViolationParsed = LCVAssessmentAtTheFileLevel(callablesEnrichedWithLicenseAtTheFileLevel, outbound_license, LCVurl)

    LCVAssessmentAtTheFileLevelReport = LCVAssessmentAtTheFileLevelGenerateReport(callablesWithLicenseViolationParsed)

    if len(LCVAssessmentAtTheFileLevelReport) > 0:
        full_report += "License compliance assessment at the file level:\n"
        for i in LCVAssessmentAtTheFileLevelReport:
            full_report += i + "\n"
    else:
        full_report += "\nThe license compliance assessment at the file level doesn't detect licenses issues.\n"

    ReportLicensesPackageComparedWithFile = CompareLicensesAtThePackageLevelWithTheFileLevel(licenses_retrieved, licenses_retrieved_at_the_file_level)

    if len(ReportLicensesPackageComparedWithFile) > 0:
        full_report += "\nReport upon incompatible licenses: scancode detected file licenses compared with the license declared at the package level:\n" + ReportLicensesPackageComparedWithFile + "\n"
    else:
        full_report += "\nThe report upon incompatible licenses between files and packages didn't show incompatibilities."

    print("License analysis done.")
    '''
    return full_report
