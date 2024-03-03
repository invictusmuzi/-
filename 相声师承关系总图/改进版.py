# -*- coding: utf-8 -*-
# @Time : 2024/2/21 21:03
# @Author : 木子宀示雨林
# @File : 改进版.py
# @Software : PyCharm
import os
import re
from graphviz import Digraph
import os
# 将 Graphviz 的 bin 目录添加到 PATH 环境变量中
os.environ["PATH"] += os.pathsep + 'D:\\Graphviz\\bin'

file_path = './师承关系.txt'

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read()

# 解析文本文件内容来构建关系图
def parse_relationships(text):
    # 使用正则表达式来匹配每一代的信息
    generations = re.findall(r'(\w+)代——第(\w+)代\n(.*?)\n第', text, re.S)

    # 定义一个字典来存储每一代与其后代的关系
    relationships = {}

    for gen in generations:
        current_gen = gen[0]  # 当前代
        next_gen = gen[1]  # 下一代
        people = gen[2].split('\n')  # 当前代的人物列表

        for person in people:
            # 分离每个人和他们的后代
            ancestor, descendants = re.split(r'\s*——\s*', person)
            print(ancestor, descendants)
            ancestor = ancestor.strip()
            descendants = [desc.strip() for desc in descendants.split('、')]

            # 将关系存储到字典中
            relationships[ancestor] = descendants

    return relationships

# 构建关系图
def build_relationship_graph(relationships):
    dot = Digraph(comment='Mentorship Tree')

    # 设置字体以支持中文显示
    dot.attr('node', fontname='Microsoft YaHei')

    # 创建节点和边
    for ancestor, descendants in relationships.items():
        # 添加祖先节点，使用 HTML 标签换行
        dot.node(ancestor, label=ancestor, shape='box', style='rounded', margin='0.1,0.05', color='lightblue2')

        # 添加后代节点和边
        for desc in descendants:
            # 添加后代节点，使用 HTML 标签换行
            dot.node(desc, label=desc, shape='box', style='rounded', margin='0.1,0.05', color='lightyellow')
            dot.edge(ancestor, desc)

    return dot

# 解析文本数据中的关系
relationships = parse_relationships(data)

# 构建关系图
mentorship_tree = build_relationship_graph(relationships)

# 设置图形排版布局为从上到下
mentorship_tree.attr(rankdir='TB')

# 保存图形文件
output_path = '/mnt/data/mentorship_tree.gv'
mentorship_tree.render(output_path, format='pdf', cleanup=True)

# 显示图形
mentorship_tree.view()
