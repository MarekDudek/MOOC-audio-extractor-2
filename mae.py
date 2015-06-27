#!/usr/bin/env python

import sys
sys.path.append('src')
from arguments  import *
from hierarchy_processing import *


if __name__ == '__main__':

    print 'MOOC audio extractor'
    skip_extraction=True

    arguments = sys.argv[1:]
    on_fail   = sys.exit
    input_dir, output_dir = validate_arguments(arguments, on_fail, skip_extraction)

    process_directory(input_dir, output_dir, skip_extraction)
