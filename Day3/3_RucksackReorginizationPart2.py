inputFile = open(r'C:\Users\imars\Documents\Advent of Code\Advent-of-Code\Day3\PuzzleInput.txt', 'r')

# String to be used to figure out the priority of a given item, using priorityString.index(item) + 1
priorityString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

elfGroup = []

badges = []

total = 0

# function to find the matching item between all 3 elves
def findMatch(elf1, elf2, elf3):
    matches = []

    #find matches between elves 1 and 2
    for char1 in elf1:
        #save time by skipping any letters that are already known to be matches
        if char1 not in matches:
            for char2 in elf2:
                if char1 == char2:
                    #store the match in the matches array
                    matches.append(char1)
                    break

    #find common item between the matches array and elf 3 and return that item
    for match in matches:
        if match in elf3:
            return match    
    

for line in inputFile:
    #if the elfGroup is full then it has already been evaluated, so we clear the elfGroup array
    if len(elfGroup) == 3:
        elfGroup.clear()
    stripped = line.strip()

    #add the current elf to the elfGroup
    elfGroup.append(stripped)

    #if the elfGroup is full at this point then it needs to be evaluated
    if len(elfGroup) == 3:
        #find the common item between all 3 elves (the badge) and add it to the badges array
        badge = findMatch(elfGroup[0], elfGroup[1], elfGroup[2])
        badges.append(badge)

#find the priority of each badge and add it to the total
for char in badges:
    value = priorityString.index(char) + 1
    total += value

# Part 2 Solution:
print(total)