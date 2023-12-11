'''from WebScraper.eBayParser import get_organic_results_ebay
from amazonParserCaller import run_spider_amazon
from WebScraper.aliExpressParser import get_organic_results_alie
import json
import sys
import os'''

import crochet
crochet.setup()

import sys
import os
import json
current_dir = os.path.dirname(os.path.abspath(__file__))
amazon_scrapy_dir = os.path.join(current_dir, '..', 'WebScraper', 'amazon', 'amazon')
sys.path.append(amazon_scrapy_dir)
#sys.path.append('/ShoppingList/WebScraper/amazon/amazon')

#calls the scrapy amazon spider from within the amazon folder
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from WebScraper.amazon.amazon.spiders.amazonSearchSpider import amazonSearchSpider  # Import your spider class
from WebScraper.eBayParser import get_organic_results_ebay
from WebScraper.aliExpressParser import get_organic_results_alie
from amazonParserCaller import run_spider_amazon
from scrapy.utils.project import get_project_settings
from twisted.internet.defer import Deferred

def getItemsFindCheapest():
    data = ""
    userItems= ""
    cheapestLow = []
    cheapestMed = []
    cheapestHi = []
    finalShopList = []
    
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, 'public', 'shopping_data.json')     #Opening user input data
    with open(file_path, 'r') as file:
        data = json.load(file)
        userItems = data["items"]               #finding user items
        if (data["budget"] == ""):
            budget = float(100.00)                  #default budget = $100
        else:
            budget = float(data["budget"])



    #searching for items online
    for i in range(0, len(userItems)):          
        listing = getCheapest(userItems[i]["text"], userItems[i]["priority"])

        #sorting items by priority
        if (userItems[i]["priority"].lower() == "high"):
            cheapestHi.append(listing)
        if (userItems[i]["priority"].lower() == "med"):
            cheapestMed.append(listing)
        if (userItems[i]["priority"].lower() == "low"):
            cheapestLow.append(listing)

    
    #sorting lists
    insertionSort(cheapestLow)
    insertionSort(cheapestMed)
    insertionSort(cheapestHi)

    #adding items to final cart
    while (budget > 0.0):
        budget = shoppingAlgo(budget, cheapestHi, finalShopList)
        budget = shoppingAlgo(budget, cheapestMed, finalShopList)
        budget = shoppingAlgo(budget, cheapestLow, finalShopList)
        break

    #writing data to JSON file
    output_path = os.path.join('finalShoppingList.json')
    with open(output_path, 'w') as outfile:
        json.dump(finalShopList, outfile,indent=4)

    print("Remaining Budget: " + str(budget))
    return finalShopList


def shoppingAlgo(budget, itemList, finalShopList):
    for item in itemList:
        if budget >= item["price"]:
            finalShopList.append(item)
            budget -= item["price"]
        else:
            break

    return budget


def insertionSort(itemList):
    for i in range(1, len(itemList)):
        key = itemList[i]
        keyVal = itemList[i]["price"]
        j = i - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and keyVal < itemList[j]["price"]:
            itemList[j + 1] = itemList[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        itemList[j + 1] = key
    return itemList


def getCheapest(item, priority): #runs scrapers and finds cheapest overall item out of the three sites

    
    #making URL for each site
    eBayURL = "https://www.ebay.com" + f"/sch/{item.replace(' ', '+')}"
    aliExpressURL = "https://aliexpress.us/w/wholesale-" + f"{item.replace(' ', '-')}" + ".html"

    #running amazon spider
    alieList = get_organic_results_alie(aliExpressURL)
    eBayList = get_organic_results_ebay(eBayURL)
    crochet.wait_for(timeout=60)(run_spider_amazon_la)(item)
    #run_spider_amazon_la(item) #amazon spider only requires item, not url

    file_path = 'scraperData/amazonItems.json'
    with open(file_path, 'r') as file:      #Opening user input data
        amazonData = json.load(file)
    
    aliExpressLowest = cheapestFromList(alieList)
    eBayLowest = cheapestFromList(eBayList)
    amazonLowest = cheapestFromList(amazonData)
    num1 = eBayLowest
    num2 = aliExpressLowest
    num3 = amazonLowest

    if (eBayLowest['price'] < aliExpressLowest['price']) and (eBayLowest['price'] < amazonLowest['price']):
        cheapestOvr = eBayLowest
    elif (aliExpressLowest['price'] < eBayLowest['price']) and (aliExpressLowest['price'] < amazonLowest['price']):
        cheapestOvr = aliExpressLowest
    else:
        cheapestOvr = amazonLowest
    cheapestOvr['keyword'] = item
    cheapestOvr["priority"] = priority
    return cheapestOvr


def cheapestFromList(scrapeResults):
    lowestPrice = 10000000
    lowestListing = ""
    for listing in scrapeResults:
        if listing['price'] < lowestPrice:
            lowestPrice = listing['price']
            lowestListing = listing
    return lowestListing

@crochet.run_in_reactor
def run_spider_amazon_la(item):
    #Output path for amazon scraper data
    
    output_relative_path = os.path.join('scraperData', 'amazonItems.json')

    output_path = os.path.join('scraperData', 'amazonItems.json')
    
    runner = CrawlerRunner(settings={
        'BOT_NAME': 'amazon',
        'SPIDER_MODULES': ['WebScraper.amazon.amazon.spiders'],
        'NEWSPIDER_MODULE': 'WebScraper.amazon.amazon.spiders',
        'ROBOTSTXT_OBEY': False,
        'SCRAPEOPS_API_KEY': '25c0074e-bf96-4973-9b74-a23998bb266a',
        'SCRAPEOPS_PROXY_ENABLED': True,
        'DOWNLOADER_MIDDLEWARES': {
            'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
            'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
            'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
        },
        'FEEDS': {
            output_path: {
                'format': 'json',
                'overwrite': True  # 'TRUE' to True for boolean value
            }
        },
    })
    

    #amazonSearchSpider.keyword_list = [item]
    deferred = runner.crawl(amazonSearchSpider, keyword_list=[item])



if __name__ == '__main__':
    print(getItemsFindCheapest())
    #getItemsFindCheapest()
    pass