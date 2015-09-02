__author__ = 'yangchen'
#build a library of command which is a kind of professional corpus
import os
def extractKeywords(filePath):
    f = open(filePath)
    valueList = []
    for line in f.readlines():
        valueOffset = line.find("value")
        if(valueOffset != -1):
            subOffset = valueOffset+7
            while(subOffset  < len(line)):
                if(line[subOffset] == '"'):
                    break;
                else:
                    subOffset += 1
                valueEnd = subOffset
            commandStr = line[valueOffset+7 : valueEnd]
            flag = 0
            for item in valueList:
                if(item == commandStr):
                    flag = -1
                    break
            if(flag == 0):
                valueList.append(commandStr)
    f.close()
    return(valueList)

def writeFile(listName):
    f = open('dictionary.txt', 'a')
    for item in listName:
        f.writelines(item+'\n')
    f.close()


path1 = 'VRP  command reference/Command_Reference_zh.hhk'
path2 = 'VRP  command reference/Command_Reference_zh.hhc'
'''
valueList1 = extractKeywords(path1)
valueList2 = extractKeywords(path2)

writeFile(valueList1)
writeFile(valueList2)
'''
path = 'VRP  command reference/vrp'
print(os.listdir(path))

#print(len(valueList1))
#print(len(valueList2))
