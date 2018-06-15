#!/usr/bin/env python
#coding=utf-8

import re


class ParseUtil:
    def parse_qsbk_list(self, qsbk_list):
        pattern = re.compile(
            u"""<div class="article block untagged.*?id='(.*?)'.*?<div class="author clearfix">.*?<img.*?src="(.*?)".*?alt="(.*?)">(.*?)
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

    def parse_qsbk_detal(self, qsbk_detail):
        return re.findall(u"<div class=\"content\">(.*?)</div>.*?class=\"comments-list clearfix\">(.*?)<div class=\"comment-tips\">", qsbk_detail, re.S)

    def parse_qsbk_detail_comment_list(self, qsbk_detail_comment_list):
        pattern = re.compile("""
<div class="avatars">.*?<a href="/users/(\d+)/" target="_blank" rel="nofollow"><img src="(.*?)" alt="(.*?)"></a>.*?<div class="replay">.*?<div class="(articleCommentGender .*?)">(\d+)</div>.*?<span class="body">(.*?)</span>.*?<div class="report">(\d+)</div>
""", re.S)

        return re.findall(pattern, qsbk_detail_comment_list)