#!/usr/local/bin/python3

from request import Request


class Uri(Request):

    def get_url(self,url,param=None):
        if not url:
            return False
        if param != None:
            return self.request.get(url,params=param)
        else:
            return self.request.get(url)

    def post_url(self,url,param):
        if not url:
            return False
        if param != None:
            return self.request.post(url,params=param)
        else:
            return self.request.post(url)

    def option_url(self,url):
        if not url:
            return False
        return self.request.options(url)

    def code(self, url):
        if not url:
            return False
        return self.get_url(url).status_code