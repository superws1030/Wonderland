# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 10:57:49 2020

@author: Wensi
"""

import rasterio
from matplotlib import pyplot
src = rasterio.open("bottom_I_aquifer.tif")
pyplot.imshow(src.read(1),cmap='pink')
pyplot.show()
from rasterio.plot import show_hist
show_hist(src, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Histogram")
