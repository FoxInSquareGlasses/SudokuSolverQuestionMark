def find_next_empty(puzzle):
    # Finds the next (x, y) of the puzzle that is not filled yet
    # Return a tuple of (x, y) or (None, None) is there are no empty slots
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == -1:
                return (row, column)
    return (None, None)

def is_valid(puzzle, guess, row, column):
    # Figures whether a guess in puzzle[row][column] is valid
    
    # Rows
    row_values = puzzle[row]
    if guess in row_values:
        return False
    
    # Columns
    column_values = []
    for i in range(9):
        column_values.append(puzzle[i][column])
    # Or, alternatively: column_values = [puzzle[i][column] for i in range(9)]
    if guess in column_values:
        return False
    
    # Subsquare
    row_start = (row // 3) * 3
    column_start = (column // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(column_start, column_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    # Otherwise,
    return True

def solve_sudoku(puzzle):
    # We will use backtracking
    # Sudokus can be interpreted as a list of lits
    # Should return whether a solution exists
    # If true, then mutates puzzle to be the solution
    
    # Step 1: choose somewhere on the puzzle
    row, column = find_next_empty(puzzle)
    
    # Step 2: if there are no empty spots left, then we should be done
    if row is None and column is None:
        return True
    
    # Step 3: if there are empty spots, then take a guess! If valid, place that guess on the puzzle
    for guess in range(1, 10): # [1, 9]
        if is_valid(puzzle, guess, row, column):
            puzzle[row][column] = guess
            
            # Step 4: recursively call the function:
            if solve_sudoku(puzzle):
                return True
            
        # Step 5: if our guess does NOT solve the puzzle, then backtrack and try another number
        puzzle[row][column] = -1
    
    # Step 6: if none of the numbers we try work, then the puzzle is unsolvable
    return False

# Test sudoku
if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    evil_board = [
        [-1, -1, -1, -1, -1,  8, -1, -1, -1],
        [-1, -1,  7, -1, -1, -1, -1,  9, -1],
        [ 9, -1, -1,  4, -1,  5, -1, -1,  2],
        [ 7, -1, -1,  2, -1,  9, -1, -1,  5],
        [-1,  6, -1, -1, -1, -1,  3, -1, -1],
        [-1, -1, -1, -1,  1, -1, -1, -1, -1],
        [-1, -1,  3,  1, -1,  4,  5, -1, -1],
        [ 4, -1, -1, -1,  8, -1, -1, -1, -1],
        [-1, -1, -1, -1,  7, -1, -1, -1,  1]
    ]
    print(solve_sudoku(evil_board))
    # Print the board, but better:
    for line in evil_board:
        print(line)