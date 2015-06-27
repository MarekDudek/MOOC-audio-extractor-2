import sys
import subprocess

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
    __print_and_flush('\tStarting extraction ...')
    pipe = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=10**8)
    __print_and_flush('working ...') 
    pipe.wait()
    print 'done.'

def __print_and_flush(message) :
    print message,
    sys.stdout.flush()
