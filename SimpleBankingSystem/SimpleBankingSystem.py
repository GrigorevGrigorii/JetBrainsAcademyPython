from random import randint
import sqlite3


conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)")


class Bank:
    def __init__(self):
        self.all_accounts = {}
        cur.execute("SELECT number, pin, balance FROM card")
        for item in cur.fetchall():
            self.all_accounts[item[0]] = {"PIN": item[1], "balance": item[2]}

        self.current_mode = "start_mode"
        self.current_account = None

    def get_menu(self):
        if self.current_mode == "start_mode":
            return "1. Create an account\n2. Log into account\n0. Exit"
        elif self.current_mode == "account_mode":
            return "1. Balance\n2. Log out\n0. Exit"

    def create_an_account(self):
        while True:
            card_number = "400000" + str(randint(10 ** 8, 10 ** 9 - 1))

            digits = list(map(int, list(card_number)))
            digits = [x * 2 if i % 2 == 0 else x for i, x in enumerate(digits)]
            digits = [x - 9 if x > 9 else x for x in digits]
            last_digit = str((10 - sum(digits) % 10) % 10)
            del digits

            card_number += last_digit
            if card_number not in self.all_accounts.keys():
                break

        card_pin = ''.join([str(randint(0, 9)) for _ in range(4)])
        card_id = str(len(self.all_accounts.keys()) + 1)

        self.all_accounts[card_number] = {"PIN": card_pin, "balance": 0}

        cur.execute("INSERT INTO card (id, number, pin) VALUES (?, ?, ?)", (card_id, card_number, card_pin))

        print("Your card has been created")
        print(f"Your card number:\n{card_number}")
        print(f"Your card PIN:\n{card_pin}\n")

    def log_into_account(self):
        card_number = input("Enter your card number:\n>")
        card_pin = input("Enter your PIN:\n>")

        if card_number not in self.all_accounts.keys() or self.all_accounts[card_number]["PIN"] != card_pin:
            print("Wrong card number or PIN!\n")
            return
        print("You have successfully logged in!\n")
        self.current_mode = "account_mode"
        self.current_account = card_number
        return

    def log_out(self):
        self.current_mode = "start_mode"
        self.current_account = None

    def processing_command(self, command):
        print()
        if self.current_mode == "start_mode":
            if command == '1':
                self.create_an_account()
            elif command == '2':
                self.log_into_account()
            elif command == '0':
                print("Bye!")
                conn.commit()
                exit()
            else:
                print("Command error")
        elif self.current_mode == "account_mode":
            if command == '1':
                print(f"Balance: {self.all_accounts[self.current_account]['balance']}\n")
            elif command == '2':
                self.log_out()
            elif command == '0':
                print("Bye!")
                conn.commit()
                exit()
            else:
                print("Command error")


my_bank = Bank()
while True:
    print(my_bank.get_menu())
    command = input('>')
    my_bank.processing_command(command)
