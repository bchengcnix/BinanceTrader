from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceWithdrawException

import json


class BinanceTrader:
    # constructor
    def __init__(self, api_key, api_secret):
        self.bclient = Client(api_key, api_secret)

    # try withdrawing a coin from a wallet
    def withdrawBalance(self, coin, address, amt):
        try:
            result = self.bclient.withdraw(
                asset=coin,
                address=address,
                amount=amt)
        except BinanceAPIException as e:
            print(e)
        except BinanceWithdrawException as e:
            print(e)
        else:
            print("Success")

    # convert to json object
    def toJson(self, conv):
        converted = json.loads(conv)
        return converted

    # return coin balance as json object
    def getBalance(self, coin):
        balance = self.bclient.get_asset_balance(asset=coin)
        temp = {}
        temp[coin] = balance
        convTemp = self.toJson(temp)
        return convTemp

    def parseCommand(self):
        # to do
        return

    def placeOrder(self, bos, coin, side, type, timeinforce, qty, price):
        if bos == 'buy':
            return

    def placeLimitOrder(self, bos, coin, qty, price):
        if bos == 'buy':
            order = self.bclient.order_limit_buy(
                symbol=coin,
                quantity=qty,
                price=price)
        else:
            order = self.bclient.order_limit_sell(
                symbol=coin,
                quantity=qty,
                price=price)
        return order

    def placeMarketOrder(self, bos, coin, qty):
        if bos == 'buy':
            order = self.bclient.order_market_buy(
                symbol=coin,
                quantity=qty)
        else:
            order = self.bclient.order_market_sell(
                symbol=coin,
                quantity=qty)
        return order
