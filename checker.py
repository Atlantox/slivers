''' Checking if image paths in slivers.json are right '''

import os
import json

def run():
    sliversData = None
    with open('slivers.json') as f:
        sliversData = json.loads(f.read())

    for sliver in sliversData:
        if not os.path.exists(sliver['art']):
            print('Sliver art missed for {0} expected filename: {1}'.format(sliver['name'], sliver['art']))

        if not os.path.exists(sliver['fullcard']):
            print('Sliver art missed for {0} expected filename: {1}'.format(sliver['name'], sliver['fullcard']))

if __name__ == '__main__':
    run()