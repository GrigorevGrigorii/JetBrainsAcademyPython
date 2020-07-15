import random

random.seed()


class TicTacToe:
    def __init__(self, board="         "):
        self.board = list(board)
        self.state_of_game = "not finished"

    def __repr__(self):
        string = f"3  {self.board[0]} {self.board[1]} {self.board[2]}\n"
        string += f"2  {self.board[3]} {self.board[4]} {self.board[5]}\n"
        string += f"1  {self.board[6]} {self.board[7]} {self.board[8]}\n"
        string += "   1  2  3"
        return string

    def __str__(self):
        string = "---------\n"
        string += f"| {self.board[0]} {self.board[1]} {self.board[2]} |\n"
        string += f"| {self.board[3]} {self.board[4]} {self.board[5]} |\n"
        string += f"| {self.board[6]} {self.board[7]} {self.board[8]} |\n"
        string += "---------"
        return string

    def over(self):
        if (self.board[0] == "X" and self.board[1] == "X" and self.board[2] == "X") or (
                self.board[3] == "X" and self.board[4] == "X" and self.board[5] == "X") or (
                self.board[6] == "X" and self.board[7] == "X" and self.board[8] == "X") or (
                self.board[0] == "X" and self.board[3] == "X" and self.board[6] == "X") or (
                self.board[1] == "X" and self.board[4] == "X" and self.board[7] == "X") or (
                self.board[2] == "X" and self.board[5] == "X" and self.board[8] == "X") or (
                self.board[0] == "X" and self.board[4] == "X" and self.board[8] == "X") or (
                self.board[2] == "X" and self.board[4] == "X" and self.board[6] == "X"):
            self.state_of_game = "X wins"
            return True
        elif (self.board[0] == "O" and self.board[1] == "O" and self.board[2] == "O") or (
                self.board[3] == "O" and self.board[4] == "O" and self.board[5] == "O") or (
                self.board[6] == "O" and self.board[7] == "O" and self.board[8] == "O") or (
                self.board[0] == "O" and self.board[3] == "O" and self.board[6] == "O") or (
                self.board[1] == "O" and self.board[4] == "O" and self.board[7] == "O") or (
                self.board[2] == "O" and self.board[5] == "O" and self.board[8] == "O") or (
                self.board[0] == "O" and self.board[4] == "O" and self.board[8] == "O") or (
                self.board[2] == "O" and self.board[4] == "O" and self.board[6] == "O"):
            self.state_of_game = "O wins"
            return True
        elif self.board.count(" ") == 0:
            self.state_of_game = "Draw"
            return True
        else:
            return False

    def make_a_move_user(self, whose_move):
        if not self.over():
            while True:
                x_y = input("Enter the coordinates: > ")
                if x_y == "exit":
                    exit(0)
                if all([n.isdigit() for n in x_y.split()]) and len(x_y.split()) == 2:
                    x, y = int(x_y.split()[0]), int(x_y.split()[1])
                    if 1 <= x <= 3 and 1 <= y <= 3:
                        if self.board[x - 3 * y + 8] == " ":
                            self.board[x - 3 * y + 8] = whose_move
                            print(self)
                            break
                        else:
                            print("This cell is occupied! Choose another one!")
                    else:
                        print("Coordinates should be from 1 to 3!")
                else:
                    print("You should enter two numbers!")

    def make_a_move_easy(self, whose_move):
        if not self.over():
            print("Making move level \"easy\"")
            while True:
                x_rand = random.randint(1, 3)
                y_rand = random.randint(1, 3)
                if self.board[x_rand - 3 * y_rand + 8] == " ":
                    self.board[x_rand - 3 * y_rand + 8] = whose_move
                    print(self)
                    break

    def make_a_move_medium(self, whose_move):
        if not self.over():
            print("Making move level \"medium\"")
            for i in range(9):
                if self.board[i] == " ":
                    temp_game = TicTacToe(''.join([self.board[j] if j != i else whose_move for j in range(9)]))
                    if temp_game.over():
                        self.board[i] = whose_move
                        print(self)
                        del temp_game
                        return
                    del temp_game
            for i in range(9):
                if self.board[i] == " ":
                    opponent = "O" if whose_move == "X" else "X"
                    temp_game = TicTacToe(''.join([self.board[j] if j != i else opponent for j in range(9)]))
                    if temp_game.over():
                        self.board[i] = whose_move
                        print(self)
                        del temp_game
                        return
                    del temp_game
            while True:
                x_rand = random.randint(1, 3)
                y_rand = random.randint(1, 3)
                if self.board[x_rand - 3 * y_rand + 8] == " ":
                    self.board[x_rand - 3 * y_rand + 8] = whose_move
                    print(self)
                    break

    @staticmethod
    def processing_command(command):
        if command == "exit":
            exit(0)
        elif len(command.split()) == 3:
            if command.split()[0] == 'start':
                if command.split()[1] == 'user':
                    if command.split()[2] == 'user':
                        game = TicTacToe()
                        print(game)
                        while not game.over():
                            game.make_a_move_user("X")
                            game.make_a_move_user("O")
                        print(game.state_of_game)
                    elif command.split()[2] == 'easy':
                        game = TicTacToe()
                        print(game)
                        while not game.over():
                            game.make_a_move_user("X")
                            game.make_a_move_easy("O")
                        print(game.state_of_game)
                    elif command.split()[2] == 'medium':
                        game = TicTacToe()
                        print(game)
                        while not game.over():
                            game.make_a_move_user("X")
                            game.make_a_move_medium("O")
                        print(game.state_of_game)
                    else:
                        print('Bad parameters!')
                elif command.split()[1] == 'easy':
                    if command.split()[2] == 'user':
                        game = TicTacToe()
                        print(game)
                        while not game.over():
                            game.make_a_move_easy("X")
                            game.make_a_move_user("O")
                        print(game.state_of_game)
                    elif command.split()[2] == 'easy':
                        game = TicTacToe()
                        print(game)
                        while not game.over():
                            game.make_a_move_easy("X")
                            game.make_a_move_easy("O")
                        print(game.state_of_game)
                    elif command.split()[2] == 'medium':
                        game = TicTacToe()
                        print(game)
                        while not game.over():
                            game.make_a_move_easy("X")
                            game.make_a_move_medium("O")
                        print(game.state_of_game)
                    else:
                        print('Bad parameters!')
                elif command.split()[1] == 'medium':
                    if command.split()[2] == 'user':
                        game = TicTacToe()
                        print(game)
                        while not game.over():
                            game.make_a_move_medium("X")
                            game.make_a_move_user("O")
                        print(game.state_of_game)
                    elif command.split()[2] == 'easy':
                        game = TicTacToe()
                        print(game)
                        while not game.over():
                            game.make_a_move_medium("X")
                            game.make_a_move_easy("O")
                        print(game.state_of_game)
                    elif command.split()[2] == 'medium':
                        game = TicTacToe()
                        print(game)
                        while not game.over():
                            game.make_a_move_medium("X")
                            game.make_a_move_medium("O")
                        print(game.state_of_game)
                    else:
                        print('Bad parameters!')
                else:
                    print('Bad parameters!')
        else:
            print('Bad parameters!')


while True:
    TicTacToe.processing_command(input('Input command: > '))
