import json
import regex as re
from lib.loading_bar import progress

def convert(pathToCsv = '', pathToJson = '', splitter = ',') :
    headerContent = []
    exportedJson = []
    csvFile = open(pathToCsv).readlines()
    length = len(csvFile)

    for line in csvFile:
        headerContent = line.replace("\"", "").split(splitter)
        break

    for lineNumber,line in enumerate(csvFile):
        if lineNumber is 0:
            continue
        lineContent = line.strip()
        arrayContent = removeJunkFromText(splitter, lineContent)

        jsonContent = {}

        if lineNumber == length - 1:
            progress(lineNumber, length, ' Successfully Converted!')
        else:
            progress(lineNumber, length, ' Converting')

        for index, content in enumerate(arrayContent):
            
            jsonContent[headerContent[index].strip()] = content.replace("\"", "")
            if index is len(arrayContent) - 1:
                exportedJson.append(jsonContent)

    # Write all data to file once ready.
    jsonFile = open(pathToJson, 'w+')
    jsonFile.write(json.dumps({ "data" : exportedJson}, indent=4))
    jsonFile.close()



def removeJunkFromText(splitter, text):
        lineContent = text
        searchCriteria = re.compile(r'"[^"]*"(*SKIP)(*FAIL)|' + splitter + r'\s*')
        arrayContent = searchCriteria.split(lineContent)

        return arrayContent
