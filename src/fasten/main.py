import sys
from readRequirementsFile import ReadRequirementsFile
from createCallGraph import CreateCallGraph
from sendPackages import SendPackages
from fasten import FastenPackage


class Main:

    url = 'http://127.0.0.1:9002'
#    forge = sys.argv[1] # mvn
#    pkg_name = sys.argv[2] # namesss
#    pkg_version = sys.argv[3] # 0.1.0
    product = "fasten-pypi-plugin" # Package name
    forge = "local" # Source the product was downloaded from
    pkg_name = "fasten-pypi-plugin" # Package containing the code to be analyzed
    version = "1.0" # Version of the product
    timestamp = "42" # Timestamp of the package's version
    pathToFile = '../../requirements.txt' # 'fasten-pypi-plugin/requirements.txt'
    packages = ReadRequirementsFile(pathToFile)
    pkgs= packages.readFile() # read requirements.txt
#    package = FastenPackage(url, forge, pkg_name, pkg_version)
#    result = package.get_pkg_metadata()
#    print(result)
    SendPackages.sendPackages(pkgs)


    print("Create Call Graph for current project")

    CreateCallGraph().createCallGraph(pkg_name, product, forge, version, timestamp)
