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
    def clear_city_from(self):
        self.find_element(*CalcPageLocators.FROM_CITY).clear()

    def clear_city_To(self):
        self.find_element(*CalcPageLocators.TO_CITY).clear()


    def choose_city_from(self, city):
        self.find_element(*CalcPageLocators.FROM_CITY).send_keys(city)
        time.sleep(1)
        for i in self.find_elements(*CalcPageLocators.CITY_LI):
            text = i.text
            for j in i.find_elements(*CalcPageLocators.FIRST_CHILD):
                text = text.replace(j.text, '').rstrip('\n')
                a = city
                if a == text:
                    i.click()

    def choose_city_to(self, city):
        self.find_element(*CalcPageLocators.TO_CITY).send_keys(city)
        time.sleep(1)
        for i in self.find_elements(*CalcPageLocators.CITY_LI):
            text = i.text
            for j in i.find_elements(*CalcPageLocators.FIRST_CHILD):
                text = text.replace(j.text, '').rstrip('\n')
                a = city
                if a == text:
                    i.click()
                    if i.get_attribute('data-has_store') == '1':
                        self.execute('document.getElementsByName("type_to")[0].checked = true;')

    def weight(self, weight):
        self.find_element(*CalcPageLocators.WEIGHT).clear()
        self.find_element(*CalcPageLocators.WEIGHT).send_keys(weight)

    def height(self, height):
        self.find_element(*CalcPageLocators.HEIGHT).clear()
        self.find_element(*CalcPageLocators.HEIGHT).send_keys(height)

    def width(self, width):
        self.find_element(*CalcPageLocators.WIDTH).clear()
        self.find_element(*CalcPageLocators.WIDTH).send_keys(width)

    def lenght(self, lenght):
        self.find_element(*CalcPageLocators.LENGTH).clear()
        self.find_element(*CalcPageLocators.LENGTH).send_keys(lenght)

    def cost(self, cost):
        self.find_element(*CalcPageLocators.COST).clear()
        self.find_element(*CalcPageLocators.COST).send_keys('250')

    def get_has_store(self):
        self.find_element(*CalcPageLocators.HAS_STORE)

    def volumes(self, lst=[], *args):
        self.weight(lst[0])
        self.height(lst[1])
        self.width(lst[2])
        self.lenght(lst[3])
        # self.cost('250')
        self.find_element(*CalcPageLocators.BODY).click()

    def result(self):
        res = self.find_element(*CalcPageLocators.RESULT)
        return res.text
        # try:
        #     res = self.wait_driver(self.presence_located(*CalcPageLocators.RESULT))
        #     return res.text
        # # res = self.find_element(*CalcPageLocators.RESULT)
        # finally:
        #     self.driver.quit()



if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    x = CalcPage(webdriver.Chrome(chrome_options=options))
    x.open('ru-calc')
    x.choose_city_to('Киев')
    x.weight('12')
    print(x.result())
    # x.choose_city_from(cities.Cities.KHARKOV)

