import matplotlib.pyplot as plt
import numpy as np  # Numpy支持大量的维度数组和矩阵运算，对数组运算提供了大量的数学函数库

x1 = np.linspace(-1, 1, 50)  # 从(-1,1)均匀取50个点
print(x1)
x2 = np.linspace(0, 2*np.pi, 50)
print(x2)
# 防止中文标签乱码，还有通过导入字体文件的方法
plt.rcParams['font.sans-serif'] = ['SimHei']

# 这个是第一个figure对象,下面的内容都会在第一个figure中显示
plt.figure()
plt.plot(x1, x1 ** 2, color="red", linewidth=3.0, linestyle="--")

# 这里第二个figure对象，在窗口上显示figure3，figsize为窗口大小
plt.figure(num=3, figsize=(10, 5))
# r代表红色，g代表绿色，-o代表实心点标记的实线，--代表虚线
plt.plot(x2, np.cos(x2), 'r-o', x2, np.sin(x2), 'g--')

# 使用子图 subplot第一个参数代表子图的总行数，第二个参数代表子图的总列数，第三个参数代表活动区域是第几个
plt.figure(num=4, figsize=(10, 5))
plt.subplot(2, 2, 1)
plt.plot(x2, np.sin(x2), 'r')
plt.subplot(2, 2, 2)
plt.plot(x2, np.cos(x2), 'g')
plt.subplot(2, 2, 3)
plt.scatter(x2, np.sin(x2))  # 散点图
plt.subplot(2, 2, 4)
# 彩色散点图，第三个参数是大小，第四个参数是颜色
plt.scatter(np.random.rand(1000), np.random.rand(1000),
            np.random.rand(1000)*50, np.random.rand(1000))
plt.colorbar()  # 添加一个颜色栏

# 添加标题，标签，图例

plt.figure(num=5, figsize=(10, 5))
plt.plot(x2, np.sin(x2), 'r-x', label="Sin(x)")
plt.plot(x2, np.cos(x2), 'g-^', label="Cos(x)")
plt.legend()  # 显示图例
plt.xlabel("X 轴")
plt.ylabel("Y 轴")
plt.xlim((0, np.pi*2))  # 横纵坐标
plt.ylim((-1, 1))

plt.title("sin and cos")

# 直方图
plt.figure(num=6, figsize=(10, 5))
plt.hist(x1, 50)
plt.show()
