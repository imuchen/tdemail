#!/usr/bin/python
# -*- coding: UTF-8 -*-
import getopt
import locale
import os
import smtplib
import sys
import time
import traceback
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')

"""
兼容python2和python3的邮件发送工具。

参数：
:param receiver: 收件人
:param [acc]: 抄送人
:param subject: 邮件主题
:param content: 邮件内容
:param [attachment]: 邮件附件

示例1：
python tdemail.py -r tiangx@tangdou.com -s 测试邮件主题 -c 测试邮件内容 -t rawlog.sql 

示例2：
如果邮件标题或邮件内容中包含空格或换行符，请以单引号包裹，如：

python tdemail.py -r tiangx@tangdou.com -s '测试 这是一个 测试啊？' -c '测试
b
d
com
内容' -t y.txt
"""


def add_attachment(path, message):
    """添加附件

    :param path:附件文件路径或附件所在目录（会将目录下所有文件当做附件发送）
    :param message:邮件实例
    :return:
    """
    att_files = []
    if os.path.isdir(path):
        for fn in os.listdir(path):
            att_files.append(fn)
    elif os.path.isfile(path):
        att_files.append(path)

    for att in att_files:
        attach = MIMEApplication(open(att, 'rb').read())
        attach["Content-Type"] = 'application/octet-stream'
        if att.rfind('/') > 0:
            file_name = att[att.rfind('/') + 1:]
        else:
            file_name = att
        # Header(file_name, 'UTF-8').encode() 解决附件中中文乱码问题
        attach["Content-Disposition"] = 'attachment; filename=' + Header(file_name, 'UTF-8').encode()
        message.attach(attach)


def send_email(receiver, acc, subject, content, attachment):
    """发送邮件主函数

    :param receiver: 收件人
    :param acc: 抄送人
    :param subject: 邮件主题
    :param content: 邮件内容
    :param attachment: 邮件附件
    :return:
    """
    # 发送邮件服务器
    smtpserver = 'smtp.exmail.qq.com'
    # 发送邮箱用户名和密码
    user = 'xxx@tangdou.com'
    password = 'xxx'
    # 发送邮箱
    sender = 'xxx@tangdou.com'
    # 收件邮箱
    receiver = receiver
    # 抄送
    acc = acc

    # 创建一个MIMEMultipart实例
    message = MIMEMultipart()
    message['From'] = Header(u'糖豆数据团队', 'utf-8')
    message['To'] = receiver
    if acc and '-1' != acc.rstrip():
        message['cc'] = acc
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容，内容后加上了日期时间和邮件简单说明，如不需要可以删掉
    text = content + "\n\n" + time.strftime("%Y-%m-%d %H:%M:%S",
                                            time.localtime(time.time())) + "\n\n注：此邮件为自动生成，如数据有异常请联系数据侧同学，谢谢！"
    message.attach(MIMEText(text, 'plain', 'utf-8'))

    # 添加附件
    if attachment and '-1' != attachment.rstrip():
        add_attachment(attachment, message)

    # 多个收件人以逗号分隔
    all_receivers = []
    if receiver:
        all_receivers = receiver.split(',')
    if acc and '-1' != acc.rstrip():
        all_receivers += acc.split(',')

    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, 25)
        smtp.login(user, password)
        smtp.sendmail(sender, all_receivers, message.as_string())
        smtp.quit()
        print('==========send email successfully==========')
    except smtplib.SMTPHeloError:
        print(traceback.print_exc())
    except smtplib.SMTPRecipientsRefused:
        print(traceback.print_exc())
    except smtplib.SMTPSenderRefused:
        print(traceback.print_exc())
    except smtplib.SMTPDataError:
        print(traceback.print_exc())


# 参数1：收件人（多人以逗号分隔），参数2：邮件主题，参数3：邮件内容，[参数4]：抄送人（多人以逗号分隔）,[参数5]：附件路径
def main(argv):
    """入口，验证参数有效性，并调用邮件发送方法

    基于options, args = getopt.getopt(args, shortopts, longopts=[])，读取输入参数。

    参数args：一般是sys.argv[1:]。过滤掉sys.argv[0]，它是执行脚本的名字，不算做命令行参数。
    参数shortopts：短格式分析串。例如："hr:a:s:c:t:"，h后面没有冒号，表示后面不带参数；r、a、s、c、t后面带有冒号，表示后面带参数。
    参数longopts：长格式分析串列表。例如：["help", "receiver=", "acc=", "subject=", "content=", "attachment="]，help后面没有等
    号，表示后面不带参数；receiver、acc、subject、content，attachment后面有等号，表示后面带参数。

    :param argv:
    :return:
    """
    # 收件人
    receiver = ""
    # 抄送人
    acc = ""
    # 邮件主题
    subject = ""
    # 邮件内容
    content = ""
    # 邮件附件文件名或目录（会将目录中所有文件当做附件发出）
    attachment = ""

    try:
        opts, args = getopt.getopt(argv, "hr:a:s:c:t:",
                                   ["help", "receiver=", "acc=", "subject=", "content=", "attachment="])
    except getopt.GetoptError:
        print('Error: tdemail.py -r <receiver> -a <acc> -s <subject> -c <content> -t <attachment>')
        print(
            '   or: tdemail.py --receiver <receiver> --acc <acc> --subject <subject> --content <content> --attachment <attachment>')
        sys.exit(2)

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('tdemail.py -r <receiver> -a <acc> -s <subject> -c <content> -t <attachment>')
            print(
                'or: tdemail.py --receiver <receiver> --acc <acc> --subject <subject> --content <content> --attachment <attachment>')
            sys.exit()
        elif opt in ("-r", "--receiver"):
            receiver = arg
        elif opt in ("-a", "--acc"):
            acc = arg
        elif opt in ("-s", "--subject"):
            subject = arg
        elif opt in ("-c", "--content"):
            content = arg
        elif opt in ("-t", "--attachment"):
            attachment = arg

    print('receiver:', receiver)
    print('acc:', acc)
    print('subject:', subject)
    print('content:', content)
    print('attachment:', attachment)

    # 必传参数：收件人、邮件主题、邮件内容
    if receiver != "" and subject != "" and content != "":
        send_email(receiver, acc, subject, content, attachment)
    else:
        print('Error! Required Parameter:-r <receiver> -s <subject> -c <content>')


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])
