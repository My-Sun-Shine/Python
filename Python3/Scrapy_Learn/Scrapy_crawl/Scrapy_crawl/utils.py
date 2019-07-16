#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/16 16:26
# @Author      ：Falling Stars
# @FileName    ：utils
# @Software    ：PyCharm
# @Description ：
from os.path import realpath, dirname
import json


def get_config(name):
    path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())