# struct模块解决bytes和其他二进制数据类型转换
import base64
import struct
# pack函数把任意类型变成bytes
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
print(struct.pack(">I", 10240099))  # b'\x00\x9c@c'
print(struct.pack("I", 10240099))

# unpack就是把bytes转为任意类型
# >IH 就是把bytes依次变成I(4字节无符号整数)和H(2字节无符号整数)
print(struct.unpack(">IH", b'\xf0\xf0\xf0\xf0\x80\x80'))

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack("<ccIIIIIIHH", s))  # c(一字节的char型)
# (b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)是window位图，大小为640*360 颜色数为24
# BM表示window位图,BA表示OS/2位图；一个4字节整数表示位图大小；一个4字节整数保留位，始终=0；一个4字节整数:时间图像的偏移量
# 一个4字节整数：Header的字节数；一个4字节整数：图像宽度；一个4字节整数：图像高度；一个2字节整数：始终为1；一个2字节整数：颜色数


bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
print(bmp_data)
# 读取前30个字节
# (b'B', b'M', 616, 0, 54, 40, 28, 10, 1, 16)
print(struct.unpack("<ccIIIIIIHH", bmp_data[:30]))
