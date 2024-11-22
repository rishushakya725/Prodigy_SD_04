def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def print_solved_answers(original, solved):
    # Print only the answers (newly filled numbers) while hiding the original numbers
    for i in range(9):
        for j in range(9):
            # Only show the solved number if the original cell was empty (0)
            if original[i][j] == 0:
                print(solved[i][j], end=" ")
            else:
                print(".", end=" ")
        print()  # Newline after each row

def is_valid(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def take_user_input():
    grid = []
    print("Enter your Sudoku puzzle (use 0 for empty cells):")
    for i in range(9):
        while True:
            try:
                row = input(f"Enter row {i+1} (9 numbers separated by spaces): ").split()
                if len(row) == 9 and all(num.isdigit() and 0 <= int(num) <= 9 for num in row):
                    grid.append([int(num) for num in row])
                    break
                else:
                    print("Invalid input. Please enter exactly 9 numbers between 0 and 9.")
            except ValueError:
                print("Invalid input. Please try again.")
    return grid

# Taking the Sudoku puzzle as input from the user
sudoku_grid = take_user_input()

# Display the unsolved Sudoku puzzle
print("\nUnsolved Sudoku Puzzle:")
print_grid(sudoku_grid)

# Copy the original grid to keep track of the initial state
original_grid = [row[:] for row in sudoku_grid]

# Solve the puzzle
if solve_sudoku(sudoku_grid):
    print("\nSolved Sudoku Puzzle:")
    print_grid(sudoku_grid)
    
    print("\nAnswers Only (showing only filled cells):")
    print_solved_answers(original_grid, sudoku_grid)
else:
    print("No solution exists for the given Sudoku puzzle.")
