# install the requests package using 'python -m pip install requests'
import requests
import json


def get_td_data(customer):
    configFile = open("config.txt", "r")
    response = requests.get(
        'https://api.td-davinci.com/api/customers/' + customer + '/transactions',
        headers={'Authorization': json.load(configFile)['td']},
        json={'continuationToken': ''}
    )
    response_data = response.json()

    return response_data["result"]

def filtered_resp(customer):
    responses = get_td_data(customer)
    responses_list = []

    data = ["locationLatitude", "locationLongitude", "currencyAmount", "merchantName", "categoryTags", "locationStreet", "originationDateTime"]

    for resp in responses:
        temp = []
        try:
            for d in data:
                temp.append(resp[d])
            responses_list.append(temp)
        except:
            pass

    return responses_list
    # responses list should be [ [locationlat, locationlong, amount], []... ]