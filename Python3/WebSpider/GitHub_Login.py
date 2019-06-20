# -*- coding:utf-8 -*-

"""
@title: 模拟GitHub登录
@author: 
"""

import requests
from lxml import etree


class Login(object):
    def __init__(self):
        '初始化类'
        self.headers = {
            'Host': 'github.com',  # 主机号
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Referer': 'https://github.com'  # 刷新地址
        }
        self.login_url = 'https://github.com/login'  # 登录地址
        self.post_url = 'https://github.com/session'  # 把登录信息提交地址
        self.logined_url = 'https://github.com/settings/profile'  # GitHub设置页面
        # 维持会话，处理Cookies, 同一个Session实例发出的所有数据的请求都保持一个cookie，而request模块每次都会自动处理cookie
        self.session = requests.Session()

    def token(self):
        # 获取隐藏在源码中的authenticity_token值.
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        # 获取authenticity_token的值 任意标签属性id="login"下的form标签下的第二个input标签的value属性
        token = selector.xpath('//*[@id="login"]/form/input[2]/@value')
        # token = selector.xpath('//*[@class="auth-form px-3"]/form/input[@type="hidden"]/@value')[1]
        print(token)
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            # ✓ 可在"xpath('//*[@id="login"]/form/input[1]/@value')" 位置复制粘贴
            'utf8': '✓',
            # 获取隐藏在源码中的authenticity_token值.
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        response = self.session.post(
            self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)

        # 保持登录的情况下
        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def dynamics(self, html):
        selector = etree.HTML(html)
        # contains()方法定位，也叫模糊定位  xpath = "//标签名[contains(@属性, '属性值')]"
        dynamics = selector.xpath(
            '//div[contains(@class, "news")]/div')  # 获取动态信息的div标签(需要处理)
        # print(len(dynamics))  # 有四个div 其中有两个是加载时显示的div,F12调试中找不到，但是获取的HTML中有
        for item in dynamics:
            value = item.xpath('./@class')      # 获取标签的class属性值, 如果没在列表, 则不做处理
            # print(value)
        repositories = selector.xpath('//ul[@class="list-style-none"]/li')
        print("存储库列表:")
        for item in repositories:
            value = item.xpath('./div/a/span')
            print(item.get("class"), value[0].get(
                "title"), "/", value[1].get("title"))

    def profile(self, html):
        selector = etree.HTML(html)
        name = selector.xpath(
            '//input[@id="user_profile_name"]/@value')    # 获取用户名称
        email = selector.xpath(
            '//select[@id="user_profile_email"]/option[@value!=""]/text()')
        print("name:", name, "email:", email)


if __name__ == "__main__":
    login = Login()
    login.login(email="1399237176@qq.com", password='mss1399237176')
