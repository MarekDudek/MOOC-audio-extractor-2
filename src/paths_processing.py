import os

def subdirectory_under_output_directory(dirpath, output_dir):
    base_name = os.path.basename(dirpath)
    subdirectory = os.path.join(output_dir, base_name)
    return subdirectory

def input_file_path(dirpath, name):
    return os.path.join(dirpath, name)

def output_file_path(input_dir, output_dir, name, dirpath):
    input_file = input_file_path(dirpath, name)
    relative_path = os.path.relpath(input_file, input_dir)
    (root, ext) = os.path.splitext(relative_path)
    return os.path.join(output_dir, root + '.mp3')