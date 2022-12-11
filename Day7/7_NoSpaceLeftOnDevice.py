import numpy

inputFile = open(r'C:\Users\imars\Documents\Advent of Code\Advent-of-Code\Day7\PuzzleInput.txt', 'r')

listing = False

folders = []

smallFolders = []

# define class for all folders/files to hold their different attributes and allow me to access/move between them easily
class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = []
        self.subfolders = []
        self.size = 0

    # define method to allow me to update the size of a folder each time a file is added to that folder or a subfolder
    def updateSize(self):
        self.size = 0
        filesSize = 0
        foldersSize = 0

        for file in self.files:
            filesSize += file.size
        self.size += filesSize

        for folder in self.subfolders:
            foldersSize += folder.size
        self.size += foldersSize
            

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

outerDirectory = Folder("outer")

# global variable to keep track of which directory the user is currently in
currentDirectory = outerDirectory

# Part 1 Solution:
for line in inputFile:
    if "$" in line:
        listing = False
        lineList = line.split()
        #define the command (whatever comes after the $)
        command = lineList[lineList.index("$")+1]
        if command == "cd":
            #define the target (whatever comes after the cd)
            target = lineList[lineList.index("cd")+1]
            if target != "..":
                # if the user enters a new directory, create that directory and assign it to all necessary variables and parents
                # could run into errors here if entering a directory twice, because it would be duplicated
                # should check to see if the folder already exists first
                newFolder = Folder(target, currentDirectory)
                currentDirectory = newFolder
                newFolder.parent.subfolders.append(newFolder)
                folders.append(newFolder)

                # useful print statement for showing how we're moving between directories
                # print(newFolder.parent.name + " --> " + newFolder.name)
            if target == "..":
                # useful print statement for showing how we're moving between directories
                # print(currentDirectory.parent.name + " <-- " + currentDirectory.name)

                # move the current directory up a level if the "cd .." command is given
                currentDirectory = currentDirectory.parent
        # this is unnecessary right now, but thought I'd add it if I need to differentiate more between command line input and output 
        # in the future
        if command == "ls":
            listing = True
    elif "$" not in line and listing == True:
        lineList = line.split()
        # if a new file is listed, create that file and assign it to all necessary variables and parents
        # could run into errors here if the list command is run on the same directory more than once, because files would be duplicated
        # should check to see if the file already exists first
        if lineList[0].isdigit():
            newFile = File(lineList[1], lineList[0])
            currentDirectory.files.append(newFile)
            #any time a new file is added, update the size of the current folder and it's parent folder
            #this doesn't work properly if the file tree gets too deep, because you need to update parents of parents and so on
            #I'm sure I could come up with a solution, but it's not necessary in this instance of the program
            currentDirectory.updateSize()
            currentDirectory.parent.updateSize()

for folder in folders:
    #update the size of all folders one more, to make sure all changes have risen to the top
    folder.updateSize()

    # these are just some useful print statements for showing all the properties of each folder
    # print("Folder: " + folder.name)
    # print("Files: ")
    # for file in folder.files:
    #     print("{0} - {1}".format(file.name, file.size))
    # print("Subfolders: ")
    # for subfolder in folder.subfolders:
    #     print(subfolder.name)
    # print("Size: " + str(folder.size))


    if folder.size <= 100000:
        smallFolders.append(folder)

total = 0

for folder in smallFolders:
    total += folder.size

print(total)