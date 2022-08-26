from selenium_service import SeleniumService
import json

selenium_service = SeleniumService()
url = 'http://quotes.toscrape.com/'

selenium_service.get_url(url=url)

data = {}
quotes = []

while selenium_service.verify_next_button():

    for quote in selenium_service.get_quotes_divs('quote'):
        text_filter = quote.text.split('\n')

        quote = text_filter[0].strip()
        author_name = text_filter[1][3:-8]

        if '.' in author_name:
            author_name = author_name.replace(' ', '')
            author_name = author_name.replace('.', '-')
        
        replaced_author_name = author_name.replace(' ', '-')

        author_url = url + f'author/{replaced_author_name}'

        tag = text_filter[2].split(':')[1].strip() if len(text_filter) > 2 else ''
        tags = tag.split(' ')

        quote_data = {
            'quote': quote,
            'author': {
                'name': author_name,
                'url': author_url,
            },
            'tags': tags
        }

        quotes.append(quote_data)
    
    selenium_service.click_next_page()

print(quotes)

data["data"] = quotes

with open("quotes.json", "w", encoding="utf-8") as arquivo:
    json.dump(data, arquivo, ensure_ascii=False, indent=4)
