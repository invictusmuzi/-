# -*- coding: utf-8 -*-
# @Time : 2024/2/25 18:07
# @Author : 木子宀示雨林
# @File : 地图绘制.py
# @Software : PyCharm
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# 读取中国地图数据
china_map = gpd.read_file("./bou2_4p.shp")

# 读取Excel文件中的戏剧分布数据
drama_distribution_df = pd.read_excel("./戏剧分布.xlsx")

# 合并的依据是地图数据中的 "Province" 列和Excel数据中的 "省份/直辖市/自治区" 列
merged_data = china_map.merge(drama_distribution_df, left_on="NAME", right_on="省份/直辖市/自治区")
# 绘制地图
fig, ax = plt.subplots(figsize=(10, 10))
# 假设 "戏剧名称" 列包含了我们需要显示的信息
merged_data.plot(ax=ax, column='戏剧名称', legend=True, legend_kwds={'label': "戏剧类型分布"})
ax.set_title('China Map')
plt.show()

# china_map.plot(ax=ax, color='lightblue', edgecolor='black')

