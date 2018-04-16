#!/usr/local/bin/python3

from bs4 import BeautifulSoup

def soup_result(html):
    soup = BeautifulSoup(html,'lxml')
    return soup

