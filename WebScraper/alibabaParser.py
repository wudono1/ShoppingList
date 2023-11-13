from bs4 import BeautifulSoup
import requests
import coverage
#Import the code coverage class so data can be run when this class is called
cov = coverage.Coverage()
cov.start()


user_input = input("Please enter an item: ")

# Function to extract Product Price
def get_price(soup):

	try:
		price = soup.find('div', class_='search-card-e-price-main').string.strip()

	except AttributeError:
		price = ""	

	return price

# Function to extract Product url
def get_url(soup):
	try:
		url_a = soup.find('a', class_='search-card-e-slider__link search-card-e-slider__gallery')
		url_value = url_a.get('href') if url_a else None
		
	except AttributeError:
		url_value = ""	

	return url_value

if __name__ == '__main__':

	search_url = "https://www.alibaba.com" + f"/trade/search?spm=a2700.galleryofferlist.pageModule_fy23_pc_search_bar.keydown__Enter&tab=all&searchText={user_input.replace(' ', '+')}"
	# Headers for request
	HEADERS = ({'User-Agent':
	            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	            'Accept-Language': 'en-US, en;q=0.5'})
    # The webpage URL
	URL = search_url

	# HTTP Request
	webpage = requests.get(URL, headers=HEADERS)

	# Soup Object containing all data
	soup = BeautifulSoup(webpage.content, "lxml")

	# Function calls to display all necessary product information
	print("Product Price =", get_price(soup))
	print("Product URL =", get_url(soup))
	print(URL)
	print()
	print()
	cov.stop()
	cov.save()
	cov.report()