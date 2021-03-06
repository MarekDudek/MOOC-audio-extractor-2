import os
import re

def lecture_subdirectory(dirpath, output_dir):
    subdir = lecture_input_subdirectory(dirpath)
    sortable_name = lecture_sortable_name(subdir)
    return os.path.join(output_dir, sortable_name)

def lecture_input_subdirectory(dirpath):
    return os.path.basename(dirpath)

def lecture_sortable_name(lecture_input_subdir):
    order, title = extract_lecture_order_and_title(lecture_input_subdir)
    return '{:0>2d} {:s}'.format(order, title)

LECTURE_INPUT_SUBDIRECTORY = re.compile(r'^ *\w+ *(\d+) *: *(.+?) *$')

def extract_lecture_order_and_title(lecture_input_subdir):
    match = LECTURE_INPUT_SUBDIRECTORY.match(lecture_input_subdir)
    if match:
        order = match.group(1)
        title = match.group(2)
        return int(order), title



def rebuild_input_file_path(dirpath, name):
    return os.path.join(dirpath, name)



LECTURE_PART_INPUT_FILE = re.compile(
    r"""^           #   match from the beginning
        \ *         #     space(s)
        (\d+)       # Technical lecture order (group)
        \ *         #     space(s)
        -           #   hyphen
        \ *         #     space(s)
        (\d+)       # Technical part order (group)
        \ *         #     space(s)
        -           #   hyphen
        \ *         #     space(s)
        (\d+)       # Lecture order (group)
        \ *         #     space(s)
        -           #   hyphen
        \ *         #     space(s)
        (\d+)       # Part order (group)
        \           #     space(s)
        (.*?)       # Part title (group)
        \ *         #     space(s)
        \(          # Opening parentesis
        \ *         #     space(s)
        (\d+)       # Minutes (group)
        \ *         #     space(s)
        -           #   hyphen
        \ *         #     space(s)
        (\d+)       # Seconds (group)
        \ *         #     space(s)
        \)          # Closing parentesis
        \ *         #     space(s)
        \.          # Dot
        \ *         #     space(s)
        (\w+)       # Extension (group)
        \ *         #     space(s)
        $           #   match till the end
        """, re.VERBOSE)

def extract_from_lecture_part(name):
    match = LECTURE_PART_INPUT_FILE.match(name)
    if match:
        technical_lecture_order = match.group(1)
        technical_part_order    = match.group(2)
        lecture_order           = match.group(3)
        part_order              = match.group(4)
        part_title              = match.group(5)
        minutes                 = match.group(6)
        seconds                 = match.group(7)
        extension               = match.group(8)
        return int(technical_lecture_order), int(technical_part_order), int(lecture_order), int(part_order), part_title, int(minutes), int(seconds), extension

def lecture_part_sortable_name(name):
    _, _, _, part_order, part_title, _, _, _ = extract_from_lecture_part(name)
    return '{:0>2d} {:s}'.format(part_order, part_title)

def output_file_path(input_dir, output_dir, dirpath, name):
    lecture_input_subdir = os.path.relpath(dirpath, input_dir)
    lecture_name         = lecture_sortable_name(lecture_input_subdir)
    lecture_part_name    = lecture_part_sortable_name(name)
    file_name            = '{0}.mp3'.format(lecture_part_name)
    return os.path.join(output_dir, lecture_name, file_name)

def extract_course_title(input_dir):
    return os.path.basename(input_dir)

