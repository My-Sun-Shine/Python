#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/8/7 15:06
# @Author      ：Falling Stars
# @FileName    ：LA11
# @Software    ：PyCharm
# @Description ：Python实现MongoDB的GridFS存储
from pymongo import MongoClient
import gridfs

MONGOURL = "mongodb://root:123456@localhost:27017"
DBNAME = "myFS"


# # -u root -p 123456 --authenticationDatabase admin 为用户权限验证

def put_gridfs(db):
    """
    mongofiles -u root -p 123456 --authenticationDatabase admin --db myFS put "1.txt"
    将1.txt存储到GridFS存储区myFS数据库中
    :param db:
    :return:
    """
    fs = gridfs.GridFS(db)
    # 第一个参数为data，为数据
    fs.put("Python file", filename="1.txt", encoding='utf-8')


def get_gridfs(db):
    """
    mongofiles -u root -p 123456 --authenticationDatabase admin --db myFS --local "2.txt" get  "1.txt"
    获取1.txt文件，另存为到本地的2.txt
    :param db:
    :return:
    """
    fs = gridfs.GridFS(db)
    # 获取最新版本的文件
    file = fs.get_last_version(filename="1.txt")
    print(file.read())


def delete_gridfs(db):
    """
    mongofiles -u root -p 123456 --authenticationDatabase admin --db myFS delete  "1.txt"
    删除存储区的1.txt
    :param db:
    :return:
    """
    fs = gridfs.GridFS(db)
    file = fs.get_last_version(filename="1.txt")
    fs.delete(file._id)


def list_gridfs(db):
    """
    mongofiles -u root -p 123456 --authenticationDatabase admin --db myFS list
    列出存储区找那个的文件
    :param db:
    :return:
    """
    fs = gridfs.GridFS(db)
    print(fs.list())


if __name__ == "__main__":
    mongo = MongoClient(MONGOURL)
    db = mongo[DBNAME]

    # put_gridfs(db)
    list_gridfs(db)
    # get_gridfs(db)
    # delete_gridfs(db)
