from selenium import webdriver
from base import Page
from locators import *
import cities
import time

class MainPage(Page):
    def check_page_is_load(self):
        return True if self.find_element(*MainPageLocators.LOGO) else False

    def check_search_field(self):
        return True if self.find_element(*MainPageLocators.SEARCH) else False


class CalcPage(Page):
    def choose_city_from(self):
        self.find_element(*CalcPageLocators.FROM_CITY).send_keys('кие')
        time.sleep(2)
        for i in self.find_elements(*CalcPageLocators.FROM_CITY_LI):
            a = cities.Cities.KIEV
            if i.text == a:
                i.click()

    def choose_city_to(self):
        self.find_element(*CalcPageLocators.TO_CITY).send_keys('харьк')
        time.sleep(2)
        for i in self.find_elements(*CalcPageLocators.TO_CITY_LI):
            a = cities.Cities.KHARKOV
            if i.text == a:
                i.click()

    def volumes(self):
        self.find_element(*CalcPageLocators.WEIGHT).send_keys('2')
        self.find_element(*CalcPageLocators.HEIGHT).send_keys('42')
        self.find_element(*CalcPageLocators.WIDTH).send_keys('42')
        self.find_element(*CalcPageLocators.LENGTH).send_keys('42')
        self.find_element(*CalcPageLocators.COST).clear()
        # self.find_element(*CalcPageLocators.COST).send_keys('250')
        self.find_element(*CalcPageLocators.BODY).click()

    def result(self):
        res = self.find_element(*CalcPageLocators.RESULT)
        print(res.text)



if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    x = CalcPage(webdriver.Chrome(chrome_options=options))
    x.open('ru-calc')
    x.choose_city_from()
    x.choose_city_to()
    x.volumes()
    time.sleep(10)
    x.result()