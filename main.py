#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Usage:
    $ python3 main.py --print or python3 main.py --dataset all --print
    $ python3 main.py --dataset animal --dump/--print
    $ python3 main.py -ds animal -d/-p
"""


import sys
import argparse

def cmdline(): # parser object
    p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    
    p.add_argument("-ds", "--dataset", choices=['all','animal','random'], default='all',
                   help="name of the dataset to use")
    p.add_argument("-v", "--verbosity", type=int, choices=[0,1,2], default=0,
                   help="increase output verbosity (default: %(default)s)")

    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("-d", "--dump",action="store_true",
                   help="stdout the results to file")
    g.add_argument("-p", "--print",action="store_true",
                   help="stdout the results to console")

    return(p.parse_args())

if __name__ == '__main__':
    
    if sys.version_info<(3,4,0):
        sys.stderr.write("You need python 3.4 or later to run this script\n")
        sys.exit(1)
    try:
        args = cmdline()
        print(args)
    except:
        print('Try $ python main.py --help')