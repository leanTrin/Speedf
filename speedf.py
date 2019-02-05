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

def getReadingRate(): #TODO: find a better function name

    text = "" # get an exerpt somewhere
    begin = time.time()


    print(text)
    input("[RETURN]")

    end = time.time()
    final = end - begin
    print(final)

def main():

    # shows the help page when need more requirements
    if(argsLength(getArgs()) == 0):
        print("Need more Arguments!")
        argumentHelp()
        exit(0)


if(__name__=="__main__"):
    main()


