import os
import shutil

print()
path = input("Sorting Folder Path: ")

fileType = {
    "Images": ['.jpg', '.png', '.jpeg', '.tif', '.tiff', '.webp', '.avif', '.heic'],
    "Documents": ['.pdf', '.csv', '.docx', '.txt', '.rft', 'odt', '.xml', '.xlsx', '.pptx'],
    "Videos": ['.mp4', '.mov', '.mkv', '.avi', '.webm'],
    "Gif": ['.gif'],
    "EXE": ['.exe'],
    "Json": ['.json'],
    "Compressed": ['.zip', '.jar']
}

def filetype(file):
    temp = file.split(".")
    return f'.{temp[-1]}'

filestemp = dict()

# open folder by path
for root, dirs, files in os.walk(path):
    for item in files:
        filestemp[item] = [f"{root}\\{item}", root, filetype(item)]


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

print("Sorting Complete.")

print()
print(f"Show Folder in {path}")
for item in os.listdir(path):
    print(item)
