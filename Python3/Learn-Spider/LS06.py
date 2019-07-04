#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/4 15:22
# @Author      ：Falling Stars
# @FileName    ：LA06
# @Software    ：PyCharm
# @Description ：requests库操作cookies
import requests


def LS06_1():
    """
    上传文件
    :return:
    """
    files = {'file': open('README.md', 'rb')}
    r = requests.post('http://httpbin.org/post', files=files)
    print(r.text)


def LS06_2():
    r = requests.get('https://www.baidu.com')
    print(r.cookies)
    for key, value in r.cookies.items():
        print(key + '=' + value)


COOKIES = '_zap=7ae8adba-9598-42b1-9e15-db74b9861933; d_c0="ADAt-yRVlQ-PTtaM38YAFOirorMspisyDUY=|1560499578"; q_c1=42525ea515a14ef7a36ce4406454d9a4|1560499581000|1560499581000; _xsrf=gLuozUvACzQYogkatomGdoPBgDnVFv6a; l_n_c=1; l_cap_id="NzZkMjBkOTJmMzc4NGZmZmIwMDZmZjkyOTk0ODdhZTE=|1562224420|9b7d6d9ee24ec1ad6f7e7308d917ac39f2cc41ee"; r_cap_id="YWY0Y2VlZDQ2NWZhNDMxNTkwM2JlN2E2YWI0ZDBiYjU=|1562224420|9cc8f0cb22020467ef0e1eba0c5ef577e0a1fe49"; cap_id="OWVjMWZlM2JmMmI5NGU3ODgxZWI2NGQwNDlkN2I5NDc=|1562224420|56bcd7f8b8c45d6663922c5749ccbbdbcbc10226"; n_c=1; __utma=51854390.775877279.1562224434.1562224434.1562224434.1; __utmb=51854390.0.10.1562224434; __utmc=51854390; __utmz=51854390.1562224434.1.1.utmcsr=germey.gitbooks.io|utmccn=(referral)|utmcmd=referral|utmcct=/python3webspider/content/3.2.1-%E5%9F%BA%E6%9C%AC%E4%BD%BF%E7%94%A8.html; __utmv=51854390.000--|3=entry_date=20190614=1; tgw_l7_route=4860b599c6644634a0abcd4d10d37251; capsion_ticket="2|1:0|10:1562225707|14:capsion_ticket|44:MTQ5M2YwMWQzNTY3NGQ2YzhkMmM4NTA1YjJmOTU3ZjI=|c7df1c82080b1035fc17bef8794e74be6f326184d80068733b595448cf4cfca1"; z_c0="2|1:0|10:1562225719|4:z_c0|92:Mi4xcWxSLUFnQUFBQUFBTUMzN0pGV1ZEeVlBQUFCZ0FsVk5OX29LWGdCS25qWHFRWkJVQ3BfajNDZVowckI3b1RhVGhB|fde8accce065985f50277bbbc60077240c9ee8997296be70ddeed270196bda26"; unlock_ticket="ABBKmcdTVQkmAAAAYAJVTT-zHV0XHjaNQQDK1l-8v1InGUePHiwkOA=="; tst=r'
USERAGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'


def LS06_3():
    """使用cookie访问知乎"""
    headers = {
        'Cookie': COOKIES,
        'Host': 'www.zhihu.com',
        'User-Agent': USERAGENT,
    }
    r = requests.get('https://www.zhihu.com', headers=headers)
    print(r.text)


def LS06_4():
    """构造RequestsCookieJar对象，访问知乎"""
    jar = requests.cookies.RequestsCookieJar()
    for cookie in COOKIES.split(';'):
        key, value = cookie.split('=', 1)
        jar.set(key, value)

    headers = {
        'Host': 'www.zhihu.com',
        'User-Agent': USERAGENT
    }

    r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
    print(r.text)


def LS06_5():
    response = requests.get('https://www.12306.cn')
    print(response.status_code)
    print(response.content.decode('utf-8'))


if __name__ == "__main__":
    # LS06_1()
    # LS06_2()
    # LS06_3()
    # LS06_4()
    LS06_5()
