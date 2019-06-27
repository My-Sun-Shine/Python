from fontTools.ttLib import TTFont
# 解析字体文件，获取字体映射关系

font1 = TTFont('Learn-A/File/f1c26632.woff')
def parse_font():
    global font1
    font1.saveXML('woff4.xml')
    keys, values = [], []
    for k, v in font1.getBestCmap().items():
        print(k, v, '\n')  # k为10进制 v为unif51e
        if v.startswith('uni'):
            keys.append(eval("u'\\u{:x}".format(k) + "'"))
            values.append(chr(int(v[3:], 16)))# 去掉uni
        else:
            keys.append("&#x{:x}".format(k))
    print(dict(zip(keys, values)))
    glyphs = font1.getGlyphOrder()[2:]
    tmp_dic = {}
    for num, un_size in enumerate(glyphs):
        # print(un_size,num)
        font_uni = int(un_size.replace('uni', '0x').lower(), 16)
        tmp_dic[font_uni] = un_size
    print(tmp_dic)


if __name__ == "__main__":
    parse_font()
