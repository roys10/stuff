import datetime
import socket
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


server_ip = '127.0.0.1'  # Localhost
server_port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"[+] Connecting to {server_ip}")
s.connect((server_ip, server_port))


# function sends print screen to server
def save_image():
    image_chunk = s.recv(2048)

    file = open(f'{server_ip},{server_port}.{datetime.date.today().strftime("%B-%d-%Y")}.jpg', "wb")

    while image_chunk:
        file.write(image_chunk)
        image_chunk = s.recv(2048)

    file.close()

def rgb2gray(rgb):
    return np.round(np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140]))


img = mpimg.imread(r'C:\Users\IITC\PycharmProjects\Roy\poo.jpg')

s.close()
