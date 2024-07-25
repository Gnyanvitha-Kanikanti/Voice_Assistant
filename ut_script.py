from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
class music():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    def play(self,query):
        self.query = query
        self.driver.get('https://www.youtube.com/results?search_query='+query)
        video = self.driver.find_element("xpath", '//*[@id="dismissible"]')
        video.click()