# # -*- coding: utf-8 -*-

import requests
import parsel

#设定访问浏览器
Base_url = 'https://www.guazi.com/sh/buy/'
Browser_head = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

for p in range(1,50):
#获取地区车辆列表
    Cars_Source_Page = requests.get(url = Base_url, headers = Browser_head)

    response = requests.get('/html/body/div[6]/ul')
    print(response)


#爬取车辆详情页
 #   for i in elements:

#保存数据