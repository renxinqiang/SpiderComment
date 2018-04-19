#!/usr/local/bin/python3

from request import uri


class Cookie(uri.Uri):

    def get_cookie(self,url):
        if not url:
            return False
        return uri.Uri().get_url(url).cookies