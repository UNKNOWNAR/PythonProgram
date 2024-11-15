class dictionaryComprehensions:
    cities = ["kolkata","dhaka","london","new york","paris"]
    countries = ["India","Bangladesh","England","USA","France"]
    z =  zip(cities,countries)
    for element in z:
        print(element)
    print(isinstance(z,tuple))
    dict = {cities:countries for cities,countries in  zip(cities,countries)}
    print(dict)