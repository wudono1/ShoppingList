import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from amazonParser import get_title, get_price, get_rating, get_review_count

class TestProductInfoExtraction(unittest.TestCase):
    @patch('requests.get')
    def test_get_title(self, mock_requests_get):
        # Mock the HTTP request and response
        mock_response = MagicMock()
        mock_response.content = b'<span class="a-size-medium a-color-base a-text-normal">Sample Product</span>'
        mock_requests_get.return_value = mock_response

        soup = BeautifulSoup(mock_response.content, 'lxml')
        title = get_title(soup)

        self.assertEqual(title, 'Sample Product')

    @patch('requests.get')
    def test_get_price(self, mock_requests_get):
        # Mock the HTTP request and response
        mock_response = MagicMock()
        mock_response.content = b'<span class="a-offscreen">$99.99</span>'
        mock_requests_get.return_value = mock_response

        soup = BeautifulSoup(mock_response.content, 'lxml')
        price = get_price(soup)

        self.assertEqual(price, '$99.99')

    @patch('requests.get')
    def test_get_rating(self, mock_requests_get):
        # Mock the HTTP request and response
        mock_response = MagicMock()
        mock_response.content = b'<i class="a-icon a-icon-star a-star-4-5">4.5 out of 5 stars</i>'
        mock_requests_get.return_value = mock_response

        soup = BeautifulSoup(mock_response.content, 'lxml')
        rating = get_rating(soup)

        self.assertEqual(rating, '4.5 out of 5 stars')

    @patch('requests.get')
    def test_get_review_count(self, mock_requests_get):
        # Mock the HTTP request and response
        mock_response = MagicMock()
        mock_response.content = b'<span class="a-size-base s-underline-text">100 reviews</span>'
        mock_requests_get.return_value = mock_response

        soup = BeautifulSoup(mock_response.content, 'lxml')
        review_count = get_review_count(soup)

        self.assertEqual(review_count, '100 reviews')

if __name__ == '__main__':
    unittest.main()
