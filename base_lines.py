import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas

def rgb2gray(rgb):
    return np.round(np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140]))

def count(img):
    colors = []
    for i in range(256):
        color = np.count_nonzero(img == i)
        colors.append(color)
    return (colors)

def list_2_graph(lst):
    plt.plot(range(0,256), lst)
    plt.show()

img = mpimg.imread(r'C:\Users\IITC\PycharmProjects\Roy\poo.jpg')
#count(img)
list_2_graph(count(img))
