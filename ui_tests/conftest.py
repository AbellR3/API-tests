from lib2to3.pgen2 import driver
import pytest
from selenium import webdriver
import time

@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome('./ui_tests/chromedriver')
    yield driver
    driver.quit()
