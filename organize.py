# This script organizes all files inside a directory based on their type
import os
from pathlib import Path

SUBDIRECTORIES = {
    "Documents": ['.pdf', '.rtf', '.txt'],
    "Audio": ['.m4a', '.m4b', '.mp3'],
    "Videos": ['.mov', '.avi', '.mp4'],
    "Images": ['.jpg', '.jpeg', '.png']
}

def pickDirectory(value):
    for category, formats in SUBDIRECTORIES.items():
        for formata in formats:
            if formata == value:
                return category
    return "MISSC"

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()