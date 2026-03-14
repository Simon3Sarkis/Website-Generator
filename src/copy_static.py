import os
import shutil

def copy_files_recursive(source_node_path, dest_node_path):
    if not os.path.exists(dest_node_path):
        os.mkdir(dest_node_path)

    for item in os.listdir(source_node_path):
        from_path = os.path.join(source_node_path, item)
        to_path = os.path.join(dest_node_path, item)
        print(f" * {from_path} -> {to_path}")

        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_files_recursive(from_path, to_path)