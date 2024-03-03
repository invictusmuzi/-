# -*- coding: utf-8 -*-
# @Time : 2024/2/27 22:35
# @Author : 木子宀示雨林
# @File : 文件内容查看.py
# @Software : PyCharm
import shapefile

# 替换为你的 .dbf 文件路径
dbf_file_path = './bou2_4p.dbf'

# # 使用 Reader 类读取 .dbf 文件
# with shapefile.Reader(dbf_file_path) as sf:
#     # 获取所有字段的信息，每个字段信息是一个元组，包括字段名、字段类型等
#     fields = sf.fields[1:]  # 第一个元素是删除标记，所以从第二个元素开始
#
#     # 提取字段名列表
#     field_names = [field[0] for field in fields]
#
#     print("列名列表：")
#     print(field_names)
#
# # 根据输出，找到看起来像是存储省份信息的列名
# 使用 Reader 类读取 .dbf 文件
with shapefile.Reader(dbf_file_path) as sf:
    # 获取所有记录
    records = sf.records()

    # 打印前几条记录的内容，以便查看数据
    for record in records[:10]:  # 查看前10条记录作为示例
        print(record)
