#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import whois

def is_available(domain):
    try:
        w = whois.whois(domain)
        return False
    except Exception as e:
        if e == "KeyboardInterrupt":
            sys.exit()
        return domain
