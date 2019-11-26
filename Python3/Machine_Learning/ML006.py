#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        : 2019/11/24 17:03
# @Author      : Ma XingWang
# @FileName    : ML006.py
# @Software    : PyCharm
# @Description ：用于分类的线性模型：线性SVM和Logistic回归

import mglearn
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression

X, y = mglearn.datasets.make_forge()  # 具有两个特征的数据集
cancer = load_breast_cancer()


def l_forge():
    """线性SVM和Logistic回归在forge数据集上的决策边界"""
    fig, axes = plt.subplots(1, 2, figsize=(10, 3))

    for model, ax in zip([LinearSVC(), LogisticRegression()], axes):
        clf = model.fit(X, y)
        mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=0.7)
        mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
        ax.set_title("{}".format(clf.__class__.__name__))
        ax.set_xlabel("Feature 0")
        ax.set_ylabel("Feature 1")
    axes[0].legend()
    plt.show()


def l_mg_forge():
    """
    不同C值的线性SVM在forge数据集上的决策边界
    C值越小对应强正则化
    """
    mglearn.plots.plot_linear_svc_regularization()
    plt.show()


def show_cancer():
    """展示威斯康星州乳腺癌数据集"""
    # 输出cancer数据集的键
    print("cancer.keys():\n{}".format(cancer.keys()))

    # 输出cancer数据集中data数据的维度，共有569条数据，每个数据有30个特征
    print("Shape of cancer data: {}".format(cancer.data.shape))

    # 输出标签，并且统计标签
    # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
    # bincount() 函数
    print("Sample counts per class:\n{}".format({n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))}))

    # 输出所有的特征
    print("Feature names：\n{}".format(cancer.feature_names))


def logistic_cancer(C):
    """"""
    x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)
    logreg = LogisticRegression(C=C).fit(x_train, y_train)
    print("训练数据集精度：{:.3f}".format(logreg.score(x_train, y_train)))
    print("测试数据集精度：{:.3f}".format(logreg.score(x_test, y_test)))
    print("")


def show_logistic_cancer(L):
    """"""
    x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)
    logreg = LogisticRegression(C=1, penalty=L).fit(x_train, y_train)
    logreg100 = LogisticRegression(C=100, penalty=L).fit(x_train, y_train)
    logreg001 = LogisticRegression(C=0.01, penalty=L).fit(x_train, y_train)

    plt.plot(logreg.coef_.T, 'o', label="C=1")
    plt.plot(logreg100.coef_.T, '^', label="C=100")
    plt.plot(logreg001.coef_.T, 'v', label="C=0.001")

    plt.xticks(range(cancer.data.shape[1]), cancer.feature_names, rotation=90)
    plt.hlines(0, 0, cancer.data.shape[1])
    plt.ylim(-5, 5)
    plt.xlabel("Coefficient index")
    plt.ylabel("Coefficient magnitude")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    l_forge()
    l_mg_forge()
    show_cancer()
    logistic_cancer(1)
    logistic_cancer(100)
    logistic_cancer(0.01)
    show_logistic_cancer("l2")
    show_logistic_cancer("l1")
