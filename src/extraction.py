import sys
import subprocess

import sys
sys.path.append('.')
from external_tools import *

def extract_audio(input_file, output_file):
    command = [ 'ffmpeg',
                '-loglevel', 'panic',
                '-i', input_file,
                '-map', '0:a',
                '-c', 'libmp3lame',
                '-q:a', '2',
                '-f', 'mp3',
                output_file
                ]
    print_single_line('\tStarting extraction ...')
    pipe = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=10**8)
    print_single_line('working ...') 
    pipe.wait()
    print_single_line('done.', done=True)

