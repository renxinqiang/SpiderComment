#!/usr/local/bin/python3

from soup import Soup


class Content(Soup):

    def string_con(self,ele):
        if not ele:
            return False
        return self.soup_result.ele.string

    def get_text_con(self,ele):
        if not ele:
            return False
        return self.soup_result.ele.get_text