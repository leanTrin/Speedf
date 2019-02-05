import PyPDF2
import sys
import time
testFile = 'test.pdf'
def getArgs():
    argv = sys.argv
    arguments = []
    for i in range(len(argv)-1):
        arguments.append(argv[i+1])
    
    return arguments

def getTextFromPdf(filename):
    readPdf = PyPDF2.PdfFileReader(filename)
    numberOfPages = readPdf.getNumPages()
    content = [readPdf.getPage(i).extractText().replace("\n","") for i in range(numberOfPages)]
    return content

def pdfWordCount(content):
    combined = ""
    for i in content:
        combined += i

    splitUp = parsed.split(" ")
    wordsLength = len(splitUp)
    return wordsLength

def getParagraphExcerpt(content):
   pass
   #TODO: this

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


print(getParagraphExcerpt(getTextFromPdf(testFile)))






