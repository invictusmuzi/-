# -*- coding: utf-8 -*-
# @Time : 2024/2/16 21:49
# @Author : 木子宀示雨林
# @File : 歌曲提取.py
# @Software : PyCharm
import os
import paddle
from paddlenlp import Taskflow
import paddle
paddle.utils.run_check()

# # 设置 CUDA_VISIBLE_DEVICES 来指定 GPU 设备
# os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # 使用 GPU 设备 0（根据需要更改）
#
# # 设置模型下载路径
# os.environ['PADDLENLP_HOME'] = 'E:\\PythonEnvironments\\paddlenlp\\.paddlenlp'
#
# schema = ['歌曲名']
#
# # 加载预训练的 UIE 模型
# uie = Taskflow('information_extraction', schema=schema)
#
# # 将模型移动到 GPU 设备
# uie.model.to('gpu')
#
# # 读取文件内容
# file_path = '作品名.txt'
# with open(file_path, 'r', encoding='utf-8') as file:
#     text = file.read()
#
# # 将输入数据移动到 GPU 设备
# text = paddle.to_tensor(text)
#
# # 执行信息抽取，提取歌曲名
# results = uie(text)
#
# print(results)
