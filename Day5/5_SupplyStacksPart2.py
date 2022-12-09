inputFile = open(r'C:\Users\imars\Documents\Advent of Code\Advent-of-Code\Day5\PuzzleInput.txt', 'r')

def createStackList():
    stackCount = 0
    stackList = []
    firstLine = True

    for line in inputFile:
        #finish the stack list when reader reaches stack number labels
        if "1" in line:
            return stackList

        index = 0

        #figure out how many stacks there are by dividing the line length by 4 (each stack is comprised of 4 characters)
        if stackCount == 0:
            stackCount = int(len(line)/4)

        #loop through each stack
        for i in range(stackCount):
            #add a new stack to the stacklist on the first time through
            if firstLine:
                newStack = []
                stackList.append(newStack)

            count = 0
            crate = ''

            #grab every four characters and place them in the crate variable
            while count < 4:
                crate += line[index]
                index += 1
                count += 1

            #if the crate variable contains an item (wrapped in []), remove the brackets and add it to the appropriate stack
            if '[' in crate:
                crate = crate.replace('[','')
                crate = crate.replace(']','')
                stackList[i].append(crate.strip())            
        
        firstLine = False
    

# Part 2 Solution:
stackList = createStackList()
print(stackList)

for line in inputFile:
    #run these instructions everytime a line has the word move in it
    if "move" in line:
        #split the line up and assign each of the digits to the appropriate variables
        instructions = line.split()
        total = int(instructions[instructions.index("move")+1])
        origin = int(instructions[instructions.index("from")+1])
        destination = int(instructions[instructions.index("to")+1])

        #insert the correct amount of items from the origin list into the beginning of the destination list, keeping them in order
        stackList[destination-1][0:0] = stackList[origin-1][0:total]
        #delete the items from the origin stack
        for i in range(total):
            stackList[origin-1].pop(0)

print(stackList)

#format the answer correctly
answer = ''
for stack in stackList:
    answer += stack[0]

print('The answer is: {0}'.format(answer))