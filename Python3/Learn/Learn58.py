from turtle import *


def drawStar(x, y):
    # 画五角星
    pu()  # 画笔抬起，移动时不划线
    goto(x, y)  # 前往定位
    pd()  # 画笔落下，移动时划线
    # set heading: 0
    seth(0)  # 设置朝向，0为东
    for i in range(5):
        fd(40)  # 前进
        rt(144)  # 转动角度


for x in range(0, 250, 50):
    drawStar(x, 0)

done()
