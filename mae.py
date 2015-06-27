#!/usr/bin/env python

import sys
import os

sys.path.append('.')
from extraction import *
from arguments  import *

def process_directory(input_dir, output_dir):

    for dirpath, dirnames, filenames in os.walk(input_dir):
        print 'Directory "{0}"'.format(dirpath)
        if dirpath == input_dir: 
            os.makedirs(output_dir)
        else:
            base_path = os.path.basename(dirpath)
            output_subdir = os.path.join(output_dir, base_path)
            os.makedirs(output_subdir)

        for name in filenames:
            input_file = os.path.join(dirpath, name)
            print '\tInput  file "{0}"'.format(input_file)
            relative_path = os.path.relpath(input_file, input_dir)
            (root, ext) = os.path.splitext(relative_path)
            output_file = os.path.join(output_dir, root + '.mp3')
            print '\tOutput file "{0}"'.format(output_file)
            extract_audio(input_file, output_file)

if __name__ == '__main__':

    print 'MOOC audio extractor'
    input_dir, output_dir = validate_arguments()
    process_directory(input_dir, output_dir)
