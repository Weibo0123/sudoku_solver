from sudoku_env import SudokuEnv
from sudoku_generator import generate_sudoku, create_sudoku

def main():
    # Prompt the player to choose difficulty
    print("Select Sudoku difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Expert")

    # Get player input
    choice = input("Enter difficulty number (1-4): ").strip()

    # Map choice to number of empty cells
    difficulty_map = {
        "1": 40,  # Easy
        "2": 50,  # Medium
        "3": 60,  # Hard
        "4": 70   # Expert
    }

    empty_cells = difficulty_map.get(choice, 40)  # Default to Easy

    # Generate a full Sudoku board
    full_board = generate_sudoku()

    # Create a puzzle with the specified number of empty cells
    puzzle = create_sudoku(full_board, empty_cells=empty_cells)

    # Initialize the environment and print the puzzle
    env = SudokuEnv(puzzle)
    env.print_board()

if __name__ == '__main__':
    main()
