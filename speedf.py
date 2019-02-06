import PyPDF2
import sys
import os
import time
import random

testFile = 'test.pdf'

def argumentHelp():
    print("help: ")
    print(">speedf -r [rate] -i [filename.txt]")
    print("r    How many words per minute can you read")
    print("i    Where the file is located")

def getTextFromPdf(filename):
    readPdf = PyPDF2.PdfFileReader(filename)
    numberOfPages = readPdf.getNumPages()
    content = [readPdf.getPage(i).extractText().replace("\n","") for i in range(numberOfPages)]
    return content

def getArgs():
    argv = sys.argv
    arguments = []
    for i in range(len(argv)-1):
        try:
            if(argv[i+1] == "-i"):
                arguments.append(["i",argv[i+2]])
            
            if(argv[i+1] == "-r"):
                arguments.append(["r",argv[i+2]])
        except Exception as e:
            print(e)
    return arguments

def argsLength(args):
    return len(args)

def getArgsValue(arguments,value):
    for i in arguments:
        if(i[0] == value):
            return i[1]

def pdfWordCount(content):
    combined = ""
    for i in content:
        combined += i

    splitUp = combined.split(" ")
    wordsLength = len(splitUp)
    return wordsLength

def fileExist(filename):
	return os.path.isfile(filename)

def getParagraphExcerpt(content):
    # TODO: this needs to be done
    pass
def wordsPerMinute(wordCount,minute):
    return wordCount/minute
def timeToReadPdf(wpm):
    return 1/wpm

def getReadingRate():

    text = "" # get an exerpt somewhere
    begin = time.time()


    print(text)
    input("[RETURN]")

    end = time.time()
    final = end - begin
    print(final)

def main():

    # shows the help page when need more requirements
    if(getArgsValue(getArgs(),"i") == None or argsLength(getArgs()) > 2):
        print("[!] Check your Arguments")
        argumentHelp()
        exit(0)

    #checks if rate arguments is a number
    if(getArgsValue(getArgs(),"r") != None):
        if(not getArgsValue(getArgs(),"r").isdigit()):
            print("[!] rate must be a number")
            argumentHelp()
            exit(0)

    # check if file exists
    if (not (fileExist(getArgsValue(getArgs(),"i")))):
        print("[!] " + getArgsValue(getArgs(),"i") + " does not exist")
        argumentHelp()
        exit(0)
    
    filename = getArgsValue(getArgs(),"i")

    #skip the reading test
    if(getArgsValue(getArgs(),"r") != None):
        # calculate the length to read the document
        exit(0)
        

if(__name__=="__main__"):
    main()


