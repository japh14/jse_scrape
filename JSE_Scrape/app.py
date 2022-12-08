import requests
import pprint
import schedule
import time

from parse_page.parse_page import ParseStockPage
from utils.utils import create_content_pages


with open('web_pages.txt') as file:
    list_of_webpages = [site.strip() for site in file.readlines()]

content_pages = create_content_pages(list_of_webpages)

stocks = []
for stock_page in content_pages:
    stocks.append(ParseStockPage(stock_page))


pprint.pprint(stocks[0].full_details)

url = "https://prod-54.westus.logic.azure.com:443/workflows/44cabac215c140dcb7d57a7478f2bba0/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=KiPxA-J9Iyc3zMqwnzlbNBniu9vVHdf8oV7thSR9wxI"
requests.post(url, json= stocks[0].full_details)

#
# print(ncb.name)
# print(ncb.trade_prices)
# print(ncb.open_prices)
# pprint.pprint(ncb.full_details)