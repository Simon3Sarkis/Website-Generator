import os
import sys
import shutil
from copy_static import copy_files_recursive
from generate_page import generate_page, generate_pages_recursive

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    dir_path_static = "./static"
    dir_path_docs = "./docs"

    print(f"Building site with basepath: {basepath}")
    
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    copy_files_recursive(dir_path_static, dir_path_docs)
    generate_pages_recursive("content", "template.html", dir_path_docs, basepath)

if __name__ == "__main__":
    main()