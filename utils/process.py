#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string

def convert_to_domain(name):
    filtered_domain = filter(lambda x: x in string.printable, name)
    filtered_domain = "".join(filtered_domain).replace(" ", "")
    domain = filtered_domain + '.com'
    return domain