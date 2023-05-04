import re

string_list = ['key-pem_fimage1_doc-new.png', 'Key-JPEG_fimage2.jpeg', 'no pattern-here', 'KEY-PNG_fimage2_extra-extra2.jpeg', 'key-JPG-fimage2_extra.anything.jpeg']

pattern = re.compile(r'^KEY-([^_]+)_(.*)', re.IGNORECASE)

for string in string_list:
    match = pattern.match(string)
    if match:
        filename = match.group(2) + '.' + match.group(1)
        with open(filename, 'w') as f:
            f.write(string)
            print(f"File {filename} created successfully")
    else:
        print("Match not found")




from pathlib import Path

def create_folders(paths):
    for path in paths:
        p = Path(path)
        if not p.exists():
            p.mkdir(parents=True, exist_ok=True)
            print(f"Created path: {path}")
        else:
            print(f"Path already exists: {path}")

# Example usage
folder_paths = ['C:/Folder1/Folder2', 'C:/Folder3']
create_folders(folder_paths)

import os

def create_folders(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created path: {path}")
        else:
            print(f"Path already exists: {path}")

# Example usage
folder_paths = ['C:/Folder1/Folder2', 'C:/Folder3']
create_folders(folder_paths)
