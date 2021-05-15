#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .colors import Colors
from tqdm import tqdm

# dump available domains to file
def stdout_file(domain, is_available, mode):
    with open("available.txt", mode) as f:
        _name = is_available(domain)
        if _name:
            tqdm.write(f"{_name} is {Colors.CGREEN}AVAILABLE!{Colors.CEND}")
            f.write(f"{_name}\n")

# print available domains to console
def stdout_console(domain, is_available):
    _name = is_available(domain)
    if _name:
        tqdm.write(f"{_name} is {Colors.CGREEN}AVAILABLE!{Colors.CEND}")
