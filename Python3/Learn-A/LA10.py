#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/8/7 14:09
# @Author      ：Falling Stars
# @FileName    ：LA10
# @Software    ：PyCharm
# @Description ：Python在MongoDB中的CDUR操作
from pymongo import MongoClient

MONGOURL = "mongodb://root:123456@localhost:27017"
DBNAME = "test"
COLLECTIONNAME = "runoob"


def add_data(collection):
    """
    insert
    :param collection:
    :return:
    """
    doc0 = {'title': 'MongoDB 教程', 'description': 'MongoDB 是一个Nosql数据库', 'by': '菜鸟教程', 'url': 'http://www.runoob.com',
            'tags': ['mongodb', 'database', 'NoSQL'], 'likes': 1200}
    doc1 = {'title': 'HTML 教程', 'description': 'HTML编写网页', 'by': '菜鸟教程', 'url': 'http://www.runoob.com',
            'tags': ['HTML', 'JavaScript', 'CSS'], 'likes': 1010}
    doc2 = {'title': 'ASP.NET 教程', 'description': 'ASP.NET编写网页', 'by': '菜鸟教程', 'url': 'http://www.runoob.com',
            'tags': ['Web Froms', 'Web API', 'MVC', 'WCF'], 'likes': 1000}
    doc3 = {'title': 'JAVA 教程', 'description': 'JAVA编写网页', 'by': '菜鸟教程', 'url': 'http://www.runoob.com',
            'tags': ['JSP', 'Spring'], 'likes': 1560}
    collection.insert(doc0)
    collection.insert([doc1, doc2, doc3])  # 一次性插入多个数据

    cursor = collection.find()
    for doc in cursor:
        print(doc)


def remove_data(collection, query=None):
    """
    delete
    :param collection:
    :param query:
    :return:
    """
    collection.remove(query)
    cursor = collection.find()
    for doc in cursor:
        print(doc)


def save_data(collection):
    """
    save()方法接受一个键值对对象作为参数，如果指定的文档已经存在于数据库中，就将其更新为指定的值，否则插入一个文档
    应该是根据_id匹配
    :param collection:
    :param doc:
    :return:
    """
    doc = collection.find_one()
    doc['description'] = "save修改"
    collection.save(doc)
    cursor = collection.find()
    for doc in cursor:
        print(doc)


def update_doc(collection, query, update, upsert=False, manipulate=False, multi=False):
    """
    
    :param collection: 
    :param query: 查询条件
    :param update: 更新
    :param upsert: 为true时，如果没有匹配到符合的文档，则进行插入，默认false
    :param safe: 
    :param multi: 为true时，可以一次性修改所有符合条件的文档
    :return: 
    """
    collection.update(query, update, upsert=upsert, manipulate=manipulate, multi=multi)
    cursor = collection.find()
    for doc in cursor:
        print(doc)


if __name__ == "__main__":
    mongodb = MongoClient(MONGOURL)
    db = mongodb[DBNAME]
    collection = db[COLLECTIONNAME]

    # add_data(collection)
    # remove_data(collection, query={'$or': [{'title': 'HTML 教程'}, {'title': 'JAVA 教程'}]})
    # save_data(collection)
    update_doc(collection, {'title': 'ASP.NET 教程'},
               {'$set': {'description': ''}, '$push': {'tags': 'update'}, '$inc': {'likes': 10000}},
               multi=True)
