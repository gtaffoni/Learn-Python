#!/usr/bin/python


'''
    Usage:
        evalute PI using Wallis formula

  Created by giuliano taffoni on 26/03/17.
  Copyright 2017 giuliano taffoni. GPL3.

'''


import sys

#takes in command-line arguments [n]
n = int(sys.argv[1]) if  len(sys.argv) > 1 else 100


pi = 2.
for i in range(1,n):
    pi =  pi * (4.*i**2/(4.*i**2-1.))

print pi

