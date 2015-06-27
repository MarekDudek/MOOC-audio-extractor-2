import sys


def print_single_line(message, done=False):
    if not done:
        print message,
        sys.stdout.flush()
    else:
        print message
