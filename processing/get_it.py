from bs4 import BeautifulSoup
import requests
import json
import time
from datetime import datetime

# url = raw_input("https://docs.google.com/document/d/e/2PACX-1vRSxDeeJEaDxir0cCd9Sfji8ZPKzNaCPZnvRCbG63Oa1ztz4B4r7xG_wsoC9ucd_ei3--Pz7UD50yQD/pub")

r  = requests.get("https://docs.google.com/document/d/e/2PACX-1vRSxDeeJEaDxir0cCd9Sfji8ZPKzNaCPZnvRCbG63Oa1ztz4B4r7xG_wsoC9ucd_ei3--Pz7UD50yQD/pub")

data = r.text

soup = BeautifulSoup(data, 'html5lib')

counties = [
            'Adams',
            'Alamosa',
            'Arapahoe',
            'Archuleta',
            'Baca',
            'Bent',
            'Boulder',
            'Broomfield',
            'Chaffee',
            'Cheyenne',
            'Clear Creek',
            'Conejos',
            'Costilla',
            'Crowley',
            'Custer',
            'Delta',
            'Denver',
            'Dolores',
            'Douglas',
            'Eagle',
            'El Paso',
            'Elbert',
            'Fremont',
            'Garfield',
            'Gilpin',
            'Grand',
            'Gunnison',
            'Hinsdale',
            'Huerfano',
            'Jackson',
            'Jefferson',
            'Kiowa',
            'Kit Carson',
            'La Plata',
            'Lake',
            'Larimer',
            'Las Animas',
            'Lincoln',
            'Logan',
            'Mesa',
            'Mineral',
            'Moffat',
            'Montezuma',
            'Montrose',
            'Morgan',
            'Otero',
            'Ouray',
            'Park',
            'Phillips',
            'Pitkin',
            'Prowers',
            'Pueblo',
            'Rio Blanco',
            'Rio Grande',
            'Routt',
            'Saguache',
            'San Juan',
            'San Miguel',
            'Sedgwick',
            'Summit',
            'Teller',
            'Washington',
            'Weld',
            'Yuma'
            ]

def match_class(target):
    def do_match(tag):
        classes = tag.get('class', [])
        return all(c in classes for c in target)
    return do_match


def get_presumed_positive_cases():
    last_update = str(datetime.fromtimestamp(time.time()))
    data = {}
    data["presumed"] = {}
    data["last_update"] = last_update

    for li in soup.find_all('li'):
        contents = li.contents

        for cont in contents:
            text = cont.string

            for county in counties:
                if county in text:
                    items = text.split()

                    try:
                        count = int(items[len(items) - 1])
                    except ValueError:
                        print(text + " <-- not a number")

                    data['presumed'][county] = count

    return data


def get_visitors_presumed_positive(data):
    for p in soup.find_all('p'):
        contents = p.contents

        for cont in contents:
            text = cont.string

            for county in counties:
                if(text is not None):
                    if county in text:

                        items = text.split()
                        try:
                            count = int(items[len(items) - 1])
                        except ValueError:
                            print(text + " <-- not a number")


                        if(county in data['presumed']):

                            existing = data['presumed'][county]
                            data['presumed'][county] = int(existing) + count
                        else:
                            data['presumed'][county] = count



if __name__ == '__main__':
    presumed_cases = get_presumed_positive_cases()
    get_visitors_presumed_positive(presumed_cases)

    print(presumed_cases)




