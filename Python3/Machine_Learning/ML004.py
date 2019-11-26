#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        : 2019/11/24 15:39
# @Author      : Ma XingWang
# @FileName    : ML004.py
# @Software    : PyCharm
# @Description ：K近邻回归

import mglearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

X, y = mglearn.datasets.make_wave(n_samples=60)  # 单特征的wave数据集


def show_wave():
    """展示单特征的wave数据集"""
    plt.plot(X, y, 'o')
    plt.xlim(-3, 3)  # 限定x轴的范围
    plt.xlabel("Feature")  # 特征
    plt.ylabel("Target")  # 标签
    plt.show()


def mg_k_wave(k):
    """使用mglearn中k近邻回归算法plot_knn_regression，标注测试点中不同个数的近邻"""
    mglearn.plots.plot_knn_regression(n_neighbors=k)
    plt.xlim(-3, 3)  # 限定x轴的范围
    plt.xlabel("Feature")  # 特征
    plt.ylabel("Target")  # 标签
    plt.show()


def sk_k_wave():
    """使用mklearn回归k近邻模型KNeighborsRegressor预测数据，并展示精度"""
    x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0)
    reg = KNeighborsRegressor(n_neighbors=3)
    reg.fit(x_train, y_train)
    print("Test set predictions:\n{}".format(reg.predict(x_test)))
    # R^2 也叫作决定系数，是回归模型预测的优度度量
    print("Test set R^2: {:.2f}".format(reg.score(x_test, y_test)))


def check_k_wave():
    """不同n_neighbors值的k近邻回归的预测结果对比"""
    x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0)
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    # 在-3到3上取1000个数据并且均匀分布
    line = np.linspace(-3, 3, 1000).reshape(-1, 1)

    for n_neighbors, ax in zip([1, 3, 9], axes):
        # 构建模型
        reg = KNeighborsRegressor(n_neighbors=n_neighbors).fit(x_train, y_train)
        ax.plot(line, reg.predict(line))  # 绘画出测试的数据
        ax.plot(x_train, y_train, "^", c=mglearn.cm2(0), markersize=8)  # 训练数据
        ax.plot(x_test, y_test, "v", c=mglearn.cm2(1), markersize=8)  # 泛化数据
        ax.set_title("{} neighbor(s)\n train score: {:.2f} test score: {:.2f}".format(
            n_neighbors, reg.score(x_train, y_train),
            reg.score(x_test, y_test)))
        ax.set_xlabel("Feature")
        ax.set_ylabel("Target")

    axes[0].legend(["Model predictions", "Training data/target", "Test data/target"], loc="best")
    plt.show()


if __name__ == "__main__":
    show_wave()
    mg_k_wave(1)
    mg_k_wave(3)
    sk_k_wave()
    check_k_wave()
