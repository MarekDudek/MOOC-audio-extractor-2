#!/usr/bin/env python

import sys
sys.path.append('.')
from arguments  import *
from hierarchy_processing import *


if __name__ == '__main__':

    print 'MOOC audio extractor'
    input_dir, output_dir = validate_arguments()
    process_directory(input_dir, output_dir)
