import sys
from readRequirementsFile import ReadRequirementsFile
from fasten import FastenPackage


class main:

    url = 'http://127.0.0.1:9002'
    forge = sys.argv[1] # mvn
    pkg_name = sys.argv[2] # namesss
    pkg_version = sys.argv[3] # 0.1.0
    pathToFile = '../../requirements.txt'
    packages = ReadRequirementsFile(pathToFile)
    packages.readFile()
    package = FastenPackage(url, forge, pkg_name, pkg_version)

    result = package.get_pkg_metadata()
    print(result)
