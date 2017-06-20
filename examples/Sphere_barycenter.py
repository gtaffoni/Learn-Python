#!/usr/bin/env python
#-----------------------------------------------------------------------------
#
#  barycenter.py
#  Learn Python
#
#  Created by giuliano taffoni on 15/03/17.
#  Copyright 2017 Guliano Taffoni. All rights reserved.
#
# The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------
'''
    Create a sphere of random distributed particles
    
    N is the number of particles
    
    '''

import numpy as np
import matplotlib.pyplot as plt
#
N=10000 # Number of particles
#
phi = 2. * np.pi  * np.random.random_sample(N)
costheta = 2. * np.random.random_sample(N) - 1
u  = np.random.random_sample(N)
theta = np.arccos ( costheta )
r = u ** (1./3.)
x = r * np.sin( theta) * np.cos( phi )
y = r * np.sin( theta) * np.sin( phi )
z = r * np.cos( theta )

plt.figure(1,figsize=(10,10))
plt.plot(x,y,'r.')
plt.show()
