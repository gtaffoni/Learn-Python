#!/usr/bin/env python
#-----------------------------------------------------------------------------
#
#  variables01.py
#  Learn Python
#
#  Created by giuliano taffoni on 31/03/17.
#  Copyright 2017 Guliano Taffoni. All rights reserved.
#
# The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------

"""
    Simple python implementation: how to strucure a code in python
    
    Varibles scope:
            global, local
    
        
"""
import numpy as np          # this is a global import

# Global variables
RA  = 145.65
DEC = 48.5
Magnitude = 5.4



def function():
    import scipy            # this is a local import
    seeing = 8              # this is a local variable
    #
    print "I am the  function"
    print " In function : %f",RA
    print " In function : Type %f",TYPE
    print " In function : seeing %f",seeing
    #
    os.getcwd()

if __name__ == '__main__':  # this is the MAIN  for python
    import os               # this is a global import
    TYPE = "Star"           # this is a global variable
    #
    function()
    #
    print "I am the main program"
    print " In __main__: RA   %f",RA
    print " In __main__: Type %f",TYPE
    print " In __main__: seeing %f",seeing

