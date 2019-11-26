#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        : 2019/11/24 14:24
# @Author      : Ma XingWang
# @FileName    : ML003.py
# @Software    : PyCharm
# @Description ：K近邻分类

import mglearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

X, y = mglearn.datasets.make_forge()  # 具有两个特征的数据集
cancer = load_breast_cancer()  # sklearn中的威斯康星州乳腺癌数据集


def show_forge():
    """展示mglearn的两个特征的forge数据集"""
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
    plt.legend(["Class 0", "Class 1"], loc=4)
    plt.xlabel("第一种特征", fontproperties='SimHei')  # first feature
    plt.ylabel("第二种特征", fontproperties='SimHei')  # second feature
    print("X.shape:{}".format(X.shape))
    plt.show()


def k_forge(k):
    """使用mglearn中的分类K近邻方法plot_knn_classification,标注测试数据不同个数的近邻"""
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
    mglearn.plots.plot_knn_classification(n_neighbors=k)
    plt.legend(["Class 0", "Class 1"], loc=4)
    plt.xlabel("第一种特征", fontproperties='SimHei')  # first feature
    plt.ylabel("第二种特征", fontproperties='SimHei')  # second feature
    plt.show()


def sk_k_forge():
    """使用sklearn上的分类k近邻方法KNeighborsClassifier进行泛化，并输出模型精度"""
    clf = KNeighborsClassifier(n_neighbors=3)
    x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0)
    clf.fit(x_train, y_train)
    print("测试集精度: {:.2f}".format(np.mean(y_test == clf.predict(x_test))))
    print("测试集精度: {:.2f}".format(clf.score(x_test, y_test)))


def check_sk_k_forge():
    """不同n_neighbors值的K近邻模型KNeighborsClassifier的决策边界"""
    # 设置三列一行的布局
    fig, axes = plt.subplots(1, 3, figsize=(10, 3))

    for n_neighbors, ax in zip([1, 3, 9], axes):
        # fit方法返回对象本身，所以我们可以将实例化和拟合放在一行代码中
        clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
        # plot_2d_separator：对于二维数据集，可以在xy平面上画出所有可能的测试点的预测结果，根据平面中每个点所属的类别对平面进行着色
        # 决策边界（decision boundary），即算法对类别0和类别1的分界线，平面中不同颜色的分界线
        mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
        mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
        ax.set_title("{} neighbor(s)".format(n_neighbors))
        ax.set_xlabel("feature 0")
        ax.set_ylabel("feature 1")
    axes[0].legend(loc=3)
    plt.show()


def k_cancer():
    """以n_neighbors为自变量，使用KNeighborsClassifier方法对比训练集精度和测试集精度"""
    x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=66)

    training_accuracy = []  # 训练集精度集合
    test_accuracy = []  # 测试集精度集合
    # n_neighbors取值从1到10
    neighbors_settings = range(1, 11)
    for n_neighbors in neighbors_settings:
        # 构造模型
        clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(x_train, y_train)
        training_accuracy.append(clf.score(x_train, y_train))  # 记录训练集精度
        test_accuracy.append(clf.score(x_test, y_test))  # 记录泛化精度

    plt.plot(neighbors_settings, training_accuracy, label="tracing accuracy")
    plt.plot(neighbors_settings, test_accuracy, label="test accracy")
    plt.xlabel("n_neighbors")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    show_forge()
    k_forge(1)
    k_forge(3)
    sk_k_forge()
    check_sk_k_forge()
    k_cancer()
