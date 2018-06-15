#!/usr/bin/env python
#coding=utf-8

import urllib, urllib2
import re

page = 1
url = "http://www.qiushibaike.com/hot/page/%s" % page
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {"User-Agent":user_agent}
try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode("utf-8")
    print content

    pattern = re.compile(
"""<div class="author clearfix">.*?<img.*?src="(.*?)".*?alt="(.*?)">(.*?)<div class="content">.*?<span>(.*?)</span>.*?""", re.S)
    items = re.findall(pattern,content)
    print "--->--->--->--->--->--->--->--->--->--->--->"
    print str(len(items)) + "---> %s " % items
    print "--->--->--->--->--->--->--->--->--->--->--->"
    for item in items:
        print "===>===>===>", item[0], item[1]
        item1 = re.findall("<!--.*?-->", item[2])
        if item1:
            print "***>***>***>", item1
        else:
            item10 = re.findall("<div class=\"(.*?)\">(\d+)</div>", item[2])
            print "***>***>***>", item10[0][0], item10[0][1]
        print item[3].strip("\n")
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason


src = """
<img src="//pic.qiushibaike.com/system/pictures/12055/120552933/medium/app120552933.jpeg" alt="糗事#120552933" class="illustration" width="100%" height="auto">
"""
print re.findall("img src=\"(.*?)\" alt=\"糗事#120552933\" class=\"illustration\" width=\"100%\" height=\"auto\">", src)