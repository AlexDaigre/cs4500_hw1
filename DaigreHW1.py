# Alex Daigre
# Aug 27th, 2018
# cs4500
# Version: Python 3.6
# Description: This program takes an imput file containing unformated times, 
#   formats them and privides the diffrences between the pairs of times.
# External Files:
# Sources:
#   https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#   https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python

def openInputFile():
    fileName = "HW1input.txt"
    return open(fileName, 'r')
    
def verifyInputFile(inputFile):
    linecount = getFileLineCount(inputFile)
    if linecount <= 0:
        print("Input file was empty.")

def getFileLineCount(inputFile):
    totallines = 0
    for line in inputFile:
        totallines += 1
    return totallines

def checkFileFormat(inputFile):
    print("")

inputFile = openInputFile()
verifyInputFile(inputFile)