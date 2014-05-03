#!/usr/bin/env python
import subprocess


def script(cmd):
    print cmd
    subprocess.call(cmd, shell=True)


if __name__  == "__main__":
    print "start script"
    ## TODO,  to be added here
    print "end script"
