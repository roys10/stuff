import socket

HOST = '127.0.0.1'
port = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, port))
s.listen()

conn, addr = s.accept()
while True:
    data = conn.recv(1024).decode()
    print(data)
    file = open(fr'{data}', "rb")
    data = file.read()

    if data == "q":
        break
    to_send = data
    conn.send(data.encode())
    file.close()

conn.close()

