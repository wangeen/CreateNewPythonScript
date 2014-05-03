#!/usr/bin/env python
import subprocess
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument("-m",  "--message",  help="this is sample python script", action='store_true')
parser.add_argument("-p",  "--prefix",  help="prefix string")
parser.add_argument("-f",  "--file",  help="file name with wildcard")
args = parser.parse_args()

def script(cmd):
    print cmd
    subprocess.call(cmd, shell=True)


if __name__  == "__main__":
    if args.message:
        print "start script"
        ## TODO,  to be added here
        print "end script"
    elif args.file and args.prefix:
        print "xxx"
        print args.file
        print args.prefix
        print "xxx"
        files = glob.glob(args.file)
        for file in files:
            script("mv {0} {1}{0}".format(file, args.prefix))
        pass
    else:
        print "please input --help for more detail"
