from BasePage import BasePage
from selenium.webdriver.common.by import By

class GoogleLocator:
    lucky_button = (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]")

class DoodlesLocator:
    last_elem = (By.ID, "latest-tag")

class SearchPage(BasePage):
    def lucky_button_click(self):
        button = self.find_element(GoogleLocator.lucky_button).click()
        return DoodlesPage(self.driver)

class DoodlesPage(BasePage):
    def find_last_date(self):
        last_date = self.find_element(DoodlesLocator.last_elem)
        return last_date