import jieba

# jieba：第三方python 中文分词组件，GitHub：https://github.com/fxsjy/jieba
# jieba分词组件特点：支持三种分词模式；支持繁体字分词；支持自定义词典；MIT授权协议

# jieba.cut 方法接受三个输入参数: 需要分词的字符串；cut_all 参数用来控制是否采用全模式；HMM 参数用来控制是否使用 HMM 模型
# jieba.cut_for_search 方法接受两个参数：需要分词的字符串；是否使用 HMM 模型。该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细
# 待分词的字符串可以是 unicode 或 UTF-8 字符串、GBK 字符串。注意：不建议直接输入 GBK 字符串，可能无法预料地错误解码成 UTF-8
# jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的 generator，可以使用 for 循环来获得分词后得到的每一个词语(unicode)
# 用jieba.lcut 以及 jieba.lcut_for_search 直接返回 list
# jieba.Tokenizer(dictionary=DEFAULT_DICT) 新建自定义分词器，可用于同时使用不同词典。jieba.dt 为默认分词器，所有全局分词相关函数都是该分词器的映射。

# jieba三种分词模式
word = "我来到北京清华大学"

# 全模式：把句子中所有的可以成词的词语都扫描出来，速度非常快，但不能解决歧义
seg_list = jieba.cut(word, cut_all=True)
print("【全模式】："+"|".join(seg_list))

# 精确模式：试图将句子最精确地切开，适合文本分析，默认模式
seg_list = jieba.cut(word, cut_all=False)
print("【精确模式】："+"|".join(seg_list))
seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print("【精确模式】："+"|".join(seg_list))

# 搜索引擎模式：在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词
seg_list = jieba.cut_for_search(word)
print("【精确模式】："+"|".join(seg_list))

# 使用自定义词典
print("----"*20)
jieba.load_userdict("Learn/File/userdict.txt")  # 载入词典
# 在程序中动态修改词典
jieba.add_word('石墨烯')  # 添加词
jieba.add_word('凱特琳')
jieba.del_word('自定义词')  # 删除词
test_sent = (
    "李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
    "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
    "「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
)
words = jieba.cut(test_sent)
print("|".join(words))
print("----"*20)
# 使用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来
print('|'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
jieba.suggest_freq(('中', '将'), True)
print('|'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
print('|'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
jieba.suggest_freq('台中', True)
print('|'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))

print("----"*20)
# Tokenize：返回词语在原文的起止位置
# 输入参数只接受 unicode
result = jieba.tokenize(u'永和服装饰品有限公司')  # 默认模式
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0], tk[1], tk[2]))
print("----"*20)
result = jieba.tokenize(u'永和服装饰品有限公司', mode='search')  # 搜索模式
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0], tk[1], tk[2]))
