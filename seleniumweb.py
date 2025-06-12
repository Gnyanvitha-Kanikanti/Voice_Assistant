from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
class infow():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    def getinfo(self,query):
        self.query = query
        self.driver.get('https://www.wikipedia.org')
        search = self.driver.find_element("xpath", '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter =self.driver.find_element("xpath", '//*[@id="search-form"]/fieldset/button')
        enter.click()