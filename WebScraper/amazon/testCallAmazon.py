from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from amazon.spiders.amazonSearchSpider import amazonSearchSpider  # Assuming your spider is in a file named amazon_spider.py

def run_spider(items):
    item = "pants"
    amazonSearchSpider.keyword_list = [item]
    process = CrawlerProcess(get_project_settings())
    process.crawl(amazonSearchSpider)
    process.start()

if __name__ == "__main__":
    run_spider()
