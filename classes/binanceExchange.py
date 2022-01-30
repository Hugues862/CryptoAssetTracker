import math
from binance.client import Client
import json
import classes.tools as tools


def dailyAccountSnapchot():
    info = client.get_account_snapshot(type='SPOT')

    with open("binanceRes.json", "r") as file:
        data = json.load(file)

    return info


class BinanceExchange():
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

    def getAccountBalances(self):
        info = self.client.get_account()
        prices = self.client.get_all_tickers()
        assets = []
        for bal in info['balances']:
            if float(bal['free']) != 0 or float(bal['locked']) != 0:
                assets.append(bal)
        res = {
            'info': {
                'assetsSymbol': [],
                'usdBalance': 0,
            },
            'data': []
        }
        for elem in prices:
            for symbol in assets:
                if elem['symbol'] == symbol['asset']+'USDT':
                    symbol['price'] = round(float(elem['price']), 5)
                    symbol['free'] = round(float(symbol['free']), 5)
                    symbol['value'] = round(symbol['price']*symbol['free'], 5)

                    res['data'].append(symbol)

        for elem in res['data']:
            res['info']['assetsSymbol'].append(elem['asset'])
            res['info']['usdBalance'] += elem['value']

        tools.writeToFile(res, 'binanceAccountAssets.json')
        return res

    def getAccountBalancesFormated(self):
        info = self.client.get_account()
        prices = self.client.get_all_tickers()
        assets = []
        for bal in info['balances']:
            if float(bal['free']) != 0 or float(bal['locked']) != 0:
                assets.append(bal)
        res = {
            'info': {
                'assetsSymbol': [],
                'usdBalance': 0,
            },
            'data': []
        }
        for elem in prices:
            for symbol in assets:
                if elem['symbol'] == symbol['asset']+'USDT':
                    symbol['price'] = round(float(elem['price']), 5)
                    free = float(symbol['free'])
                    if free < 1:
                        symbol['free'] = round(free, 5)
                    elif free < 10:
                        symbol['free'] = round(free, 2)
                    else:
                        symbol['free'] = round(free, 1)

                    symbol['value'] = round(symbol['price']*symbol['free'], 2)

                    res['data'].append(symbol)

        for elem in res['data']:
            res['info']['assetsSymbol'].append(elem['asset'])
            res['info']['usdBalance'] += elem['value']

        res['data'] = sorted(
            res['data'], key=lambda d: d['value'], reverse=True)

        tools.writeToFile(res, 'binanceAccountAssets.json')
        return res
