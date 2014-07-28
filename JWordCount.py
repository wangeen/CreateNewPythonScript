#!/usr/bin/env python
import subprocess
import argparse
import os


def script(cmd):
    print cmd
    subprocess.call(cmd, shell=True)


if __name__  == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w",  "--word",  help="the word will be counted.")
    parser.add_argument("-f",  "--file",  help="ascii file.")
    args = parser.parse_args()
    wordCount = 0
    if args.word and args.file:
        if os.path.exists(args.file) is False:
            os.exit("Can't find file"+args.file)
        handle = open(args.file)
        while 1:
            line = handle.readline()
            if not line:
                break
            if line.find(args.word)>0:
                wordCount += 1
                pass
        handle.close()
        print wordCount,"  ",  args.word, "got!"

    else:
        parser.print_help()
