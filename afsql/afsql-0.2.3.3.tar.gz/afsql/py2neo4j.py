# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     pp
   Description :
   Author :       asdil
   date：          2022/2/28
-------------------------------------------------
   Change Activity:
                   2022/2/28:
-------------------------------------------------
"""
__author__ = 'Asdil'
import warnings
from uuid import uuid1
from py2neo import Graph, Relationship, Node
from py2neo.matching import RelationshipMatcher, NodeMatcher


def get_uid():
    """get_uid方法用于返回uid1
    """
    return str(uuid1())


class Py2neo4j:
    """
    Neo4j类用于操作neo4j图数据库
    """

    def __init__(self, url, user, password, database=None):
        """__init__(self):方法用于初始化数据

        Parameters
        ----------
        url: str
            neo4j服务器地址
        user: str
            用户名
        password: str
            密码
        database : str or None
            数据了名称
        Returns
        ----------
        """
        self.url = url
        self.user = user
        self.password = password
        self.database = database
        self.driver = Graph(url, auth=(user, password), name=database)

    def create_node(self, labels, parameters, add_uid=False):
        """create_node方法用于创建node节点

        Parameters
        ----------
        labels : list or str
            标签集合或者字符串
        parameters: dict
            参数字典
        add_uid: bool
            是否添加uid参数, 它和id(p)是相同的

        Returns
        ----------
        """
        if type(labels) is str:
            labels = [labels]
        node = Node(*labels, **parameters)
        self.driver.create(node)
        if add_uid:
            parameters = {'uid': get_uid()}
            node.update(**parameters)
            self.driver.push(node)
        return node

    def update_node(self, node, labels=None, parameters={}, cover_lables=False,
                    cover_parameters=False, add_uid=False):
        """update_node方法用于

        Parameters
        ----------
        node: py2neo.data.Node
            节点对象
        labels : list or None
            标签集合
        parameters: dict
            参数字典
        cover_parameters: bool
            是否删除原有的属性，只保留更新的labels, parameters
        cover_lables: bool
            是否删除原有的标签
        add_uid: bool
            是否添加uid

        Returns
        ----------
        """
        if parameters is None:
            parameters = {}
        if cover_parameters:
            for key in node.keys():
                del node[key]
        if cover_lables:
            node.clear_labels()
        if add_uid:
            parameters['uid'] = get_uid()
        if labels:
            if type(labels) is str:
                labels = [labels]
            node.update_labels(labels)
        if parameters:
            node.update(**parameters)
        self.driver.push(node)
        return node

    def del_node(self, node=None, labels=None, id=None, uid=None):
        """del_node方法用于删除节点

        Parameters
        ----------
        node: py2neo.data.Node
            节点对象
        id: int or None
            节点id
        uid: str or None
            节点uid
        labels: str or None
            节点标签集合

        Returns
        ----------
        """
        if node:
            self.driver.delete(node)
        elif labels:
            labels = ':'.join(labels)
            cyper = f'MATCH (p:{labels}) DELETE p;'
            self.driver.run(cyper)
        elif id:
            cyper = f'MATCH (p) WHERE id(p)=$id DELETE p;'
            self.driver.run(cyper, {'id': id})
        elif uid:
            cycler = f'MATCH (p) WHERE p.uid=$uid DELETE p;'
            self.driver.run(cycler, {'uid': uid})

    def create_relationship(self, node1, node2, label='', parameters={}, add_uid=False):
        """create_relationship方法用于

        Parameters
        ----------
        node1 : py2neo.data.Node
            节点1
        node2 : py2neo.data.Node
            节点2
        label: str
            节点关系
        parameters: dict
            关系属性
        add_uid: bool
            是否添加uid

        Returns
        ----------
        """
        relation = Relationship(node1, label, node2, **parameters)
        self.driver.create(relation)
        if add_uid:
            parameters = {'uid': get_uid()}
            relation.update(**parameters)
        self.driver.push(relation)
        return relation

    def delete_all(self):
        """delete_all方法用于删除图数据所有数据,慎用"""
        self.driver.delete_all()

    def run(self, cyper, parameters=None):
        """run方法用于运行cyper
        eg: cyper = 'match (p1)-[r]->(p2) where labels(p1)=$l1 return p1'
            neo4j_db.run(cyper, {'l1': ['aa']})

        Parameters
        ----------
        cyper : str
            cyper 语句
        parameters: dict or None
            参数列表
        Returns
        ----------
        """
        ret = self.driver.run(cyper, parameters)
        return ret

    def run_one(self, cyper, parameters=None):
        """run_one(self):方法用于运行cyper返回第一个数据

        Parameters
        ----------
        cyper : str
            cyper 语句
        parameters: dict or None
            参数列表
        Returns
        ----------
        """
        ret = self.driver.evaluate(cyper, parameters)
        return ret

    def get_by_id(self, uid):
        """get_id方法用于用于根据id查找

        Parameters
        ----------
        uid : str or int
            节点自身的id

        Returns
        ----------
        """
        if type(uid) is int:
            cyper = f'match (p) where id(p)=$uid return p limit 1'
        else:
            cyper = f'match (p) where id(p)=$uid return p limit 1'
        node = self.driver.evaluate(cyper, {'uid': uid})
        return node

    def delete_relationship(self, node1=None, node2=None, label1=[], parameters1={}, r_label=None,
                            label2=[], parameters2={}, delete_node=False):
        """delete_relationship方法用于删除关系或者关系和节点
        db.delete_relationship(label1=['xxx'],
                             parameters1={'a':2},
                            label2=['yyy'],
                            delete_node=True)
        db.delete_relationship(node1=node1,
                             node2=node2,
                            r_label=['yyy'])
        Parameters
        ----------
        node1: Node or None
            from 节点
        node2: Node or None
            to 节点
        label1: list or str or None
            节点1的标签集合
        parameters1: dict
            节点1的属性集合
        label2: list or str or None
            节点2的标签集合
        parameters2: dict
            节点2的属性集合
        r_label: str
            关系的标签
        delete_node: bool
            是否同时删除节点，需要正没有其他的关系

        Returns
        ----------
        """
        # 判断是否传入节点
        if not node1:
            node_matcher = NodeMatcher(self.driver)
            label1 = [label1] if type(label1) is str else label1
            label2 = [label2] if type(label2) is str else label2
            node1 = node_matcher.match(*label1).where(**parameters1).first()
            node2 = node_matcher.match(*label2).where(**parameters2).first()
        relationship_matcher = RelationshipMatcher(self.driver)
        relationships = relationship_matcher.match([node1, node2], r_type=r_label)
        for relationship in relationships.all():
            self.driver.separate(relationship)
        if delete_node:
            self.driver.delete(node1)
            self.driver.delete(node2)

    def update_relationship(self, node1=None, node2=None, id=None, uid=None, label1=[], parameters1={},
                            r_label=None, label2=[], parameters2={}, new_r_label=None,
                            new_r_parameters={}):
        """update_relationship方法用于更新关系

        Parameters
        ----------
        node1: Node
            from节点
        node2: Node
            to节点
        id: int or None
            关系的id
        uid: str or None
            关系的uid
        label1: list or str or None
            节点1的标签集合
        parameters1: dict
            节点1的属性集合
        label2: list or str or None
            节点2的标签集合
        parameters2: dict
            节点2的属性集合
        r_label:
            关系的标签
        new_r_label: str or None
            新的关系标签
        new_r_parameters: dict
            新的关系属性

        Returns
        ----------
        """
        def combine_dict(d1, d2):
            for key in d2:
                if key not in d1:
                    d1[key] = d2[key]
            return d1

        if node1 and node2:
            relationship_matcher = RelationshipMatcher(self.driver)
            relationships = relationship_matcher.match([node1, node2], r_type=r_label)
            relationships = relationships.all()
            if not relationships:
                warnings.warn('警告！没有匹配到关系，请检查')
            for relationship in relationships:
                if new_r_label:
                    parameters = dict(relationship)
                    new_r_parameters = combine_dict(new_r_parameters, parameters)
                    # 删除关系
                    self.driver.separate(relationship)
                    self.create_relationship(node1, node2, new_r_label, new_r_parameters)
                else:
                    relationship.update(**new_r_parameters)
                    self.driver.push(relationship)
            return

        if type(label1) is str:
            label1 = [label1]
        if type(label2) is str:
            label2 = [label2]
        if uid or id:
            if uid:
                cyper = f'MATCH g=(node1)-[r]->(node2) WHERE r.uid=$uid RETURN g'
            else:
                uid = id
                cyper = f'MATCH g=(node1)-[r]->(node2) WHERE id(r)=$uid RETURN g'
            graph = self.driver.evaluate(cyper, {'uid': uid})
            relationship = graph.relationships[0]
            node1, node2 = graph.nodes
            if new_r_label:
                parameters = dict(relationship)
                new_r_parameters = combine_dict(new_r_parameters, parameters)
                # 删除关系
                self.driver.separate(relationship)
                self.create_relationship(node1, node2, new_r_label, new_r_parameters)
            else:
                relationship.update(new_r_parameters)
                self.driver.push(relationship)
        else:
            node_matcher = NodeMatcher(self.driver)
            relationship_matcher = RelationshipMatcher(self.driver)
            node1 = node_matcher.match(*label1).where(**parameters1).first()
            node2 = node_matcher.match(*label2).where(**parameters2).first()
            relationships = relationship_matcher.match([node1, node2], r_type=r_label)
            for relationship in relationships.all():
                if new_r_label:
                    parameters = dict(relationship)
                    new_r_parameters = combine_dict(new_r_parameters, parameters)
                    # 删除关系
                    self.driver.separate(relationship)
                    self.create_relationship(node1, node2, new_r_label, new_r_parameters)
                else:
                    relationship.update(new_r_parameters)
                    self.driver.push(relationship)
