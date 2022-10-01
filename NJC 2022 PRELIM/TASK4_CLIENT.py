from socket import socket
client = socket()
client.connect(("localhost", 8888))

print(client.recv(1024).decode())
option = input("Enter an option: ")
client.sendall(option.encode())

print(client.recv(1024).decode())
client.close()
