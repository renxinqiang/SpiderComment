#!/usr/local/bin/python3

from soup import Soup


class Dom(Soup):

    def title(self):
        return self.soup_result.title

    def p(self):
        return self.soup_result.p

    def body(self):
        return self.soup_result.body

    def div(self):
        return self.soup_result.div

    def html(self):
        return self.soup_result.html

    def script(self):
        return self.soup_result.script

    def find_all(self,type,attr_str={}):
        if not attr_str or not type:
            return False
        return self.soup_result.find_all(type=attr_str)

    def find_select(self,css):
        if not css:
            return False
        return self.soup_result.select(css)

