inputFile = open(r'C:\Users\imars\Documents\Advent of Code\Day2\PuzzleInput.txt', 'r')

# Converts first letter into chosen RPS symbol
opponentSymbol = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

# Converts second letter into the desired result
desiredResult = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
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

# Given the opponent's choice and the desired result, returns what the player should choose
def findSelfSymbol(oppSymbol, desiredResult):
    selfSymbol = ""

    symbols = ["rock", "paper", "scissors"]

    if desiredResult == "draw":
        selfSymbol = oppSymbol
    elif desiredResult == "lose":
        if oppSymbol == "rock":
            selfSymbol = "scissors"
        else:
            selfSymbol = symbols[symbols.index(oppSymbol)-1]
    elif desiredResult == "win":
        if oppSymbol == "scissors":
            selfSymbol = "rock"
        else:
            selfSymbol = symbols[symbols.index(oppSymbol)+1]

    return selfSymbol
    

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
    # Assign the symbol that the player should choose to the selfSymbol variable
    selfSymbol = findSelfSymbol(opponentSymbol[line[0]], desiredResult[line[2]])

    # Add a score for the symbol each player chose
    opponentScore += symbolScore[opponentSymbol[line[0]]]
    selfScore += symbolScore[selfSymbol]

    # Figure out win/lose/draw for each player and store it in an array
    result = findWinner(symbolScore[opponentSymbol[line[0]]], symbolScore[selfSymbol])

    # Add a score for win/lose/draw result for each player
    opponentScore += resultScore[result[0]]
    selfScore += resultScore[result[1]]

# Part 2 Solution:
print("Opponent scored: " + str(opponentScore))
print("You scored: " + str(selfScore))
