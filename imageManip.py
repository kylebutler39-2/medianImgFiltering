from PIL import Image
import numpy as npy
from os import listdir

pics = []

for img in listdir("proj1images"):
    pics.append(npy.array(Image.open("proj1images/" + img)))

newImgValues = npy.uint8(npy.median(pics, 0))
finalImg = Image.fromarray(newImgValues)
finalImg.save("finalImg.png", "PNG")
