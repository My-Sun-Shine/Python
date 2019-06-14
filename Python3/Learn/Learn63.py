import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))


from_addr = "1399237176@qq.com"
password = "osdasxnimdavhffi"
to_addr = "1399237176@qq.com"
smtp_server = "smtp.qq.com"

# 发生文本
# msg = MIMEText("Hello,World.................Python")
# 发生HTML邮箱
msg = MIMEText('<html><body><h1>Hello</h1>' +
               '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
               '</body></html>', 'html', 'utf-8')

msg["From"] = _format_addr("Python爱好者<%s>" % from_addr)
msg["To"] = _format_addr("管理员<%s>" % to_addr)
msg["Subject"] = Header("来自SMTP的问候....", "utf-8").encode()


server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口为25
server.set_debuglevel(1)  # 打印和SMTP服务器交互的所有信息
server.login(from_addr, password)
# as_string() 把MIMEText对象变成字符串
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
