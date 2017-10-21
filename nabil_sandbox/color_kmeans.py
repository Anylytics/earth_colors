# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 09:58:35 2017

@author: nabilenayet
"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2

# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#ap.add_argument("-c", "--clusters", required = True, type = int,
#	help = "# of clusters")
baseDir = "/Users/nabilenayet/Documents/Anylytics/earthp0rn/images/20170125_015722_n2ACNC0.jpg"
#args = vars(ap.parse_args())
 
# load the image and convert it from BGR to RGB so that
# we can dispaly it with matplotlib
#print(baseDir + args["image"])
#image = cv2.imread(baseDir + args["image"])
image = cv2.imread(baseDir)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print("Got to line 26")
print(image)
# show our image
plt.figure()
plt.axis("off")
plt.imshow(image)

# reshape the image to be a list of pixels
image = image.reshape((image.shape[0] * image.shape[1], 3))


# cluster the pixel intensities
#clt = KMeans(n_clusters = args["clusters"])
clt = KMeans(n_clusters = 3)
print(clt)
clt.fit(image)

# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color
hist = utils.centroid_histogram(clt)
bar = utils.plot_colors(hist, clt.cluster_centers_)
 
# show our color bart
plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()