from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from amazon.spiders.amazonSearchSpider import amazonSearchSpider  # Assuming your spider is in a file named amazon_spider.py
import os

'''class amazonSpiderCaller:
    item = "green pants"

    def run_spider(self):
        amazonSearchSpider.keyword_list = [self.item]
        process = CrawlerProcess(get_project_settings())
        process.crawl(amazonSearchSpider)
        process.start()'''
