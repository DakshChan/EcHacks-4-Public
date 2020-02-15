# install the requests package using 'python -m pip install requests'
import requests
import json
import tdData

# gets the type of purchase and adds a green tag
def get_green_alt(data, transNum):

    greenData = data[transNum][4][0]

    configFile = open("config.txt", "r")
    if greenData.lower() == "food and dining":
         greenData = "organic " + greenData.lower()

    else:
        greenData = "green " + greenData.lower()

    return greenData

# def find_place(query, key, lat, long):
#     response = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query='+ query.replace(' ','+') + '&key=' + key + '&location=' + lat + ',' + long + '&radius=2000')
#     print (response)
#     return response

