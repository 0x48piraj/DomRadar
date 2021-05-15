#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create an file with available domains
def stdout_file(domain, is_available, mode):
    with open("available.txt", mode) as f:
        _name = is_available(domain)
        if _name:
            print(f"{_name} is AVAILABLE!")
            f.write(f"{_name}\n")

#Print available domains
def stdout_console(domain, is_available):
    _name = is_available(domain)
    if _name:
        print(f"{_name} is AVAILABLE!")
