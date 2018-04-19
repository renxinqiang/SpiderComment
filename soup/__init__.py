#!/usr/local/bin/python3

from bs4 import BeautifulSoup


class Soup:

    soup_result = None

    def __init__(self,html,type = 'lxml'):
        self.soup_result = BeautifulSoup(html,type)
        pass