__author__ = 'yangchen'
import re
def wordSegment(filePath):
    f = open(filePath)
    lineList = []
    attributeList = []
    for line in f.readlines():
        line1 = line.strip()
        print(line1.__class__)
        if((len(line1) != 0) and (line1[-1] == ';')):
            lineList.append(line1.split(' '))
            if(line1[-2] == ']' or line1[-2] =='"'):
                attributeList.append(lineList[-1][0])
            else:
                attributeList.append(lineList[-1][:-1])
    return(lineList, attributeList)

def readLibrary(path):
    f = open(path)
    commandList = []
    for lines in f:
        commandList.append(lines.strip())
    return(commandList)

def findAllIndex(longStr, subStr):
    i = 0
    l = len(longStr)
    s = len(subStr)
    offsetList = []
    while(i < l and longStr[i:].find(subStr) != -1):
        offsetList.append(i + longStr[i:].find(subStr))
        i = offsetList[-1]+s
    return(offsetList)

def commandsMatch(filePath):
    commandList = readLibrary('AllCommandersOutput.txt')
    occurredCommand = []
    f = open(filePath)
    count=0
    for lines in f:
        count += 1
        commandDict1 = dict()
        commandDict2 = dict()
        for command in commandList:
            offsetList = findAllIndex(lines, command)
            length = len(command)
            if(len(offsetList) > 0):
                for offset in offsetList:
                    if(offset == 0 and (lines[length] == ' ' or lines[length] == '\n')):
                        if(offset in commandDict1.keys()):
                            commandDict1[offset].append(command)
                        else:
                            commandDict1[offset] = []
                            commandDict1[offset].append(command)

                    elif(offset > 0 and lines[offset-1] == ' ' and (lines[offset + length] == ' ' or lines[offset + length] == '\n')):
                        if(len(commandDict2) == 0):
                            commandDict2[offset] = []
                            commandDict2[offset].append(command)
                        else:
                            if(offset in commandDict2.keys()):
                                commandDict2[offset].append(command)
                            else:
                                commandDict2[offset] = []
                                commandDict2[offset].append(command)

        print(count, commandDict1, commandDict2)
        for keys in commandDict1:
            occurredCommand.append(commandDict1[keys][-1])
        for keys in commandDict2:
            occurredCommand.append(commandDict2[keys][-1])
    return(list(set(occurredCommand)))

filePath = 'sample0(1).cfg'
filePath1 = 'atla'
#expressionList, attribute = wordSegment(filePath)
#print(expressionList)
#print(attribute)
result = commandsMatch(filePath1)

sorted(result)
print(len(result))
print(result)
