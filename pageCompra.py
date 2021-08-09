from selenium.webdriver.common.by import By

class PageCompra:


    def __init__(self, my_driver):
        self.driver = my_driver
        self.quantity_value = (By.XPATH, '//*[@id="quantity_wanted"]')
        self.button_value = (By.CLASS_NAME, 'icon-plus')

    def enter_quantity(self, quantity):
        self.driver.find_element(*self.quantity_value).clear()
        self.driver.find_element(*self.quantity_value).send_keys(quantity)

    def click_button_value(self, quantity):
        for i in range(quantity):
            self.driver.find_element(*self.button_value).click()


    def return_value(self):
        return self.driver.find_element(*self.quantity_value).get_attribute('value')

