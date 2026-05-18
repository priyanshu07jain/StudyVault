import os
import shutil
import hashlib
from pathlib import Path
from logger import log

CATAGORIES = {
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.odt', '.rtf'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    'Code': ['.py', '.js', '.ts', '.html', '.css', '.java', '.cpp'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
    'Data': ['.csv', '.json', '.xml', '.xlsx', '.db', '.sql'],
    'Others': [],
}

# organize_files 
def organize_files(directory):
    for file in Path(directory).iterdir():
        if file.is_file():
            for folder, exts in CATAGORIES.items():
                if file.suffix in exts:
                    dest = Path(directory)/folder
                    dest.mkdir(exist_ok=True)
                    print(dest)
                    print(str(file))
                    shutil.move(str(file), dest)
                    log(f"Moved {file.name} -> {folder}")

#find duplicates
def find_duplicates(directory):
    hashes={}
    duplicates=[]
    for file in Path(directory).rglob("*"):
        if file.is_file():
            h=hashlib.md5(file.read_bytes()).hexdigest()
            if h in hashes:
                duplicates.append((file,hashes[h]))
            else:
                hashes[h]=file
    return duplicates

#backup_folder of the orignal 
def backup_folder(src,dest):
    import datetime
    timestamp=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name=f"{dest}/backup_{timestamp}.zip"
    shutil.make_archive(backup_name.replace(".zip",""),"zip",src)
    log(f"Backup created:{backup_name}")


# organize_files(r"C:\Users\developer\Documents\test")
# # dupe=find_duplicates(r"C:\Users\developer\Documents\test")
# # for d in dupe:
# #     print(d)
# #     print("")
# # print(type(dupe))
# # backup_folder(r"C:\Users\developer\Documents\test\Documents",r"C:\Users\developer\Documents\test\backup")