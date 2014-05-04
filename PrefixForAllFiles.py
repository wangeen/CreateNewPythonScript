#!/usr/bin/env python
import subprocess, os
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument("-m",  "--message",  help="../PrefixForAllFiles.py -p a -i *.jpg (-d if delete)", action='store_true')
parser.add_argument("-p",  "--prefix",  help="prefix string")
parser.add_argument("-d",  "--delete",  help="delete prefix string else add", action='store_true')
parser.add_argument("-i",  "--input",  help="file name with wildcard", nargs='*')
args = parser.parse_args()

def script(cmd):
    print cmd
    subprocess.call(cmd, shell=True)


if __name__  == "__main__":
    if args.input and args.prefix:
        if args.delete:
            for f in args.input:
                if os.path.exists(f):
                    index = f.find(args.prefix)
                    if index  == 0:
                        newFileName = f[index+len(args.prefix):]
                        script("mv {0} {1}".format(f, newFileName))
                        pass
                    print index
                else:
                    print "Not found ", f
                pass
        else:
            for f in args.input:
                if os.path.exists(f):
                    script("mv {0} {1}{0}".format(f, args.prefix))
                else:
                    print "Not found ", f
            pass
        pass
    else:
        print "--help for more detail."
