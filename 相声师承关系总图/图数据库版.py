# -*- coding: utf-8 -*-
# @Time : 2024/2/21 21:27
# @Author : 木子宀示雨林
# @File : 图数据库版.py
# @Software : PyCharm

from neo4j import GraphDatabase
import json


class KnowledgeGraphBuilder:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_person_if_not_exists(self, name, generation):
        with self.driver.session() as session:
            result = session.run("MATCH (p:Person {name: $name}) RETURN p", name=name)
            existing_node = result.single()
            if existing_node:
                return existing_node['p']
            else:
                return self._create_and_return_person(session, name, generation)

    def create_mentorship(self, mentor, disciple):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_mentorship, mentor, disciple)

    @staticmethod
    def _create_and_return_person(tx, name, generation):
        query = (
            "CREATE (p:Person {name: $name, generation: $generation}) "
            "RETURN p"
        )
        result = tx.run(query, name=name, generation=generation)
        return result.single()[0]

    @staticmethod
    def _create_and_return_mentorship(tx, mentor, disciple):
        query = (
            "MATCH (m:Person {name: $mentor}), (d:Person {name: $disciple}) "
            "CREATE (m)-[:MENTOR]->(d)"
        )
        tx.run(query, mentor=mentor['name'], disciple=disciple['name'])


def main():
    # 从文件读取数据
    file_path = '存储字典.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 初始化知识图谱构建器
    kg_builder = KnowledgeGraphBuilder("bolt://localhost:7687", "neo4j", "lzl200256")

    # 遍历数据，创建人物节点和师徒关系
    for generation, persons in data.items():
        for mentor, disciples in persons.items():
            mentor_node = kg_builder.create_person_if_not_exists(mentor, generation)
            next_generation = str(int(generation) + 1)
            for disciple in disciples:
                disciple_node = kg_builder.create_person_if_not_exists(disciple, next_generation)
                kg_builder.create_mentorship(mentor_node, disciple_node)

    # 关闭数据库连接
    kg_builder.close()


if __name__ == "__main__":
    main()
