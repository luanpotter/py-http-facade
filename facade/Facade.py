#!/usr/bin/python
# -*- coding: utf-8 -*-

class HttpFacade(object):
    """Http Facade Class"""
    headers = {}
    queries = {}
    method  = None
    base_url = None
    _body = None
    is_gzip = False
    time_out = 3 * 60 * 1000
    followRedirects = False
    fixedSize = False

    def __init__(self, base_url):
        self.headers = {}
        self.queries = {}
        self.base_url = base_url

    def header(self, key, header):
        """add header to facade."""
        if not key in self.headers :
            self.headers[key] = []
        self.headers[key].append(header)
        return self
    
    def timeout(self, time):
        """set timeout for request."""
        self.time_out = time
        return self

    def notimeout(self):
        """remove timeout from request."""
        self.time_out = None
        return self

    def cookies(self,cookies):
        """add cookies to request."""
        cookies_str = ""
        for k in cookies.keys :
            cookies_str += k + '=' + cookies[k]
        return self.header("Cookie", cookies_str)

    def gzip(self, accept_content):
        """set GZIP to request."""
        self.is_gzip = True
        return self.header("Accept-Encoding", accept_content)

    
    def query(self, key, query):
        """add header to facade."""
        if not key in self.queries :
            self.queries[key] = []
        self.queries[key].append(query)
        return self

    def body(self, body):
        """add body to facade."""
        self._body = body
        return self
