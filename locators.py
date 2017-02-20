from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGO = (By.XPATH, '//div[2]/nav/div[1]/a/img')
    SEARCH = (By.CLASS_NAME, 'menu-link--search')

class CalcPageLocators():
    FROM_CITY = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/div[1]/ul/li[1]/section/div[2]/div[1]/label/input')
    FROM_CITY_LI = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/div[1]/ul/li[1]/section/div[2]/div[1]/ul/li')
    TO_CITY = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/div[1]/ul/li[1]/section/div[3]/div[1]/label/input')
    TO_CITY_LI = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/div[1]/ul/li[1]/section/div[3]/div[1]/ul/li')
    WEIGHT = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/div[2]/ul/li/section[2]/div[2]/label/input')
    LENGTH = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/div[2]/ul/li/section[3]/div[2]/div/label[1]/input')
    WIDTH = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/div[2]/ul/li/section[3]/div[2]/div/label[2]/input')
    HEIGHT = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/div[2]/ul/li/section[3]/div[2]/div/label[3]/input')
    COST = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/div[2]/ul/li/section[11]/div[2]/label/input')
    RESULT = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/section/div/ul/li[2]/p/span')
    BODY = (By.CLASS_NAME, 'content-part')