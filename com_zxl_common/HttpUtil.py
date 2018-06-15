#!/usr/bin/env python
#coding=utf-8

import urllib
import urllib2


class HttpUtil:

    def get_http_content(self, url, headers):
        try:
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            return response.read().decode("utf-8")
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print "e.code:" + e.code
            if hasattr(e, "reason"):
                print "e.reason:" + e.reason


    def get_qsbk_list_by_page(self, page):
        # https://www.qiushibaike.com/article/120535436
        url = "http://www.qiushibaike.com/hot/page/%s" % page
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent":user_agent}
        return self.get_http_content(url, headers)
