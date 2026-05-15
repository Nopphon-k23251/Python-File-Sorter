import os
import shutil

"""
Sorting Files by Type
"""
def filetype(file):
    """Get file type by file name."""
    temp = file.split(".")
    return f'.{temp[-1]}'

"""Main Function"""
def main():
    # File type dictionary
    fileType = {
        "Images": ['.jpg', '.png', '.jpeg', '.tif', '.tiff', '.webp', '.avif', '.heic'],
        "Documents": ['.pdf', '.csv', '.docx', '.txt', '.rft', 'odt', '.xml', '.xlsx', '.pptx'],
        "Videos": ['.mp4', '.mov', '.mkv', '.avi', '.webm'],
        "Gif": ['.gif'],
        "EXE": ['.exe'],
        "Json": ['.json'],
        "Compressed": ['.zip', '.jar'],
        "Application": ['.apk', '.app', '.deb', '.dmg', '.msi', '.rpm', '.msix'],
    }
    # Temporary file dictionary
    filestemp = dict()
    # Get sorting folder path
    path = input("Sorting Folder Path: ")
    # open folder by path
    for root, dirs, files in os.walk(path):
        for item in files:
            filestemp[item] = [f"{root}\\{item}", root, filetype(item)]

    # Create folder and move file to folder
    for storage in fileType:
        folder_path = None
        try:
            os.mkdir(path=f'{path}\\{storage}')
            folder_path = f"{path}\\{storage}"
            print(f"Created New Folder Complete : Name - {storage}")
        except FileExistsError:
            folder_path = f"{path}\\{storage}"

        for item in filestemp:
            itmetype = filestemp[item][-1]
            itmepath = filestemp[item][0]
            parent = filestemp[item][1]

            if itmetype in fileType[storage] and parent==path:
                shutil.move(itmepath, folder_path)
                print(f'move {item} to {storage}.')
            else:
                if parent!=path:
                    p = parent.split("\\")
                    print(f"Skip file:{item}, Parent: {p[-1]}")
    # Move file to other folder
    print("Sorting Complete.")
    # Show folder in path
    print(f"Show Folder in {path}")
    for item in os.listdir(path):
        print(item)
main()
