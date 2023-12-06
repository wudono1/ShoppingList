from WebScraper.eBayParser import get_organic_results
from WebScraper.amazonParserCaller import run_spider
from WebScraper.aliExpressParser import get_organic_results

import sys

def lowestItemListing(amazonList, alibabaList, ebayList):
    lowestListing = None
    lowestPrice = sys.maxint


    for item in amazonList: #finding cheapest amazon listing
        if item["price"] < lowestPrice:
            lowestPrice = item["price"]
            lowestListing = item

    for item2 in alibabaList: #finding cheapest alibaba listing
        if item2["price"] < lowestPrice:
            lowestPrice = item2["price"]
            lowestListing = item2

    for item3 in ebayList: #finding cheapest ebay listing
        if item3["price"] < lowestPrice:
            lowestPrice = item3["price"]
            lowestListing = item3
    
    return lowestListing

def maximizeBudget():
    pass