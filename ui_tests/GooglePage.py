from BasePage import BasePage
from selenium.webdriver.common.by import By

class GoogleLocator:
    lucky_button = (By.XPATH, "//input[@value='Мне повезёт!']")

class SearchPage(BasePage):
    def lucky_button(self):
        button = self.find_element(GoogleLocator.lucky_button)
        return button