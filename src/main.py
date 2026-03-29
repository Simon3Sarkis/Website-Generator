import os
import shutil
from copy_static import copy_files_recursive
from generate_page import generate_page

def main():
    dir_path_static = "./static"
    dir_path_public = "./public"

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()