inputFile = open(r'C:\Users\imars\Documents\Advent of Code\Advent-of-Code\Day4\PuzzleInput.txt', 'r')

elfGroups = []

total = 0

for line in inputFile:  
    elfGroup = []
    string = line.strip()
    #split each line into a list containing the ranges of the two elves
    elves = string.split(',')
    for elf in elves:
        #split the range of each elf into a list containing the low and high, deleting the hyphen
        sections = elf.split('-')
        
        #add each list of ranges into a list of containing ranges for each of the two elves
        elfGroup.append(sections)
    
    #add each list containing two elves into an all encompassing list for all groups
    elfGroups.append(elfGroup)

#loop through the list of all groups
for pair in elfGroups:
    #compare the lows and highs of the elves in each group to determine which overlap
    if int(pair[0][1]) >= int(pair[1][0]) and int(pair[0][0]) <= int(pair[1][1]):
        #elf1 section extends into elf2 section
        total += 1

    #use elif here to make sure a group doesn't get counted twice if both ranges are exactly equal
    elif int(pair[0][0]) <= int(pair[1][1]) and int(pair[0][1]) >= int(pair[1][0]):
        #elf2 section extends into elf1 section
        total += 1


# Part 2 Solution:
print(total)