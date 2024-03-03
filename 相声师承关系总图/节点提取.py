# -*- coding: utf-8 -*-
# @Time : 2024/2/20 20:53
# @Author : 木子宀示雨林
# @File : 节点提取.py
# @Software : PyCharm

import re

file_path = './师承关系.txt'

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read()
# print(data)
# 使用正则表达式来匹配每一代的信息
generations = re.findall(r'(\w+)代——第(\w+)代\n(.*?)\n第', data, re.S)
# 定义一个字典来存储每一代与其后代的关系
total={}

# print(generations)

for gen in generations:
    current_gen = gen[0]  # 当前代
    next_gen = gen[1]  # 下一代
    people = gen[2].split('\n')  # 当前代的人物列表
    relationships = {}
    # print(people)
    for person in people:
        # 分离每个人和他们的后代
        ancestor, descendants = re.split(r'\s*——\s*', person)
        # print(ancestor, descendants)
        ancestor = ancestor.strip()
        descendants = [desc.strip() for desc in descendants.split('、')]

        # 将关系存储到字典中
        relationships[ancestor] = descendants
    total[current_gen]=relationships

print(total)