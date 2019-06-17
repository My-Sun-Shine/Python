# 发送可以显示图片在邮件内容的邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


# 邮箱SMTP服务器
smtp_server = "smtp.qq.com"
# 发件人邮箱
from_addr = "1399237176@qq.com"
# 授权码
password = "osdasxnimdavhffi"
# 收件人邮箱列表
to_addr = ["1399237176@qq.com", "1224758579@qq.com"]

# 邮件标题
mail_title = "MXW的邮件"

# 邮件正文 send_image为图片引用的ID
mail_content = """
 <p>你好，Python 邮件发送测试...</p>
 <p>这是使用python登录qq邮箱发送HTML格式和图片的测试邮件：</p>
 <p><a href='http://www.yiibai.com'>易百教程</a></p>
 <p>图片演示：</p>
 <p><img src="cid:send_image"></p>
"""
msgText = MIMEText(mail_content, "html", "utf-8")


# 邮件正文
msg = MIMEMultipart("related")
msg["Subject"] = Header(mail_title, "utf-8")
msg["From"] = from_addr
msg["To"] = Header("接收者", "utf-8")  # 收件人的别名

msgAlternative = MIMEMultipart("alternative")
msg.attach(msgAlternative)

msgAlternative.attach(msgText)  # 添加HTML


with open("Python3/Learn/File/timg.jpg", "rb") as f:
    msgImage = MIMEImage(f.read())

# 定义图片ID，在HTML文本中引用
msgImage.add_header("Content-ID", "<send_image>")
msg.attach(msgImage)


smtp = SMTP_SSL(smtp_server)
smtp.set_debuglevel(1)
smtp.ehlo(smtp_server)
smtp.login(from_addr, password)
smtp.sendmail(from_addr, to_addr, msg.as_string())
smtp.quit()
