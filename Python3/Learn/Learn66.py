# poplib收邮件
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib


def print_info(msg, index=0):
    if index == 0:  # index用于缩进显示
        # 遍历获取发件人、收件人、主题
        for header in ["From", "To", "Subject"]:
            # 获取相应的内容
            value = msg.get(header, '')
            if value:
                if header == "Subject":
                    value = decode_str(value)  # 解码主题
                else:
                    hdr, addr = parseaddr(value)  # parseaddr：解析在字符串中的email地址
                    name = decode_str(hdr)  # 解码主题
                    value = u"%s <%s>" % (name, addr)
                print("%s%s: %s" % (' '*index, header, value))
    # 如果消息由多个部分组成，则返回true
    if msg.is_multipart():
        # 返回list，包含所有的子对象
        parts = msg.get_payload()
        # enumerate将其组成一个索引序列，利用可以同样获取索引和值
        for n, part in enumerate(parts):
            # 打印消息模块
            print("%spart %s" % (' '*index, n))
            # 打印分割符号
            print("%s-------------------" % (' '*index))
            # 递归打印
            print_info(part, index+1)
    else:
        # 递归结束条件，
        content_type = msg.get_content_type()  # 返回消息的内容类型
        if content_type == "text/plain" or content_type == "text/html":
            content = msg.get_payload(decode=True)  # 返回list，包含所有的子对象，开启解码
            # 猜测字符集
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print("%sText: %s" % (" "*index, content+"..."))
        else:
            print("%sAttachment:%s" % (' '*index, content_type))


def decode_str(s):
    # 邮件的Subject或者Email所包括的名字都是经过编码之后的str，要正常显示，就必须decode
    value, charset = decode_header(s)[0]  # 在不转回字符的情况下解码消息头值，返回一个list
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    charset = msg.get_charset()  # 获取字符集
    if charset is None:
        content_type = msg.get("Content-Type", "").lower()
        # find:检测字符串中是否包含子字符串
        pos = content_type.find("charset=")  # 返回 charset= 头字符的位置
        if pos >= 0:
            # 移除字符串头尾指定的字符串
            charset = content_type[pos+8:].strip()
    return charset


# 邮箱SMTP服务器
pop_server = "pop.qq.com"
# 收件人邮箱
to_addr = "1399237176@qq.com"
# 授权码
password = "osdasxnimdavhffi"

# 连接到POP3服务器
server = poplib.POP3(pop_server)
server.set_debuglevel(1)
print(server.getwelcome().decode("utf-8"))

# 身份认证
server.user(to_addr)
server.pass_(password)

# stat() 返回邮件数量和占用空间
print("Message:%s. Size:%s" % server.stat())
# list[]返回所有邮件的编号
resp, mails, octets = server.list()
print("编号列表")
print(mails)

# 获取最新一封邮件，索引是从1开始
index = len(mails)
resp, lines, octets = server.retr(index-15)  # 获取最新一封邮件
# lines存储了原始文本的每一行，可以获取整个邮件的原始文本
msg_content = b"\r\n".join(lines).decode("utf-8")
msg = Parser().parsestr(msg_content)

print_info(msg)

# 可以根据邮件索引号直接从服务器删除邮件
# server.dele(index)
# 关闭连接
server.quit()
