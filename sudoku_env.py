# sudoku_env
class SudokuEnv:
    def __init__(self, board):
        self.board = [row[:] for row in board]

    def is_valid(self, row, col, value):
        # Check the row
        if any(self.board[row][c] == value for c in range(9)):
            return False

        # Check the column
        if any(self.board[r][col] == value for r in range(9)):
            return False

        # Check 3×3 box
        start_row = row // 3 * 3
        start_col = col // 3 * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == value:
                    return False

        return True

    def get_empty_cell(self, row, col):
        empty = []
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    empty.append((r, c))
        return empty

    def apply_action(self, action):
        row, col, value = action
        # If the cell is empty and the input is valid, apply the number to the board
        if self.board[row][col] == 0 and self.is_valid(row, col, value):
            self.board[row][col] = value
            return True
        return False

    def is_solved(self):
        # If all the cells are not 0, return True
        return all(self.board[r][c] != 0 for r in range(9) for c in range(9))

    def print_board(self):
        for r in range(9):
            if r % 3 == 0:
                print("+-------+-------+-------+")
            row_str = "| "
            for c in range(9):
                val = self.board[r][c] if self.board[r][c] != 0 else "."
                row_str += str(val) + " "
                if (c + 1) % 3 == 0:
                    row_str += "| "
            print(row_str)
        print("+-------+-------+-------+")


