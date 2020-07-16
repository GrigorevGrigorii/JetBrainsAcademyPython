import random

random.seed()


class TicTacToe:
    def __init__(self, board="         "):
        self.board = list(board)
        self.state_of_game = "not finished"
        print(self)

    def __repr__(self):
        string = f"3  {self.board[0]} {self.board[1]} {self.board[2]}\n"
        string += f"2  {self.board[3]} {self.board[4]} {self.board[5]}\n"
        string += f"1  {self.board[6]} {self.board[7]} {self.board[8]}\n"
        string += "   1 2 3"
        return string

    def __str__(self):
        string = "---------\n"
        string += f"| {self.board[0]} {self.board[1]} {self.board[2]} |\n"
        string += f"| {self.board[3]} {self.board[4]} {self.board[5]} |\n"
        string += f"| {self.board[6]} {self.board[7]} {self.board[8]} |\n"
        string += "---------"
        return string

    def over(self, board=None):
        if board is None:
            board = self.board
        list_of_all_combination = [board[0:3], board[3:6], board[6:9], board[0:7:3], board[1:8:3], board[2:9:3], board[0:9:4], board[2:7:2]]
        if any([combination == ['X', 'X', 'X'] for combination in list_of_all_combination]):
            if board == self.board:
                self.state_of_game = "X wins"
            return True
        elif any([combination == ['O', 'O', 'O'] for combination in list_of_all_combination]):
            if board == self.board:
                self.state_of_game = "O wins"
            return True
        elif board.count(" ") == 0:
            if board == self.board:
                self.state_of_game = "Draw"
            return True
        else:
            return False

    def make_a_move(self, whose_move, x=None, y=None, index=None):
        index = x - 3 * y + 8 if (x is not None and y is not None) else index
        self.board[index] = whose_move
        print(self)

    def make_a_random_move(self, whose_move):
        while True:
            rand_cell = random.randint(0, 8)
            if self.board[rand_cell] == " ":
                self.make_a_move(whose_move, index=rand_cell)
                break

    def make_a_move_user(self, whose_move):
        if not self.over():
            while True:
                x_y = input("Enter the coordinates: > ").strip()
                if x_y == "exit":
                    exit(0)
                if all([n.isdigit() for n in x_y.split()]) and len(x_y.split()) == 2:
                    x, y = map(int, x_y.split())
                    if 1 <= x <= 3 and 1 <= y <= 3:
                        if self.board[x - 3 * y + 8] == " ":
                            self.make_a_move(whose_move, x=x, y=y)
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
            self.make_a_random_move(whose_move)

    def make_a_move_medium(self, whose_move):
        if not self.over():
            print("Making move level \"medium\"")
            opponent = "O" if whose_move == "X" else "X"
            cell = None
            for i in range(9):
                if self.board[i] == " ":
                    if self.over([self.board[j] if j != i else whose_move for j in range(9)]):
                        self.make_a_move(whose_move, index=i)
                        return
                    if self.over([self.board[j] if j != i else opponent for j in range(9)]) and cell is None:
                        cell = i
            if cell is not None:
                self.make_a_move(whose_move, index=cell)
            else:
                self.make_a_random_move(whose_move)

    @staticmethod
    def processing_command(command):
        if command == "exit":
            exit(0)
        elif len(command.split()) == 3:
            if command.split()[0] == 'start':
                if command.split()[1] == 'user' and command.split()[2] == 'user':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_user("X")
                        game.make_a_move_user("O")
                    print(game.state_of_game)
                elif command.split()[1] == 'user' and command.split()[2] == 'easy':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_user("X")
                        game.make_a_move_easy("O")
                    print(game.state_of_game)
                elif command.split()[1] == 'user' and command.split()[2] == 'medium':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_user("X")
                        game.make_a_move_medium("O")
                    print(game.state_of_game)
                elif command.split()[1] == 'easy' and command.split()[2] == 'user':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_easy("X")
                        game.make_a_move_user("O")
                    print(game.state_of_game)
                elif command.split()[1] == 'easy' and command.split()[2] == 'easy':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_easy("X")
                        game.make_a_move_easy("O")
                    print(game.state_of_game)
                elif command.split()[1] == 'easy' and command.split()[2] == 'medium':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_easy("X")
                        game.make_a_move_medium("O")
                    print(game.state_of_game)
                elif command.split()[1] == 'medium' and command.split()[2] == 'user':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_medium("X")
                        game.make_a_move_user("O")
                    print(game.state_of_game)
                elif command.split()[1] == 'medium' and command.split()[2] == 'easy':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_medium("X")
                        game.make_a_move_easy("O")
                    print(game.state_of_game)
                elif command.split()[1] == 'medium' and command.split()[2] == 'medium':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_medium("X")
                        game.make_a_move_medium("O")
                    print(game.state_of_game)
                else:
                    print('Bad parameters!')
        else:
            print('Bad parameters!')


while True:
    TicTacToe.processing_command(input('Input command: > ').strip())
