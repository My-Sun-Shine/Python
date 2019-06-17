# 发送带有附件的邮件
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL

# 邮箱SMTP服务器
smtp_server = "smtp.qq.com"
# 发件人邮箱
from_addr = "1399237176@qq.com"
# 授权码
password = "osdasxnimdavhffi"
# 收件人邮箱列表
to_addr = ["1399237176@qq.com", "1224758579@qq.com"]

# 邮件正文
mail_content = "你好，这是使用python发送的邮件测试，带附件"
# 邮件标题
mail_title = "MXW的邮件"

# 邮件正文
msg = MIMEMultipart()
msg["Subject"] = Header(mail_title, "utf-8")
msg["From"] = from_addr
msg["To"] = Header("接收者", "utf-8")  # 收件人的别名
msg.attach(MIMEText(mail_content, "HTML", "utf-8"))  # 邮件内容


att1 = MIMEText(open("Python3/Learn/File/test01.txt",
                     "rb").read(), "base64", "utf-8")
att1["Content-Type"] = "application/octet-stream"
# 这里的filename是用于邮件显示附件
att1["Content-Disposition"] = "attachment;filename='551.txt'"
msg.attach(att1)

att2 = MIMEText(open("Python3/Learn/File/test02.txt",
                     "rb").read(), "base64", "utf-8")
att2["Content-Type"] = "application/octet-stream"
att2["Content-Disposition"] = "attachment;filename='1231.txt'"
msg.attach(att2)

att3 = MIMEText(open("Python3/Learn/File/timg.jpg",
                     "rb").read(), "base64", "utf-8")
att3["Content-Type"] = "application/octet-stream"
att3["Content-Disposition"] = "attachment;filename='timg.jpg'"
msg.attach(att3)

smtp = SMTP_SSL(smtp_server)
smtp.set_debuglevel(1)
smtp.ehlo(smtp_server)
smtp.login(from_addr, password)
smtp.sendmail(from_addr, to_addr, msg.as_string())
smtp.quit()
