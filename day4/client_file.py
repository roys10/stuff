import socket


server_ip = '127.0.0.1'  # Localhost
server_port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"[+] Connecting to {server_ip}")
s.connect((server_ip, server_port))

while True:
    file_name = input("what is the file's path:")

    s.send(file_name.encode())
    data = s.recv(1024).decode()
    new_file = fr'new_{file_name}'
    print(f"new file is: {new_file}")
    file = open(new_file, "w")
    file.write(data)
    file.close()


s.close()
