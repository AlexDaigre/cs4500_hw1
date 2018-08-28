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
#   https://realpython.com/python-f-strings/
#   https://stackoverflow.com/questions/3096953/how-to-calculate-the-time-interval-between-two-time-strings
#   https://stackoverflow.com/questions/27942128/get-everything-after-last-character-occurrence-python
#   https://docs.python.org/2/library/string.html
#   https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation

import sys
import re
import datetime
import itertools

# Opens our input file and stores the contents in a list.
# Each line is its own enrty in the list.
def openInputFileAndGetContents():
    fileName = "HW1input.txt"
    fileContents = []
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            fileContents.append(line.rstrip())
    return fileContents

# Opens the output file and writes the contents to it.
# takes our output data and writes each element in the list to its own line.
def openOutputFileAndWriteContents(outputData):
    fileName = "HW1output.txt"
    with open(fileName, 'w') as outputFile:
        for line in outputData:
            outputFile.write(line+"\n")

# Verifies the file contents for correct number of lines and correct 
# formating of individual lines.
def verifyFileContents(fileContents, outputData):
    linecount = len(fileContents)
    if linecount <= 0:
        outputData.append("Input file was empty.")
        print("Input file was empty.")
    elif linecount > 40:
        outputData.append("Input has greater than 40 lines, please use between 0 and 40 lines.")
        print("Input has greater than 40 lines, please use between 0 and 40 lines.")
    else:
        for line in fileContents:
            if checklineFormat(line) != True:
                outputData.append("This input was not correct: " + line)
    return outputData

# Uses a regular expression to check if our data maches the format in 
# the specifications.
def checklineFormat(line):
    lineRegExp = re.compile("((?!2[4-9]:)[0-2][0-9]:[0-5][0-9])")
    if lineRegExp.match(line):
        print("Verified: ", line)
        return True
    else:
        print("This input was not correct: " + line)
        return False

# Here we generate the, non-error output to write to our file.
# We loop over the the data we got from our input file, find the
# time diffrences and format all resulting data, then handle whether our data
# had an even or odd number of lines  
def generateOutput(fileContents, outputData):
    for index, times in enumerate(pairwise(fileContents)):
        # The pairwise itterator returns every element compaired with the next:
        # eg. s -> (s0, s1) (s1, s2) etc. However we only want everyother pair 
        # like this so we only run the code every other itteration
        if index % 2 == 0:
            timeDiffrence = getTimeDifference(times[0], times[1])
            outputData.append(f"{times[0]}, {times[1]} => {timeDiffrence}")
            print(f"{times[0]}, {times[1]} => {timeDiffrence}")
    # The itterator raises stop iteration on last element of stop iteration 
    # as a full pair cannot be generated. As such, we handle that last element here.
    # If the list was even, we add the appropriate message here
    if len(fileContents) % 2 != 0:
        outputData.append(f"There was not a matching time for this time: {fileContents[len(fileContents)-1]}")
        print(f"There was not a matching time for this time: {fileContents[len(fileContents)-1]}")
    else:
        outputData.append("All time pairs processed: program ending.")
        print("All time pairs processed: program ending.")
    return outputData

# This is one of the recipies from https://docs.python.org/3/library/itertools.html#itertools-recipes
# We use it to generate an itterator that returns each element mached with the next 
# element.
def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

# We transfor each of our times to a dateTime object, then perform the subtraction,
# and then we transform the resulting timeDelta back into a formated string.
# When generating the output, as we have no dates, we always assume the shortest 
# time between the two dates.
def getTimeDifference(time1, time2):
    pythonTime1 = transformStringTimeToPythonTime(time1)
    pythonTime2 = transformStringTimeToPythonTime(time2)
    timeDiffrence = pythonTime1 - pythonTime2
    if timeDiffrence.days < 0:
        timeDiffrence = datetime.timedelta(days=0,seconds=timeDiffrence.seconds, microseconds=timeDiffrence.microseconds)
    return transformPythonTimeDiffrenceToStringTime(timeDiffrence)

# Transforms our string time to the python datetime object
def transformStringTimeToPythonTime(time):
    return datetime.datetime.strptime(time,"%H:%M")

# Take the TimeDiffrence object, cast to a string, then trim the seconds off.
def transformPythonTimeDiffrenceToStringTime(timeDiffrence):
    timeDiffrenceString = str(timeDiffrence)
    return timeDiffrenceString[:timeDiffrenceString.rindex(':')]


# The main section of our program
# we read the contents, verify them, generate the data we want to output,
# and finaly write it to file.
outputData = []
fileContents = openInputFileAndGetContents()
print("File open: ", fileContents)

errorOutput = verifyFileContents(fileContents, outputData)
if errorOutput:
    openOutputFileAndWriteContents(errorOutput)
    sys.exit()

outputData = generateOutput(fileContents, outputData)

openOutputFileAndWriteContents(outputData)
