import PyPDF2
import sys
import time
import random

testFile = 'test.pdf'

def argumentHelp():
    print("help: ")
    print(">speedf -r [rate] -i [filename.txt]")

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

    splitUp = parsed.split(" ")
    wordsLength = len(splitUp)
    return wordsLength

def getParagraphExcerpt(content):
    # TODO: this needs to be done
    pass
def wordsPerMinute(wordCount,minute):
    return wordCount/minute

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
        print("Check your Arguments")
        argumentHelp()
        exit(0)
    #TODO: add a try catch for when file does not exist
    filename = getArgsValue(getArgs(),"i")


    if((getArgsValue(getArgs(),"r") not None) and (getArgsValue(getArgs(),"r").isdigit()) ):
        #TODO: skips the reading test
        pass
    #TODO: add a try catch for when the input is not a digit

    print(filename)
if(__name__=="__main__"):
    main()


