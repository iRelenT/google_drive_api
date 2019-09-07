import os
import ast

# POSSIBLE IMPROVAL #################################################
# - instead of writing to file with strings use json.dump(), therefore we can read from file and store into list
#   only with json.load()
# - you can get rid of ast.literal.eval then
#####################################################################

#sadasdasdsadsa
# contains dictionary with path and infos
foldersList = []


# add new path(s) to the list
# add aditional infos for each path!
def addPath():
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
            foldersList.append(dict)
        else:
            print("Not a path! Try again")
            pathAmount += 1
        i += 1
    createFileFromList()

# return the amount of paths, so the main program only works if fileSize > 0
def getFoldersList():
    createListFromfile()
    return foldersList if len(foldersList) > 0 else []

# adds new path(s) to the folders.txt file
def createFileFromList():
    file = open(getConfFile(), "a")
    for i in range(len(foldersList)):
        file.write(str(foldersList[i]) + "?\n")
    file.close()

# gets the path(s) from the folders.txt, converts them to dict and adds path(s) to the foldersList list
# returns the list
def createListFromfile():
    if os.path.getsize(getConfFile()) > 0:
        file = open(getConfFile(), "r")
        list = file.read()

        while(True):
                # Better ---> foldersList = [entrys for entrys in list.split(",")]
                endIndex = list.find("?")
                if endIndex != -1:
                    nextPath = list[:endIndex]
                    list = list[endIndex + 1:]
                    foldersList.append(nextPath)
                else:
                    break
        # converts from string to dict! idea: https://stackoverflow.com/questions/48828586/create-dict-from-string-in-python/48828669#48828669
        # possible solutions:
        #   - could've picked each key - value pair and put it to a new dict and add it after
        #   - make it a one liner
        for i in range(len(foldersList)):
            content = foldersList[i]
            foldersList[i] = ast.literal_eval(content)
    else:
        print("No paths found! Add paths? [Y/N]")
        choice = input()
        if choice is "y" or choice is "Y":
            addPath()
        else:
            print("No paths added!")
# delete path_conf.txt to turn off synchronization of the folders
def deleteConfFile():
    pass

# searches for the path_conf.txt file
def getConfFile():
    path = ""
    for root,dirs,files in os.walk(os.getcwd()):
        for file in files:
            if file == "path_conf.txt":
                path = os.path.join(root,file)
                return path
# if PathStorage.py is used from the terminal
if __name__ == '__main__':
    pass
