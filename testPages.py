from selenium import webdriver
from testCases import test_cases
from pages import MainPage
import xmlrunner
import unittest
import time

class MainPageTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get('https://intime.ua/')

    def test_check_page_is_load(self):
        print('\n' + str(test_cases(0)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_is_load())

    def test_search_field_presention(self):
        print('\n' + str(test_cases(1)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_search_field())

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-report'))