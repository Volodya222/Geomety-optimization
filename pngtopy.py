import PIL
from PIL import Image
import  copy
import cv2
import numpy as np

def convert(x: str):
    N = 100
    with PIL.Image.open(x) as im:
        img_list = list(im.tobytes())

    # print(img_list)

    img = cv2.imread(x, cv2.IMREAD_GRAYSCALE)  # The image pixels have range [0, 255]
    # img //= 255  # Now the pixels have range [0, 1]
    img_list = img.tolist()  # We have a list of lists of pixels

    result = []
    for row in img_list:
        row_str = [p for p in row]
        result.append(row_str)
    result = np.array(result)
    result1 = copy.copy(result)
    for i in result:
        for j in range(len(i)):
            if (i[j] / 100 > 1) & (i[j] / 100 < 2.2):
                i[j] = 1
            else:
                if (i[j] / 100 < 1):
                    i[j] = 2
                if (i[j] / 100 > 2.2):
                    i[j] = 0
    # return result.reshape((-1,))
    return result
res = convert('g2.jpeg')
print(res.max())

