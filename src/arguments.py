import os

def validate_arguments(args, on_fail, skip_extraction):

    if len(args) != 2:
        on_fail('Two arguments required, input and output directories')

    input_dir, output_dir = map(os.path.abspath, args)

    print 'Input  directory is "{0}"'.format(input_dir)
    print 'Output directory is "{0}"'.format(output_dir)

    if not os.path.isdir(input_dir):
        on_fail('Input directory does not exist and it should')

    if os.path.isdir(output_dir):
        if not skip_extraction:
            on_fail('Output directory exists and it should not')

    return input_dir, output_dir
