#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys


def txt2csv(path):
    iconv_cmd = 'iconv -f utf-8 -t gb2312 ' + path + ' > cp_' + path
    os.system(iconv_cmd)
    rm_cmd = 'rm -f ' + path
    os.system(rm_cmd)
    mv_cmd = 'mv ' + 'cp_' + path + ' ' + path
    os.system(mv_cmd)


if __name__ == '__main__':
    txt2csv(sys.argv[1])
