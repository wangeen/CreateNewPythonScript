#!/usr/bin/env python
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m",  "--message",  help="this is sample python script", action='store_true')
args = parser.parse_args()

def script(cmd):
    print cmd
    subprocess.call(cmd, shell=True)


if __name__  == "__main__":
    if args.message:
        print "start script"
        ## TODO,  to be added here
        print "end script"
    else:
        parser.print_help()
