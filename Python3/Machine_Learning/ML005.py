#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        : 2019/11/24 15:57
# @Author      : Ma XingWang
# @FileName    : ML005.py
# @Software    : PyCharm
# @Description ：线性模型：线性回归OLS、岭回归、lasso回归

import mglearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso

boston = load_boston()  # 波士顿房价数据集boston
X_wave, y_wave = mglearn.datasets.make_wave(n_samples=60)  # 单特征的wave数据集
X_boston, y_boston = mglearn.datasets.load_extended_boston()  # mglearn中的波士顿房价扩展数据集boston


def ols_wave():
    """使用线性回归OLS，即普通最小二乘法来预测wave数据集"""
    x_train, x_test, y_train, y_test = train_test_split(X_wave, y_wave, random_state=42)
    lr = LinearRegression().fit(x_train, y_train)
    print("lr.coef_: {}".format(lr.coef_))  # “斜率”参数（w，也叫作权重或系数），其中每一个元素对应一个输入特征
    print("lr.intercept_: {}".format(lr.intercept_))  # 偏移或截距（b）
    print("训练集精度：{:.2f}".format(lr.score(x_train, y_train)))
    print("测试集精度：{:.2f}".format(lr.score(x_test, y_test)))


def show_boston():
    """波士顿房价数据集"""
    print("Data shape: {}".format(boston.data.shape))
    # 上面那个数据集只有13个特征，但是我们可以对这个数据集进行扩展，因为可以把两两特征的乘积作为新的特征
    # 13个特征+13个特征的两两组合有放回的 13!+13=104
    print("X_boston.shape: {}".format(X_boston.shape))


def ols_boston():
    """使用sklearn中LinearRegression线性回归OLS预测mglearn中的boston扩展数据集"""
    x_train, x_test, y_train, y_test = train_test_split(X_boston, y_boston, random_state=0)
    lr = LinearRegression().fit(x_train, y_train)
    # 训练集和测试集之间的性能差异是过拟合的明显标志
    print("训练集精度：{:.2f}".format(lr.score(x_train, y_train)))
    print("测试集精度：{:.2f}".format(lr.score(x_test, y_test)))


def ridge_boston(alpha):
    """使用sklearn中的岭回归Ridge预测mglearn中的boston扩展数据集"""
    x_train, x_test, y_train, y_test = train_test_split(X_boston, y_boston, random_state=0)
    ridge = Ridge(alpha=alpha).fit(x_train, y_train)
    print("训练集精度：{:.2f}".format(ridge.score(x_train, y_train)))
    print("测试集精度：{:.2f}".format(ridge.score(x_test, y_test)))
    print("")


def check_boston():
    """将不同alpha的岭回归Ridge和线性回归LinearRegression的w系数，并显示在图片上"""
    x_train, x_test, y_train, y_test = train_test_split(X_boston, y_boston, random_state=0)
    ridge = Ridge(alpha=1.0).fit(x_train, y_train)
    ridge10 = Ridge(alpha=10).fit(x_train, y_train)
    ridge01 = Ridge(alpha=0.1).fit(x_train, y_train)
    lr = LinearRegression().fit(x_train, y_train)
    plt.plot(ridge.coef_, 's', label="Ridge alpha=1")
    plt.plot(ridge10.coef_, '^', label="Ridge alpha=10")
    plt.plot(ridge01.coef_, 'v', label="Ridge alpha=0.1")
    plt.plot(lr.coef_, 'o', label="LinearRegression")
    # x 轴为index索引，y 轴为该索引对于的coef值
    plt.xlabel("Coefficient index")
    plt.ylabel("Coefficient magnitude")
    plt.hlines(0, 0, len(lr.coef_))  # 水平线
    plt.ylim(-25, 25)
    plt.xlim(0, 120)
    plt.legend()
    plt.show()


def plot_ridge():
    """
    对波士顿房价数据集做二次抽样，并在数据量逐渐增加的子数据集上分别对 LinearRegression 和 Ridge(alpha=1) 两个模型进行评估（
    将模型性能作为数据集大小的函数进行绘图，这样的图像叫作学习曲线
    """
    mglearn.plots.plot_ridge_n_samples()
    plt.show()


def lasso_boston(alpha, iter):
    """不同alpha参数的lasso回归模型对boston扩展数据集的预测"""
    x_train, x_test, y_train, y_test = train_test_split(X_boston, y_boston, random_state=0)
    # 在减小alpha的同时，最好增加max_iter的值
    lasso = Lasso(alpha=alpha, max_iter=iter).fit(x_train, y_train)
    # alpha=1时显示欠拟合，=0.01时显示过拟合
    print("训练集精度：{:.2f}".format(lasso.score(x_train, y_train)))
    print("测试集精度：{:.2f}".format(lasso.score(x_test, y_test)))
    print("使用特征的数量：{}".format(np.sum(lasso.coef_ != 0)))
    print("")


def check_lasso():
    """不同alpha参数的lasso回归和ridge岭回归的系数对比"""
    x_train, x_test, y_train, y_test = train_test_split(X_boston, y_boston, random_state=0)
    lasso = Lasso(alpha=1, max_iter=1000).fit(x_train, y_train)  # 大多数系数都为0
    lasso001 = Lasso(alpha=0.01, max_iter=100000).fit(x_train, y_train)
    lasso0001 = Lasso(alpha=0.001, max_iter=1000000).fit(x_train, y_train)  # 大多数系数都不为0
    ridge01 = Ridge(alpha=0.1).fit(x_train, y_train)  # 所有系数都不为0

    plt.plot(lasso.coef_, 's', label="Lasso alpha=1")
    plt.plot(lasso001.coef_, '^', label="Lasso alpha=0.01")
    plt.plot(lasso0001.coef_, 'v', label="Lasso alpha=0.001")
    plt.plot(ridge01.coef_, 'o', label="Rigde alpha=0.1")
    plt.legend(ncol=2, loc=(0, 1.05))
    plt.ylim(-25, 25)
    plt.xlim(0, 120)
    plt.xlabel("Coefficient index")
    plt.ylabel("Coefficient magnitude")
    plt.show()


if __name__ == "__main__":
    ols_wave()
    show_boston()
    ols_boston()
    ridge_boston(1)
    ridge_boston(10)
    ridge_boston(0.1)
    check_boston()
    plot_ridge()
    lasso_boston(1.0, 1000)
    lasso_boston(0.01, 100000)
    lasso_boston(0.001, 1000000)
    check_lasso()
