# Send package name and version to FASTEN and receive Call Graph for it
import json

class SendPackages:

    @staticmethod
    def sendPackages(pkgs):

        print("In function sendPackages:")
        pkgs = json.loads(pkgs)

        for package in pkgs:
            print(package + " " + pkgs[package])
