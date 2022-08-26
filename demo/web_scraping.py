from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json
    
with open('demo/data/'+'data.json', 'w') as f:
    json.dump([], f)

def write_json(new_data, filename='data.json'):
    with open('demo/data/'+filename, 'r+') as f:
        file_data = json.load(f)
        
        file_data.append(new_data)
        
        f.seek(0)
        
        json.dump(file_data, f, indent=4, ensure_ascii=False)

# Utilizei a biblioteca webdriver-manager para gerenciar o binario do browser.
browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('http://quotes.toscrape.com/')

isNextDisabled = False

while not isNextDisabled:

    try:
        items =  browser.find_elements(By.XPATH, '//div[@class="quote"]') 

        for item in items:
            
            quote = item.find_element(By.CLASS_NAME, 'text').text
            quote = quote.strip('“”')
            
            author = item.find_element(By.CLASS_NAME, 'author').text
            url = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
            
            try:
                tags = item.find_elements(By.CLASS_NAME, 'tag')
                tag_list = []
                
                for tag in tags:
                    tag = tag.text
                    tag_list.append(tag)
            except:
                pass
            
            write_json({
                "quote": quote,
                "author": {
                    "name": author,
                    "url": url,
                },
                "tags": tag_list
            })
        
        try:
            next_btn = browser.find_element(By.XPATH, '//li[@class="next"]/a')
            next_btn.click()
        except:
            isNextDisabled = True
        
    except Exception as e:
        print(e, "error")
        isNextDisabled = True

    