import pyautogui as pg
import numpy as np
import time


grid = []

# Taking input from the user to populate the grid
while True:
    row = list(input("Row: ")) # Convert the user's input into a list of individual characters
    ints = []

    for n in row:
        ints.append(int(n))
    grid.append(ints)

    if len(grid) == 9:
        break
    print("Row " + str(len(grid)) + " complete")



time.sleep(1)


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
    final = []
    str_fin = []
    for i in range(9):
        print(matrix[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))

    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey("right")
        counter.append(num)
        if len(counter) % 9 == 0:
            pg.hotkey("down")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")



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
