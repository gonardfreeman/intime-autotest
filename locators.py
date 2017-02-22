from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGO = (By.XPATH, '//div[2]/nav/div[1]/a/img')
    SEARCH = (By.CLASS_NAME, 'menu-link--search')

class CalcPageLocators():
    FROM_CITY = (By.XPATH, '//div[contains(@class, "cities")]/label[@data-placeholder="Откуда"]/input')
    TO_CITY = (By.XPATH, '//div[contains(@class, "cities")]/label[@data-placeholder="Куда"]/input')
    CITY_LI = (By.XPATH, '//div[contains(@class, "cities")]/ul/li')
    WEIGHT = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/div[2]/ul/li/section[2]/div[2]/label/input')
    LENGTH = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/div[2]/ul/li/section[3]/div[2]/div/label[1]/input')
    WIDTH = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/div[2]/ul/li/section[3]/div[2]/div/label[2]/input')
    HEIGHT = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/div[2]/ul/li/section[3]/div[2]/div/label[3]/input')
    COST = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/div[2]/ul/li/section[11]/div[2]/label/input')
    RESULT = (By.XPATH, '//div[3]/div[2]/div[1]/section[1]/div[1]/section/div/ul/li[2]/p/span')
    BODY = (By.CLASS_NAME, 'content-part')
    FIRST_CHILD = (By.XPATH, './*')
    HAS_STORE = (By.XPATH, '//*[@data-has_store]')
    INPUT_OFFICE = (By.XPATH, '//li[contains(@class, "calc--route")]/section//div[@class="radio-box"]//input[@name="type_to"]')