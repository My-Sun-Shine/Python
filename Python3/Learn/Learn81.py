import matplotlib.pyplot as plt

ax = []                    # 定义一个 x 轴的空列表用来接收动态的数据
ay = []                    # 定义一个 y 轴的空列表用来接收动态的数据
bx = []
by = []
plt.ion()                  # 开启一个画图的窗口
# plt.rcParams['savefig.dpi'] = 200 #图片像素
# plt.rcParams['figure.dpi'] = 200 #分辨率
plt.rcParams['figure.figsize'] = (10, 10)        # 图像显示大小
plt.rcParams['font.sans-serif'] = ['SimHei']  # 防止中文标签乱码，还有通过导入字体文件的方法
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['lines.linewidth'] = 0.5  # 设置曲线线条宽度
for i in range(100):       # 遍历0-99的值
    plt.clf()              # 清除之前画的图
    plt.suptitle("总标题", fontsize=30)
    ax.append(i)           # 添加 i 到 x 轴的数据中
    ay.append(i**2)        # 添加 i 的平方到 y 轴的数据中
    agraphic = plt.subplot(2, 1, 1)
    agraphic.set_title('子图表标题1')  # 添加子标题
    agraphic.set_xlabel('x轴', fontsize=10)  # 添加轴标签
    agraphic.set_ylabel('y轴', fontsize=20)
    plt.plot(ax, ay, 'g-')  # 等于agraghic.plot(ax,ay,'g-')

    bx.append(i)
    by.append(-i**3+i**2+i)
    bgraghic = plt.subplot(2, 1, 2)
    bgraghic.set_title('子图表标题2')
    bgraghic.set_xlabel('x轴', fontsize=10)  # 添加轴标签
    bgraghic.set_ylabel('y轴', fontsize=20)
    bgraghic.plot(bx, by, 'r^')

    plt.pause(0.1)         # 暂停一秒
plt.ioff()             # 关闭画图的窗口
plt.show()
