from bs4 import BeautifulSoup
import requests, json
import coverage
import sys

#Import the code coverage class so data can be run when this class is called
cov = coverage.Coverage()
cov.start()


user_input = input("Please enter an item: ")


def getAll(search_url):
	HEADERS = ({
		'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
		'Accept-Language': 'en-US, en;q=0.5'})
	
	# HTTP Request
	webpage = requests.get(search_url, headers=HEADERS)

	data = []

	# Soup Object containing all data
	soup = BeautifulSoup(webpage.content, "lxml")
	for item_elem in soup.select(".card-info.list-card-layout__info"):
		title_element = item_elem.select_one('.search-card-e-title a')
		
		if title_element:
			title = title_element.get_text(strip=True)
			link = item_elem.select_one('.search-card-e-detail-wrapper')['href']
            
			try:
				price = item_elem.select_one('.search-card-e-price-main').text
			except:
				price = None
		data.append({
			'item': {'title': title, 'link': link, 'price': float(price[price.rfind("$") + 1:])}
		})
		print(json.dumps(data, indent=2, ensure_ascii=False))
	
	


'''
def getLinkAndPrice(item):
	# The webpage URL
	URL = "https://www.alibaba.com" + f"/trade/search?spm=a2700.galleryofferlist.pageModule_fy23_pc_search_bar.keydown__Enter&tab=all&searchText={item.replace(' ', '+')}"
    
    # Headers for request
	HEADERS = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
		'Accept-Language': 'en-US, en;q=0.5'
	}

	# HTTP Request
	webpage = requests.get(URL, headers=HEADERS)

	data = []

	# Soup Object containing all data
	soup = BeautifulSoup(webpage.content, "lxml")


	for item_elem in soup.select(".card-info.list-card-layout__info"):
		title_element = item_elem.select_one('.search-card-e-title a')
		
		if title_element:
			title = title_element.get_text(strip=True)
			link = item_elem.select_one('.search-card-e-detail-wrapper')['href']
            
			try:
				price = item_elem.select_one('.search-card-e-price-main').text
			except:
				price = None
		data.append({
			'item': {'title': title, 'link': link, 'price': float(price[price.rfind("$") + 1:])}
		})
		print(json.dumps(data, indent=2, ensure_ascii=False))
'''
		

if __name__ == '__main__':
	
	search_url = "https://www.alibaba.com" + f"/trade/search?spm=a2700.galleryofferlist.pageModule_fy23_pc_search_bar.keydown__Enter&tab=all&searchText={user_input.replace(' ', '+')}"
	# Headers for request
	HEADERS = ({'User-Agent':
	            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	            'Accept-Language': 'en-US, en;q=0.5'})

	'''
	# HTTP Request
	webpage = requests.get(search_url, headers=HEADERS)

	# Soup Object containing all data
	soup = BeautifulSoup(webpage.content, "lxml")
	'''
	
	getAll(search_url)
	
	cov.stop()
	cov.save()
	cov.report()
