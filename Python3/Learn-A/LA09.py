#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/8/7 11:22
# @Author      ：Falling Stars
# @FileName    ：LA09
# @Software    ：PyCharm
# @Description ：Python聚合MongoDB数据以及distinct函数

from pymongo import MongoClient

MONGOURL = "mongodb://root:123456@localhost:27017"
DBNAME = "Scrapy_A"
COLLECTIONNAME = "kr"


def get_distinct(collection, query=None, fileds=None, distinct_str=None):
    """
    符合查询条件的结果将distinct_str指定的属性值都放在一个数组中，去重
    :param collection:
    :param query:查询条件
    :param fileds:显示字段
    :param distinct_str:distinct值
    :return:
    """
    if distinct_str:
        distinct_array = collection.find(query, fileds).distinct(distinct_str)
        print(distinct_array)
        print(len(distinct_array))
        # return distinct_array
    else:
        print([])
        # return []


def get_group(collection):
    """
    group函数
    :return:
    """
    # var group_reduce = function(curr, result){
    #     result.sum += curr.article_id
    #     result.total += 1
    # }
    # var group_finalize = function(result){
    #     result.avg = result.sum / result.total
    # }
    # db.kr.group({
    #     key: {column_id: 1},
    #     cond: {},
    #     reduce: group_reduce,
    #     initial: {sum: 0, total: 0, avg: 0},
    #     finalize: group_finalize
    # })
    key = {'column_id': True}
    cond = {}
    reduce = "function(curr, result){result.sum += curr.article_id; result.total += 1;}"
    initial = {'sum': 0, 'total': 0, 'avg': 0}
    finalize = "function(result){result.avg = result.sum / result.total}"
    result = collection.group(key, cond, initial, reduce, finalize)
    for r in result:
        print(r)


def get_aggregate(collection):
    """
    aggregate函数
    :return:
    """
    # db.kr.aggregate(
    #     {$match: {column_id: {$gt: 100}}},
    #     {$group: {
    #         _id: "$column_id",
    #         total: {$sum: 1},
    #         sum: {$sum: "$article_id"},
    #         avg: {$avg: "$article_id"}}
    #     },
    #     {$sort: {total: 1, sum: 1, avg: 1}},
    #     {$skip: 1},
    #     {$limit: 5}
    # )
    match = {'$match': {"column_id": {'$gt': 100}}}
    group = {'$group': {'_id': '$column_id', 'total': {'$sum': 1}, 'sum': {'$sum': "$article_id"},
                        'avg': {'$avg': "$article_id"}}}
    sort = {'$sort': {'total': 1, 'sum': 1, 'avg': 1}}
    skip = {'$skip': 1}
    limit = {'$limit': 5}
    result = collection.aggregate([match, group, sort, skip, limit])
    for r in result:
        print(r)


if __name__ == "__main__":
    mongodb = MongoClient(MONGOURL)
    db = mongodb[DBNAME]
    collection = db[COLLECTIONNAME]

    # db.kr.distinct('article_title',{'column_id': 18})
    # print(db.kr.distinct('article_title', {'column_id': 18}).length)
    # get_distinct(collection, query={'column_id': 18}, distinct_str='article_title')

    # get_group(collection)
    get_aggregate(collection)
