import pytest
from selenium import webdriver


class tests(object):

    def __init__(self):
        pass

    def start_web_driver(self):

        driver = webdriver.Firefox()
        driver.get(self.url)
        assert 'GitHub' in driver.title
