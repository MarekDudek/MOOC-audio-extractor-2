import os

def lecture_subdirectory(dirpath, output_dir):
    base_name = os.path.basename(dirpath)
    subdirectory = os.path.join(output_dir, base_name)
    return subdirectory

def lecture_subdirectory2(dirpath, output_dir):
    subdir = lecture_input_subdirectory(dirpath)
    sortable_name = lecture_sortable_name(subdir)
    pass

def lecture_input_subdirectory(dirpath):
    return os.path.basename(dirpath)

def lecture_sortable_name(lecture_input_subdir):
    order, title = extract_lecture_order_and_title(lecture_input_subdir)
    return '{:0>2d} {:s}'.format(order, title)


import re
LECTURE_INPUT_SUBDIRECTORY = re.compile(r'^ *\w+ *(\d+) *: *(.+?) *$')

def extract_lecture_order_and_title(lecture_input_subdir):
    match = LECTURE_INPUT_SUBDIRECTORY.match(lecture_input_subdir)
    if match:
        order = match.group(1)
        title = match.group(2)
        return int(order), title

def rebuild_input_file_path(dirpath, name):
    return os.path.join(dirpath, name)



def output_file_path(input_dir, output_dir, dirpath, name) :
    input_file = rebuild_input_file_path(dirpath, name)
    relative_path = os.path.relpath(input_file, input_dir)
    (root, ext) = os.path.splitext(relative_path)
    return os.path.join(output_dir, root + '.mp3')


