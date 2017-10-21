#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:13:58 2017

@author: nabilenayet
"""


from sklearn.cluster import KMeans
import utils
import cv2


def retrieveColors(im):
    rawImage = cv2.imread(im)
    image = cv2.cvtColor(rawImage, cv2.COLOR_BGR2RGB)
    return calcKMeans(image)


def calcKMeans(im):
    #print("Calculating k-means clusters...")
    clt = KMeans(n_clusters = 3)
    #print(clt)
    imReshaped = im.reshape((im.shape[0] * im.shape[1], 3))
    clt.fit(imReshaped)
    
    # build a histogram of clusters and then create a figure
    # representing the number of pixels labeled to each color
    hist = utils.centroid_histogram(clt)
    bar = utils.plot_colors(hist, clt.cluster_centers_)
    return bar