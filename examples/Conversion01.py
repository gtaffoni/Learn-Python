#!/usr/bin/env python
#-----------------------------------------------------------------------------
#
#  Conversion01.py
#  Learn Python
#
#  Created by giuliano taffoni on 15/03/17.
#  Copyright 2017 Guliano Taffoni. All rights reserved.
#
# The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------

'''
    Convert RA and DEC from radians to degrees and vicevers

    Usage:
        Conversion01.py  R[D] RA DEC'
 
            R from radian'
            D from degree'
            
'''
import numpy as np

PI = 3.141592653589793  # convetionally used for constant (upper char)
                        # WARNING: constant in python does not exist

# Print the usage and exit
def usage():
    
    print ' -------------------------------------------------------------------------'
    print ' '
    print ' Typical usage:'
    print ' Conversion01.py  R[D] RA DEC'
    print ' '
    print ' R from radian'
    print ' D from degree'
    print ' '
    print ' Example:'
    print '     Conversion01.py R 140.5 33.5 '
    print ' '
    print ' -------------------------------------------------------------------------'
    sys.exit(' ')



# convert radians to degrees in decimal format
def rad_to_dec(radian):
    degree = (radian * 180.)/PI
    return degree

#  convert degrees decimal  format to degrees om sexa format
def deg_to_sexa(degree):
    import math
    sexa = np.zeros((3))
    fractional, integer = math.modf(degree)
    sexa[0] = int(integer)
    fractional, integer = math.modf(fractional*60.0)
    sexa[1] = int(integer)
    sexa[2] = fractional*60.
    return sexa

#  convert degrees in sexa format to radians
def sexa_to_rad(degree):
    deg = degree[0]+degree[1]/60.+degree[2]/60.
    rad = degree_to_rad(deg)
    return rad

# convert degrees in decimal format to radians
def degree_to_rad(degree):
    rad = (degree * PI) / 180.
    return rad

# wrapper to execute the conversion from degree to radians
# input maybe in sexa or decimal format
def dec_to_rad(degree):
    if isinstance(degree, list):        # if it is in sexa
        output = sexa_to_rad(degree)
    elif isinstance(degree, float):     # if it is in decimal
        output = degree_to_rad(degree)
    else:
        usage()
    return output

# read inputs from command line and create the proper numerical rapresentation
def chech_input_format(_argument):
    if _argument.startswith("[") and _argument.endswith("]"):
        output = map(float,_argument[1:-1].split(','))
    else:
        output = float(_argument)
    return output



if __name__ == '__main__':      # this is the MAIN  for python
    import sys                  # this is true for all the functions in the file
    #takes in command-line arguments [n]
    if len(sys.argv) < 3:
        usage()
    
    
    Rad_or_Deg = sys.argv[1]        # what is the convesion to do?

    if sys.argv[1] == 'R':              # Radian --> degree
        RA  = float(sys.argv[2])
        DEC = float(sys.argv[3])
        
        RA  = rad_to_dec(RA)
        DEC = rad_to_dec(DEC)
        print("RA = %f DEC = %f") % (RA,DEC)
        RA_SEXA  = deg_to_sexa(RA)      # Convert to Sexadecimal format
        DEC_SEXA = deg_to_sexa(DEC)     # Convert to Sexadecimal format
        print "RA  = ", RA_SEXA
        print "DEC = ", DEC_SEXA
    elif  sys.argv[1] == 'D':           # Degree --> Radian
        RA  = sys.argv[2]
        DEC = sys.argv[3]
        RA  = chech_input_format(RA)    # check if the imput is in deg or sexa format
        DEC = chech_input_format(DEC)
        RA_RAD  = dec_to_rad(RA)
        DEC_RAD = dec_to_rad(DEC)
        print("RA = %f DEC = %f") % (RA_RAD,DEC_RAD)
    else:
        usage()




