import sys
import socket
args = sys.argv

with socket.socket() as my_socket:
    IP_address = args[1]
    port = int(args[2])
    message = args[3].encode()

    my_socket.connect((IP_address, port))

    my_socket.send(message)

    response = my_socket.recv(1024).decode()
    print(response)
