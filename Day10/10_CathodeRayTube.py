inputFile = open(r'C:\Users\imars\Documents\Advent of Code\Advent-of-Code\Day10\PuzzleInput.txt', 'r')

firstTarget = 20
interval = 40

cycle = 1
x = 1

rowLength = 40
rowCount = 6

targets = {}

def noop():
    addCycle()
        

def addx(value):
    global x
    addCycle()
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

#Part 1 Solution
for line in inputFile:
    line = line.strip()
    instructions = line.split()
    command = instructions[0]

    if command == 'noop':
        noop()
        
    elif command == 'addx':
        value = int(instructions[1])
        addx(value)

print(addTargets())