from bs4 import BeautifulSoup
import requests, json, lxml
import coverage
import os
#Import the code coverage class so data can be run when this class is called
cov = coverage.Coverage()
cov.start()


#headers for web scraping
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}


def get_organic_results_ebay(user_search_url):
    #returns title, link, price of a product listing

    html = requests.get(user_search_url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    

    data = []

    #searching thru products from ebay search tab
    for item in soup.select('.s-item__wrapper.clearfix'):
        try:
            title = item.select_one('.s-item__title').text
        except:
            title = None
        try:
            link = item.select_one('.s-item__link')['href']
        except:
            link = None

        try:
            price = item.select_one('.s-item__price').text
            price = float(price[price.rfind("$") + 1:])
        except:
            price = None

    #appending data
        if (title != "Shop on eBay" and title != None and link != None and price != None):
            data.append(
                {'title': title, 'link': link, 'price': price}
            )

    #writing data to JSON file
    '''
    output_path = os.path.join('scraperData', 'eBayItemOutput.json')
    with open(output_path, 'w') as outfile:
        json.dump(data, outfile,indent=4)
'''
    #print(json.dumps(data, indent = 2, ensure_ascii = False))
    #print(data)
    return data
'''
test_item = "water bottle"
user_search_URL = "https://www.ebay.com" + f"/sch/{test_item.replace(' ', '+')}"
results = get_organic_results_ebay(user_search_URL)
print(results[1])
'''
'''
if __name__ == '__main__':
    
    #item = input("Enter an item: ")
    
    test_item = "water bottle"
    #user_search_URL = "https://www.ebay.com" + f"/sch/{test_item.replace(' ', '+')}"
    #get_organic_results_ebay(user_search_URL)
    get_organic_results_ebay(test_item)
    
    cov.save
    cov.stop
    # Generate and print a coverage report
    cov.report
'''