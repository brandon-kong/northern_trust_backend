import requests

key_exchange = 'b8d89fa457e55a3b9da87c2f' #jeff's key
key_1forge = 'BnReWSbhxlByR3xBvg6T8sRc0PRClfh2' #dylan's key

def conversionRate(base, result): 
    url_exchange = "https://v6.exchangerate-api.com/v6/" + key_exchange + "/pair/" + base + "/" + result
    url_1forge = "https://api.1forge.com/quotes?pairs=" + base + "/" + result + "&api_key=" + key_1forge
    exchange = requests.get(url_exchange) 
    _1forge = requests.get(url_1forge)

    if (exchange.status_code == 200 and _1forge.status_code == 200):
        rate_exchange = exchange.json()
        rate_1forge = _1forge.json()
        if (rate_exchange["time_last_update_unix"] <= rate_1forge[0]["t"]):
            return rate_1forge
        else:
            return rate_exchange
    else:
        return None
    
def conversion(base, result, amount):
    return (conversionRate(base, result))[0]["p"] * amount
