import PyPDF2
import sys
import os
import time
import random
# Reddit imports
import praw

#Reddit functions

subReddit = 'todayilearned'
reddit = praw.Reddit(client_id='3QBnDb_NxGrPBA',
                     client_secret='s531SAL5eUWGk4O_sXQ4WcOozFc',
                        user_agent='my user agent')

def getSubmissions(amount):
# get random submisions
    data = []
    while(len(data) < amount):
        submission = reddit.subreddit(subReddit).random()
        while(submission.title in data or len(submission.title) < 100):
            submission = reddit.subreddit(subReddit).random()
        data.append(submission.title)

    for i in range(len(data)):
        data[i] = str.replace(data[i],"TIL","Today I learned")
    return data

##End of Reddit Functions###################


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
    print("Please Wait...")
    try:
        text = getSubmissions(1)[0]
    except Exception as e:
        print(e)
        print("Ok.")
        text = """Nearby are services that provide food, fuel, repairs, and entertainment. Drivein theaters and fast food chains abound. Waterfront businesses have docks built for those arriving by boat to do their shopping, laundry, or to transfer suitcases from the family car. The local merchants deliver goods to the cabin by road or by water. Entrepreneurs make a businesss of servicing and maintaining cabins during the owners absence in the off seasons. Most of these "cottages", whether on the lake shore, or located five well paved streets from the water, rival the homes of many city dwellers. These lake side communities, although seasonal, differ little from the urban living from which they offer escape."""


    print("A paragraph will appear in front of you. Read it then as soon as you are done, press <return> to continue")
    print("[-] keep your hand on the button")
    input("\nPress <return> to show the text")
    
    begin = time.time()
    print("\n")
    print(text)
    input("\nPress <return> to continue")

    end = time.time()
    final = end - begin
    return [pdfWordCount(text),final/60]
def formatTime(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h,24)
    date = ("%dd %dh%02dm%02ds" % (d ,h, m, s))
    return date
            
def test():
    pass
def main():
    print("Loading...")
    
    arguments = getArgs()
    filename = getArgsValue(arguments,"i")
    rate = getArgsValue(arguments,"r")
    
    # shows the help page when need more requirements
    if(filename == None or argsLength(arguments) > 2):
        print("[!] Check your Arguments")
        argumentHelp()
        exit(0)

    #checks if rate arguments is a number
    if(rate != None):
        if(not rate.isdigit()):
            print("[!] rate must be a number")
            argumentHelp()
            exit(0)

    # check if file exists
    if (not (fileExist(filename))):
        print("[!] " + filename + " does not exist")
        argumentHelp()
        exit(0)

    pdfText = ""
    try:
        pdfText = getTextFromPdf(filename) 
    except Exception as e:
        print(e)
        print("That might not be a pdf")
        argumentHelp()
        exit(0)
    ###########
    #   MAIN PROGRAM
    ####################

    #skip the reading test
    if(rate != None):
        # calculate the length to read the document
        pdfTime = ( pdfWordCount(pdfText) ) / ( int( rate ) )
        pdfTime = pdfTime * 60 # Turns minutes to seconds
        print("You can finish the book '%s' in about %s" % (filename.strip(".pdf"),formatTime(pdfTime)))
        exit(0)
    else:
        # TODO: if the uese needs a reading test
        #       Maybe get a paragraph from 'todayilearned' reddit pag
        print("Ok.")
        readRate = getReadingRate()
        pdfTime = ( (pdfWordCount(pdfText) * (readRate[1]) ) / ( readRate[0]) ) * 60 
        print("\nYou can finish the book '%s' in about %s" % (filename.strip(".pdf"),formatTime(pdfTime)))
        exit(0)



if(__name__=="__main__"):
    main()
