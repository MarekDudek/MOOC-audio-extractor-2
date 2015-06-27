import sys
import os

def validate_arguments():

    args = sys.argv[1:]
    if len(args) != 2:
        print 'Two arguments required, input and output directories'
        sys.exit(1)

    input_dir  = sys.argv[1]
    output_dir = sys.argv[2]

    print 'Input  directory is "{0}"'.format(input_dir)
    print 'Output directory is "{0}"'.format(output_dir)

    if not os.path.isdir(input_dir):
        print 'Input directory does not exist and it should'
        sys.exit(1)

    if os.path.isdir(output_dir):
        print 'Output directory exists and it should not'
        sys.exit(1)

    return input_dir, output_dir
