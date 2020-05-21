from country_list import countries_for_language
from country_list import available_languages

def getcountries():
    countries = []
    for language in available_languages ():
        countries.append (dict (countries_for_language (language)))
    dictionary = dict ([(key, []) for key in countries[96]])
    
    #7 96 204 263
    for country in dictionary:
        
        dictionary[country].append(countries[7][country])
        dictionary[country].append(countries[96][country])
        dictionary[country].append(countries[204][country])
        dictionary[country].append(countries[263][country])
        dictionary[country] = list(set(dictionary[country]))
    return (dictionary)
