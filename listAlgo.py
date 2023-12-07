from WebScraper.eBayParser import get_organic_results_ebay
from amazonParserCaller import run_spider_amazon
from WebScraper.aliExpressParser import get_organic_results_alie
import json
import sys
import os

def getItemsFindCheapest():
    data = ""
    userItems= ""
    cheapestLow = []
    cheapestMed = []
    cheapestHi = []
    finalShopList = []
    

    file_path = 'public/shopping_data.json'     #Opening user input data
    with open(file_path, 'r') as file:
        data = json.load(file)
        userItems = data["items"]               #finding user items
        budget = float(data["budget"])
    if not (isinstance(budget, float)):
        budget = float(100.00)                  #default budget = $100



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
        budget = shoppingAlgo(budget, cheapestLow, finalShopList)
        budget = shoppingAlgo(budget, cheapestMed, finalShopList)
        budget = shoppingAlgo(budget, cheapestHi, finalShopList)
        break

    #writing data to JSON file
    output_path = os.path.join('finalShoppingList.json')
    with open(output_path, 'w') as outfile:
        json.dump(finalShopList, outfile,indent=4)

    return


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
    amazonURL = "https://www.amazon.com" + f"/s?k={item.replace(' ', '+')}"
    eBayURL = "https://www.ebay.com" + f"/sch/{item.replace(' ', '+')}"
    aliExpressURL = "https://aliexpress.us/w/wholesale-" + f"{item.replace(' ', '-')}" + ".html"

    #running amazon spider
    run_spider_amazon(amazonURL)

    file_path = 'scraperData/amazonItems.json'
    with open(file_path, 'r') as file:      #Opening user input data
        amazonData = json.load(file)
    

    alieList = get_organic_results_alie(aliExpressURL)
    eBayList = get_organic_results_ebay(eBayURL)
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




if __name__ == '__main__':
    print(getItemsFindCheapest())
    #getItemsFindCheapest()
    pass