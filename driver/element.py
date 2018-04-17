#!/usr/local/bin/python3

from driver import Driver
from log import Log
from selenium.common.exceptions import NoSuchElementException


class Element(Driver):

    def find_by_id(self, id=None):
        if not id:
            return False
        try:
            return self.driver.find_element_by_id(id)
        except NoSuchElementException:
            Log().write_log('Driver','Element Select Faild!!!')

    def find_by_css_select(self, css=None):
        if not css:
            return False
        try:
            return self.driver.find_element_by_css_selector(css)
        except NoSuchElementException:
            Log().write_log('Driver', 'Element Select Faild!!!')

    def find_by_class_name(self, name=None):
        if not name:
            return False
        try:
            return self.driver.find_element_by_class_name(name)
        except NoSuchElementException:
            Log().write_log('Driver', 'Element Select Faild!!!')


    def find_by_link_text(self, text):
        if not text:
            return False
        try:
            return self.driver.find_element_by_link_text(text)
        except NoSuchElementException:
            Log().write_log('Driver', 'Element Select Faild!!!')
