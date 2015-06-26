#!/usr/bin/env python

import sys
import os


def validate_arguments():

    if len(sys.argv) != (2 + 1):
        print 'Two arguments required, input and output directories'
        sys.exit(1)

    input_dir  = sys.argv[1]
    output_dir = sys.argv[2]

    print 'Input  directory is "%s"' % (input_dir, )
    print 'Output directory is "%s"' % (output_dir, )

    if not os.path.isdir(input_dir):
        print 'Input directory does not exist and it should'
        sys.exit(1)

    if os.path.isdir(output_dir):
        print 'Output directory exists and it should not'
        sys.exit(1)

    return input_dir, output_dir

def process_directory(input_dir, output_dir):

    for dirName, subdirList, fileList in os.walk(input_dir):
        if dirName == input_dir: 
            os.makedirs(output_dir)
        else:
            pass

        for fname in fileList:
            pass

if __name__ == '__main__':

    print 'MOOC audio extractor'
    input_dir, output_dir = validate_arguments()
    process_directory(input_dir, output_dir)
