from selenium import webdriver
# from testCases import test_cases
from pages import MainPage, CalcPage
from testData import *
import xmlrunner
import unittest
import cities
import time
from mk_cities import mk_cities

#
# class MainPageTest(unittest.TestCase):
#     def setUp(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("--start-maximized")
#         self.driver = webdriver.Chrome(chrome_options=options)
#         self.driver.get('https://intime.ua/')
#
#     def test_check_page_is_load(self):
#         print('\n' + str(test_cases(0)))
#         page = MainPage(self.driver)
#         self.assertTrue(page.check_page_is_load())
#
#     def test_search_field_presention(self):
#         print('\n' + str(test_cases(1)))
#         page = MainPage(self.driver)
#         self.assertTrue(page.check_search_field())
#
#     def tearDown(self):
#         self.driver.close()


class CalcPageTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get('https://intime.ua/ru-calc')

    @unittest.skip('dont need now')
    def test_multi_calc_less30_positive(self):
        page = CalcPage(self.driver)
        page.choose_city_from(cities.Cities.KHARKOV)
        page.choose_city_to(cities.Cities.KIEV)
        print('BVW<30_10 = boundary values less 30 kg and test with 10 kg <-- just for notes')
        print('POSITIVE TESTING! must be equal')
        for item in dataWL30positive.keys():
            with self.subTest(item=item):
                page.volumes(dataWL30positive[item])
                time.sleep(0.5)
                print('test---', item, ', values---', dataWL30positive[item], ', expected ---', data[item],
                      ', result is ---', page.result())
                self.assertEqual(page.result(), data[item])

    @unittest.skip('dont need now')
    def test_multi_calc_less30_negative(self):
        page = CalcPage(self.driver)
        page.choose_city_from(cities.Cities.KHARKOV)
        page.choose_city_to(cities.Cities.KIEV)
        print('BVW<30_10 = boundary values less 30 kg and test with 10 kg <-- just for notes')
        print('NEGATIVE TESTING! must be not EQUAL')
        for item in dataWL30negative.keys():
            with self.subTest(item=item):
                page.volumes(dataWL30negative[item])
                time.sleep(0.5)
                print('test---',item, ', values---',dataWL30negative[item], ' expected ---', data[item], ' result is ---', page.result())
                self.assertNotEqual(page.result(), data[item])

    @unittest.skip('dont need now')
    def test_multi_calc_w_more30_vw_less30_positive(self):
        page = CalcPage(self.driver)
        page.choose_city_from(cities.Cities.KHARKOV)
        page.choose_city_to(cities.Cities.KIEV)
        print('###BVW<30_10 = boundary values less 30 kg and test with 10 kg <-- just for notes')
        print('Testing of weight more 30 kg volume weight less 30 kg')
        print('POSITIVE TESTING! must be EQUAL')
        for item in dataWM30VWL30positive.keys():
            with self.subTest(item=item):
                page.volumes(dataWM30VWL30positive[item])
                time.sleep(0.5)
                print('test---', item, ', values---', dataWM30VWL30positive[item], ' expected ---', data[item],
                      ' result is ---', page.result())
                self.assertEqual(page.result(), data[item])

    @unittest.skip('dont need now')
    def test_multi_calc_w_more30_vw_less30_negative(self):
        page = CalcPage(self.driver)
        page.choose_city_from(cities.Cities.KHARKOV)
        page.choose_city_to(cities.Cities.KIEV)
        print('BVW<30_10 = boundary values less 30 kg and test with 10 kg <-- just for notes')
        print('Testing of weight more 30 kg volume weight less 30 kg')
        print('NEGATIVE TESTING! must be NOT EQUAL')
        for item in dataWM30WL30negative.keys():
            with self.subTest(item=item):
                page.volumes(dataWM30WL30negative[item])
                time.sleep(0.5)
                print('test---', item, ', values---', dataWM30WL30negative[item], ' expected ---', data[item],
                      ' result is ---', page.result())
                self.assertNotEqual(page.result(), data[item])

    @unittest.skip('dont need now')
    def test_multi_calc_w_less30_vw_more30_positive(self):
        page = CalcPage(self.driver)
        page.choose_city_from(cities.Cities.KHARKOV)
        page.choose_city_to(cities.Cities.KIEV)
        print('###BVW<30_10 = boundary values less 30 kg and test with 10 kg <-- just for notes')
        print('Testing of weight less 30 kg Volume weight more 30 kg')
        print('POSITIVE TESTING! must be EQUAL')
        for item in dataWL30VWM30positive.keys():
            with self.subTest(item=item):
                page.volumes(dataWL30VWM30positive[item])
                time.sleep(0.5)
                print('test---', item, ', values---', dataWL30VWM30positive[item], ' expected ---', data[item],
                      ' result is ---', page.result())
                self.assertEqual(page.result(), data[item])

    @unittest.skip('dont need now')
    def test_multi_calc_w_less30_vw_more30_negative(self):
        page = CalcPage(self.driver)
        page.choose_city_from(cities.Cities.KHARKOV)
        page.choose_city_to(cities.Cities.KIEV)
        print('BVW<30_10 = boundary values less 30 kg and test with 10 kg <-- just for notes')
        print('Testing of weight less 30 kg Volume weight more 30 kg')
        print('NEGATIVE TESTING! must be NOT EQUAL')
        for item in dataWL30VWM30negative.keys():
            with self.subTest(item=item):
                page.volumes(dataWL30VWM30negative[item])
                time.sleep(0.5)
                print('test---', item, ', values---', dataWL30VWM30negative[item], ' expected ---', data[item],
                      ' result is ---', page.result())
                self.assertNotEqual(page.result(), data[item])

    @unittest.skip('dont need now')
    def test_multi_calc_w_more30_vw_more30_positive(self):
        page = CalcPage(self.driver)
        page.choose_city_from(cities.Cities.KHARKOV)
        page.choose_city_to(cities.Cities.KIEV)
        print('###BVW<30_10 = boundary values less 30 kg and test with 10 kg <-- just for notes')
        print('Testing of weight more 30 kg Volume weight more 30 kg')
        print('POSITIVE TESTING! must be EQUAL')
        for item in dataWM30VWM30positive.keys():
            with self.subTest(item=item):
                page.volumes(dataWM30VWM30positive[item])
                time.sleep(0.5)
                print('test---', item, ', values---', dataWM30VWM30positive[item], ' expected ---', data[item],
                      ' result is ---', page.result())
                self.assertEqual(page.result(), data[item])

    @unittest.skip('dont need now')
    def test_multi_calc_w_more30_vw_more30_negative(self):
        page = CalcPage(self.driver)
        page.choose_city_from(cities.Cities.KHARKOV)
        page.choose_city_to(cities.Cities.KIEV)
        print('BVW<30_10 = boundary values less 30 kg and test with 10 kg <-- just for notes')
        print('Testing of weight more 30 kg Volume weight more 30 kg')
        print('NEGATIVE TESTING! must be NOT EQUAL')
        for item in dataWM30VWM30negative.keys():
            with self.subTest(item=item):
                page.volumes(dataWM30VWM30negative[item])
                time.sleep(0.5)
                print('test---', item, ', values---', dataWM30VWM30negative[item], ' expected ---', data[item],
                      ' result is ---', page.result())
                self.assertNotEqual(page.result(), data[item])

    # @unittest.skip('dont need now')
    def test_different_cities(self):
        page = CalcPage(self.driver)
        page.weight('31')
        page.clear_city_from()
        page.choose_city_from('Киев')
        print('Из Киев ')
        for cityTo in mk_cities():
            with self.subTest(cityTo=cityTo):
                page.clear_city_To()
                page.choose_city_to(cityTo)
                time.sleep(0.5)
                print('в город '+cityTo+' --- '+page.result())


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-report'))
