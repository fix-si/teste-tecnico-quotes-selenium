from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class SeleniumService():

    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def close(self):
        self.driver.quit()

    def get_url(self, url):
        try:
            self.driver.get(url)
            return True
        except:
            return False


    def get_quotes_divs(self, atribute):
            
        divs = self.driver.find_elements(By.CLASS_NAME, atribute)

        return divs

    def get_data(self, atribute):

        data = self.driver.find_element(By.CLASS_NAME, atribute).text

        return data

    def verify_next_button(self):

        try:
            self.driver.find_element(By.CLASS_NAME, 'next')
            return True
        except:
            return False

    def click_next_page(self):

        next_page = self.driver.find_element(By.CSS_SELECTOR, 'body > div > div:nth-child(2) > div.col-md-8 > nav > ul > li.next > a').get_attribute('href')

        self.get_url(next_page)