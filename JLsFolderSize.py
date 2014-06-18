#!/usr/bin/env python
import subprocess
import argparse
import os


def script(cmd):
    subprocess.call(cmd, shell=True)


if __name__  == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m",  "--message",  help="script for print all the sub folders size.", action='store_true')
    parser.add_argument("-p",  "--path",  help="print all folders size in current path.")
    args = parser.parse_args()
    if args.message:
        print "start script"
        ## TODO,  to be added here
        print "end script"
    elif args.path:
        print "check for path ", args.path
        for item in os.listdir(args.path):
            item = os.path.join(args.path, item)
            if os.path.isdir(item) is True:
                item = item.replace(" ", "\ ")
                cmd = "du -sh {0}".format(item)
                script(cmd)
            pass
    else:
        parser.print_help()
