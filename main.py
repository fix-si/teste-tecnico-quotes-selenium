from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
from time import sleep
options = Options()
options.add_argument("--headless") 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("http://quotes.toscrape.com")
citacoes = {
    "data":[]
}



elements = []
existsNextPage = True
while existsNextPage:
    sleep(5)
    for data in driver.find_elements(By.CLASS_NAME,"quote"):
        quote = data.find_element(By.CLASS_NAME,"text").text
        authorName = data.find_element(By.CSS_SELECTOR,".author").text
        authorUrl = data.find_element(By.CSS_SELECTOR,"span>a").get_attribute("href")
        rawTags = data.find_elements(By.CSS_SELECTOR,".tag")
        tags = []
        for tag in rawTags:
            tags.append(tag.text)
        quote = {
            "quote": quote,
            "author": {
                "name": authorName,
                "url": authorUrl
            },
            "tags": tags

        }
        citacoes.get("data").append(quote)
    if(driver.find_elements(By.CSS_SELECTOR, ".next")==[]):
        existsNextPage = False
    else:
        driver.get(driver.find_elements(By.XPATH, "/html/body/div/div[2]/div[1]/nav/ul/li[contains(@class, 'next')]/a")[0].get_attribute("href"))



with open("citacoes.json", "w") as arquivo:
    json.dump(citacoes, arquivo, indent=4)
print('Salvo com sucesso')



driver.quit()
		
		