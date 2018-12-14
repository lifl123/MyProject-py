#!/usr/bin/env python
import unittest
from mytestcases import tryTestfan
from mytestcases import tryBaiduTestSuitePrc
import HTMLTestRunner

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

mysuite = unittest.TestSuite()
mysuite.addTest(unittest.makeSuite(tryBaiduTestSuitePrc.BaiduUnit))
mysuite.addTest(unittest.makeSuite(tryTestfan.Testfan))

filename = 'E:\\Python\\TestFan-20181202\\report\\baiduResult6.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='百度搜索测试报告',
    description='用例执行情况：')
runner.run(mysuite)


# 只需要改这些即可，开始
smtpserver = 'smtp.163.com'
username = '13723639562@163.com'
password = 'abc123'     # 设置客户端授权码 的 密码
sender = '13723639562@163.com'
# 收件人为多个收件人
receiver = ['13723639562@163.com']
subject = '自动化测试报告'
mailbody = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://ask.testfan.cn"
filename = 'E:\\Python\\TestFan-20181202\\report\\baiduResult6.html'
# 只需要改这些即可，结束


msg = MIMEMultipart('mixed')
msg['Subject'] = subject
msg['From'] = '13723639562@163.com <13723639562@163.com>'
# 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
msg['To'] = ";".join(receiver)


# 构造文字内容
text_plain = MIMEText(mailbody, 'plain', 'utf-8')
msg.attach(text_plain)


# 构造附件
sendfile = open(filename, 'rb').read()
text_att = MIMEText(sendfile, 'base64', 'utf-8')
text_att["Content-Type"] = 'application/octet-stream'
# 附件可以重命名成aaa.txt，最好用原来文件名
# text_att["Content-Disposition"] = 'attachment; filename="smail.py"'
# 另一种实现方式
text_att.add_header('Content-Disposition', 'attachment', filename=filename)
msg.attach(text_att)

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
# smtp.set_debuglevel(1)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
