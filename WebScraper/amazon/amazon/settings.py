
BOT_NAME = 'amazon'

SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

SCRAPEOPS_API_KEY = '333c5a4f-1191-4528-91eb-8b27c874def4'

SCRAPEOPS_PROXY_ENABLED = True
# SCRAPEOPS_PROXY_SETTINGS = {'country': 'us'}

# Add In The ScrapeOps Monitoring Extension
EXTENSIONS = {
'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
}

FEEDS = { 
    "amazonItems.json": { 
        'format': 'json',
        'overwrite' : 'TRUE'
    }
    }

LOG_LEVEL = 'INFO'

DOWNLOADER_MIDDLEWARES = {

    ## ScrapeOps Monitor
    'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    
    ## Proxy Middleware
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

# Max Concurrency On ScrapeOps Proxy Free Plan is 1 thread
CONCURRENT_REQUESTS = 1