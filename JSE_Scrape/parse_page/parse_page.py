from bs4 import BeautifulSoup

from locators.prices import StockPriceLocators


class ParseStockPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = StockPriceLocators.STOCK_NAME
        return self.soup.select_one(locator).string

    @property
    def trade_prices(self):
        locator = StockPriceLocators.TRADE_PRICE_LOCATOR
        prices_label = ['Last Traded Price', 'Close Price', 'Change ($)', 'Change (%)']
        prices = [e.string for e in self.soup.select(locator)]
        return dict(zip(prices_label, prices))

    @property
    def open_prices(self):
        locator = StockPriceLocators.OPEN_PRICE_LOCATORS
        prices_label = ['Open', 'Bid', 'Ask', 'Volume Traded (units)']
        prices = [e.string for e in self.soup.select(locator)]
        return dict(zip(prices_label, prices))

    @property
    def full_details(self):
        return {'company': self.name, 'trade_price': self.trade_prices, 'open_price': self.open_prices}