import os
import sys
sys.path.append('.')
from extraction import *
from paths_processing import *
from id3_tags import *

def process_directory(input_dir, output_dir, skip_extraction):

    for dirpath, dirnames, filenames in os.walk(input_dir):
        print 'Directory "{0}"'.format(dirpath)
        if dirpath == input_dir: 
            if not skip_extraction:
                os.makedirs(output_dir)
            pass
        else:
            lecture = lecture_subdirectory(dirpath, output_dir)
            if not skip_extraction:
                os.makedirs(lecture)

        for name in filenames:
            input_file  = rebuild_input_file_path(dirpath, name)
            print '\tInput  file "{0}"'.format(input_file)
            output_file = output_file_path(input_dir, output_dir, dirpath, name)
            print '\tOutput file "{0}"'.format(output_file)
            if not skip_extraction:
                extract_audio(input_file, output_file)
            fix_id3_tags(input_dir, output_dir, dirpath, name, output_file)
