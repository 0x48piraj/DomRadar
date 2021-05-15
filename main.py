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

from utils.ds import load_all, load_dataset
from utils.avail import is_available
from utils.stdout import stdout_file, stdout_console

def cmdline():
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

def main():
    args = cmdline()
    dataset = args.dataset
    if dataset == 'all':
        names = load_all()
        if args.dump:
            for name in names:
                mode = "w" if name == names[0] else "a"
                stdout_file(name, is_available, mode)
        if args.print:
            for name in names:
                stdout_console(name, is_available)
    else:
        names = load_dataset(dataset)
        if args.dump:
            for name in names:
                mode = "w" if name == names[0] else "a"
                stdout_file(name, is_available, mode)
        if args.print:
            for name in names:
                stdout_console(name, is_available)

if __name__ == '__main__':
    
    if sys.version_info<(3,4,0):
        sys.stderr.write("You need python 3.4 or later to run this script\n")
        sys.exit(1)
    try:
        main()
    except:
        print('Try $ python main.py --help')
