class CoffeeMachine:
    def __init__(self, money, water, milk, coffee_beans, disposable_cups, current_state="choosing_action"):
        self.money = money
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.current_state = current_state

    def buy(self, n):
        if n == 1:
            if self.water >= 250 and self.coffee_beans >= 16 and self.disposable_cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.money += 4
                self.water -= 250
                self.coffee_beans -= 16
                self.disposable_cups -= 1
            else:
                if not self.water >= 250:
                    print("Sorry, not enough water!")
                if not self.coffee_beans >= 16:
                    print("Sorry, not enough coffee beans")
                if not self.disposable_cups >= 1:
                    print("Sorry, not enough disposable cups")
        elif n == 2:
            if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20 and self.disposable_cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.money += 7
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.disposable_cups -= 1
            else:
                if not self.water >= 350:
                    print("Sorry, not enough water!")
                if not self.milk >= 75:
                    print("Sorry, not enough milk!")
                if not self.coffee_beans >= 20:
                    print("Sorry, not enough coffee beans!")
                if not self.disposable_cups >= 1:
                    print("Sorry, not enough disposable cups!")
        elif n == 3:
            if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12 and self.disposable_cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.money += 6
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.disposable_cups -= 1
            else:
                if not self.water >= 200:
                    print("Sorry, not enough water!")
                if not self.milk >= 100:
                    print("Sorry, not enough milk!")
                if not self.coffee_beans >= 12:
                    print("Sorry, not enough coffee beans!")
                if not self.disposable_cups >= 1:
                    print("Sorry, not enough disposable cups!")
        else:
            print("Error")

    def fill(self, water, milk, coffee_beans, disposable_cups):
        self.water += water
        self.milk += milk
        self.coffee_beans += coffee_beans
        self.disposable_cups += disposable_cups

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def remaining(self):
        print()
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"{self.money} of money")

    def speak(self):
        if self.current_state == "choosing_action":
            print("Write action (buy, fill, take, remaining, exit):")
        elif self.current_state == "choosing_coffee":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        elif self.current_state == "filling 1":
            print("Write how many ml of water do you want to add:")
        elif self.current_state == "filling 2":
            print("Write how many ml of milk do you want to add:")
        elif self.current_state == "filling 3":
            print("Write how many grams of coffee beans do you want to add:")
        elif self.current_state == "filling 4":
            print("Write how many disposable cups of coffee do you want to add:")

    def action(self, act):
        if self.current_state == "choosing_action":
            if act == "buy":
                self.current_state = "choosing_coffee"
            elif act == "fill":
                self.current_state = "filling 1"
            elif act == "take":
                self.take()
            elif act == "remaining":
                self.remaining()
            elif act == "exit":
                exit(0)
            else:
                print("Error")
        elif self.current_state == "choosing_coffee":
            self.current_state = "choosing_action"
            if act == "back":
                print()
                return
            self.buy(int(act))
        elif self.current_state == "filling 1":
            self.current_state = "filling 2"
            self.fill(int(act), 0, 0, 0)
        elif self.current_state == "filling 2":
            self.current_state = "filling 3"
            self.fill(0, int(act), 0, 0)
        elif self.current_state == "filling 3":
            self.current_state = "filling 4"
            self.fill(0, 0, int(act), 0)
        elif self.current_state == "filling 4":
            self.current_state = "choosing_action"
            self.fill(0, 0, 0, int(act))
        print()


coffee_machine = CoffeeMachine(550, 400, 540, 120, 9)

while True:
    coffee_machine.speak()
    coffee_machine.action(input("> "))
