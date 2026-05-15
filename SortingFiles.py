"""Sorting files by type."""

import os
import shutil

FILE_TYPES = {
    "Images": [
        '.jpg', '.png', '.jpeg',
        '.tif', '.tiff', '.webp',
        '.avif', '.heic'
    ],
    "Documents": [
        '.pdf', '.csv', '.docx',
        '.txt', '.rft', '.odt',
        '.xml', '.xlsx', '.pptx'
    ],
    "Videos": [
        '.mp4', '.mov',
        '.mkv', '.avi', '.webm'
    ],
    "Gif": ['.gif'],
    "EXE": ['.exe'],
    "Json": ['.json'],
    "Compressed": ['.zip', '.jar'],
    "Application": [
        '.apk', '.app', '.deb',
        '.dmg', '.msi', '.rpm',
        '.msix'
    ],
}


def read_file_type(file_name):
    """Get file type by file name."""
    return os.path.splitext(file_name)[1].lower()


def main():
    """Main function."""
    files_temp = {}
    path = input("Sorting Folder Path: ")
    for root, _, files in os.walk(path):
        if root != path:
            continue
        for item in files:
            item_path = os.path.join(root, item)
            files_temp[item_path] = {
                "name": item,
                "type": read_file_type(item)
            }
    # Create folder and move file to folder
    for storage in FILE_TYPES:
        os.makedirs(
            os.path.join(path, storage),
            exist_ok=True
        )

    for item_path, data in files_temp.items():
        item_type = data["type"]
        item_name = data["name"]

        for storage, extensions in FILE_TYPES.items():
            if item_type in extensions:
                    
                destination = os.path.join(
                    path,
                    storage,
                    item_name
                )

                shutil.move(item_path, destination)

                print(f"Moved {item_name} to {storage}")
                break

    print("Sorting Complete.")
    # Show folder in path
    print(f"Show Folder in {path}")
    for item in os.listdir(path):
        print(item)

if __name__ == "__main__":
    main()
