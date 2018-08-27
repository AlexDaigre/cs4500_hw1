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
#   https://stackoverflow.com/questions/179369/how-do-i-abort-the-execution-of-a-python-script
#   https://docs.python.org/3/library/re.html#re.compile
#   https://regexr.com/

import sys
import re

def openInputFile():
    fileName = "HW1input.txt"
    return open(fileName, 'r')
    
def verifyInputFile(inputFile):
    linecount = getFileLineCount(inputFile)
    if linecount <= 0:
        print("Input file was empty.")
        return False
    #Unsure about spec
    # elif linecount > 40:
    #     print("Input has greater than 40 lines.")
    #     return False
    # elif (linecount % 2) != 0:
    #     print("Input does not .")
    #     return False
    for line in inputFile:
        if checklineFormat(line) != True:
            print("This input was not correct: ", line)
            return False
    return True

def getFileLineCount(inputFile):
    totallines = 0
    for line in inputFile:
        totallines += 1
    return totallines

def checklineFormat(line):
    lineRegExp = re.compile("/((?!24:)[0-2][0-9]:[0-5][0-9]\n)/g")
    if lineRegExp.match(line):
        return True
    else:
        print("This input was not correct: ", line)
        return False


inputFile = openInputFile()
if verifyInputFile(inputFile) != True:
    sys.exit(1)

