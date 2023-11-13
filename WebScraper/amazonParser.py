from bs4 import BeautifulSoup
import requests
import coverage

# Import the code coverage class so data can be run when this class is called
cov = coverage.Coverage()
cov.start()

user_input = input("Please enter an item: ")

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

''' Function to extract Product Rating
def get_rating(soup):
    try:
        rating = soup.find("span", attrs={'class': 'a-size-base a-color-base'}).string.strip()

    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()
        except:
            rating = ""

    return rating
    '''

'''Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'class': 'a-size-base'}).string.strip()

    except AttributeError:
        review_count = ""

    return review_count
    '''

if __name__ == '__main__':
    search_url = "https://www.amazon.com" + f"/s?k={user_input.replace(' ', '+')}"
    # Headers for request
    HEADERS = ({
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    })

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

    cov.stop()
    cov.save()
    # Generate and print a coverage report
    cov.report()
