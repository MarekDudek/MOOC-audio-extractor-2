import os
import sys
sys.path.append('.')
from extraction import *
from paths_processing import *

def process_directory(input_dir, output_dir):

    for dirpath, dirnames, filenames in os.walk(input_dir):
        print 'Directory "{0}"'.format(dirpath)
        if dirpath == input_dir: 
            os.makedirs(output_dir)
        else:
            output_subdir = subdirectory_under_output_directory(dirpath, output_dir)
            os.makedirs(output_subdir)

        for name in filenames:
            input_file = input_file_path(dirpath, name)
            print '\tInput  file "{0}"'.format(input_file)
            output_file = output_file_path(input_dir, output_dir, name, dirpath)
            print '\tOutput file "{0}"'.format(output_file)
            extract_audio(input_file, output_file)