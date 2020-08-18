from random import randint
import sqlite3


conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)")


def luhn(number):
    digits = list(map(int, list(number)))
    digits = [x * 2 if i % 2 == 0 else x for i, x in enumerate(digits)]
    digits = [x - 9 if x > 9 else x for x in digits]
    luhn_last_digit = str((10 - sum(digits) % 10) % 10)
    del digits
    return luhn_last_digit


class Bank:
    def __init__(self):
        self.current_mode = "start_mode"
        self.id_of_current_card = 0

    def get_menu(self):
        if self.current_mode == "start_mode":
            return "1. Create an account\n2. Log into account\n0. Exit"
        elif self.current_mode == "account_mode":
            return "1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit"

    def create_an_account(self):
        while True:
            card_number = "400000" + str(randint(10 ** 8, 10 ** 9 - 1))
            card_number += luhn(card_number)

            cur.execute("SELECT * FROM card WHERE number = ?", (card_number,))
            if not cur.fetchall():
                break

        card_pin = ''.join([str(randint(0, 9)) for _ in range(4)])
        cur.execute("SELECT * FROM card")
        card_id = str(len(cur.fetchall()) + 1)

        cur.execute("INSERT INTO card (id, number, pin) VALUES (?, ?, ?)", (card_id, card_number, card_pin))
        conn.commit()

        print("Your card has been created")
        print(f"Your card number:\n{card_number}")
        print(f"Your card PIN:\n{card_pin}\n")

    def log_into_account(self):
        card_number = input("Enter your card number:\n>")
        card_pin = input("Enter your PIN:\n>")

        cur.execute("SELECT * FROM card WHERE number = ? AND pin = ?", (card_number, card_pin))
        data = cur.fetchone()

        if not data:
            print("Wrong card number or PIN!\n")
            return
        print("You have successfully logged in!\n")
        self.current_mode = "account_mode"
        self.id_of_current_card = data[0]
        return

    def balance(self):
        cur.execute("SELECT * FROM card WHERE id = ?", (self.id_of_current_card,))
        print(f"Balance: {cur.fetchone()[3]}\n")

    def add_income(self):
        income = int(input("Enter income:\n>"))

        cur.execute("UPDATE card SET balance = balance + ? WHERE id = ?", (income, self.id_of_current_card))
        conn.commit()

        print("Income was added!\n")

    def do_transfer(self):
        print("Transfer")
        card_number = input("Enter card number:\n>")

        cur.execute("SELECT * FROM card WHERE id = ?", (self.id_of_current_card,))
        data_out = cur.fetchone()
        cur.execute("SELECT * FROM card WHERE number = ?", (card_number,))
        data_in = cur.fetchone()

        if luhn(card_number[:-1]) != card_number[15]:
            print("Probably you made mistake in the card number. Please try again!\n")
            return
        elif not data_in:
            print("Such a card does not exist.\n")
            return
        elif card_number == data_out[1]:
            print("You can't transfer money to the same account!\n")
            return

        amount = int(input("Enter how much money you want to transfer:\n>"))

        if amount > data_out[3]:
            print("Not enough money!\n")
            return

        cur.execute("UPDATE card SET balance = balance - ? WHERE id = ?", (amount, self.id_of_current_card))
        conn.commit()
        cur.execute("UPDATE card SET balance = balance + ? WHERE number = ?", (amount, card_number))
        conn.commit()
        print("Success!\n")

    def close_account(self):
        cur.execute("DELETE FROM card WHERE id = ?", (self.id_of_current_card,))
        conn.commit()
        self.log_out()
        print("The account has been closed!\n")

    def log_out(self):
        self.current_mode = "start_mode"
        self.id_of_current_card = 0

    def processing_command(self, command):
        print()
        if self.current_mode == "start_mode":
            if command == '1':
                self.create_an_account()
            elif command == '2':
                self.log_into_account()
            elif command == '0':
                print("Bye!")
                exit()
            else:
                print("Command error")
        elif self.current_mode == "account_mode":
            if command == '1':
                self.balance()
            elif command == '2':
                self.add_income()
            elif command == '3':
                self.do_transfer()
            elif command == '4':
                self.close_account()
            elif command == '5':
                self.log_out()
            elif command == '0':
                print("Bye!")
                exit()
            else:
                print("Command error")


my_bank = Bank()
while True:
    print(my_bank.get_menu())
    command = input('>')
    my_bank.processing_command(command)
