import os
from PathStorage import *
#FIRSTRUNFILE = True
#FIRSTRUNFOLDER = True
EXCLUDEDFILES = []
EXCLUDEDFOLDERS = []

finishedMetadataFile = []
finishedMetadataFolder = []

def prepareFiles():
    pathStorage = PathStorage()
    list = pathStorage.getFoldersList()

    # whole folders one by one
    for synch_folders in list:
        rootPath = synch_folders['path']

        # get the excluded files/folders and the content of the  which might be seperated by comma
        EXCLUDEDFOLDERS = [folder for folder in str(synch_folders['excludeFolder']).split(",")]
        EXCLUDEDFILES = [file for file in str(synch_folders['excludeFile']).split(",")]
        content = [content for content in str(synch_folders['content']).split(",")]


        metadata = createMetadata(rootPath,type="folder")
        id  = uploadFile(metadata,type="folder")
        finishedMetadataFolder.append(metadata)

        walkThree(rootPath,id)




def walkThree(source ,id):
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


        metadata = createMetadata(rootPath + "/" + file,type="file",id=id)
        uploadFile(metadata,type="file")
        finishedMetadataFile.append(metadata)

    for folder in folders:
        #if FIRSTRUNFOLDER:
        #    if file in EXCLUDEDFOLDERS:
        #        FIRSTRUNFOLDER = False
        #       continue

        # might solve the issue with double test folders! +1
        metadata = createMetadata(rootPath + "/" + folder,type="folder",id=id)
        finishedMetadataFolder.append(metadata)
        id = uploadFile(metadata,type="folder")
        walkThree(rootPath + "/" + folder,id)


def createMetadata(path,type,id = ""):
    metadata = {}

    if type == "folder":
        metadata['name'] = str(path).rsplit("/")[-1]
        metadata['mimeType'] = getSpecificMime(type = "folder")
        # for the root Folder there will be no parents Id provided! check default id value in func def!
        if id != "": metadata['parents'] = [id]
        return metadata
    elif type == "file":
        # /home/-file.py-    ->    file.py
        fileName = str(path).rsplit("/")[-1]
        metadata['name'] = fileName
        metadata['mimeType'] = getSpecificMime(type="file",extension=fileName.rsplit(".")[-1])
        metadata['parents'] = [id]
        return metadata


def getSpecificMime(type,extension=""):
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


def uploadFile(metadata,type):
    if type == "folder":

        # hard coded ID just for testing!
        return "1AHGJSKDJASHFCACMCWUIIFPASKÖSJ"
    elif type == "file":
        print("upload!")





prepareFiles()
