import jieba


def show(cut_text):
    """
    制作中文词云
    :return: None
    """
    from wordcloud import WordCloud
    import cv2
    import matplotlib.pyplot as plt
    stopwords = {'这些': 0, '那些': 0, '因为': 0, '所以': 0, "哪里": 0}  # 噪声词
    # 文本
    cloud = WordCloud(
        # 设置字体，不指定就会出现乱码
        font_path="Learn/File/FZSTK.TTF",
        # 设置背景色
        background_color='black',
        # 词云形状
        mask=None,
        # 允许最大词汇
        max_words=2000,
        # 最大号字体
        max_font_size=50,
        stopwords=stopwords  # 过滤噪声词
    )
    wCloud = cloud.generate(cut_text)
    wCloud.to_file('Learn/File/cloud.jpg')

    plt.imshow(wCloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def data(words):
    counts = {}
    for word in words:
        if len(word) == 1:  # 单个字不算
            continue
        else:
            counts[word] = counts.get(word, 0)+1
    items = list(counts.items())  # 将键值对转换成列表
    items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序
    for i in range(20):
        word, count = items[i]
        print("{0:<5}{1:>5}".format(word, count))


if __name__ == "__main__":
    url1 = "Learn\File\红楼梦.txt"
    url2 = "Learn\File\西游记.txt"
    url3 = "Learn\File\水浒传.txt"
    url4 = "Learn\File\三国演义.txt"
    with open(url1, "r", encoding="utf-8") as f:
        txt = f.read()
        words = jieba.lcut(txt)
        data(words)
        show(" ".join(words))
