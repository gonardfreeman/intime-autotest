from selenium import webdriver
from base import Page
from locators import *

class MainPage(Page):
    def check_page_is_load(self):
        return True if self.find_element(*MainPageLocators.LOGO) else False

    def check_search_field(self):
        return True if self.find_element(*MainPageLocators.SEARCH) else False

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    x = MainPage(webdriver.Chrome(chrome_options=options))
    x.open('')
    print(x.check_page_is_load())
    print(x.check_search_field())