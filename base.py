from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Page():
    def __init__(self, driver, base_url='https://intime.ua/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def execute(self, script):
        return self.driver.execute_script(script)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def open(self, page):
        url = self.base_url + page
        self.driver.get(url)

    def presence_located(self, *locator):
        return EC.presence_of_element_located(*locator)

    def wait_driver(self, located):
        return WebDriverWait(self.driver,10).until(located)

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    x = Page(webdriver.Chrome(chrome_options=options))
    x.open('')
    print(x.get_url())