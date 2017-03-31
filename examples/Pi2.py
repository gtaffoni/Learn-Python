#!/usr/bin/env python
#-----------------------------------------------------------------------------
#
#  Pi2.py
#  Learn Python
#
#  Created by giuliano taffoni on 31/03/17.
#  Copyright 2017 Guliano Taffoni. All rights reserved.
#
# The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------


'''
    Usage:
        evalute PI using Wallis formula

'''


def function():
    pi = 2.
    for i in range(1,n):
        pi =  pi * (4.*i**2/(4.*i**2-1.))
    return pi


if __name__ == '__main__':  # this is the MAIN  for python
    import sys               # this is true for all the functions in the file
    #takes in command-line arguments [n]
    n = int(sys.argv[1]) if  len(sys.argv) > 1 else 100
    pi = function()
    print pi
