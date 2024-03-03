# -*- coding: utf-8 -*-
# @Time : 2024/2/14 21:06
# @Author : 木子宀示雨林
# @File : 小说爬虫.py
# @Software : PyCharm
import requests
from lxml import etree
import re
def get_urls(url):
    url_list = []
    # 发送请求获取网页内容
    response = requests.get(url)
    tree = etree.HTML(response.text)
    li_list = tree.xpath('//*[@id="list"]/dl/dd')
    for li in li_list:
        url = li.xpath('./a/@href')[0]
        url_list.append(url)
    return url_list

def save_to_file(all_contents):
    with open('作品名.txt', 'w', encoding='utf-8') as f:
        for name in all_contents:
            f.write(name + '\n')
def main():
    url = 'https://www.sz-jsds.com/32_32147/'
    urls_list = get_urls(url)
    all_contents = []
    for url in urls_list:
        url = 'https:' + url
        response = requests.get(url)
        tree = etree.HTML(response.text)
        contents = tree.xpath('//*[@id="content"]/text()')
        content_text = '\n'.join(contents)
        pattern = r'《(.*?)》'
        content = re.findall(pattern, content_text)
        all_contents.extend(content)
    all_contents = list(set(all_contents))
    save_to_file(all_contents)
    print('保存成功')

if __name__ == "__main__":
    main()
