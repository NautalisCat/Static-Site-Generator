import os
import shutil

static_directory = "/Users/sleeper/Dev/Static-Site-Generator/static"
public_directory = "/Users/sleeper/Dev/Static-Site-Generator/public"

if os.path.exists(public_directory):
    print("Public folder exist. Will proceed to delete")
    shutil.rmtree(public_directory)
os.mkdir(public_directory)

def recurs_filecopy(source, destination):
    file_entries = os.listdir(path=source)
    print(file_entries)
    for file in file_entries:
        source_path = os.path.join(source, file)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination)
            print(f"Adding {source_path} to Public Directory")
        elif os.path.isdir(source_path):
            dest_file_path = os.path.join(destination,file)
            os.mkdir(dest_file_path)
            recurs_filecopy(source_path, dest_file_path)
