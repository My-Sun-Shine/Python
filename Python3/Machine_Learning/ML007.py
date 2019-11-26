#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        : 2019/11/24 21:58
# @Author      : Ma XingWang
# @FileName    : ML007.py
# @Software    : PyCharm
# @Description ：用于多分类的线性模型：一对多余

import mglearn
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt

X, y = make_blobs(random_state=42)  # 三分类的数据集


def show_blobs():
    """展示三分类的blobs数据集"""
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
    plt.xlabel("Feature 0")
    plt.ylabel("Feature 1")
    plt.legend(["Class 0", "Class 1", "Class 2"])
    plt.show()


def svc_blobs():
    """三个一对其余分类器的决策边界"""
    linear_svm = LinearSVC().fit(X, y)
    print("Coef shape: {}".format(linear_svm.coef_.shape))
    print("Intercept shape: {}".format(linear_svm.intercept_.shape))
    mglearn.plots.plot_2d_classification(linear_svm, X, fill=True, alpha=0.7)
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
    line = np.linspace(-15, 15)
    for coef, intercept, color in zip(linear_svm.coef_, linear_svm.intercept_, ['b', 'r', 'g']):
        plt.plot(line, -(line * coef[0] + intercept) / coef[1], c=color)
    plt.ylim(-10, 15)
    plt.xlim(-10, 8)
    plt.xlabel("Feature 0")
    plt.ylabel("Feature 1")
    plt.legend(['Class 0', 'Class 1', 'Class 2', 'Line class 0', 'Line class 1', 'Line class 2'], loc=(1.01, 0.3))
    plt.show()


if __name__ == "__main__":
    show_blobs()
    svc_blobs()
