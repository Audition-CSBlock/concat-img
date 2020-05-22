import os
import cv2
import numpy as np

# Specify images
img1 = cv2.imread('img/cat.png')
img2 = cv2.imread('img/2.jpg')

# Concatenate read images
img_v = cv2.vconcat([img1, img1])
# Make new dir
if not os.path.exists('out'):
    os.makedirs('out')
# Write concatenated images
cv2.imwrite('out/out.png', img_v)