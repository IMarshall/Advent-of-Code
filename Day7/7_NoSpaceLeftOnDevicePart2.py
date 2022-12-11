import numpy

inputFile = open(r'C:\Users\imars\Documents\Advent of Code\Advent-of-Code\Day7\PuzzleInput.txt', 'r')

listing = False

folders = []

largeFolders = []

diskSpace = 70000000

requiredSpace = 30000000

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

# Part 2 Solution:
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
                folderExists = False
                for folder in currentDirectory.subfolders:
                    if folder.name == target:
                        currentDirectory = folder
                        folderExists = True
                        break
                if folderExists == False:
                    newFolder = Folder(target, currentDirectory)
                    currentDirectory = newFolder
                    newFolder.parent.subfolders.append(newFolder)
                    folders.append(newFolder)
            if target == "..":
                # move the current directory up a level if the "cd .." command is given
                currentDirectory = currentDirectory.parent
        # this is unnecessary right now, but thought I'd add it if I need to differentiate more between command line input and output 
        # in the future
        if command == "ls":
            listing = True
    elif "$" not in line and listing == True:
        lineList = line.split()
        # if a new file is listed, create that file and assign it to all necessary variables and parents
        if lineList[0].isdigit():
            fileExists = False
            for file in currentDirectory.files:
                if file.name == lineList[1]:
                    fileExists = True
            if fileExists == False:
                newFile = File(lineList[1], lineList[0])
                currentDirectory.files.append(newFile)
                #any time a new file is added, update the size of the current folder and all of its parent folders
                currentDirectory.updateSize()
                parentDirectory = currentDirectory.parent
                while parentDirectory != None:
                    parentDirectory.updateSize()
                    parentDirectory = parentDirectory.parent

#figure out how much space has been used and how much needs to be opened up to perform the update
usedDiskSpace = 0

for folder in folders:
    if folder.name == "/":
        usedDiskSpace = folder.size

spaceAvailable = diskSpace - usedDiskSpace

spaceToOpen = requiredSpace - spaceAvailable

#get a list of all folders large enough to allow the update if they were deleted
for folder in folders:
    if folder.size >= spaceToOpen:
        largeFolders.append(folder.size)

#sort that list in ascending order
largeFoldersSorted = numpy.sort(largeFolders)

#print the first item in the sorted list, which is the smallest folder that will free up enough space for the update
print(largeFoldersSorted[0])