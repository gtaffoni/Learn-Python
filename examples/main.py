#!/usr/bin/env python
#-----------------------------------------------------------------------------
#
#  main.py
#  Learn Python
#
#  Created by giuliano taffoni on 31/03/17.
#  Copyright 2017 Guliano Taffoni. All rights reserved.
#
# The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------

"""
    Simple python implementation: how to strucure a code in python
    
    Prints a list.
    
    if __name__ == '__main__':
    
"""


import numpy as np  # this is true for all the functions in the file

def function():
    import numpy  # this is local to the function
    print "I am the main function"
    os.getcwd()


if __name__ == '__main__':  # this is the MAIN  for python
    import os               # this is true for all the functions in the file
    function()
