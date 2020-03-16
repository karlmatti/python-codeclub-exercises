class TicTacToe:
    def __init__(self):

        self.game = [[None, None, None], [None, None, None], [None, None, None]]
        self.state = 3

    def get_state(self):
        return self.state

    def add_move(self, row, col, player):
        if player == 'x':
            self.game[row][col] = 'x'
        elif player == 'O':
            self.game[row][col] = 'o'
        self.calculate_winner()
        for x in range(3):
            print(self.game[x])
        print('\n')

        if self.state == 3:
            self.check_tie()


    def calculate_winner(self):
        if self.check_diagonals() != 0:
            if self.check_diagonals() == 'o':
                self.state = 0
            elif self.check_diagonals() == 'x':
                self.state = 1
        elif self.check_columns() != 0:
            if self.check_columns() == 'o':
                self.state = 0
            elif self.check_columns() == 'x':
                self.state = 1
        elif self.check_rows() != 0:
            if self.check_rows() == 'o':
                self.state = 0
            elif self.check_rows() == 'x':
                self.state = 1

    def check_diagonals(self):
        grid = self.game
        diag1 = {grid[0][0], grid[1][1], grid[2][2]}
        diag2 = {grid[0][2], grid[1][1], grid[2][0]}
        if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
            return grid[1][1]
        else:
            return 0

    def check_columns(self):
        grid = self.game
        # columns
        for x in range(0, 3):
            column = {grid[0][x], grid[1][x], grid[2][x]}
            if len(column) == 1 and grid[0][x] != 0:
                return grid[0][x]
        return 0

    def check_rows(self):
        grid = self.game
        # rows
        for x in range(0, 3):
            row = {grid[x][0], grid[x][1], grid[x][2]}

            if len(row) == 1 and grid[x][0] != 0:
                return grid[x][0]
        return 0
    def check_tie(self):
        if None not in self.game:
            self.state = 2



game = TicTacToe()

game.add_move(0, 0, 'x')
game.add_move(0, 1, 'O')
game.add_move(0, 2, 'x')
game.add_move(1, 0, 'x')
game.add_move(1, 1, 'O')
game.add_move(1, 2, 'x')
game.add_move(2, 0, 'O')
game.add_move(2, 1, 'x')
game.add_move(2, 2, 'O')
print(game.get_state())