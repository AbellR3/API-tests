from GooglePage import SearchPage

def test_click_lucky_button(browser):
    page = SearchPage(browser)
    page.go_to_site()
    page.lucky_button().click()
    assert page.driver.current_url == 'https://www.google.com/doodles'