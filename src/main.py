import os
import shutil
import sys
import fileinput

from copy_static import copy_files_recursive
from generate_page import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"
docs_path ="./docs"
basepath = ""

def main():
    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]
        
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, docs_path)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, docs_path, basepath)


main()
