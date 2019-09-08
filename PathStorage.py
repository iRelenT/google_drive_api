import os
import json

class PathStorage:
    def init(self):
        # contains dictionary with path and infos
        self.FOLDERSLIST = []


    # add new path(s) to the list
    # add aditional infos for each path!
    def addPath(self):
        pathAmount = input("How many paths do you want to add? Amount: ")
        pathAmount = int(pathAmount)
        i = 1
        while i <= pathAmount:
            path = input("Enter Path here: ")
            if os.path.isdir(path) is True:
                content = input(
                    "Enter info: [CONTENT = example: programming working dir,game pictures] Seperate by comma if multiple options!"
                    "\nContent: ")
                excludeFile = input(
                    "Enter info: [EXCLUDE FILE = example: file1.py,file2.txt] Seperate by comma if multiple options!"
                    "\nEXCLUDE FILE: ")

                excludeFolder = input(
                    "Enter info: [EXCLUDE = example: pictures,documents] Seperate by comma if multiple options!"
                    "\nEXCLUDE FOLDER: ")
                dict = {}
                dict["path"] = path
                dict["content"] = content
                dict["excludeFile"] = excludeFile
                dict["excludeFolder"] = excludeFolder
                self.FOLDERSLIST.append(dict)
            else:
                print("Not a path! Want to add another? [Y/N]\n")
                choice = input()
                if choice is "y" or choice is "Y":
                    pathAmount += 1
            i += 1
        self.createFileFromList()

    # return the amount of paths, so the main program only works if fileSize > 0
    def getFoldersList(self):
        self.createListFromfile()
        return self.FOLDERSLIST if len(self.FOLDERSLIST) > 0 else []

    # adds new path(s) to the folders.txt file
    def createFileFromList(self):
        currDicts = []
        if os.path.getsize(self.getConfFile()) > 0:
            with open(self.getConfFile(),"r") as file:
                currDicts = list(json.load(file))
        for entrys in self.FOLDERSLIST:
            currDicts.append(entrys)
        with open(self.getConfFile(),"w") as file:
            json.dump(currDicts,file)


    # gets the path(s) from the path_conf.txt, json reads the file
    def createListFromfile(self):
        if os.path.getsize(self.getConfFile()) > 0:
            with open(self.getConfFile(),"r") as file:
                 self.FOLDERSLIST = list(json.load(file))
        else:
            print("No paths found! Add paths? [Y/N]")
            choice = input()
            if choice is "y" or choice is "Y":
                self.addPath()
            else:
                print("No paths added!")
    # delete path_conf.txt to turn off synchronization of the folders
    def deleteConfFile(self):
        pass

    # searches for the path_conf.txt file
    def getConfFile(self):
        path = ""
        for root,dirs,files in os.walk(os.getcwd()):
            for file in files:
                if file == "path_conf.txt":
                    path = os.path.join(root,file)
                    return path

