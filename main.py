#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example:
    $ python3 main.py --print or python3 main.py --dataset all --print
    $ python3 main.py --dataset animal --dump/--print
    $ python3 main.py -ds animal -d/-p
"""


import sys
import os
import argparse
from tqdm import tqdm

from utils.ds import load_all, load_dataset
from utils.avail import is_available
from utils.stdout import stdout_file, stdout_console
from utils.process import convert_to_domain

def cmdline():
    p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    
    p.add_argument("-ds", "--dataset", default='all',
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

    if os.environ.get("OS", "") == "Windows_NT":
        os.system("color")

    if dataset == 'all':
        names = load_all()
        if args.dump:
            for name in tqdm(names, position=0, leave=True):
                name = convert_to_domain(name)
                mode = "w" if name == names[0] else "a"
                stdout_file(name, is_available, mode)
        if args.print:
            for name in tqdm(names, position=0, leave=True):
                name = convert_to_domain(name)
                stdout_console(name, is_available)
    else:
        names = load_dataset(dataset)
        if args.dump:
            for name in tqdm(names):
                name = convert_to_domain(name)
                mode = "w" if name == names[0] else "a"
                stdout_file(name, is_available, mode)
        if args.print:
            for name in tqdm(names):
                name = convert_to_domain(name)
                stdout_console(name, is_available)

if __name__ == '__main__':
    
    if sys.version_info<(3,4,0):
        sys.stderr.write("You need python 3.4 or later to run this script\n")
        sys.exit(1)
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
