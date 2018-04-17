#!/usr/local/bin/python3

from selenium import webdriver

class Driver:

    driver = None

    def __init__(self):
        if self.driver is None:
            self.driver = webdriver.Firefox()
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()