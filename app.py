from WebScraper.eBayParser import get_organic_results
from WebScraper.amazonParser import get_title, get_price, get_rating, get_review_count
from WebScraper.alibabaParser import get_title, get_price, get_image, get_rating
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        item_name = request.form['item_name']
        user_search_URL_ebay = "https://www.ebay.com" + f"/sch/{item_name.replace(' ', '+')}"
        result = get_organic_results(user_search_URL_ebay)
        return result

if __name__ == '__main__':
    app.run(debug=True)


