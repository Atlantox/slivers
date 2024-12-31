''' Listing all files in target folder and exporting it as a JSON '''

import os
import json

def SliversToJson(folder):
    ''' Iterate between files in a folder and exports a JSON file with sliver name, art and fullcard path '''
    fullPath = os.path.join(os.getcwd(), folder)

    if os.path.exists(fullPath) is False:
        print(f"The folder '{folder}' not found")
        return    

    sliversData = []
    for filename in os.listdir(fullPath):
        fixedName = filename.replace('_', ' ')
        sliverName = fixedName.split('.')[0]

        data = {
        "name": sliverName,
        "art": "arts/" + filename,
        'fullcard': "fullcards/" + filename
        }

        sliversData.append(data)        

    with open('slivers.json', 'w') as f:
        json.dump(sliversData, f, indent=4)

if __name__ == "__main__":
  targetFolder = 'arts'
  SliversToJson(targetFolder)