inputFile = open(r'C:\Users\imars\Documents\Advent of Code\Advent-of-Code\Day3\PuzzleInput.txt', 'r')

# String to be used to figure out the priority of a given item, using priorityString.index(item) + 1
priorityString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

matches = []

total = 0

#function to find the matching item between the two compartments
def findMatch(compartment1, compartment2):
    for char1 in compartment1:
        for char2 in compartment2:
            if char1 == char2:
                return char1

for line in inputFile:
    stripped = line.strip()
    #get the size of the complete rucksack by removing whitespace from each line and getting the length
    rucksackSize = len(stripped)
    #get the size of each compartment by dividing that in half
    compartmentSize = rucksackSize/2
    #splice the rucksack string into two halves representing each of the compartments
    compartment1 = stripped[0:int(compartmentSize)]
    compartment2 = stripped[int(compartmentSize):len(stripped)]
    #find the match between the two compartments and add it to the matches array
    match = findMatch(compartment1, compartment2)
    matches.append(match)

#find the priority of each match and add it to the total
for char in matches:
    value = priorityString.index(char) + 1
    total += value    

# Part 1 Solution:
print(total)