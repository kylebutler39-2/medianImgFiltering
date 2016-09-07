"""
Title: imageManip.py
Author: Kyle Butler-Fish
Abstract: Reads in images, finds the median value of each pixel, and creates a new image using the median pixel values
Date: 9/7/16
"""

#Library imports
from PIL import Image
import numpy as npy
from os import listdir

#Creates an array to store the images in
pics = []

#Creates an array for each image imported and adds those arrays to the pics array
for img in listdir("proj1images"):
    pics.append(npy.array(Image.open("proj1images/" + img)))

#Finds and stores the median pixel values of all of the imported images & converts the pixel values to 8-bit
newImgValues = npy.uint8(npy.median(pics, 0))

#Creates a new image using the median pixel values of the imported images
finalImg = Image.fromarray(newImgValues)

#Saves the new image
finalImg.save("finalImg.png", "PNG")
