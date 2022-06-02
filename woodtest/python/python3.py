# -*- coding: utf-8 -*- 
# @Time : 2020/11/29 21:23 
# @Author : Aries 
# @Site :  
# @File : python3.py 
# @Software: PyCharm
# liujun

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart

#---------------1.跟发件相关的参数--------
smtpserver = "smtp.163.com"              #发件服务器
port = 0                                 #端口
sender = "liu223344@163.com"                #账号
psw = "LHBLWXWXCZARCNUT"
receiver = ["54279397@qq.com"]             #收件人
#---------------2.编辑邮件的内容---------
file_path = "result.html"
with open(file_path,"rb") as fp:
    mail_body = fp.read()

# subject = "这个是主题163"
#正文
# body = "<p>这个是发送的163邮件</p>"
msg = MIMEMultipart()
msg["from"] = sender
msg["to"] = ";".join(receiver)
msg["subject"] = "这个是主题163"

body = MIMEText(mail_body,"html","utf-8")
msg.attach(body)

#附件
att = MIMEText(mail_body,"html","utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="test_report.html"'
msg.attach(att)


#--------------3.发送邮件--------
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender,psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver.psw)         #兼容qq邮件
    smtp.login(sender,psw)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()