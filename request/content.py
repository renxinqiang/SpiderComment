#!/usr/local/bin/python3

from request import uri


class Content(uri.Uri):
    __result = None

    def text(self, url, param):
        self.__result = uri.Uri().get_url(url, param)
        return self.__result.content

    def content(self, url, param):
        self.__result = uri.Uri().get_url(url, param)
        return self.__result.text