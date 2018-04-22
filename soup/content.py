#!/usr/local/bin/python3


class Content():

    def string_con(self,ele):
        if not ele:
            return False
        return ele.string

    def get_text_con(self,ele):
        if not ele:
            return False
        return ele.get_text