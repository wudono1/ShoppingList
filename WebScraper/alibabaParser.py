from bs4 import BeautifulSoup
import requests

user_input = input("Please enter an item: ")

# Function to extract Product Title
def get_title(soup):
	
	try:
		# Outer Tag Object
		title = soup.find('h2', attrs={'data-aplus-auto-card-mod': 'area=title&areaContent=2row&target=detail'})

		# Inner NavigableString Object
		title_value = title.string

		# Title as a string value
		title_string = title_value.strip()

		# # Printing types of values for efficient understanding
		# print(type(title))
		# print(type(title_value))
		# print(type(title_string))
		# print()

	except AttributeError:
		title_string = ""	

	return title_string

# Function to extract Product Price
def get_price(soup):

	try:
		price = soup.find('div', class_='search-card-e-price-main').string.strip()

	except AttributeError:
		price = ""	

	return price

# Function to extract Product Rating
def get_rating(soup):

	try:
		rating = soup.find("i", attrs={'class':'.seb-supplier-review__score'}).string.strip()
		
	except AttributeError:
		
		try:
			rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
		except:
			rating = ""	

	return rating

# Function to extract image url
def get_image(soup):
	try:
		image_url = soup.find("span", attrs={'class':'.seb-img-switcher__imgs img'}).string.strip()
		
	except AttributeError:
		image_url = ""	

	return image_url

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
	print("Product Title =", get_title(soup))
	print("Product Price =", get_price(soup))
	print("Product Rating =", get_rating(soup))
	print("Number of Product Reviews =", get_image(soup))
	print(URL)
	print()
	print()
