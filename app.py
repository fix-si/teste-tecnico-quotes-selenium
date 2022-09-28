import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

data = []

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

i = 1
while True:
    url = f"http://quotes.toscrape.com/page/{i}/"

    driver.get(url)
    quotes = driver.find_elements(
        By.CLASS_NAME, "quote")

    if quotes:
        for quote in quotes:
            buffer = {}
            quote_text = quote.find_element(By.CLASS_NAME, 'text').text
            quote_author_name = quote.find_element(
                By.CLASS_NAME, 'author').text
            quote_author_url = quote.find_element(
                By.CSS_SELECTOR, "span > a").get_attribute('href')
            tags = []
            for tag in quote.find_elements(By.CLASS_NAME, 'tag'):
                tags.append(tag.text)

            buffer['quote'] = quote_text
            buffer['author'] = {
                'name': quote_author_name, 'url': quote_author_url}
            buffer['tags'] = tags
            data.append(buffer)

    else:
        break

    i += 1

json_object = json.dumps(data, indent=4, ensure_ascii=False)


with open("data.json", "w", encoding='utf8') as outfile:
    outfile.write(json_object)

driver.close()
