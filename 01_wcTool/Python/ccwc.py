#Reading from a file

import getopt, sys, os

argList = sys.argv[1:]
# print(argList)
options = "c:"

longOptions = ["character"]

try:
    arguments, values = getopt.getopt(argList, options, longOptions)

    for currentArg, currentValue in arguments:
        if currentArg in ("-c", "--Character"):
            
            fileReader = open("text.txt", "r")
            print(str(os.path.getsize("text.txt")) + " " + argList[1])
            fileReader.close()


except getopt.error as err:
    print(str(err))