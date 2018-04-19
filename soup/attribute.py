#!/usr/local/bin/python3

from soup import Soup


class Attribute(Soup):

    def name(self,ele):
        if not ele:
            return False
        return self.soup_result.ele['name']

    def class_name(self,ele):
        if not ele:
            return False
        return self.soup_result.ele['class']

    def get_attr(self,ele,attr):
        if not ele or not attr:
            return False
        return ele[attr]