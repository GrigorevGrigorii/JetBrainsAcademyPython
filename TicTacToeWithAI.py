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
        list_of_all_combination = [board[0:3], board[3:6], board[6:9], board[0:7:3], board[1:8:3], board[2:9:3],
                                   board[0:9:4], board[2:7:2]]
        if any(combination == ['X', 'X', 'X'] for combination in list_of_all_combination):
            if board == self.board:
                self.state_of_game = "X wins"
            return "X wins"
        elif any(combination == ['O', 'O', 'O'] for combination in list_of_all_combination):
            if board == self.board:
                self.state_of_game = "O wins"
            return "O wins"
        elif board.count(" ") == 0:
            if board == self.board:
                self.state_of_game = "Draw"
            return "Draw"
        else:
            return ""

    def make_a_move(self, player, x=None, y=None, index=None):
        index = x - 3 * y + 8 if (x is not None and y is not None) else index
        self.board[index] = player
        print(self)

    def make_a_random_move(self, player):
        while True:
            rand_cell = random.randint(0, 8)
            if self.board[rand_cell] == " ":
                self.make_a_move(player, index=rand_cell)
                break

    def make_a_move_user(self, player):
        if not self.over():
            while True:
                x_y = input("Enter the coordinates: > ").strip()
                if x_y == "exit":
                    exit(0)
                try:
                    x, y = map(int, x_y.split())
                except ValueError:
                    print("You should enter two numbers!")
                else:
                    if 1 <= x <= 3 and 1 <= y <= 3:
                        if self.board[x - 3 * y + 8] == " ":
                            self.make_a_move(player, x=x, y=y)
                            break
                        else:
                            print("This cell is occupied! Choose another one!")
                    else:
                        print("Coordinates should be from 1 to 3!")

    def make_a_move_easy(self, player):
        if not self.over():
            print("Making move level \"easy\"")
            self.make_a_random_move(player)

    def make_a_move_medium(self, player):
        if not self.over():
            print("Making move level \"medium\"")
            opponent = 'O' if player == 'X' else 'X'
            cell = None
            for i in [i for i in range(9) if self.board[i] == ' ']:
                if self.over([self.board[j] if j != i else player for j in range(9)]):
                    self.make_a_move(player, index=i)
                    return
                if self.over([self.board[j] if j != i else opponent for j in range(9)]) and cell is None:
                    cell = i
            if cell is not None:
                self.make_a_move(player, index=cell)
            else:
                self.make_a_random_move(player)

    def minimax(self, new_board, player, maximizer_mark):
        state = self.over(new_board)
        if state == "Draw":
            return 0
        elif state:
            return 1 if state.split()[0] is maximizer_mark else -1

        scores = []
        for move in [i for i in range(9) if self.board[i] == ' ']:
            board_with_a_new_move = [self.board[i] if i != move else player for i in range(9)]
            opponent = 'O' if player == 'X' else 'X'
            scores.append(self.minimax(board_with_a_new_move, opponent, maximizer_mark))
        return max(scores) if player is maximizer_mark else min(scores)

    def make_a_move_hard(self, player):
        if not self.over():
            print("Making move level \"hard\"")
            if self.board.count(' ') == 9 or 8:
                self.make_a_random_move(player)
            else:
                best_score = -2
                best_move = None
                for move in [i for i in range(9) if self.board[i] == ' ']:
                    opponent = 'O' if player == 'X' else 'X'
                    board_with_a_new_move = [self.board[i] if i != move else player for i in range(9)]
                    score = self.minimax(board_with_a_new_move, opponent, player)
                    if score > best_score:
                        best_score = score
                        best_move = move
                self.make_a_move(player, index=best_move)

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
                elif command.split()[1] == 'user' and command.split()[2] == 'hard':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_user("X")
                        game.make_a_move_hard("O")
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
                elif command.split()[1] == 'easy' and command.split()[2] == 'hard':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_easy("X")
                        game.make_a_move_hard("O")
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
                elif command.split()[1] == 'medium' and command.split()[2] == 'hard':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_medium("X")
                        game.make_a_move_hard("O")
                    print(game.state_of_game)
                elif command.split()[1] == 'hard' and command.split()[2] == 'user':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_hard("X")
                        game.make_a_move_user("O")
                    print(game.state_of_game)
                elif command.split()[1] == 'hard' and command.split()[2] == 'easy':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_hard("X")
                        game.make_a_move_easy("O")
                    print(game.state_of_game)
                elif command.split()[1] == 'hard' and command.split()[2] == 'medium':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_hard("X")
                        game.make_a_move_medium("O")
                    print(game.state_of_game)
                elif command.split()[1] == 'hard' and command.split()[2] == 'hard':
                    game = TicTacToe()
                    while not game.over():
                        game.make_a_move_hard("X")
                        game.make_a_move_hard("O")
                    print(game.state_of_game)
                else:
                    print('Bad parameters!')
        else:
            print('Bad parameters!')


while True:
    TicTacToe.processing_command(input('Input command: > ').strip())
