# ShoppingList

A Chrome extension that helps users find everything on their shopping list online for cheap prices. Users can input a budget in US dollars as well as a list of items (a word or phrase that describes what they want to buy) into their shopping list. The application then takes the shopping list and budget, scrapes amazon.com, ebay.com, and alibab.com by searching for those items, and returns the cheapest items that fit under the shopping list. The application does not account for shipping and other additional fees.

GitHub: https://github.com/wudono1/ShoppingList



Extensions and packages needed:

For web server functionality: Install npm from the Node.js official website. You can find other tutorials on downloading npm and node.js online
After you have done so, install the following using the terminal command "npm install" or ("sudo npm install" for some) followed by: --save-dev mocha nyc, JSDOM, requests, requests_mock, npm express, node js

For backend: pip (or pip3) install: bs4, scrapy, coverage, unittest2, scrapeops-scrapy, scrapeops-scrapy-proxy-sdk, twisted, crochet



Web Scraping Notes: 

1. The Amazon webscraper uses the Scrapy webscraping framework, which is contained within the amazon folder within the WebScraper directory. The web scraping spider has filepath shoppinglist/webscraper/amazon/amazon/spiders/amazonSearchSpider.py, and the spider in that file has name = "amazon".

If you want to test the amazon spider itself, cd to any location within the /ShoppingList/WebScraper/amazon subdirectory in the terminal and run the following in the terminal: scrapy crawl amazon. The results of the scrape will show up in a a json file at ShoppingList/WebScraper/amazon/amazonItems.json. Note, however, that changing the name of the spider from (name = "amazon") to something else, for example, (name = "amazon_spider") will mean that the terminal command to run the spider will be "scray crawl amazon_spider" instead of "scrapy crawl amazon".

If you use listAlgo.py to call the spider, you can simply run the python file itself to run it like any other Python script using run_spider_amazon() in the file. The results of the scrape will show up at ShoppingList/scraperData/amazonItems.json However, you should make sure that you are in the correct root directory (ShoppingList) if you decide to run listAlgo.py from the terminal. If you are in the subdirectory ShoppingList/scraperData, for example, running listAlgo from the terminal will return an error.

In order to bypass Amazon's automatic detection of web scraping, we use an api using a free account from ScrapeOps.io. However, ScrapeOp's free account only gives 1,000 page scraping credits. If those 1000 credits are used up, a new API key must be used.  Our project only uses ScrapeOps for the Amazon spider, so the API affects none of the other web scrapers. Current locations of the key can be found in the files ShoppingList/WebScraper/amazon/amazon/settings.py and ShoppingList/amazonParserCaller.py. As of time of submission, there are approximately 800 credits left. Once the credits have expired, the amazon spider will no longer return results when ran. To fix this, simply create a free account on ScrapeOps.io and copy the API key given to you into the appropriate locations within the two files designated above. The password to the account that contains the old API key is not needed.

Finally, to run either ShoppingList/listAlgo.py or ShoppingList/amaonParserCaller.py, make sure that you are in the ShoppingList directory. If you are in an inner directory such as WebScraper or scraperData, the files will not run properly.


2. The eBay, aliExpress, and Alibaba parsers use custom headers to bypass scraping restrictions. If the headers deprecate, there are a variety of proxy methods, headers, and APIs that can be found online to bypass webscraping restrictions.


3. While the current package has four working webscrapers (amazon, aliExpress, eBay, Alibaba), we do not utilize Alibaba. This is because we felt that alibaba's search results were too industrial in nature and would not be useful to a normal customer who would shop through our application. However, since we strongly considered using it, we chose to keep it there instead of deleting it. For aliExpress and eBay, the results of the scrape will appear at the directory ShoppingList/scraperData



Instructions to run:

1. make sure the node server is running by entering "node server.js" in the terminal, and clicking on the localhost link.


2. Access your HTML file through the server, for example, by navigating to http://localhost:3000 in your browser. For reference, your terminal  should look like this:
    Example terminal output for accessing HTML file: 
    donovan@Donovans-MacBook-Pro ShoppingList % node server.js                                                           
    Server is running at http://localhost:3000 <---click on this link


3. In the textbox that displays "Enter item here...", enter a word or phrase for the item that you want to buy. Generally, being more specific when entering an item may allow for more pertinent results. Once you have entered an item, the item will appear under the "Shopping List Items" section. You may toggle the priority of the item between "high", "medium", and "low", depending on how much you want to buy that item. When finding your items online, the webscraper will first fit high-priority items into your budget until there are no more high-priority items that fit under the remaining budget. It will do the same with all medium- and all low- priority items, in that order. 

If you want to change you item description, you may press the "edit" button to do so, and press the "save" button that appears afterwards to save your changes. if you no longer want to look for that item, pressing the "delete" button will remove that item from your shopping list.

You may also enter a maximum budget in USD into the "budget" textbox that the website will not exceed when shopping for your items. If you don't enter a budget, the site will default to a $100 budget. Once you press the "Find your items online!" button, the user input data will appear at ShoppingList/public/shopping_data.json.


4. Wait for the results to compute. Webscraping is inherently slow, so one item may take up to 10 seconds sometimes. The results will appear directly under the "Find your items online!" button. If you've already pressed the "Find your items online!" button and the webpage displayed your results, but you want to search for another list of items, simply enter your new items, press "Find your items online!" button again, and the old shopping results should be automatically cleared.

   NOTE: When looking through the shopping results, you may notice that the cheapest items are consistently from AliExpress. This is not a bug; rather, AliExpress usually offers a "Welcome Deal" to first-time buyers. Though we have not bought anything on the site yet, our assumption is that, once the site's users are logged into AliExpress and have already bought something, the prices will revert to normal. Additionally, because AliExpress buys directly from manufacturers, they are able to resell items at a relatively cheap cost compared to other companies.
