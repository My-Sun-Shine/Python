#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        : 2019/11/17 11:59
# @Author      : Ma XingWang
# @FileName    : ML001.py
# @Software    : PyCharm
# @Description ：机器学习涉及库的使用

import numpy as np  # 多维数组，高级数学函数(线性代数运算和傅里叶变化)，伪随机数生成器
from scipy import sparse  # 线性代数改机程序，数学函数优化、信号处理、特殊数学函数和统计分布
import matplotlib.pyplot as plt  # 科学绘图，如折线图、直方图、散点图
import pandas as pd  # 处理和分析数据的Python库

# 输出二维数组
x = np.array([[1, 2, 3], [4, 5, 6]])
print("x:\n{}".format(x))

# 输出二维数组，并转换为CSR格式的稀疏矩阵
eye = np.eye(4)
print("Numpy array:\n{}".format(eye))  # 二维，对角线为1，其余都是0
sparse_matrix = sparse.csr_matrix(eye)  # 将数组转换为CSR格式的Scipy稀疏矩阵
print("\nScipy sparse CSR matrix:\n{}".format(sparse_matrix))

# 二维数组转换为COO格式的稀疏矩阵
data = np.ones(4)
# print(data)
row_indices = np.arange(4)
# print(row_indices)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("Coo representation:\n{}".format(eye_coo))  # coo格式的稀疏矩阵

# sin函数图形
x = np.linspace(-10, 10, 100)  # 在-10到10之间生成一个数列，共100个数
y = np.sin(x)
plt.plot(x, y, marker="x")
plt.show()

# 数据表格
data = {'Name': ["John", "Anna", "Peter", "Linda"],
        'Location': ["New York", "Paris", "Berlin", "London"],
        'Age': [24, 25, 26, 27]}

data_pandas = pd.DataFrame(data)
print(data_pandas)
print(data_pandas[data_pandas.Age > 25])
