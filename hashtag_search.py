import collections
import json
import folium
from geopy.geocoders import Nominatim
from dic_countries import getcountries

geolocator = Nominatim ()


def geolocate(country):
    try:
        # Geolocate the center of the country
        loc = geolocator.geocode ( country )
        # And return latitude and longitude
        return (loc.latitude, loc.longitude)
    except:
        pass
def getKeysByValue(dictOfElements, valueToFind):
    Key = ''
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            Key = item[0]
    return  Key

tweets = []
countries = getcountries ()
dictionary = dict ( [(key, []) for key in countries.keys()] )
with open ( "tweets.jsonl", "r" ) as f:
    for line in f:
        tweets.append ( json.loads ( line ) )
for tweet in tweets:
    for nation in countries.keys():
        for country in countries[nation]:
            if country in tweet["user"]["location"] or nation in tweet["user"]["location"]:

                for hasht in tweet["entities"]["hashtags"]:
                    dictionary[nation].append (hasht["text"])
                break


m = folium.Map ( location=[10, 10], zoom_start=5 )
tooltip = 'click'

for country in dictionary:
    counter = collections.Counter ( dictionary[country] )
    dictionary[country] = counter.most_common ( 30 )
    try:
        folium.Marker (geolocate(countries[country][1]),
                        popup=dictionary[country],
                        ).add_to ( m )
    except:
        pass

m.save ( 'map.html' )
