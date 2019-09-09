from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import FileMetadata


class ApiInterface:

    def __init__(self,creds):
        self.creds = creds
        self.initialize()
    def buildService(self):
        return build('drive', 'v3', credentials=self.creds)

    def initialize(self):
        self.service = self.buildService()
        # service has the functions described at: https://developers.google.com/drive/api/v3/reference/files?authuser=2
        # service handles the GET,POST Methods!
        pass
    def uploadToDrive(self,metadata,type,path = ""):
        if type == "folder":
            id = self.service.files().create(body=metadata,
                                                fields='id').execute()['id']
            return id
        elif type == "file":
            #path shouldn't be empty!
            #add "/" + metadata['name'] to it
            #not working yet

            metadata = dict(metadata)
            media = MediaFileUpload(path + "/" + metadata['name'],
                                    mimetype=metadata['mimeType'])
            metadata.pop('mimeType')
            self.service.files().create(body=metadata,media_body=media,fields='name,id').execute()


    def downloadFile(self):
        pass

