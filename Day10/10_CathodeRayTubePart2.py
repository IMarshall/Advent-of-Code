import math

inputFile = open(r'C:\Users\imars\Documents\Advent of Code\Advent-of-Code\Day10\PuzzleInput.txt', 'r')

firstTarget = 20
interval = 40

cycle = 1
x = 1

screen = []
rowLength = 40
rowCount = 6

targets = {}

def renderPixel():
    row = int(math.floor((cycle-1)/rowLength))
    if x-1 <= (cycle-1)%rowLength <= x+1:
        screen[row][(cycle-1)%rowLength] = '#'
    else:
        screen[row][(cycle-1)%rowLength] = '.'

def noop():
    renderPixel()
    addCycle()

def addx(value):
    global x
    renderPixel()
    addCycle()
    renderPixel()
    x += value
    addCycle()

def addCycle():
    global cycle
    global x
    cycle += 1
    if cycle == firstTarget or (cycle-firstTarget)%interval == 0:
        targets[cycle] = cycle*x

def addTargets():
    total = 0
    for targetValue in targets.values():
        total += targetValue
    return total

# BUILD 2D ARRAY
for i in range(rowCount):
    newRow = []
    for n in range(rowLength):
        newRow.append('-')
    screen.append(newRow)


#Part 2 Solution
for line in inputFile:
    line = line.strip()
    instructions = line.split()

    command = instructions[0]
    print(line)
    if command == 'noop':
        noop()
        
    elif command == 'addx':
        value = int(instructions[1])
        addx(value)

for r in screen:
    print(r)