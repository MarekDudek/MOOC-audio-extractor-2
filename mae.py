#!/usr/bin/env python

import sys
import os

if __name__ == '__main__':

    print 'MOOC audio extractor'

    if len(sys.argv) != (2 + 1):
        print 'Two arguments required, input and output directories'
        sys.exit(1)

    input_dir  = sys.argv[1]
    output_dir = sys.argv[2]

    print 'Input  directory is "%s"' % (input_dir, )
    print 'Output directory is "%s"' % (output_dir, )
