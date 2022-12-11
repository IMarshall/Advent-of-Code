inputFile = open(r'C:\Users\imars\Documents\Advent of Code\Advent-of-Code\Day8\PuzzleInput.txt', 'r')

forest = []

visibleTrees = 0

# FUNCTION TO CHECK EACH ROW FOR TREES VISIBLE FROM THE SIDES
def checkRow(row, col):
    treeRow = forest[row]
    tree = forest[row][col]
    
    blockedRight = False
    blockedLeft = False

    # OUTSIDE TREES AUTOMATICALLY MARKED VISIBLE
    if col == 0 or col == len(treeRow)-1:
        return True

    else:
        # CHECK EACH TREE TO THE RIGHT
        for i in range(col+1,len(treeRow)):
            if treeRow[i] >= tree:
                blockedRight = True
                break
        # CHECK EACH TREE TO THE LEFT
        for i in range(col-1, -1, -1):
            if treeRow[i] >= tree:
                blockedLeft = True
                break
    
    # IF TREE NOT VISIBLE FROM EITHER SIDE, RETURN FALSE
    if blockedLeft and blockedRight:
        return False
    # IF TREE IS VISIBLE RETURN TRUE
    else:
        return True

# FUNCTION TO CHECK EACH COLUMN FOR TREES VISIBLE FROM NORTH OR SOUTH
def checkCol(row, col):
    tree = forest[row][col]

    blockedTop = False
    blockedBot = False

    # OUTSIDE TREES AUTOMATICALLY MARKED VISIBLE
    if row == 0 or row == len(forest)-1:
        return True
    
    # CHECK EACH TREE TO THE SOUTH
    for i in range(row+1, len(forest)):
        if forest[i][col] >= tree:
            blockedBot = True
            break
    # CHECK EACH TREE TO THE NORTH
    for i in range(row-1, -1, -1):
        if forest[i][col] >= tree:
            blockedTop = True
            break

    # IF TREE NOT VISIBLE FROM NORTH OR SOUTH, RETURN FALSE
    if blockedTop and blockedBot:
        return False
    # IF TREE VISIBLE FROM NORTH OR SOUTH, RETURN TRUE
    else:
        return True

# Part 1 Solution:

for line in inputFile:
    newRow = []
    # DIVIDE EACH LINE INTO A LIST
    for char in line.strip():
        newRow.append(int(char))
    # CREATE A LIST OF LISTS REPRESENTING THE FOREST
    forest.append(newRow)

row = 0
col = 0

for treeRow in forest:
    for tree in treeRow:
        if col >= len(forest[0]):
            col = 0
            row += 1

        # CHECK EACH TREE FOR VISIBILITY FROM SIDES
        if checkRow(row, col) == False:
            # IF NOT VISIBLE FROM SIDES, CHECK NORTH AND SOUTH. IF VISIBLE FROM NORTH OR SOUTH, ADD TO TOTAL
            if checkCol(row, col) == True:
                visibleTrees += 1
        # IF VISIBLE FROM SIDES, ADD TO TOTAL
        else:
            visibleTrees += 1

        col += 1

print("Visible trees: {}".format(visibleTrees))