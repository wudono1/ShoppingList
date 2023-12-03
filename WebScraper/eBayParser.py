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
    