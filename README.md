Script's Erklärung (work in progress aber automatischer Download hat geklappt)
======================
_____________________________________________________________________________________________________________________________

Main.py: Main ist der Einstieg des Skripts. Hier kann man über das Terminal entscheiden, ob ein neuer Pfad für das Hochladen hinzugefügt werden soll, oder ob die angegebenen Ordner hochgeladen werden sollen. [Das Downloaden wurde noch nicht fertiggestellt]

PathStorage.py: Ist dafür zuständig, dass Pfade in die path_conf.txt im JSON Format abgespeichert werden oder die Pfade aus der Konfig. Datei in FOLDERSLIST für weitere Verwendung im Upload/Download verwendet werden.

ApiInterface.py: Kümmert sich momentan nur um den Upload.

FileMetaData.py: Hier kümmert sich das Skript um die Metadaten der Dateien die man hochladen will. Ganz wichtig war hier, dass ein Order oder eine Datei in einem „Parent-Ordner“ dann in den Metadaten die ID des „Parent-Ordners“ angeben muss, sodass der Baum der Verzeichnisse auf Google Drive richtig dargestellt wird.
Ein relativ anspruchsvollerer Teil des Skripts war den kompletten Inhalt eines zum hochladen erwünschten Ordners „durchzulaufen“ (theoretisch hat jeder weitere Ordner noch n weitere), und jeder einzelnen Datei die entsprechenden Metadaten mitzugeben (also ID des Parent-Ordner usw.). Da musste für die Implementierung schonmal das Whiteboard für Skizzen herhalten.

Auth.py: Von Google mitgeliefert

##### info:(Das Projekt bis zu diesem Zeitpunkt ist innerhalb einer Woche entstanden, also waren meine Python Kenntnisse auch nicht die besten.)

Google-drive-api
================
_____________________________________________________________________________________________________________________________

###### Intro:
>        Auto upload of a directory with all its containing files and subfolders to google drive. 
>        Only works for linux atm.
>        IMPORTANT: all files in root folder and subfolders need to have an extension!!!
    
###### Required : 
>        Python 2.7 or above
    
>        google-api-python-client
>        google-auth-httplib2
>        google-auth-oauthlib

###### Install libraries: 
>        pip install  google-api-python-client 
>        pip install  google-auth-httplib2 
>        pip install  google-auth-oauthlib

###### Download 
>        Download these files and put them in Folder "XYZ"
    
>        1. ApiInterface.py
>        2. Auth.py
>        3. FileMetadata.py
>        4. Main.py
>        5. PathStorage.py

###### Enter following url into browser and follow steps below

>        https://developers.google.com/drive/api/v3/quickstart/python?refresh=
        
>        1. Click on "Enable the drive api" button (log in into google acc) 
>            - (better create test google acc if you dont trust me!)
>        2. Agree termes of service
>        3. Press "download client configuration" and then "done"
>        4. Put downloaded "credentials.json" file into folder XYZ with all other scripts
>        5. Open terminal in folder XYZ and type "python3 Main.py"
>        6. Enjoy
        
    
