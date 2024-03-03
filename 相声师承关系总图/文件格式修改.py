# -*- coding: utf-8 -*-
# @Time : 2024/2/21 22:05
# @Author : 木子宀示雨林
# @File : 文件格式修改.py
# @Software : PyCharm
import json


def fix_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = file.read()

    # 替换单引号为双引号
    json_data = json_data.replace("'", '"')

    # 使用双引号包裹属性名
    json_data = fix_property_names(json_data)

    # 将修复后的数据写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(json_data)


def fix_property_names(json_str):
    # 使用正则表达式匹配属性名，确保双引号包裹
    import re
    pattern = r'(?<!\\)\'(.*?)(?<!\\)\'(?=\s*:)'

    def replace(match):
        return '"' + match.group(1) + '"'

    return re.sub(pattern, replace, json_str)


# 调用函数修复指定的 JSON 文件
json_file_path = "./存储字典.txt"
fix_json_file(json_file_path)
print("JSON 文件修复完成！")
