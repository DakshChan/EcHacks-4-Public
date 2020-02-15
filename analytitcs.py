#["locationLatitude", "locationLongitude", "currencyAmount", "merchantName", "categoryTags", "locationStreet", "originationDateTime"]


def spending_per_catagory(response_data):
    catagories = []
    dict_catagories = {}
    for i in range(len(response_data)):
        catagories.append(response_data[4])
        dict_catagories[catagories] = 0
    for i in range(len(response_data)):
        dict_catagories[response_data[4]] += response_data[2]
    return dict_catagories

def average_amount_per_purchase(response_data):
    dollars = 0;
    for i in range(len(response_data)):
        dollars += response_data[2]
    dollars /= len(response_data)
    return dollars

def next_month_pred_wolf(response_data):
    date = []
    amount = []
    for i in range(len(response_data)):
        date.append(response_data[6])
        amount.append(response_data[])
