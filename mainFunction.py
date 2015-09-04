#This is the interface for extracting the commands

from attributeExtraction import commandsMatch

def countCommands(filePath):
    return(commandsMatch(filePath))

results = countCommands('atla')
print(results)
