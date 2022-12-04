import numpy

inputFile = open(r'C:\Users\imars\Documents\Advent of Code\Day1\PuzzleInput.txt', 'r')

elves = [0]

newElf = True

for line in inputFile:
    if len(line.strip()) == 0:
        newElf = True
        elves.append(0)
    else:
        elves[len(elves)-1] += int(line)
        newElf = False

# Part 1 Solution:
print('Total of elf with most calories: ' + str(numpy.max(elves)))

# Part 2 Solution
sortedElves = numpy.sort(elves)

numberToReturn = 3

total = 0

for x in range(1, numberToReturn+1):
    total += sortedElves[len(sortedElves)-x]

print('Total of top ' + str(numberToReturn) + ' elves: ' + str(total))