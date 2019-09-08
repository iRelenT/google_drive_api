from __future__ import print_function
import Auth as auth
from PathStorage import *
from FileMetadata import *

class Main():
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.control()

    def control(self):
        # objects
        authentication = auth.Auth(self.SCOPES)
        creds = authentication.checkCredentials()
        pathStorage = PathStorage()
        # ---------------------------------------

        message = "[OPTIONS]:\n'-add' for adding a path to config file\n'-del' for deleting config file\n" \
                  "'-up' for uploading all synch_folders from config file\n'-ex' for exit program\n"
        choice = input(message)
        while(choice != "-ex"):
            if choice == "-add":
                pathStorage.addPath()
            elif choice == "-del":
                pathStorage.deleteConfFile()
            elif choice == "-up":
                fileMetadata = FileMetadata(creds)
                fileMetadata.prepareFiles(pathStorage.getFoldersList())
            choice = input(message)
if __name__ == '__main__':
    Main()