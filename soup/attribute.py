#!/usr/local/bin/python3

class Attribute():

    def name(self,ele):
        if not ele:
            return False
        return ele['name']

    def class_name(self,ele):
        if not ele:
            return False
        return ele['class']

    def get_attr(self,ele,attr):
        if not ele or not attr:
            return False
        return ele[attr]