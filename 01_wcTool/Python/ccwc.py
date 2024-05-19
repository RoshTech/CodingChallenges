#Reading from a file

import getopt, sys, os, string

def get_bytes_in_file(file):
    fileReader = open(file, "rb")   
    byte=0
    whitespaces = [" ", "\t", "\n", "\v", "\r", "\f"]
    while 1:
        char = fileReader.read(1)
        if not char: 
            break

        if (char in whitespaces or char):
            byte+=1

    fileReader.close()
    return byte

def get_lines_in_file(file):
    fileReader = open(file, "rb")
    line = 0
    while(fileReader.readline()):
        line += 1

    fileReader.close()
    return line

def get_words_in_file(file):
    fileReader = open(file, "rb")
    words = 0
    while 1:
        line = fileReader.readline()
        words += len(line.split())
        if not line:
            break

    fileReader.close()
    return words

def get_chars_in_file(file):
    fileReader = open(file, "rb")
    chars = 0
    whitespaces = [" ", "\t", "\n", "\v", "\r", "\f"]
    while 1:
        char = fileReader.read(1)
        if char not in whitespaces:
            chars +=1
        if not char: 
            break
    fileReader.close()
    return chars

def help():
    print('Coding Challenge wc Tool')
    print('Usage: python3 ccwc.py [OPTIONS] [FILE]')
    print('Options:')
    print('  -c, --bytes\n\tprint the number of bytes')
    print('  -l, --lines\n\tprint the number of lines')
    print('  -w, --words\n\tprint the number of word')
    print('  -m, --chars\n\tprint the number of chars')


if __name__ == "__main__" :
    argList = sys.argv[1:]
    options = "clwm"
    longOptions = ["bytes", "lines", "words", "chars"]       
    # print(argList)
    if len(argList) == 0:
        help()
    elif len(argList) == 1 and argList[0] not in options:  
        print(str(get_lines_in_file(argList[0])) + " " + str(get_words_in_file(argList[0])) + " " +  str(get_bytes_in_file(argList[0])) + " " + argList[0])

    else:
        try:
            arguments, values = getopt.getopt(argList, options, longOptions)

            for currentArg, currentValue in arguments:
                # print(arguments)
                if currentArg in ("-c", "--bytes"):
                    print(str(get_bytes_in_file(argList[1])) + " " + argList[1])
                elif currentArg in ("-l", "--lines"):
                    print(str(get_lines_in_file(argList[1])) + " " + argList[1])                 
                elif currentArg in ("-w", "--words"):
                    print(str(get_words_in_file(argList[1])) + " " + argList[1])                 
                elif currentArg in ("-m", "--chars"):
                    print(str(get_chars_in_file(argList[1])) + " " + argList[1])  
                else:
                    print('Usage: python3 ccwc.py [OPTIONS] file')



        except getopt.error as err:
            print(str(err))