import os
import time
from lib.csv_to_json import convert

def extractAllCsv(exceptions):

    path = pathToCsv('')
    listOfFiles = os.listdir(path)
    if not listOfFiles:
        print('Oops. No files to convert!')
        print('Please add atleast more .csv file at this path: {}'.format(path))
        return
    print('Conversion is in the process: ')
    time.sleep(3)
    for index, file in enumerate(listOfFiles):
        if file.endswith('.csv'):
            print('')
            print('{})'.format(index + 1), file)
            for exception in exceptions:
                if(exception['name'] != file):
                    convert(os.path.join(path, file), os.path.join(pathToJson('{}'.format(file.replace('.csv', '.json', 1)))))
                else:
                    convert(os.path.join(path, file), os.path.join(pathToJson('{}'.format(file.replace('.csv', '.json', 1)))), exception['separator'])

def pathToJson(name):
    if os.path.exists(os.path.join(os.getcwd(), 'Extracted')) == False:
        os.makedirs('Extracted')
    return os.path.join(os.getcwd(), 'Extracted', name)

def pathToCsv(name):
    if os.path.exists(os.path.join(os.getcwd(), 'Ready')) == False:
        os.makedirs('Ready')
    return os.path.join(os.getcwd(), 'Ready', name)