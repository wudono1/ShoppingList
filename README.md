# ShoppingList
A Chrome extension that helps users find everything on their shopping list

GitHub: https://github.com/wudono1/ShoppingList

Extensions and packages needed:
For web functionality: Need bs4, npm, npm install --save-dev mocha nyc, JSDOM, requests, requests_mock, npm express, node js
For backend, pip (or pip3) install: bs4, scrapy, coverage, unittest2, scrapeops-scrapy, scrapeops-scrapy-proxy-sdk, twisted, crochet

Web Scraping Notes: 
1. The Amazon webscraper uses the Scrapy webscraping framework, which is contained within the amazon folder within the WebScraper directory. The web scraping spider has filepath shoppinglist/webscraper/amazon/amazon/spiders/amazonSearchSpider.py, and the spider in that file has name = "amazon". The amazonParserCaller.py file is a file that is able to call the spider from outside the scrapy project directory. 

If you want to test the spider itself, cd to the outer amazon folder in the terminal (cd webscraper/amazon/amazon/spiders) and run the following in the terminal: scrapy crawl amazon. The results of the scrape will show up in a a json file at ShoppingList/WebScraper/amazon/amazonItems.json.
If you use amazonParserCaller.py or listAlgo.py to call the spider, you can simply run the python file itself to run it like any other Python script. The results of the scrape will show up at ShoppingList/scraperData/amazonItems.json

In order to bypass Amazon's automatic detection of web scraping, we use an api using a free account from ScrapeOps.io. However, ScrapeOp's free account only gives 1,000 page scraping credits. If those 100 credits are used up, a new API key must be used. The current locations of the key can be found in the files ShoppingList/WebScraper/amazon/amazon/settings.py and ShoppingList/amazonParserCaller.py. As of time of submission, there are approximately 950 credits left. Once the credits have expired, the amazon spider will no longer run successfully. To fix this, simply create a free account on ScrapeOps.io and copy the API key given to you into the appropriate locations within the two files designated above.

Finally, to run either ShoppingList/listAlgo.py or ShoppingList/amaonParserCaller.py, make sure that you are in the ShoppingList directory. If you are in an inner directory such as WebScraper or scraperData, the files will not run properly.

2. The eBay, aliExpress, and Alibaba parsers use custom headers to bypass scraping restrictions. If the headers deprecate, there are a variety of headers for beautiful soup to bypass scraping restrictions. These can be found with a Google search.

3. While the current package has four working webscrapers (amazon, aliExpress, eBay, Alibaba), we do not utilize Alibaba. This is because we felt that alibaba's search results were too industrial in nature and would not be useful to a normal customer who would shop through our application. However, since we strongly considered using it, we chose to keep it there instead of deleting it. For aliExpress and eBay, the results of the scrape will appear at the directory ShoppingList/scraperData



Instructions to run:
1. make sure the node server is running by entering "node server.js" in the terminal, and clicking on the localhost link.

2. Access your HTML file through the server, for example, by navigating to http://localhost:3000 in your browser. Once you press the "Find your items online!" button, the user input data will appear at ShoppingList/public/shopping_data.json.
    Example terminal output for accessing HTML file: 
    donovan@Donovans-MacBook-Pro ShoppingList % node server.js                                                           
    Server is running at http://localhost:3000 <---click on this link
3. Run the listAlgo.py file. The method should take approximately 30 seconds. The result will be in finalShoppingList.json.
