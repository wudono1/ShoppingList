import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
amazon_scrapy_dir = os.path.join(current_dir, '..', 'WebScraper', 'amazon', 'amazon')
sys.path.append(amazon_scrapy_dir)
#sys.path.append('/ShoppingList/WebScraper/amazon/amazon')


#calls the scrapy amazon spider from within the amazon folder

from scrapy.crawler import CrawlerProcess
from WebScraper.amazon.amazon.spiders.amazonSearchSpider import amazonSearchSpider  # Import your spider class

def run_spider(item):
    #Output path for amazon scraper data
    output_path = os.path.join('scraperData', 'amazonItemOutput.json')
    

    #crawler settings
    process = CrawlerProcess(settings={
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
    

    amazonSearchSpider.keyword_list = [item]
    process.crawl(amazonSearchSpider)  # Replace AmazonSearchSpider with your spider class name
    process.start()

if __name__ == "__main__":
    run_spider("phone case")


'''
import sys
sys.path.append('/Users/donovan/Documents/GitHub/ShoppingList/WebScraper/amazon/amazon')
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
from amazon.amazon.spiders.amazonSearchSpider import AmazonSearchSpider  # Import your spider class

def run_spider():
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',  # Example: Output to JSON
        'FEED_URI': 'output.json'  # Example: Output filename
        # Add other settings as needed
    })
    
    process.crawl(AmazonSearchSpider)  # Replace AmazonSearchSpider with your spider class name
    process.start()

if __name__ == "__main__":
    run_spider()
'''