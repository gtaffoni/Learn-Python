#!/usr/bin/env python
#-----------------------------------------------------------------------------
#
#  Pi.py
#  Learn Python
#
#  Created by giuliano taffoni on 15/03/17.
#  Copyright 2017 Guliano Taffoni. All rights reserved.
#
# The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------


'''
    Usage:
        evalute PI using Wallis formula


'''


import sys

#takes in command-line arguments [n]
n = int(sys.argv[1]) if  len(sys.argv) > 1 else 100


pi = 2.
for i in range(1,n):
    pi =  pi * (4.*i**2/(4.*i**2-1.))

print pi


