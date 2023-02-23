import socket

HOST = '127.0.0.1'
port = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, port))
s.listen()

conn, addr = s.accept()


file = open('poo.jpg', "rb")
image_data = file.read(2048)

while image_data:
    conn.send(image_data)
    image_data = file.read(2048)


file.close()
conn.close()

