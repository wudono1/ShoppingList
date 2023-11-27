from bs4 import BeautifulSoup
import requests, json, lxml
import coverage
#Import the code coverage class so data can be run when this class is called
cov = coverage.Coverage()
cov.start()

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}


def get_organic_results(user_search_URL):
    html = requests.get(user_search_URL, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    

    data = []

    for item in soup.select('.s-item__wrapper.clearfix'):
        title = item.select_one('.s-item__title').text
        link = item.select_one('.s-item__link')['href']

        '''try:
            condition = item.select_one('.SECONDARY_INFO').text
        except:
            condition = None

        try:
            shipping = item.select_one('.s-item__logisticsCost').text
        except:
            shipping = None

        try:
            location = item.select_one('.s-item__itemLocation').text
        except:
            location = None

        try:
            watchers_sold = item.select_one('.NEGATIVE').text
        except:
            watchers_sold = None

        if item.select_one('.s-item__etrs-badge-seller') is not None:
            top_rated = True
        else:
            top_rated = False

        try:
            bid_count = item.select_one('.s-item__bidCount').text
        except:
            bid_count = None

        try:
            bid_time_left = item.select_one('.s-item__time-left').text
        except:
            bid_time_left = None

        try:
            reviews = item.select_one('.s-item__reviews-count span').text.split(' ')[0]
        except:
            reviews = None

        try:
            exctention_buy_now = item.select_one('.s-item__purchase-options-with-icon').text
        except:
            exctention_buy_now = None'''

        try:
            price = item.select_one('.s-item__price').text
        except:
            price = None

        data.append({
            'item': {'title': title, 'link': link, 'price': float(price[price.rfind("$") + 1:])}
        })

    #print(json.dumps(data, indent = 2, ensure_ascii = False))
    print(data)

if __name__ == '__main__':
    
    #item = input("Enter an item: ")
    
    test_item = "dog food"
    user_search_URL = "https://www.ebay.com" + f"/sch/{test_item.replace(' ', '+')}"
    get_organic_results(user_search_URL)
    cov.save
    cov.stop
    # Generate and print a coverage report
    cov.report
    