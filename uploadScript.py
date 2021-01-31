# This script needs a client_sercrets.json file in its directory. This file contains credentials that could be gotten from GoogleDrive API

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

with open('testing.txt', 'r') as file:
    file_drive = drive.CreateFile({'title': os.path.basename(file.name)})
    file_drive.SetContentString(file.read())
    file_drive.Upload()