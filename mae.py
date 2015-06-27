#!/usr/bin/env python

import sys

sys.path.append('.')
from arguments  import *
from hierarchy_processing import *

import functools


if __name__ == '__main__':

    print 'MOOC audio extractor'

    arguments = sys.argv[1:]
    on_fail   = functools.partial(sys.exit, 1)
    input_dir, output_dir = validate_arguments(arguments, on_fail)

    process_directory(input_dir, output_dir)
