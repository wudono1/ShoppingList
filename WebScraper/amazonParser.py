from bs4 import BeautifulSoup
import requests
import coverage
import json

# Import the code coverage class so data can be run when this class is called
cov = coverage.Coverage()
cov.start()

user_input = input("Please enter an item: ")

HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
})


def get_organic_results(user_search_URL):
    html = requests.get(user_search_URL, headers=HEADERS).text
    soup = BeautifulSoup(html, 'lxml')
    

    data = []

    for item in soup.select('.puis-padding-right-micro'):
        print(item)
        '''       
        title = item.select_one('.a-size-base-plus .a-color-base .a-text-normal').text
        link = item.select_one('.a-link-normal .s-underline-text .s-underline-link-text .s-link-style .a-text-normal')['href']

        try:
            price = item.select_one('.a-offscreen').text
        except:
            price = None

        data.append({
            'item': {'title': title, 'link': link, 'price': float(price[price.rfind("$") + 1:])}
        })
        '''
    #print(json.dumps(data, indent = 2, ensure_ascii = False))
    print(data)
          

# Function to extract Product Title
def get_title(soup):
    try:
        # Outer Tag Object
        title = soup.find("span", id={"productTitle"}, attrs={"class": 'a-size-large product-title-word-break'})

        # Inner NavigableString Object
        title_value = title.string

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Product Price
def get_price(soup):
    try:
        price = soup.find("span", attrs={'class': 'aok-offscreen'}).string.strip()

    except AttributeError:
        price = ""

    return price


if __name__ == '__main__':
    '''
    search_url = "https://www.amazon.com" + f"/s?k={user_input.replace(' ', '+')}"
    
    # Headers for request
    
    
    # HTTP Request
    webpage = requests.get(search_url, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")

    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

    # Store the links
    links_list = []

    # Loop for extracting links from Tag Objects
    for link in links:
        if len(links_list) >= 10:
            break  # Stop adding links if the list size is already 10
        links_list.append(link.get('href'))

    for link in links_list:
        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        # Function calls to display all necessary product information
        print("Product Title =", get_title(new_soup))
        print("Product Price =", get_price(new_soup))
        #print("Product Rating =", get_rating(new_soup))
        #print("Number of Product Reviews =", get_review_count(new_soup))
        print()
        print()
    '''

    headers = {
        "access-control-allow-credentials": "true",
        "access-control-allow-origin": "*",
        "content-length": "2085",
        "content-type": "application/json",
        "date": "Sat, 02 Dec 2023 23:18:18 GMT",
        "expect-ct": "max-age=2592000, report-uri=\"https://sentry.repl.it/api/10/security/?sentry_key=615192fd532445bfbbbe966cd7131791\"",
        "replit-cluster": "global",
        "server": "RapidAPI-1.2.8",
        "strict-transport-security": "max-age=7095596; includeSubDomains",
        "x-rapidapi-region": "AWS - us-east-1",
        "x-rapidapi-version": "1.2.8",
        "x-ratelimit-rapid-free-plans-hard-limit-limit": "500000",
        "x-ratelimit-rapid-free-plans-hard-limit-remaining": "499993",
        "x-ratelimit-rapid-free-plans-hard-limit-reset": "2002207",
        "x-ratelimit-requests-limit": "500000",
        "x-ratelimit-requests-remaining": "499993",
        "x-ratelimit-requests-reset": "2002207"
}

    url = "https://dripcrawler.p.rapidapi.com/"

    payload = {
        "url": "https://www.amazon.com/s?k=phone&page=1",
        "javascript_rendering": "False"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "fd741e6270mshf71dc7aeb399912p1935b1jsn086c169e3203",
        "X-RapidAPI-Host": "dripcrawler.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())

    cov.stop()
    cov.save()
    # Generate and print a coverage report
    cov.report()
