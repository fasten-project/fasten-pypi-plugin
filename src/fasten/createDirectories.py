import os

class CreateDirectories:

    @staticmethod
    # Check whether the specified path exists or not
    def DirectoryCheck(cg_path, scg_path):
        dirs_to_check = [cg_path,scg_path]

        for directory in dirs_to_check:
            isExist = os.path.exists(directory)
            if not isExist:
              os.makedirs(directory)
              print("The directory '"+directory+"' was not existent and has been created!")
        return
