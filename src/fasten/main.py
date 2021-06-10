import sys
from fasten import FastenPackage


class main:

    url = 'http://127.0.0.1:9002'
    forge = sys.argv[1]
    pkg_name = sys.argv[2]
    pkg_version = sys.argv[3]

    package = FastenPackage(url, forge, pkg_name, pkg_version)

    result = package.get_pkg_metadata()
    print(result)
