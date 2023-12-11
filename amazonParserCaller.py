import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
amazon_scrapy_dir = os.path.join(current_dir, '..', 'WebScraper', 'amazon', 'amazon')
sys.path.append(amazon_scrapy_dir)
#sys.path.append('/ShoppingList/WebScraper/amazon/amazon')

#calls the scrapy amazon spider from within the amazon folder
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from WebScraper.amazon.amazon.spiders.amazonSearchSpider import amazonSearchSpider  # Import your spider class


def run_spider_amazon(item):
    #Output path for amazon scraper data
    
    output_relative_path = os.path.join('..', '..', 'scraperData', 'amazonItems.json')

    output_path = os.path.join('scraperData', 'amazonItems.json')
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, 'scraperData', 'amazonItems.json') 
    
    
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
    

    '''
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
    amazonSearchSpider.keyword_list = [item]
    runner = CrawlerRunner()

    d = runner.crawl("amazon")
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # the script will block here until the crawling is finished
    '''

'''if __name__ == "__main__":
    run_spider_amazon("phone case")
'''