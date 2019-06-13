from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import re


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        # 开始标签
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        # 结束标签
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        # 数据
        print(data.replace(' ', '.').replace('\n', r'\n'))

    def handle_comment(self, data):
        # 注释
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        # 特殊字符 英文表示的&nbsp;
        print('&%s;' % name)

    def handle_charref(self, name):
        # 特殊字符 数字表示的&#1234;
        print('&#%s;' % name)


parser = MyHTMLParser()
# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


class PythonHTMLParser(HTMLParser):
    '找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，'
    '然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点'

    def __init__(self):
        super().__init__()
        self.parsedata = ""  # 设置一个标志位

    def handle_starttag(self, tag, attrs):
        # attrs是元组的list集合[(,),(,)]
        # 开始标签
        if ("class", "event-title")in attrs:
            self.parsedata = "name"
        if tag == "time":
            self.parsedata = "time"
        if tag == "span" and ("class", "say-no-more") in attrs:
            self.parsedata = "year"
        if tag == "span" and ("class", "event-location") in attrs:
            self.parsedata = "location"

    def handle_endtag(self, tag):
        # 结束标签
        self.parsedata = ""

    def handle_data(self, data):
        # 数据
        if self.parsedata == "name":
            print("会议名称:", data)
        if self.parsedata == "location":
            print("会议地点:", data)
            print("——"*30)
        if self.parsedata == "time":
            print("会议月份:", data)
        if self.parsedata == "year" and re.match(r"\d{4}", data):
            print("会议年份:", data.strip())


with request.urlopen("https://www.python.org/events/python-events/") as f:
    data = f.read()
    PythonHTMLParser().feed(data.decode("utf-8"))
