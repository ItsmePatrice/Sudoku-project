import numpy as np


grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]


# Check if a number (n) can fit at a specific position. x for x-axis and y for y-axis
def possible(x, y, n):
    for i in range(0, 9): 
        # Check if any of the numbers in the y-axis correspond to n. If so, we don't want n because it's already in the column
        if grid[i][x] == n and i != y:
            return False
        
    for j in range(0, 9): #check row for number
        if grid[y][j] == n and j != x:
            return False
        
    # Make sure the number isn't in the square (box) of the current cell

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3 # try this (y // 3) * 3

    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 + 3):
            if grid[Y][X] == n:
                return False
            
    return True


def Print(matrix):
    for i in range(9):
        print(matrix[i])


# Solve the Sudoku using a backtracking algorithm
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        if solve():
                            return True
                        grid[y][x] = 0
                return False
    return True


solve()
Print(grid)
print("More?")
