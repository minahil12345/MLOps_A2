import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.bbc.com/news/articles/crgy7xypwj8o'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
script_tag = soup.find('script', id='__NEXT_DATA__')

# Extract the JSON data
if script_tag:
    json_data = json.loads(script_tag.contents[0])

    print(json_data.keys())

    # Access the specific data you need
    props = json_data.get('props', {})
    page_props = props.get('pageProps', {})
    articles = page_props.get('page', {}).get('@\"news\",\"articles\",\"crgy7xypwj8o\",', {}).get('contents', [])

    for article in articles:
        
        headline = article.get('type', {}).get('headline', {}).get('model', {}).get('blocks', [])[0].get('model', {}).get('blocks', [])[0].get('model', {}).get('text', '')
        print('Headline:', headline)