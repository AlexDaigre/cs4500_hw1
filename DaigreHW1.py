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
#   

import sys
import re

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


fileContents = openInputFileAndGetContents()
outputData = []
print("File open: ", fileContents)
if verifyFileContents(fileContents, outputData) != True:
    outputData.append("input file was not verified")
    print("input file was not verified")
else:
    outputData.append("All time pairs processed: program ending.")
    print("All time pairs processed: program ending.")
openOutputFileAndWriteContents(outputData)

