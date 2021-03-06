import os

# package imports
from finance_apis import alphavantage, coingecko

# get APIs keys
import secrets


# --------------------------------------------------------------------------------
# constants
# --------------------------------------------------------------------------------
ALPHAVANTAGE_APIKEY = os.environ.get('ALPHAVANTAGE_APIKEY')


# --------------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------------
def main():
    test_alphavantage()
    print(3*'\n')
    test_coingecko()


# --------------------------------------------------------------------------------
# functions
# --------------------------------------------------------------------------------
def test_alphavantage():
    """Usage example of alphavantage.py
    The user must get an AlphaVatange key before using this library.
    """
    df = alphavantage.get_daily('AAPL', ALPHAVANTAGE_APIKEY)
    print('AlphaVantage daily data:')
    print(df, 2*'\n')
    
    df = alphavantage.get_intraday('AAPL', ALPHAVANTAGE_APIKEY, 60)
    print('AlphaVantage hourly data:')
    print(df)


def test_coingecko():
    """Usage example of coingecko.py
    """
    pairs = [('bitcoin', 'usd'), ('ethereum', 'usd')]
    dates = ['12-10-2015', '13-10-2015']
    
    val = coingecko.historical_prices(pairs[0], dates)
    print('CoinGecko Historical Prices')
    print(val)


# --------------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------------
if __name__ == "__main__":
    main()