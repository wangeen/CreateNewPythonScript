#!/usr/bin/env python
import subprocess
import argparse


def script(cmd):
    print cmd
    subprocess.call(cmd, shell=True)


if __name__  == "__main__":
    script("plink -N wangeen@wangeen.com -D 127.0.0.1:7070")
