from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGO = (By.XPATH, '//div[2]/nav/div[1]/a/img')
    SEARCH = (By.CLASS_NAME, 'menu-link--search')