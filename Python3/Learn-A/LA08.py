#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/8/6 12:31
# @Author      ：Falling Stars
# @FileName    ：LA08
# @Software    ：PyCharm
# @Description ：Python查询MongoDB数据库

from pymongo import MongoClient

MONGOURL = "mongodb://root:123456@localhost:27017"
DBNAME = "Scrapy_A"
COLLECTIONNAME = "kr"


def get_one(collection):
    """
    获取单个doc
    """
    doc = collection.find_one()
    print("Single Document:")
    print(doc)


def get_all(collection, query=None, sorter=None, limit_num=None, fileds=None, filed=None, s_num=None, e_num=None):
    """
    获取全部文档
    :param collection:集合
    :param query:查询条件
    :param sorter:排序
    :param limit_num:limit()函数，限制返回的数量
    :param fileds:限制返回的字段
    :param filed:是否只获取文档的属性
    :param s_num:游标就是个集合，对集合进行切片
    :param enum:
    :return:
    """
    print("\nMany Using While Loop:")

    # 查询，并限制返回的字段，格式为{'article_title': True, '_id': False}；其中True代表可以显示，_id属性默认显示
    cursor = collection.find(query, fileds)

    # 排序，格式为[('column_id', 1), ('article_title', 1)]；其中1为升序，-1为降序
    if sorter:
        cursor.sort(sorter)

    # 限制返回的数量
    if limit_num:
        cursor.limit(limit_num)

    # 集合切片
    if s_num:
        if e_num and e_num > s_num:
            cursor = cursor[s_num, e_num]
        else:
            cursor = cursor[s_num]
    else:
        if e_num:
            cursor = cursor[:e_num]

    docs = []
    for doc in cursor:
        # 是否只获取某个属性
        if filed:
            docs.append(doc[filed])
        else:
            docs.append(doc)
    print(docs)


def get_count(collection, query=None):
    """
    获取总数量
    :param collection:
    :param query:
    :return:
    """
    if not query:
        query = {}
    cursor = collection.find(query)
    # print(cursor.count())
    print("Num:", cursor.count())


def get_page(collection, pagesize, pagenum, query=None, sorter=None, fileds=None):
    """
    分页函数
    :param collection:
    :param pagesize:每页大小
    :param pagenum:页码
    :param query:查询条件
    :param sorter:排序
    :param fileds:显示字段
    :return:
    """
    if pagesize <= 0 or pagenum <= 0:
        return []
    cursor = collection.find(query, fileds)
    if sorter:
        cursor = cursor.sort(sorter)

    cursor = cursor.skip(pagesize * pagenum - pagesize).limit(pagesize)
    docs = []
    for doc in cursor:
        docs.append(doc)
    print(docs)


if __name__ == "__main__":
    mongodb = MongoClient(MONGOURL)
    db = mongodb[DBNAME]
    collection = db[COLLECTIONNAME]
    # db.kr.findOne()
    # get_one(collection)

    # db.kr.find({'column_id': {$lt:100}}).count()
    # get_count(collection, query={'column_id': {'$lt': 100}})

    # db.kr.find({},{_id:0,article_title:1}).limit(10)
    # get_all(collection, filed="article_title", e_num=10)

    # db.kr.find().limit(10)
    # get_all(collection, e_num=10)

    # db.kr.find({'column_id': 18},{_id:0,article_title:1}).limit(20)
    # get_all(collection, query={'column_id': 18}, filed="article_title", e_num=20)

    # db.kr.find({'column_id': {$lt:100}},{_id:0,article_title:1}).limit(20)
    # get_all(collection, query={'column_id': {'$lt': 100}}, filed="article_title", e_num=20)

    # db.kr.find({'column_id': {$lt:100}},{_id:0,article_title:1}).sort({column_id:1,article_title:1}).limit(20)
    # get_all(collection, query={'column_id': {'$lt': 100}}, sorter=[('column_id', 1), ('article_title', 1)],
    #         filed="article_title", e_num=20)
    # get_all(collection, query={'column_id': {'$lt': 100}}, sorter=[('column_id', 1), ('article_title', 1)],
    #         filed="article_title", limit_num=20)

    # db.kr.find({}, {_id: 0, article_title: 1}).limit(20)
    # get_all(collection, fileds={'article_title': True, '_id': False}, limit_num=20)

    # db.kr.find({},{_id:0,article_title:1,id:1}).skip(10*20-10).limit(10)
    # get_page(collection, 10, 20, fileds={'article_title': True, 'id': True, '_id': False})

    # db.kr.find({},{_id:0,article_title:1,id:1}).sort({article_title:1}).skip(10*20-10).limit(10)
    # get_page(collection, 10, 20, fileds={'article_title': True, 'id': True, '_id': False},sorter=[('article_title',1)])

# collection.write_concern = {'w': 1, 'j': True, 'wtimeout': 10000, 'fsync': True}
