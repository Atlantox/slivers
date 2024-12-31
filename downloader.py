''' Getting al slivers and downloading the fullcard image '''

import urllib
from mtgsdk import Card

def run():
    slivers = Card.where(subtypes='sliver').all()

    for sliver in slivers:
        filePath = 'fullcards/'
        sliverName = sliver.name.replace(' ', '_')
        fileName = filePath + sliverName + '.jpg'
        sliverImage = sliver.image_url

        try:
            urllib.request.urlretrieve(sliverImage, f'{fileName}')
        except Exception as exc:
            print(f"Image not found for {sliverName} image from url {sliverImage} {str(exc)}")
    

if __name__ == "__main__":
    run()