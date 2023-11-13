import unittest
from unittest.mock import patch
from bs4 import BeautifulSoup
from requests import Response
import requests_mock
import requests
from alibabaParser import get_price, get_url 

#run tests with coverage run -m unittest TestProductInfo.py
#run tests with coverage report -m

class TestProductInfo(unittest.TestCase):

    def setUp(self):
        self.user_input = "laptop"
        self.search_url = f"https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.pageModule_fy23_pc_search_bar.keydown__Enter&tab=all&searchText={self.user_input.replace(' ', '+')}"

    @requests_mock.Mocker()
    def test_get_price(self, mock_request):
        # Mock the HTTP request and response
        mock_request.get(self.search_url, text='<div class="search-card-e-price-main">$145.60 - $154.90</div>')
        
        # Call the function with the mocked request
        with patch('builtins.input', return_value=self.user_input):
            price = get_price(BeautifulSoup(requests.get(self.search_url).content, "lxml"))

        # Assert the result
        self.assertEqual(price, '$145.60 - $154.90')

    @requests_mock.Mocker()
    def test_get_url(self, mock_request):
        # Mock the HTTP request and response
        mock_request.get(self.search_url, text='<a class="search-card-e-slider__link search-card-e-slider__gallery" href="https://www.alibaba.com/product-detail/wholesale-laptops-Cheapest-OEM-Core-i5_1600705379299.html?spm=a2700.galleryofferlist.topad_classic.d_title.3efe1ac8LCfFQf">Test URL</a>')

        # Call the function with the mocked request
        with patch('builtins.input', return_value=self.user_input):
            url = get_url(BeautifulSoup(requests.get(self.search_url).content, "lxml"))

        # Assert the result
        self.assertEqual(url, 'https://www.alibaba.com/product-detail/wholesale-laptops-Cheapest-OEM-Core-i5_1600705379299.html?spm=a2700.galleryofferlist.topad_classic.d_title.3efe1ac8LCfFQf')


if __name__ == '__main__':
    unittest.main()
