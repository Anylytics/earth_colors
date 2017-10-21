#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:10:55 2017

@author: nabilenayet
"""

import os
import calcColors as km
import matplotlib.pyplot as plt


indir = '/Users/nabilenayet/Documents/Anylytics/earthp0rn/githubProject/earth_colors/images'

for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        fullFile = str(os.path.join(root, f))
        print(fullFile)
        thisImage = km.retrieveColors(fullFile)
        #print(thisImage)
        # show our color bart
        plt.figure()
        plt.axis("off")
        plt.imshow(thisImage)
        plt.show()