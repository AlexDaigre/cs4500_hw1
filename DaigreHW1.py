# Alex Daigre
# Aug 27th, 2018
# cs4500
# Version: Python 3.7
# Description: This program takes an imput file containing unformated times, 
#   formats them and privides the diffrences between the pairs of times.
# External Files:
# Sources:
#   https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#   https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
#   https://stackoverflow.com/questions/179369/how-do-i-abort-the-execution-of-a-python-script
#   https://docs.python.org/3/library/re.html#re.compile
#   https://regexr.com/
#   https://www.w3schools.com/python/python_lists.asp
#   https://docs.python.org/3/library/stdtypes.html#str.rstrip
#   https://docs.python.org/2/library/time.html
#   https://stackoverflow.com/questions/10494312/parsing-time-string-in-python
#   https://stackoverflow.com/questions/44596077/datetime-strptime-in-python
#   https://docs.python.org/3/library/itertools.html#itertools-recipes

import sys
import re
import datetime
import itertools

def openInputFileAndGetContents():
    fileName = "HW1input.txt"
    fileContents = []
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            fileContents.append(line.rstrip())
    return fileContents

def openOutputFileAndWriteContents(outputData):
    fileName = "HW1output.txt"
    with open(fileName, 'w') as outputFile:
        for line in outputData:
            outputFile.write(line+"\n")
    
def verifyFileContents(fileContents, outputData):
    linecount = len(fileContents)
    if linecount <= 0:
        outputData.append("Input file was empty.")
        print("Input file was empty.")
        return False
    elif linecount > 40:
        outputData.append("Input has greater than 40 lines, please use between 0 and 40 lines.")
        print("Input has greater than 40 lines, please use between 0 and 40 lines.")
        return False
    for line in fileContents:
        if checklineFormat(line) != True:
            outputData.append("This input was not correct: " + line)
            return False
    return True

def getFileLineCount(inputFile):
    totalLines = 0
    for line in inputFile:
        totalLines += 1
    print("Line count: " + totalLines)
    return totalLines

def checklineFormat(line):
    lineRegExp = re.compile("((?!2[4-9]:)[0-2][0-9]:[0-5][0-9])")
    if lineRegExp.match(line):
        print("Verified: ", line)
        return True
    else:
        print("This input was not correct: " + line)
        return False

def generateOutput(fileContents, outputData):
    for a,b in pairwise(fileContents):
        print(a, b)

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


outputData = []
fileContents = openInputFileAndGetContents()
print("File open: ", fileContents)

if verifyFileContents(fileContents, outputData) != True:
    openOutputFileAndWriteContents(outputData)
    sys.exit()

generateOutput(fileContents, outputData)

outputData.append("All time pairs processed: program ending.")
print("All time pairs processed: program ending.")
