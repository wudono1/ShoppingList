from WebScraper.eBayParser import get_organic_results_ebay
from amazonParserCaller import run_spider_amazon
from WebScraper.aliExpressParser import get_organic_results_alie
import json
import sys

def getItemsFindCheapest():
    data = ""
    userItems= ""
    budget = ""
    
    file_path = 'public/shopping_data.json'
    with open(file_path, 'r') as file:      #Opening user input data
        data = json.load(file)
        userItems = data["items"]
        budget = float(data["budget"])

def getCheapest(item, priority): #runs scrapers and finds cheapest overall item out of the three sites

    #making URL for each site
    amazonURL = "https://www.amazon.com" + f"/s?k={item.replace(' ', '+')}"
    ebayURL = "https://www.ebay.com" + f"/sch/{item.replace(' ', '+')}"
    aliExpressURL = "https://aliexpress.us/w/wholesale-" + f"{item.replace(' ', '-')}" + ".html"

    #running amazon spider
    run_spider_amazon(amazonURL)

    file_path = 'scraperData/amazonItems.json'
    with open(file_path, 'r') as file:      #Opening user input data
        data = json.load(file)
        userItems = data["items"]
        budget = float(data["budget"])
    eBayLowest = cheapestFromList(get_organic_results_ebay(ebayURL))
    aliExpressLowest = cheapestFromList(get_organic_results_ebay(aliExpressURL))

def cheapestFromList(scrapeResults):
    lowestPrice = 10000000
    lowestListing = ""
    for listing in scrapeResults:
        if listing['price'] < lowestPrice:
            lowestPrice = listing['price']
            lowestListing = listing
    return lowestListing



    


def maximizeBudget():
    pass

getItemsFindCheapest()