# -*- coding: UTF-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailManage:

    def send_email(self,report_name):
        # 定义SMTP服务器
        smtpserver = 'smtp.163.com'
        # 发送邮件的用户名和客户端密码
        username = 'liu223344@163.com'
        password = 'LHBLWXWXCZARCNUT' # 授权码iver
        # 接受邮件的邮箱
        receiver = '89526793@qq.com,54279397@qq.com'
        # 创建邮件对象 pip install emails
        message = MIMEMultipart('related')
        subject = 'mumu自动化测试报告'
        fujian = MIMEText(open(report_name,'rb').read(),'html','utf-8')
        # 把邮件的信息组装到邮件对象里面
        message['from'] = username
        message['to'] = receiver
        message['subject'] = subject
        message.attach(fujian)
        # 登录smtp服务器并发送右键
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(username, receiver, message.as_string())
        smtp.quit()



