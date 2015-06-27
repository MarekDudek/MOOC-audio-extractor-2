import subprocess

import sys
sys.path.append('.')
from external_tools import *
from paths_processing import *

def fix_id3_tags(input_dir, output_dir, dirpath, name, output_file):
    __remove_all_tags(output_file)
    __add_tags(input_dir, output_dir, dirpath, name, output_file)


def __remove_all_tags(output_file):
    command = [ 'eyeD3', '--remove-all', output_file ]
    pipe = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=10**8)
    pipe.wait()

def __add_tags(input_dir, output_dir, dirpath, name, output_file):
    course_title = extract_course_title(input_dir)
    lecture_title = lecture_sortable_name(lecture_input_subdirectory(dirpath))
    command = [ 
        'eyeD3', 
        '--artist', course_title,
        '--album', lecture_title,
        output_file 
    ]
    pipe = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=10**8)
    pipe.wait()
