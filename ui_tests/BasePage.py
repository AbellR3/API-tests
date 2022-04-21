from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.base_url = 'https://google.com'

    def find_element(self,  locator, time=5):
        return WebDriverWait(self.driver, timeout=time).until(EC.element_to_be_clickable(locator))

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, timeout=time).until(EC.element_to_be_clickable(locator))

    def go_to_site(self):
        return self.driver.get(self.base_url)
