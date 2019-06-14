# PIL模块图像缩放、切片、旋转、滤镜、输出文字、调色板
import random
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

# 获取根目录路径
root_dir = os.getcwd()
# print(root_dir)
data_dir = os.path.join(root_dir, "Python3/Learn/File")
# print(data_dir)
# 打开一个jpg图像
im = Image.open(os.path.join(data_dir, "timg.jpg"))
# 获取图像尺寸
w, h = im.size
print(w, h)
im.thumbnail((w//2, h//2))  # 缩放图片
im.filter(ImageFilter.BLUR)  # 应用滤镜
#im.save("Bigtimg.jpg", "jpeg")
im.show()


def rndChar():
    return chr(random.randint(65, 90))


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60*4
height = 60
image = Image.new("RGB", (width, height), (255, 255, 255))  # 画板
font = ImageFont.truetype(r'C:\Windows\Fonts\ahronbd.ttf', 36)  # 加载字体
draw = ImageDraw.Draw(image)  # 获取画笔
for x in range(width):
    for y in range(height):
        # 画点
        draw.point((x, y), fill=rndColor())

for t in range(4):
    # 写字
    draw.text((60*t+10, 10), rndChar(), font=font, fill=rndColor2())

image.show()
