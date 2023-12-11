from bs4 import BeautifulSoup
import requests, json, lxml
import coverage
#Import the code coverage class so data can be run when this class is called
import re


cov = coverage.Coverage() #for testing
cov.start()

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}


def get_organic_results_alie(user_search_URL):  
    #finds all relevant item results for aliExpress

    html = requests.get(user_search_URL, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    

    data = []

    for item in soup.select('.search-item-card-wrapper-gallery'):
        try:
            title = item.select_one('.multi--titleText--nXeOvyr').text
        except:
            title = None

        try:
            link = item.select_one('.search-card-item')['href']
        except:
            link = None

        try:
            price_el = item.select_one('.multi--price-sale--U-S0jtj')
            price = float(price_el.select('span')[1].text + price_el.select('span')[2].text + price_el.select('span')[3].text)
        except:
            price = None

        if (title != None and link != None and price != None):
            data.append(
                {'title': title, 'link': link, 'price': price}
            )

        
    '''
    #writes data to JSON file, can be uncommented and run for testing purposes
    output_path = os.path.join('scraperData', 'aliExpItemOutput.json')
    with open(output_path, 'w') as outfile:
        json.dump(data, outfile,indent=4)
    
    #print(json.dumps(data, indent = 2, ensure_ascii = False))
    print(data)
    '''
    return data


'''
Also for testing purposes, commented out for final
if __name__ == '__main__':
    
    #item = input("Enter an item: ")
    
    test_item = "bottle"
    user_search_URL = "https://aliexpress.us/w/wholesale-" + f"{test_item.replace(' ', '-')}" + ".html"
    #get_organic_results_alie(user_search_URL)
    
    cov.save    #for testing
    cov.stop
    # Generate and print a coverage report
    cov.report
'''