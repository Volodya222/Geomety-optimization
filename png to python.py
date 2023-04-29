import PIL
from PIL import Image
import cv2
import numpy as np


with PIL.Image.open('to python2.png') as im: img_list = list(im.tobytes())

# print(img_list)
import numpy as np
import cv2

img = cv2.imread("comsol_2.png", cv2.IMREAD_GRAYSCALE) # The image pixels have range [0, 255]
# img //= 255  # Now the pixels have range [0, 1]
img_list = img.tolist() # We have a list of lists of pixels

result = []
for row in img_list:
    row_str = [p for p in row]
    result.append(row_str)
result = np.array(result)
print(result)
print(type(result))