import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

from PIL import Image

im = Image.open("./image.webp")
im.save("image.png")
 
img = cv.imread('image.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

 
titles = ['Original Image','BINARY']
images = [img, thresh1]
 
for i in range(len(images)):
    plt.plot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

im = Image.fromarray(images[1])
im.save('processed_image.png') 
plt.show()