import time
import os
import pypiResolver

class ExecutePypiResolver:

    @staticmethod
    def executePypiResolver(requirementsTxt):
        filename = requirementsTxt+"_pypi_resolved.txt"
        package_list = pypiResolver.run_pip(requirementsTxt, True)

        if os.path.exists(filename):
            os.remove(filename)
            #print("The previous "+filename+" has been deleted successfully")
        #else:
            # print("The file "+filename+" does not exist!")

        for i in package_list[1]:

            packageAndVersion = i[0]+"=="+i[1]+"\n"
            with open(filename, "a") as myfile:
                myfile.write(packageAndVersion)

        if (len(filename)) > 0:
            #print("The new " + filename + " has been created successfully")
            time.sleep(20)
        return filename
