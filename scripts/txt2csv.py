#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys


def f_txt2csv(path):
    """将txt文件转为csv，解决非标准csv文件在excel中打开出现乱码的问题

    :param path: txt文件路径
    :return:
    """
    iconv_cmd = 'iconv -f utf-8 -t gb2312 ' + path + ' > conv_' + path
    iconv_cmd_result = os.system(iconv_cmd)
    if iconv_cmd_result == 0:
        rm_cmd = 'rm -f ' + path
        rm_cmd_result = os.system(rm_cmd)
        if rm_cmd_result == 0:
            mv_cmd = 'mv conv_' + path + ' ' + path
            mv_cmd_result = os.system(mv_cmd)
            if mv_cmd_result == 0:
                return 0
    return -1


def file_convert(path):
    print('path:' + path)
    att_files = []
    if os.path.isdir(path):
        for fn in os.listdir(path):
            att_files.append(fn)
    elif os.path.isfile(path):
        att_files.append(path)

    for att in att_files:
        if att.rfind('/') > 0:
            file_name = att[att.rfind('/') + 1:]
        else:
            file_name = att
        # 将非标准csv文件转为标准csv
        if file_name.endswith('.csv'):
            if f_txt2csv(file_name) != 0:
                print '文件' + file_name + '转csv失败！'


if __name__ == '__main__':
    file_convert(sys.argv[1])
