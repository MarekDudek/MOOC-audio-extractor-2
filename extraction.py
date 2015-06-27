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
    _print_single_line('\tStarting extraction ...')
    pipe = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=10**8)
    _print_single_line('working ...') 
    pipe.wait()
    _print_single_line('done.', done=True)

def _print_single_line(message, done=False) :
    if done:
        print message
        return
    print message,
    sys.stdout.flush()
