#!/usr/bin/pyhton

#  fitsio.py
#  
#
#  Created by giuliano taffoni on 23/05/16.
#


import pyfits
import numpy as np
import matplotlib.pyplot as plot


hdulist = pyfits.open('OBJ/ima0001.fits')

hdulist.info()

header = hdulist[0].header

type(header)

header.keys()

header.values()


header['HISTORY']

header[('HISTORY',0)]

# modifica header

header['FOCUSSSZ']

header.comments['FOCUSSSZ']

header['FOCUSSSZ'] = 3.0


header.set('OBSERV2','taffoni')


header.comments['OBSERV2'] =  'un commento'


header.remove('OBSERV2')

# DATI

data = hdulist[0].data

data.shape

data.dtype

data.max()

data.min()

maximum_indices = np.where(data==data.max())

hdulist

# update existing image
hdulist.writeto('newimage.fits')


#f = pyfits.open('original.fits', mode='update')
# making changes in data and/or header
#f.flush()  # changes are written back to original.fits
#f.close()  # closing the file will also flush any changes and prevent further writing

