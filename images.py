import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def rgb2gray(rgb):
    return np.round(np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140]))

def color(img):
    print(img)



img = mpimg.imread(r'C:\Users\IITC\PycharmProjects\Roy\poo.jpg')


#color(gray_img)
img[img > 100] = 0
gray_img = plt.imshow(rgb2gray(img), cmap="gray")
plt.show()

