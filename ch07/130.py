import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

opening_price = float(btc['opening_price'])
fluctuation = float(btc['max_price']) - float(btc['min_price'])
max_price = float(btc['max_price'])

if opening_price+fluctuation > max_price:
    print("bull market")
else:
    print("bear market")