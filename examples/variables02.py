#!/usr/bin/env python
#-----------------------------------------------------------------------------
#
#  variables02.py
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

# Global variables
RA  = 145.65




def function():

    RA = 80.0              # this is a local variable will not change the global RA
    #
    print "I am the  function"
    print " --> In function : %f",RA
    #

def function2():
    
    global RA
    RA = 80.0        # this is a global variable will  change the global RA
    #
    print "I am the  function 2"
    print " --> In function 2 : %f",RA
#



if __name__ == '__main__':  # this is the MAIN  for python
    function()
    #
    print "I am the main program"
    print " --> In __main__: RA   %f",RA
    #
    function2()
    print "I am the main program again"
    print " --> In __main__: RA   %f",RA

