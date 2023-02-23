import socket


server_ip = '127.0.0.1'  # Localhost
server_port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"[+] Connecting to {server_ip}")
s.connect((server_ip, server_port))

while True:
    to_send = input("send:")
    s.send(to_send.encode())

    data = s.recv(1024).decode()
    print(f"from server: {data}")

s.close()
