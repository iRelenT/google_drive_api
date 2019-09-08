import os
from ApiInterface import *

#FIRSTRUNFILE = True
#FIRSTRUNFOLDER = True

class FileMetadata():
    EXCLUDEDFILES = []
    EXCLUDEDFOLDERS = []

    finishedMetadataFile = []
    finishedMetadataFolder = []
    def __init__(self,creds):
        self.interface = ApiInterface(creds)

    def prepareFiles(self,pathFile):

        list = pathFile

        # whole folders one by one
        for synch_folders in list:
            rootPath = synch_folders['path']

            # get the excluded files/folders and the content of the  which might be seperated by comma
            EXCLUDEDFOLDERS = [folder for folder in str(synch_folders['excludeFolder']).split(",")]
            EXCLUDEDFILES = [file for file in str(synch_folders['excludeFile']).split(",")]
            content = [content for content in str(synch_folders['content']).split(",")]


            metadata = self.createMetadata(rootPath,type="folder")
            newId  = self.interface.uploadToDrive(metadata,type="folder")
            self.finishedMetadataFolder.append(metadata)
            self.walkThree(rootPath,newId)

    def walkThree(self,source ,rootId):
        rootPath = source
        wholeDir = os.listdir(rootPath)


        # split the directory in files/folders

        # only names, without path
        folders = []
        # only names, without path
        files = []
        path = ""
        for x in wholeDir:
            path = rootPath + "/" + x
            if os.path.isfile(path) == True:
                files.append(x)
            else:
                folders.append(x)
            path = rootPath


        for file in files:
            #if FIRSTRUNFILE:
            #    if file in EXCLUDEDFILES:
            #        FIRSTRUNFILE = False
            #        continue


            #metadata = self.createMetadata(rootPath + "/" + file,type="file",id=id)
            #self.interface.uploadToDrive(metadata,type="file")
            #self.finishedMetadataFile.append(metadata)
            pass

        for folder in folders:
            #if FIRSTRUNFOLDER:
            #    if file in EXCLUDEDFOLDERS:
            #        FIRSTRUNFOLDER = False
            #       continue

            metadata = self.createMetadata(rootPath + "/" + folder,type="folder",id=rootId)
            self.finishedMetadataFolder.append(metadata)
            newId = self.interface.uploadToDrive(metadata,type="folder")
            self.walkThree(rootPath + "/" + folder,newId)


    def createMetadata(self,path,type,id = ""):
        metadata = {}

        if type == "folder":
            metadata['name'] = str(path).rsplit("/")[-1]
            metadata['mimeType'] = self.getSpecificMime(type = "folder")
            # for the root Folder there will be no parents Id provided! check default id value in func def!
            if id != "": metadata['parents'] = [id]
            return metadata
        elif type == "file":
            # /home/-file.py-    ->    file.py
            fileName = str(path).rsplit("/")[-1]
            metadata['name'] = fileName
            metadata['mimeType'] = self.getSpecificMime(type="file",extension=fileName.rsplit(".")[-1])
            metadata['parents'] = [id]
            return metadata


    def getSpecificMime(self,type,extension=""):
        if type == "folder":
            return "application/vnd.google-apps.folder"
        else:
            mimeTypes = {
                "xls" : 'application/vnd.ms-excel',
                "xlsx" : 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                "xml" : 'text/xml',
                "ods" : 'application/vnd.oasis.opendocument.spreadsheet',
                "csv" : 'text/plain',
                "tmpl" : 'text/plain',
                "pdf" : 'application/pdf',
                "php" : 'application/x-httpd-php',
                "jpg" : 'image/jpeg',
                "png" : 'image/png',
                "gif" : 'image/gif',
                "bmp" : 'image/bmp',
                "txt" : 'text/plain',
                "doc" : 'application/msword',
                "js"  : 'text/js',
                "py" : 'text / x - python',
                "swf" : 'application/x-shockwave-flash',
                "mp3" : 'audio/mpeg',
                "zip" : 'application/zip',
                "rar" : 'application/rar',
                "tar" : 'application/tar',
                "arj" : 'application/arj',
                "cab" : 'application/cab',
                "html": 'text/html',
                "default" : 'application/octet-stream',
            }

            return mimeTypes[extension] if extension in mimeTypes.keys() else ""
