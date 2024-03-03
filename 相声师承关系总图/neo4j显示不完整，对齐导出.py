# -*- coding: utf-8 -*-
# @Time : 2024/2/21 22:18
# @Author : 木子宀示雨林
# @File : neo4j显示不完整，对齐导出.py
# @Software : PyCharm
from neo4j import GraphDatabase
import networkx as nx
import matplotlib.pyplot as plt

def export_graph_to_gexf(driver, file_path):
    query = (
        "MATCH (n)-[r]->(m) "
        "RETURN n, r, m"
    )
    with driver.session() as session:
        result = session.run(query)
        graph = nx.DiGraph()
        for record in result:
            source = record['n']['name']
            target = record['m']['name']
            graph.add_edge(source, target)

    nx.write_gexf(graph, file_path)

def main():
    # Neo4j 连接配置
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "lzl200256"

    # 连接 Neo4j 数据库
    driver = GraphDatabase.driver(uri, auth=(user, password))

    # 导出图形数据为 GEXF 格式
    file_path = "graph_data.gexf"
    export_graph_to_gexf(driver, file_path)

    # 关闭数据库连接
    driver.close()

    print("Graph data exported to", file_path)

if __name__ == "__main__":
    main()
