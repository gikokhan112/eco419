from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'bcd983c0237a4e4b97663aa0fd05398d'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

@app.route('/')
def home():
    # Get parameters from the URL
    country = request.args.get('country', 'us')  # Default to 'us'
    category = request.args.get('category', None)
    query = request.args.get('query', '')  # For search
    page = request.args.get('page', 1, type=int)  # Pagination (default page 1)

    params = {
        'apiKey': API_KEY,
        'country': country,
        'category': category,
        'q': query,  # This sends the search term to the API
        'page': page,
        'pageSize': 10  # Number of articles per page
    }

    # Fetch the articles
    if query:  # If there's a search term
        response = requests.get('https://newsapi.org/v2/everything', params=params)
    else:  # If there's no search term
        response = requests.get(BASE_URL, params=params)

    news_data = response.json()

    # Pass articles, page, query, and category to the template
    return render_template('home.html', articles=news_data.get('articles', []), page=page, query=query, category=category)

if __name__ == '__main__':
    app.run(debug=True)

