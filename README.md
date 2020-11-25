Google-drive-api (work in progress)
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
        
        
        
Script's documentation
======================
_____________________________________________________________________________________________________________________________

    
