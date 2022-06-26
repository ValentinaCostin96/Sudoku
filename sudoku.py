'''
Author: Valentina Costin
Project: Sudoku using backtraking
Description: The table game is a list of lists where each inner list is a row in sudoku game
'''

def find_next_empty(table):
    ''' 
    Find the next row, col which is empty.
    Returns a tuple (row, col) or (None, None) if there is none
    '''

    for row in range(9):
        for col in range(9):
            if table[row][col] == -1:
                return row, col

    return None, None # if there is no empty space on the table

def is_valid(table, guess_number, row, col):
    ''' Check if that guess number is valid on the row, col position '''
    
    row_vals = table[row]

    # check if the value already exists on the row
    if guess_number in row_vals:
        return False

    col_vals = []

    for i in range(9):
        col_vals.append(table[i][col])
  
   # check if the value already exists on the column
    if guess_number in col_vals:
        return False

    # check if the value already exists on the square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if table[r][c] == guess_number:
                return False

    return True

def sudoku(table):
    row, col =  find_next_empty(table)

    # Check if we still have empty cells
    if row is None:
        return True 

    # if we have empty cells than we can make a guess between [1,9]
    for guess_number in range(1, 10):
        # check if the number is valid and write it on the table if it is
        if is_valid(table, guess_number, row, col):
            table[row][col] = guess_number 

            # call sudoku function recursively 
            if sudoku(table):
                return True

        # if the number is not valid, we have to backtrack and try another number
        table[row][col] = -1 # reset the guess cell

    # if none of the numbers which we tried did not work then this game is unsolvable!!!
    return False

if __name__ == '__main__':
    table = [
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

    if sudoku(table) == False:
        with open('sudoku_solution.txt', 'w') as file_sudoku:
            for row in table:
                file_sudoku.write(str(row) + "\n")
    else:
        print("This game has no solution!")

    print("End Sudoku!")