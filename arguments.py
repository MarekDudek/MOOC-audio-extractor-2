import os

def validate_arguments(args, on_fail):

    if len(args) != 2:
        print 'Two arguments required, input and output directories'
        on_fail()

    input_dir  = args[0]
    output_dir = args[1]

    print 'Input  directory is "{0}"'.format(input_dir)
    print 'Output directory is "{0}"'.format(output_dir)

    if not os.path.isdir(input_dir):
        print 'Input directory does not exist and it should'
        on_fail()

    if os.path.isdir(output_dir):
        print 'Output directory exists and it should not'
        on_fail()

    return input_dir, output_dir
