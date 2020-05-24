import os
import cv2
import numpy as np

# Specify images
images = os.listdir('img')
imagesconverted = [cv2.imread('img/'+i) for i in images]

# Concatenate read images
img_h = cv2.hconcat(imagesconverted)
# Make new dir
if not os.path.exists('out'):
    os.makedirs('out')
# Write concatenated images
cv2.imwrite('out/out.png', img_h)