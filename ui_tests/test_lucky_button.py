from xml.sax.handler import all_features
import allure_commons
from GooglePage import SearchPage



def test_click_lucky_button(browser):
    page = SearchPage(browser)
    page.go_to_site()
    doodle_page = page.lucky_button_click()
    assert page.driver.current_url == 'https://www.google.com/doodles'
    assert doodle_page.find_last_date().text == "14 апр. 2022 г."