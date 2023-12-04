import os
import sys
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher

# Add the relative Scrapy project path to the system path
sys.path.append('./amazon')

from amazon.amazon.spiders.amazonSearchSpider import amazonSearchSpider  # Import your spider

def run_spider():
    
    # Initialize CrawlerRunner with custom settings
    runner = CrawlerRunner()

    # Connect a callback function to the spider_closed signal
    def spider_closed(spider):
        reactor.stop()

    # Register the callback
    dispatcher.connect(spider_closed, signal=signals.spider_closed)

    # Run the spider
    d = runner.crawl(amazonSearchSpider)
    d.addBoth(lambda _: reactor.stop())

    # Start the reactor (event loop)
    from twisted.internet import reactor
    reactor.run()

if __name__ == "__main__":
    run_spider()
