#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def creator(domain, is_available, mode):
    with open("available.txt", mode) as f:
        _name = is_available(domain)
        if _name:
            print(f"{_name} is AVAILABLE")
            f.write(f"{_name}\n")
