from WebScraper.eBayParser import get_organic_results
from amazonParserCaller import run_spider
from WebScraper.aliExpressParser import get_organic_results
import json
import sys

def getAllItems():
    # Path to your JSON file
    file_path = 'public/shopping_data.json'
    

    # Open the JSON file and load its contents
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Now 'data' contains the contents of your JSON file
    print(data)  # You can work with the data as needed


def maximizeBudget():
    pass

lowestItemListing()