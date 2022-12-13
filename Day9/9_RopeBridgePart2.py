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
        newRow.append('')
    grid.append(newRow)

startingPosition = [abs(vMin), abs(hMin)]

# make a knot class and instantiate the head and the tails, just to make it easier to reference their positions
class Knot:
    def __init__(self, row, col):
        self.row = row
        self.col = col

head = Knot(startingPosition[0], startingPosition[1])

# create the number of tails we need and store them in a tails list so we can easily loop through them later
tailCount = 9

tails = []

for i in range(tailCount):
    newTail = Knot(startingPosition[0], startingPosition[1])
    tails.append(newTail)

#function to move the head - not actually marking the head on the grid because it's not necessary at least right now
def moveHead(direction):
    if direction == 'R':
        head.col += 1
    elif direction =='L':
        head.col -= 1
    elif direction == 'U':
        head.row -= 1
    elif direction == 'D':
        head.row += 1

#function to move the tails according to the movement of the knot directly in front of them
def moveTail(leader, tail, tailNumber):
    #only move the tail if the leader is more than 2 units away - tail should always be aligned behind the head in direction of movement
    #this first if statement is for diagonal movement (leader is more than 2 units away on both x and y axis)
    if abs(leader.row - tail.row) > 1 and abs(leader.col - tail.col) > 1:
        if leader.row > tail.row:
            tail.row = leader.row - 1
        else:
            tail.row = leader.row + 1
        if leader.col > tail.col:
            tail.col = leader.col - 1
        else:
            tail.col = leader.col + 1
        

    elif abs(leader.row - tail.row) > 1:
        if leader.row > tail.row:
            tail.row = leader.row - 1
            tail.col = leader.col
        else:
            tail.row = leader.row + 1
            tail.col = leader.col

    elif abs(leader.col - tail.col) > 1:
        if leader.col > tail.col:
            tail.col = leader.col - 1
            tail.row = leader.row
        else:
            tail.col = leader.col + 1
            tail.row = leader.row

    #mark each tail position on the grid
    grid[tail.row][tail.col] += str(tailNumber)

# read the file again and move the head and tails according to the instructions
for line in inputFile:
    instructions = (line.strip()).split()
    direction = instructions[0]
    count = int(instructions[1])

    for i in range(count):
        moveHead(direction)
        for i in range(len(tails)):
            if i == 0:
                moveTail(head, tails[i], i+1)
            else:
                moveTail(tails[i-1], tails[i], i+1)

# specify which tail we're counting unique positions for
whichTailToCount = 9

tailPositions = 0

# look at each square on the grid and count how many squares have had the tail in them
for row in grid:
    for col in row:
        if str(whichTailToCount) in col:
            tailPositions += 1

# Part 2 Solution
print(tailPositions)