import requests

COINDESK_API = "https://api.coindesk.com/v1/bpi/currentprice.json"


class Bitcoin:
    def __init__(self):
        pass

    def get_btc_current_price(self):
        """
        Retrieve Current Price of Bitcoin in USD
        :return current BTC price (float)
        """
        response = requests.get(COINDESK_API)
        response.raise_for_status()
        return response.json()["bpi"]["USD"]["rate_float"]
