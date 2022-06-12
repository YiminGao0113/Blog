# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Blog/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "YiminGao0113/Blog@gh-pages"
}

# 站点设置
site_name = "Yimin's Blog"
site_logo = "${static_prefix}logo.png"
site_build_date = "2022-04-02T16:51+08:00"
author = "高一民"
email = "yg9bq@virginia.edu"
author_homepage = "https://yimingao.com/"
description = "Dream big, start small."
key_words = ['Maverick', '高一民', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Github",
        "url": "https://github.com/YiminGao0113/",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "我的主页",
        "url": "https://yimingao.com/",
        "brief": "🏄‍ Have Fun"
    },
    {
        "name": "Mini Discord",
        "url": "http://yimindiscord.com:5000/",
        "brief": "🏄‍ Have Fun"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/AlanDecode",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/YiminGao0113",
        "icon": "gi gi-github"
    },
    # {
    #     "name": "Weibo",
    #     "url": "https://weibo.com/5245109677/",
    #     "icon": "gi gi-weibo"
    # }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
