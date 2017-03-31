#!/usr/bin/env python
#-----------------------------------------------------------------------------
#
#  Integrate01.py
#  Learn Python
#
#  Created by giuliano taffoni on 15/03/17.
#  Copyright 2017 Guliano Taffoni. All rights reserved.
#
# The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------

'''

  Usage:
  
        evaluate an intengral using the trapeziodal method
        
        Dx = (b-a)/n
        A = Sum(F(a)+F(a+Dx))*Dx/2


  Created by giuliano taffoni on 24/03/17.
  Copyright 2017 giuliano taffoni. All rights reserved.

'''

import numpy as np
import sys

#takes in command-line arguments [a,b,n]
a = float(sys.argv[1])
b = float(sys.argv[2])
n = int(sys.argv[3])

def f(x): #Function to be integrated. We use a zero centerd parabola.
    return x*x

def Trapezio(a, b, n):
    '''Numerically integrate with the trapezoid rule on the interval from
    a to b with n trapezoids.
    '''
    integral = -(f(a) + f(b))/2.0
    for x in np.linspace(a,b,n+1):
        integral = integral + f(x)
    integral = integral * (b-a)/n
    return integral

integral = Trapezio(a, b, n)
print "With n =", n, "trapezoids, our estimate of the integral\
from", a, "to", b, "is", integral
