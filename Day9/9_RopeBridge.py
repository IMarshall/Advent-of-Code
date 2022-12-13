inputFile = open(r'C:\Users\imars\Documents\Advent of Code\Advent-of-Code\Day9\PuzzleInput.txt', 'r')

#defining necessary variables for figuring out grid size and knot starting position
rTotal = 0
lTotal = 0
uTotal = 0
dTotal = 0

vTotal = 0
vMax = 0
vMin = 0
hTotal = 0
hMax = 0
hMin = 0

for line in inputFile:
    instructions = (line.strip()).split()
    direction = instructions[0]
    count = int(instructions[1])

    #figure out how far the head moves in every direction
    if direction == "R":
        rTotal += count
        hTotal += count
        if hTotal > hMax:
            hMax = hTotal
        if hTotal < hMin:
            hMin = hTotal
        
    elif direction == "L":
        lTotal += count
        hTotal -= count
        if hTotal > hMax:
            hMax = hTotal
        if hTotal < hMin:
            hMin = hTotal

    elif direction == "U":
        uTotal += count
        vTotal -= count
        if vTotal > vMax:
            vMax = vTotal
        if vTotal < vMin:
            vMin = vTotal

    elif direction == "D":
        dTotal += count
        vTotal += count
        if vTotal > vMax:
            vMax = vTotal
        if vTotal < vMin:
            vMin = vTotal

#reset the input file so we can read through it again later
inputFile.seek(0)

#build the grid
gridHeight = abs(vMax - vMin + 1)
gridWidth = abs(hMax - hMin + 1)

grid = []

for row in range(gridHeight):
    newRow = []
    for col in range(gridWidth):
        newRow.append('.')
    grid.append(newRow)

startingPosition = [abs(vMin), abs(hMin)]

# make a knot class and instantiate the head and the tail, just to make it easier to reference their positions
class Knot:
    def __init__(self, row, col):
        self.row = row
        self.col = col

head = Knot(startingPosition[0], startingPosition[1])
tail = Knot(startingPosition[0], startingPosition[1])

#function to move the head movement - not actually marking the head on the grid because it's not necessary at least right now
def moveHead(direction):
    if direction == 'R':
        head.col += 1
    elif direction =='L':
        head.col -= 1
    elif direction == 'U':
        head.row -= 1
    elif direction == 'D':
        head.row += 1

#function to move the tail according to the movement of the head
def moveTail(direction):
    #only move the tail if the head is more than 2 units away - tail should always be aligned behind the head in direction of movement
    if abs(head.row - tail.row) > 1 or abs(head.col - tail.col) > 1:
        if direction == 'R':
            tail.col = head.col-1
            tail.row = head.row
        elif direction =='L':
            tail.col = head.col+1
            tail.row = head.row
        elif direction == 'U':
            tail.row = head.row+1
            tail.col = head.col
        elif direction == 'D':
            tail.row = head.row-1
            tail.col = head.col
    #mark each tail position on the grid
    grid[tail.row][tail.col] = '#'

# read the file again and move the head and tail according to the instructions
for line in inputFile:
    instructions = (line.strip()).split()
    direction = instructions[0]
    count = int(instructions[1])

    for i in range(count):
        moveHead(direction)
        moveTail(direction)

tailCount = 0

# look at each square on the grid and count how many squares have had the tail in them
for row in grid:
    for col in row:
        if col == '#':
            tailCount += 1

# Part 1 Solution
print(tailCount)