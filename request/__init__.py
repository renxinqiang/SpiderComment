#!/usr/local/bin/python3

import requests

def reques_get(url):
    req = requests.get(url)
    content = req.content
    return content
