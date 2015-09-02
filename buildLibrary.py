__author__ = 'yangchen'
#build a library of command which is a kind of professional corpus

def extractKeywords(filePath):
    f = open(filePath)
    valueList = []
    for line in f.readlines():
