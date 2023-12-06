from typing import Any, Optional
import scrapy
from urllib.parse import urljoin

class amazonSearchSpider(scrapy.Spider):
    keyword_list = ['napkins']
    name = "amazon"
    
    def start_requests(self):
        for keyword in self.keyword_list:
            amazon_search_url = "https://www.amazon.com" + f"/s?k={keyword.replace(' ', '+')}"
            yield scrapy.Request(url=amazon_search_url, callback=self.parse_search_results, meta={'keyword': keyword, 'page': 1})

    def parse_search_results(self, response):
        page = response.meta['page']
        keyword = response.meta['keyword'] 

        ## Extract Overview Product Data
        search_products = response.css("div.s-result-item[data-component-type=s-search-result]")
        for product in search_products:
            relative_url = product.css("h2>a::attr(href)").get()
            asin = relative_url.split('/')[3] if len(relative_url.split('/')) >= 4 else None
            product_url = urljoin('https://www.amazon.com/', relative_url).split("?")[0]

            #price_as_string = product.css(".a-price[data-a-size=xl] .a-offscreen::text").get()
            if (product_url != "https://www.amazon.com/sspa/click"):
                yield  {
                        "keyword": keyword,
                        "asin": asin,
                        "url": product_url,
                        "ad": True if "/slredirect/" in product_url else False, 
                        "title": product.css("h2>a>span::text").get(),
                        "price": product.css(".a-price[data-a-size=xl] .a-offscreen::text").get(),
                        "rating": (product.css("span[aria-label~=stars]::attr(aria-label)").re(r"(\d+\.*\d*) out") or [None])[0],
                    }

