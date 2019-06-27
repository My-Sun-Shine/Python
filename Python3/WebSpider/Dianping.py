# -*- coding:utf-8 -*-

"""
@title: 爬取大众点评数据，其中三个方法来自https://github.com/Northxw/Python3_WebSpider
@author: 
"""

import re
import requests
from bs4 import BeautifulSoup  # 分析HTML
import lxml.html
from xml.dom import minidom
import xml.sax as sax
from lxml import etree
# 字体反爬所用的css文件链接和svg文件链接，可能都会有变化，可以查看Python 爬虫-字体数字反爬笔记
CSS_URL = "http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/730ea64068ac685fcc153e58ef62f96b.css"
SVG_NUM_URL = "http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/282ddfdfb214b515c0fe580b90d30c62.svg"
SVG_FONT_URL1 = "http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/648b743e32160d30da90cd1b41014dbd.svg"
SVG_FONT_URL2 = "http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/bd4a1826c0f3503a31f7f4fa4685af11.svg"
# 这个是针对字体使用网站自定义字体，进行破解
WOFF_URL = 'http://s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/f1c26632.woff'
FONT_DICT = {58739: '1', 58275: '2', 63321: '3', 63537: '4', 58042: '5', 59755: '6', 59348: '7', 63702: '8', 60197: '9', 61011: '0',
             62903: '店', 61518: '中', 63181: '美', 59539: '家', 59383: '馆', 57593: '小', 61793: '车', 62322: '大', 58233: '市', 57482: '公',
             59810: '酒', 62998: '行', 57734: '国', 61225: '品', 60657: '发', 60773: '电', 59620: '金', 61618: '心', 60693: '业', 58140: '商',
             61343: '司', 60034: '超', 59023: '生', 59562: '装', 60387: '园', 63170: '场', 63365: '食', 58009: '有', 58790: '新', 58875: '限',
             58628: '天', 63098: '面', 62920: '工', 58598: '服', 62516: '海', 59184: '华', 59989: '水', 61641: '房', 61154: '饰', 59032: '城',
             62627: '乐', 61952: '汽', 60381: '香', 60258: '部', 61800: '利', 63559: '子', 61099: '老', 63225: '艺', 62218: '花', 61533: '专',
             59833: '东', 62355: '肉', 59651: '菜', 62537: '学', 60746: '福', 61619: '饭', 62026: '人', 63102: '百', 60945: '餐', 62743: '茶',
             58187: '务', 61155: '通', 57891: '味', 60055: '所', 62980: '山', 59661: '区', 60645: '门', 59252: '药', 63534: '银', 61972: '农',
             61870: '龙', 60107: '停', 59488: '尚', 63687: '安', 57580: '厂', 59287: '鑫', 61387: '一', 61720: '容', 60788: '动', 57909: '南',
             60570: '具', 57444: '源', 58301: '兴', 58736: '鲜', 62398: '记', 58825: '时', 62864: '机', 57423: '烤', 58455: '文', 58398: '康',
             62123: '信', 59745: '果', 58779: '阳', 63299: '理', 60115: '锅', 62520: '宝', 60756: '达', 63489: '地', 62900: '儿', 63659: '衣',
             62399: '特', 58549: '产', 61501: '西', 59349: '批', 59050: '坊', 63241: '州', 61753: '牛', 58820: '佳', 61640: '化', 61642: '五',
             58061: '米', 61212: '修', 57697: '爱', 60132: '北', 58681: '养', 58923: '卖', 60430: '建', 63320: '材', 63593: '三', 62133: '会',
             62229: '鸡', 61006: '室', 62691: '红', 62634: '站', 58897: '德', 59604: '王', 61732: '光', 59248: '名', 61310: '丽', 59662: '油',
             58120: '院', 60175: '堂', 60548: '烧', 60133: '江', 57611: '社', 57708: '合', 63414: '星', 59470: '货', 60364: '型', 61414: '村',
             57885: '自', 61777: '科', 58664: '快', 63669: '便', 60154: '日', 62860: '民', 59658: '营', 60814: '和', 58146: '活', 59694: '童',
             59011: '明', 60597: '器', 62899: '烟', 62374: '育', 63200: '宾', 59485: '精', 58856: '屋', 63543: '经', 61022: '居', 58694: '庄',
             61041: '石', 63394: '顺', 62720: '林', 59120: '尔', 60728: '县', 61297: '手', 61358: '厅', 63370: '销', 63315: '用', 61774: '好',
             59578: '客', 57440: '火', 61663: '雅', 59075: '盛', 58451: '体', 58184: '旅', 61435: '之', 63674: '鞋', 58111: '辣', 60370: '作',
             59467: '粉', 60820: '包', 63696: '楼', 58729: '校', 60114: '鱼', 63119: '平', 60417: '彩', 60435: '上', 61442: '吧', 61939: '保',
             58033: '永', 60476: '万', 63269: '物', 59224: '教', 57377: '吃', 62209: '设', 59154: '医', 60239: '正', 62750: '造', 63698: '丰',
             58832: '健', 61129: '点', 62001: '汤', 60789: '网', 57538: '庆', 61635: '技', 59195: '斯', 58573: '洗', 60245: '料', 61502: '配',
             61599: '汇', 61122: '木', 62017: '缘', 62034: '加', 60942: '麻', 60563: '联', 59187: '卫', 59591: '川', 60692: '泰', 60142: '色',
             61804: '世', 57798: '方', 63133: '寓', 62170: '风', 58853: '幼', 60881: '羊', 62612: '烫', 62508: '来', 60194: '高', 60066: '厂',
             58418: '兰', 62231: '阿', 58703: '贝', 59602: '皮', 62191: '全', 57934: '女', 62783: '拉', 61731: '成', 60101: '云', 60267: '维',
             60444: '贸', 59308: '道', 63508: '术', 59466: '运', 58916: '都', 62000: '品', 60694: '博', 58287: '河', 59623: '瑞', 58592: '宏',
             59161: '京', 61987: '际', 57572: '路', 57876: '祥', 57791: '青', 59144: '镇', 57770: '厨', 63235: '培', 57893: '力', 63710: '惠',
             58734: '连', 62441: '马', 62501: '鸿', 58579: '钢', 60129: '训', 62677: '影', 62067: '甲', 61834: '助', 60375: '窗', 60628: '布',
             59980: '富', 57916: '牌', 61765: '头', 62795: '四', 63162: '多', 58229: '妆', 62219: '吉', 57806: '苑', 58826: '沙', 61812: '恒',
             61081: '隆', 58024: '春', 59440: '干', 63064: '饼', 58106: '氏', 59495: '里', 58411: '二', 60307: '管', 63730: '诚', 59920: '制',
             60441: '售', 62469: '嘉', 59933: '长', 59747: '轩', 61015: '杂', 63103: '副', 61696: '清', 61728: '计', 60336: '黄', 61965: '讯',
             63095: '太', 60917: '鸭', 61721: '号', 62074: '街', 57550: '交', 62354: '与', 57431: '叉', 59876: '附', 58283: '近', 63336: '层',
             60929: '旁', 60074: '对', 61475: '巷', 62738: '栋', 62935: '环', 59619: '省', 62300: '桥', 58211: '湖', 60997: '段', 61838: '乡',
             63459: '厦', 60329: '府', 58695: '铺', 59071: '内', 58470: '侧', 63041: '元', 59225: '购', 62671: '前', 63307: '幢', 63326: '滨',
             63232: '处', 61448: '向', 60324: '座', 62991: '下', 62284: '県', 62944: '凤', 63377: '港', 62488: '开', 62633: '关', 59817: '景',
             63314: '泉', 57595: '塘', 59691: '放', 61554: '昌', 58591: '线', 60090: '湾', 57496: '政', 63247: '步', 63033: '宁', 59648: '解',
             57644: '白', 61201: '田', 58195: '町', 62134: '溪', 62025: '十', 61737: '八', 61277: '古', 62386: '双', 59962: '胜', 62418: '本',
             59656: '单', 61935: '同', 60270: '九', 60457: '迎', 63277: '第', 60562: '台', 57847: '玉', 59911: '锦', 60399: '底', 57433: '后',
             62196: '七', 58103: '斜', 59806: '期', 60325: '武', 63673: '岭', 58352: '松', 59216: '角', 58032: '纪', 60785: '朝', 61296: '峰',
             62567: '六', 61002: '振', 59276: '珠', 61391: '局', 63002: '岗', 59966: '洲', 58891: '横', 60742: '边', 62438: '济', 60265: '井',
             62716: '办', 62022: '汉', 61087: '代', 61417: '临', 62140: '弄', 62578: '团', 59289: '外', 62579: '塔', 60846: '杨', 62763: '铁',
             58163: '浦', 63560: '字', 63092: '年', 62007: '岛', 60167: '陵', 60254: '原', 61278: '梅', 62269: '进', 58391: '荣', 63188: '友',
             61686: '虹', 58113: '央', 61817: '桂', 57420: '沿', 63577: '事', 60627: '津', 60080: '凯', 62375: '莲', 62838: '丁', 59938: '秀',
             63091: '柳', 62467: '集', 57803: '紫', 59001: '旗', 57744: '张', 61561: '谷', 61460: '的', 60981: '是', 62316: '不', 63281: '了',
             63369: '很', 63733: '还', 60877: '个', 61119: '也', 63564: '这', 60805: '我', 59592: '就', 60432: '在', 60262: '以', 60740: '可',
             58362: '到', 58541: '错', 60813: '没', 60960: '去', 62512: '过', 62378: '感', 62849: '次', 60656: '要', 58730: '比', 60007: '觉',
             61477: '看', 61908: '得', 58824: '说', 61158: '常', 61206: '真', 59309: '们', 63106: '但', 61168: '最', 58536: '喜', 61009: '哈',
             59825: '么', 63562: '别', 60829: '位', 61090: '能', 58314: '较', 61273: '境', 63403: '非', 63145: '为', 57677: '欢', 59210: '然',
             58349: '他', 57414: '挺', 60769: '着', 62766: '价', 57717: '那', 58901: '意', 61282: '种', 60156: '想', 59030: '出', 63361: '员',
             61121: '两', 62318: '推', 60632: '做', 63111: '排', 62951: '实', 61736: '分', 61629: '间', 59887: '甜', 60800: '度', 59995: '起',
             60169: '满', 60924: '给', 62798: '热', 61833: '完', 62863: '格', 61519: '荐', 61749: '喝', 63113: '等', 57839: '其', 60159: '再',
             57925: '几', 60609: '只', 58623: '现', 59614: '朋', 62869: '候', 59550: '样', 59493: '直', 59939: '而', 61835: '买', 62729: '于',
             59664: '般', 57679: '豆', 59706: '量', 63191: '选', 61655: '奶', 62533: '打', 57741: '每', 59508: '评', 61627: '少', 62311: '算',
             60216: '又', 57555: '因', 58884: '情', 60097: '找', 61823: '些', 58819: '份', 57606: '置', 62663: '适', 62241: '什', 59603: '蛋',
             59290: '师', 60280: '气', 61917: '你', 62146: '姐', 59791: '棒', 63150: '试', 62267: '总', 60179: '定', 59945: '啊', 61617: '足',
             63473: '级', 60188: '整', 57769: '带', 61102: '虾', 61527: '如', 61455: '态', 63015: '且', 60647: '尝', 57974: '主', 58434: '话',
             62382: '强', 57848: '当', 59407: '更', 57939: '板', 61362: '知', 63190: '己', 58205: '无', 58596: '酸', 61464: '让', 59107: '入',
             60790: '啦', 59742: '式', 61019: '笑', 59894: '赞', 57476: '片', 58180: '酱', 61547: '差', 58210: '像', 60661: '提', 58121: '队',
             59234: '走', 62785: '嫩', 59675: '才', 60282: '刚', 63555: '午', 60546: '接', 62461: '重', 59453: '串', 59125: '回', 57666: '晚',
             57430: '微', 62573: '周', 63115: '值', 58126: '费', 61062: '性', 59520: '桌', 61007: '拍', 62898: '跟', 62403: '块', 61634: '调',
             63686: '糕'}
# 数据头文件
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_lxsdk_cuid=16b8d23243bc8-0267b092299ad5-3e385c0c-100200-16b8d23243cc8; _lxsdk=16b8d23243bc8-0267b092299ad5-3e385c0c-100200-16b8d23243cc8; _hc.v=68f51e89-25eb-d3f0-e029-71aa2a804705.1561441019; cy=3; cye=hangzhou; s_ViewType=10',
    'Host': 'www.dianping.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

# 函数的具体分析查看Python 爬虫-字体数字反爬笔记


def get_coordinate_value(css_url, class_):
    """
    处理class, 获取坐标值
    """
    css_html = requests.get(css_url).text
    info_css = re.findall(
        r'%s{background:-(\d+).0px -(\d+).0px' % class_, css_html, re.S)[0]
    return info_css


def get_completed_nums(svg_num_url, css_url, class_list):
    """
    处理数字
    """
    completed_nums = ''
    result_svg = requests.get(svg_num_url).text
    # svg页面源码中text标签内的文本值 # 示例a：56422383356911691085268889707857...
    a, b, c = re.findall('y=.*?>(.*?)<', result_svg, re.S)
    # text标签内的y属性值 # 示例: 46, 83, 129
    y1, y2, y3 = re.findall('y="(.*?)">', result_svg, re.S)
    # 字体大小 # 示例：x = 12,......
    divisor = eval(re.search('x="(\d{2}) ', result_svg, re.S).group(1))
    for class_ in class_list:
        x, y = get_coordinate_value(css_url, class_)
        x, y = int(x), int(y)
        if y < int(y1):
            completed_nums += a[x // divisor]
        elif y < int(y2):
            completed_nums += b[x // divisor]
        elif y < int(y3):
            completed_nums += c[x // divisor]
    return completed_nums


def get_completed_font_425(svg_font_url, css_url, class_list):
    """
    处理文字
    - 2019/4/25 测试期间规律：svg源码中通过y确定偏移字体所在文本行, 然后通过text[x//divisor]获取正常字符
    """
    completed_font = ''
    svg_font_text = re.sub('<\?xml.*?\?>', '', requests.get(svg_font_url).text)
    # 获取y、text值组成的元组列表
    y_text_list = re.findall('y="(.*?)">(.*?)<', svg_font_text, re.S)
    divisor = eval(re.search('font-size:(\d+)px',
                             svg_font_text, re.S).group(1))
    for class_ in class_list:
        # class对应坐标值
        x, y = get_coordinate_value(css_url, class_)
        x, y = int(x), int(y)
        # 获取当前class对应文字所在文本行
        class_text = [tup[-1] for tup in y_text_list if y < int(tup[0])][0]
        # 根据偏移量获取最终需要的文字
        target_text = class_text[x // divisor]
        completed_font += target_text
    return completed_font


def get_font(data_list, svg_font_url):
    """
    解析中文
    """
    if len(data_list) == 0:
        return ''
    content = etree.tostring(
        data_list[0], method='xml', encoding="utf-8").decode('UTF-8', 'strict')
    61696
    for data in data_list[0]:
        class_list = []
        class_data = data.get("class")
        class_list.append(class_data)
        data = get_completed_font_425(svg_font_url, CSS_URL, class_list)
        content = content.replace('<svgmtsi class="%s"/>' % class_data, data)
    content = content.replace('<span class="addr">', '').replace('</span>', '')
    content = content.replace('<span class="tag">', '').replace('</span>', '')
    return content.strip()
    # re.sub("\D", '', content)


def get_nums(data_list):
    """
    解析数字
    """
    if len(data_list) == 0:
        return ''
    content = etree.tostring(
        data_list[0], method='xml', encoding="utf-8").decode('UTF-8', 'strict')
    # print(content)
    for data in data_list[0]:
        class_list = []
        class_data = data.get("class")
        class_list.append(class_data)
        data = get_completed_nums(SVG_NUM_URL, CSS_URL, class_list)
        content = content.replace('<svgmtsi class="%s"/>' % class_data, data)
    # print(re.sub("\D", '', content))
    return re.sub("\D", '', content)


def parse_data(text):
    """
    解析数据
    """
    selector = etree.HTML(text)
    li_list = selector.xpath('//*[contains(@class, "shop-all-list")]/ul/li')
    data = []
    for li in li_list:
        txt_tit = li.xpath(
            './div[contains(@class, "txt")]/div[contains(@class, "tit")]/a')[0]
        pic_img = li.xpath('./div[contains(@class, "pic")]/a/img')[0]
        txt_comment = li.xpath(
            './div[contains(@class, "txt")]/div[contains(@class, "comment")]')[0]
        txt_addr = li.xpath(
            './div[contains(@class, "txt")]/div[contains(@class, "tag-addr")]')[0]
        _data = {
            # 店铺名称
            "name": txt_tit.xpath('./h4/text()')[0],
            # 店铺链接
            "shop_detail_url": txt_tit.xpath('./@href')[0],
            # 店铺封面
            "img": pic_img.xpath('./@src')[0].split('%')[0] if pic_img.xpath('./@src') != '' else pic_img.xpath('./@data-src')[0].split('%')[0],
            # 星级
            "stars": txt_comment.xpath('./span/@title')[0],
            # 评论数
            "comments": get_nums(txt_comment.xpath('./a[contains(@class,"review-num")]/b')),
            # 人均价
            "price": get_nums(txt_comment.xpath('./a[contains(@class,"mean-price")]/b')),
            # 详细地址
            "addr_detail": get_font(txt_addr.xpath('./span[contains(@class,"addr")]'), SVG_FONT_URL2),
            # 类型
            "type": get_font(txt_addr.xpath('./a')[0].xpath('./span[contains(@class,"tag")]'), SVG_FONT_URL1),
            # 地址
            "addr": get_font(txt_addr.xpath('./a')[1].xpath('./span[contains(@class,"tag")]'), SVG_FONT_URL1)
        }
        print(_data)
        print("----"*30)


def get_font_w(data_list):
    """
    data_list:数据，woff_url字体链接
    """
    if len(data_list) == 0:
        return ''
    # content = etree.tostring(data_list.xpath('./span')[0], method='html')
    content = '<svgmtsi class="tagName">&#xf4c7;</svgmtsi><svgmtsi class="tagName">&#xebcc;</svgmtsi>'
    # 例如 <svgmtsi class="tagName">&#xf4c7;</svgmtsi><svgmtsi class="tagName">&#xebcc;</svgmtsi>
    content = str(content).replace('&#', '0')
    # 例如 <svgmtsi class="tagName">62663;</svgmtsi><svgmtsi class="tagName">60364;</svgmtsi>
    for key in FONT_DICT.keys():
        key_16 = hex(key)
        initstr = str(key_16) + ';'
        content = content.replace(initstr, str(FONT_DICT[key]))
    # <svgmtsi class="tagName">适</svgmtsi><svgmtsi class="tagName">型</svgmtsi>
    print(content)


if __name__ == '__main__':
    res = requests.get("https://www.dianping.com/xian/ch0", headers=HEADERS)
    print(res.status_code)
    parse_data(res.text)
    # get_font_w("a")
