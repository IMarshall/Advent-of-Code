inputFile = open(r'C:\Users\imars\Documents\Advent of Code\Advent-of-Code\Day8\PuzzleInput.txt', 'r')

forest = []

visibleTrees = 0

bestScenicScore = 0

# CREATE CLASS TO EASILY STORE TREE PROPERTIES
class Tree:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.scenicScore = 0

allTrees = []

# FUNCTION TO CHECK EACH ROW FOR TREE VIEW DISTANCE FROM THE SIDES
def checkRow(row, col):
    newTree = Tree(row, col)
    allTrees.append(newTree)

    treeRow = forest[row]
    tree = forest[row][col]
    
    blockedRight = False
    blockedLeft = False

    viewDistanceLeft = 0
    viewDistanceRight = 0

    # OUTSIDE TREES AUTOMATICALLY GIVEN SCENIC SCORE 0
    if col == 0 or col == len(treeRow)-1:
        newTree.scenicScore = 0
        return newTree

    else:
        # CHECK VIEW DISTANCE TO THE RIGHT
        for i in range(col+1,len(treeRow)):
            if treeRow[i] >= tree:
                blockedRight = True
                viewDistanceRight = i-col
                break
        # CHECK VIEW DISTANCE TO THE LEFT
        for i in range(col-1, -1, -1):
            if treeRow[i] >= tree:
                blockedLeft = True
                viewDistanceLeft = col-i
                break
    
    # IF TREE IS VISIBLE RETURN VIEW DISTANCE TO EDGE OF FOREST
    if not blockedLeft:
        viewDistanceLeft = col
    if not blockedRight:
        viewDistanceRight = len(treeRow)-col-1
    
    # CALCULATE SCENIC SCORE AND RETURN THE TREE
    newTree.scenicScore = viewDistanceLeft * viewDistanceRight

    return newTree


# FUNCTION TO CHECK EACH COLUMN FOR TREES VISIBLE FROM NORTH OR SOUTH
def checkCol(newTree):
    row = newTree.row
    col = newTree.col

    tree = forest[row][col]

    blockedTop = False
    blockedBot = False

    viewDistanceTop = 0
    viewDistanceBot = 0

    # OUTSIDE TREES AUTOMATICALLY MARKED VISIBLE
    if row == 0 or row == len(forest)-1:
        newTree.scenicScore = 0
        return newTree
    
    # CHECK VIEW DISTANCE TO THE SOUTH
    for i in range(row+1, len(forest)):
        if forest[i][col] >= tree:
            blockedBot = True
            viewDistanceBot = i - row
            break
    # CHECK VIEW DISTANCE TO THE NORTH
    for i in range(row-1, -1, -1):
        if forest[i][col] >= tree:
            blockedTop = True
            viewDistanceTop = row - i
            break

    # IF TREE VISIBLE RETURN DISTANCE TO EDGE OF FOREST
    if not blockedTop:
        viewDistanceTop = row
    if not blockedBot:
        viewDistanceBot = len(forest)-row-1

    # CALCULATE SCENIC SCORE AND RETURN THE TREE
    newTree.scenicScore = newTree.scenicScore * viewDistanceTop * viewDistanceBot

    return newTree

# Part 2 Solution:

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

        # GET SCENIC SCORE
        tree = checkRow(row, col)
        checkCol(tree)
        
        # IF THIS IS THE BEST SCENIC SCORE SO FAR, RECORD IT
        if tree.scenicScore > bestScenicScore:
            bestScenicScore = tree.scenicScore

        col += 1

print("Best Scenic Score: {}".format(bestScenicScore))