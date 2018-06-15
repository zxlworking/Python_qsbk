#!/usr/bin/env python
#coding=utf-8

import re


class ParseUtil:
    def parse_qsbk_list(self, qsbk_list):

        pattern = re.compile(
            u"""<div class="author clearfix">.*?<img.*?src="(.*?)".*?alt="(.*?)">(.*?)
<div class="content">.*?<span>(.*?)</span>
.*?<!-- 图片或gif -->(.*?)<div class="stats">(.*?)<div id="qiushi_counts.*?""",
            re.S)
        return re.findall(pattern, qsbk_list)

    def parse_qsbk_anonymity(self, qsbk_anonymity):
        return re.findall("<!--.*?-->", qsbk_anonymity)

    def parse_qsbk_author_sex_age(self, qsbk_author_sex_age):
        return re.findall("<div class=\"(.*?)\">(\d+)</div>", qsbk_author_sex_age)

    def parse_qsbk_thumb(self, qsbk_thumb):
        return re.findall("<img src=\"(.*?)\" alt=.*?>", qsbk_thumb)

    def parse_qsbk_vote_comment(self, qsbk_vote_comment):
        return re.findall(u"<span class=\"stats-vote\"><i class=\"number\">(\d+)</i> 好笑</span>.*?\n.*?\n.*?\n.*?\n<i class=\"number\">(\d+)</i> 评论", qsbk_vote_comment)