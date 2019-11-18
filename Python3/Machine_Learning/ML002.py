#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        : 2019/11/17 14:22
# @Author      : Ma XingWang
# @FileName    : ML002.py
# @Software    : PyCharm
# @Description ：三分类问题，通过多个特征中预测鸢尾花的品种，鸢尾花的不同品种叫做类别

from sklearn.datasets import load_iris  # 鸢尾花数据集合
from sklearn.model_selection import train_test_split  # 随机分割数据集
from sklearn.neighbors import KNeighborsClassifier  # K近邻分类算法
import pandas as pd
import mglearn  # 通常是用来快速美化绘图
import matplotlib.pyplot as plt
import numpy as np

# 鸢尾花数据集合
iris_dataset = load_iris()
# 使用函数将数据集打乱，其中75%作为训练集，25%作为测试集；X 代表data，Y 代表target集合
# random_state 参数指定随机数生成器的种子
X_train, X_test, Y_train, Y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)


def display_data():
    """鸢尾花数据集合每个键的含义以及其内容"""

    # 获取数据集的键
    print("Keys for iris_dataset:\n{}".format(iris_dataset.keys()))

    # DESCR 键对应的值是数据集的简要说明
    print("\n" + iris_dataset['DESCR'][:200])

    # target_names 键对应的值是一个字符串数组，里面包含需要预测的花的品种
    print("\nTarget names:{}".format(iris_dataset["target_names"]))

    # feature_names 键对应的值是一个字符串列表，对每个特征(花萼长度、花萼宽度、花瓣长度、花瓣宽度)进行的说明
    print("\nFeature names:{}".format(iris_dataset["feature_names"]))

    # data 键包括花萼长度、花萼宽度、花瓣长度、花瓣宽度的测量数据，格式是Numpy数组
    # data 数组的每一行对应一朵花，列代表每朵花的四个测量数据
    print("\nType of data:{}".format(type(iris_dataset['data'])))
    print("\nShape of data:{}".format(iris_dataset['data'].shape))
    print("\nFrist five rows of data：{}".format(iris_dataset['data'][:5]))

    # target 是个一维数组、每朵花对应其中的一个数据
    # 数字的代表含义由 iris['target_names'] 数组给出：0 代表 setosa，1 代表 versicolor，2 代表 virginica
    print("\nType of target:{}".format(type(iris_dataset['target'])))
    print("\nShape of target:{}".format(iris_dataset['target'].shape))
    print("\nTarget：{}".format(iris_dataset['target']))

    # filename 键存放数据文件的路径
    print("\nFile name：" + iris_dataset['filename'])


def split_data():
    """检查分割的数据集，获取数组的shape"""

    print("X_train shape: {}".format(X_train.shape))
    print("y_train shape: {}".format(Y_train.shape))
    print("X_test shape: {}".format(X_test.shape))
    print("y_test shape: {}".format(Y_test.shape))


def check_data():
    """分析数据"""

    # 以feature_names为列进行整理数据
    iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset['feature_names'])
    print(iris_dataframe)

    # c=Y_train：根据Y_train来区分颜色
    # figsize=(15, 15)：以英寸为单位的图像大小，一般以元组 (width, height) 形式设置
    # marker='o'：Matplotlib可用的标记类型，如’.’，’,’，’o’等
    # hist_kwds={'bins': 20}：对角线直方图的分割个数
    # alpha：图像透明度，一般取(0,1]
    pd.plotting.scatter_matrix(iris_dataframe, c=Y_train, figsize=(15, 15), marker='o', hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)

    # 对角线部分：核密度估计图，就是用来看某 一个 变量分布情况，横轴对应着该变量的值，纵轴对应着该变量的密度（可以理解为出现频次）
    # 非对角线部分：两个变量之间分布的关联散点图；将任意两个变量进行配对，以其中一个为横坐标，另一个为纵坐标，将所有的数据点绘制在图上，用来衡量两个变量的关联度（Correlation）
    # 展示散点图矩阵
    plt.show()


def k_data():
    """
    使用K近邻算法
    训练集中与新数据点最近的任意k个邻居（比如距离最近的3个或5个邻居），而不是只考虑最近的那一个，然后可以用这些邻居中数量最多的类别做出预测
    """
    # knn对象对算法进行了封装，既包含用训练数据构建模型的算法，也包括对新数据点进行预测的算法
    # n_neighbors 参数：邻居的数目
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, Y_train)  # 基于训练集来构建模型
    # print(knn.fit(X_train,Y_train))

    # 直接使用knn对象的score方法计算精度
    print("Test set score: {:.2f}".format(knn.score(X_test, Y_test)))

    # 将测试数据集传入，获取预测结果
    y_pred = knn.predict(X_test)
    print("Test set predictions:\n {}".format(y_pred))
    # 对比预测结果和真实结果，得到精确度97%
    print("Test set score: {:.2f}".format(np.mean(y_pred == Y_test)))


if __name__ == "__main__":
    # display_data()
    # split_data()
    # check_data()
    k_data()
