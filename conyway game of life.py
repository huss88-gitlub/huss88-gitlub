import random
import time
import copy

WIDTH = 60
HEIGHT = 20

# Initialize the grid with random states
nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextCells.append(column)

while True:
    print("\n\n\n\n\n")
    currentCells = copy.deepcopy(nextCells)

    # Print the current state of cells
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()

    # Calculate the next state of cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCord = (x - 1) % WIDTH
            rightCord = (x + 1) % WIDTH
            aboveCord = (y - 1) % HEIGHT
            belowCord = (y + 1) % HEIGHT

            numE = 0
            if currentCells[leftCord][aboveCord] == '#':
                numE += 1
            if currentCells[x][aboveCord] == '#':
                numE += 1
            if currentCells[rightCord][aboveCord] == '#':
                numE += 1
            if currentCells[leftCord][y] == '#':
                numE += 1
            if currentCells[rightCord][y] == '#':
                numE += 1
            if currentCells[leftCord][belowCord] == '#':
                numE += 1
            if currentCells[x][belowCord] == '#':
                numE += 1
            if currentCells[rightCord][belowCord] == '#':
                numE += 1

            # Apply Conway's Game of Life rules
            if currentCells[x][y] == '#' and (numE == 2 or numE == 3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numE == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '

    time.sleep(1)
