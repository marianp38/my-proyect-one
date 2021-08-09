import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pageIndex import PageIndex
from pageItems import PageItems
from pageCompra import PageCompra



class SearchCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument('start-maximized')
        #option.add_argument('--headless')
        self.driver = webdriver.Chrome('Chromedriver.exe', chrome_options=option)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait('5')
        #self.driver.maximize_window()
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.compraPage = PageCompra(self.driver)

    #@unittest.skip('Not needed now')
    def test_search_no_elements(self):
        try:
            self.indexPage.search('Hola')
            self.assertEqual(self.itemsPage.return_no_element_text(), 'No results were found for your search "Hola"')
        except:
            self.driver.save_screenshot('error.jpg')


    #@unittest.skip('Not needed now')
    def test_search_find_chiffon(self):
        self.indexPage.search('Chiffon')
        self.assertTrue('CHIFFON' in self.itemsPage.return_section_title())

    #@unittest.skip('Not needed now')
    def test_search_elements_tshirts(self):
        self.indexPage.search('T-shirts')
        self.assertTrue('SHIRTS' in self.itemsPage.return_section_title())

    #@unittest.skip('Not needed now')
    def test_tarea(self):
        self.indexPage.search('T-shirts')
        self.itemsPage.click_orange_button()
        self.compraPage.enter_quantity('25')
        self.compraPage.click_button_value(3)
        number = self.compraPage.return_value()
        self.assertTrue(number == '28')

    #@unittest.skip('Not needed now')
    def test_selections(self):
        self.indexPage.search('T-shirts')
        self.itemsPage.select_by_text('Product Name: A to Z')
        self.itemsPage.select_by_value('name:desc')
        self.itemsPage.select_by_index(1)
        time.sleep(3)

    #def test_dresses_options(self):
        #self.indexPage.click_dresses()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


