from classes.binanceExchange import BinanceExchange
from classes.tools import clear
from rich.console import Console
from rich.table import Column, Table
import os
from dotenv import load_dotenv
load_dotenv()
binance_api_key = os.environ.get("binance_api_key")
binance_api_secret = os.environ.get("binance_api_secret")


console = Console()

binance = BinanceExchange(binance_api_key, binance_api_secret)

binanceAccountBalances = binance.getAccountBalancesFormated()


def printConsole():
    clear()
    table = Table(show_header=True,
                  header_style="bold magenta")
    table.add_column("Asset", style="dim", justify='center')
    table.add_column("Free", justify='center')
    table.add_column('Price', justify='center')
    table.add_column('Value', justify='center')

    for elem in binanceAccountBalances['data']:
        print(elem)
        table.add_row(str(elem['asset']), str(elem['free']),
                      str(elem['price']), str(elem['value'])+" $")
    console.print(table)


printConsole()
