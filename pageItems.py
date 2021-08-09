from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class PageItems:

    def __init__(self, my_driver):
        self.no_results_banner = (By.XPATH, '//*[@id="center_column"]/p')
        self.title_banner = (By.XPATH, '//*[@id="center_column"]/h1/span[1]')
        self.orange_button = (By.ID, 'color_1')
        self.driver = my_driver
        self.order = (By.ID, 'selectProductSort')

    def return_no_element_text(self):
        return self.driver.find_element(*self.no_results_banner).text

    def return_section_title(self):
        return self.driver.find_element(*self.title_banner).text

    def click_orange_button(self):
        self.driver.find_element(*self.orange_button).click()

    def select_by_text(self, text):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_visible_text(text)

    def select_by_value(self, text):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_value(text)

    def select_by_index(self, text):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_index(text)


