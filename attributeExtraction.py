__author__ = 'yangchen'
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
        commandList.append(lines.strip('\n'))
    return(commandList)

def commandsMatch(filePath):
    commandList = readLibrary('AllCommandersOutput.txt')
    occurredCommand = []
    f = open(filePath)
    for lines in f:
        for command in commandList:
            if(lines.find(command+' ') != -1):
                occurredCommand.append(command)
                break
    occurredCommand = set(occurredCommand)
    print(list(occurredCommand))

filePath = './atla'
#expressionList, attribute = wordSegment(filePath)
#print(expressionList)
#print(attribute)
commandsMatch(filePath)
