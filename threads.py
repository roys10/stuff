import threading
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os


class Tor:
    def __init__(self):
        self.lst = []
        self.lock = threading.Lock()
        self.b_lock = threading.Lock()
        self.b_lock.acquire()

    def push(self, x):
        self.lock.acquire()
        if self.b_lock.locked():
            self.b_lock.release()
        self.lst.append(x)
        self.lock.release()

    def b_pop(self):
        self.b_lock.acquire()

        x = self.pop()
        if len(self) > 0:
            self.b_lock.release()
        return x

    def pop(self):

        if len(self) == 0:
            raise ValueError('No items in queue')
        else:
            self.lock.acquire()
            x = self.lst[0]
            del self.lst[0]
            self.lock.release()
            return x

    def peek(self):
        if len(self) == 0:
            raise ValueError('No items in  queue')
        return self.lst[0]

    def __len__(self):
        return len(self.lst)

def rgb2gray(rgb):
    return np.round(np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140]))


# t1 will use this, it reads from input dir and puts in queue
def check_inputdir(q, lock):

    lock.acquire()

    while len(os.listdir(r'C:\Users\IITC\PycharmProjects\Roy\InputDir')) == 0:
        pass

    print("hi")

    for img in os.listdir(r'C:\Users\IITC\PycharmProjects\Roy\InputDir'):
        path = fr'InputDir\{img}'
        q.push(mpimg.imread(path))
        # os.remove(path)
    # print(len(q))
    lock.release()



def gray_queue(q1,gray_q):
    while len(q1) != 0:
        gray_q.push = rgb2gray(q1.b_pop())
    print(len(gray_q))

def gray2output(gray_q):
    while len(gray_q) != 0:
        mpimg.imsave('name.png', gray_q)


lock1 = threading.Lock()
q1 = Tor()
q2 = Tor()
# lst = os.listdir(r'C:\Users\IITC\PycharmProjects\Roy\InputDir')
# lock1.acquire()
threading.Thread(target=check_inputdir(q1,lock1)).start()
threading.Thread(target=gray_queue(q1,q2)).start()
threading.Thread(target=gray2output(q2)).start()
# lst = os.listdir(r'C:\Users\IITC\PycharmProjects\Roy\InputDir')

# threading.Thread(target=t.b_lock).start()

