inputFile = open(r'C:\Users\imars\Documents\Advent of Code\Day2\PuzzleInput.txt', 'r')

# Converts letters from each line into chosen RPS symbols
opponentSymbol = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

selfSymbol = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

# Converts each choice to the appropriate score
symbolScore = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

# Converts each result into the appropriate score
resultScore = {
    "win": 6,
    "draw": 3,
    "lose": 0
}

# Determines win/lose/draw for each player and returns an array representing those results
def findWinner(oppSymbol, selfSymbol):
    if oppSymbol == selfSymbol:
        return ["draw", "draw"]

    elif oppSymbol > selfSymbol:
        if oppSymbol != 3:
            return ["win", "lose"]
        elif selfSymbol == 2:
            return ["win", "lose"]
        elif selfSymbol == 1:
            return["lose", "win"]

    else:
        if selfSymbol != 3:
            return ["lose", "win"]
        if oppSymbol == 2:
            return ["lose", "win"]
        if oppSymbol == 1:
            return ["win", "lose"]

opponentScore = 0
selfScore = 0

for line in inputFile:
    # Add a score for the symbol each player chose
    opponentScore += symbolScore[opponentSymbol[line[0]]]
    selfScore += symbolScore[selfSymbol[line[2]]]

    # Figure out win/lose/draw for each player and store it in an array
    result = findWinner(symbolScore[opponentSymbol[line[0]]], symbolScore[selfSymbol[line[2]]])

    # Add a score for win/lose/draw result for each player
    opponentScore += resultScore[result[0]]
    selfScore += resultScore[result[1]]

# Part 1 Solution:
print("Opponent scored: " + str(opponentScore))
print("You scored: " + str(selfScore))

# Part 2 Solution:
