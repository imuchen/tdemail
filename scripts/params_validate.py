#!/usr/bin/python
# -*- coding: UTF-8 -*-

import getopt
import sys


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
        print 'params is ok'
    else:
        print('Error! Required Parameter:-r <receiver> -s <subject> -c <content>')




if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])