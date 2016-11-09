#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''

import os,sys
import time
from models.model import DbControl

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

today = time.strftime('%Y-%m-%d')


def formattime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def loaduser():
    # userlist=[]
    # with open(BASE_DIR+'/userlist','r') as f:
    #     while 1:
    #         line = f.readline()
    #         if not line:
    #             break
    #         temp = line.strip().split(',')
    #         if temp[1]<today:
    #             userlist.append(temp[0])
    #             # yield temp[0]
    #         else:
    #             continue
    db = DbControl()
    userlist = db.searchuser()
    return userlist


def savedata(flage,tmTel,err=None):
    if flage == '商品已售完':
        print('\033[1;33;m [{}] {} {} {} \033[0m'.format(formattime(),'1',flage, tmTel))
    elif flage == '余额不足':
        print('\033[1;33;m [{}] {} {} {} \033[0m'.format(formattime(),'2',flage, tmTel))
    elif flage == '非法操作！':
        print('\033[1;31;m [{}] {} {} {} \033[0m'.format(formattime(),'3',flage, tmTel))
    elif flage == '错误':
        print('\033[1;31;m [{}] {} {} {} \033[0m'.format(formattime(),'4',flage, tmTel))
    elif flage == '失败':
        print('\033[1;31;m [{}] {} {} {} {} \033[0m'.format(formattime(),'5',flage, tmTel ,err))
    elif flage == '付款成功':
        print('\033[1;32;m [{}] {} {} {} \033[0m'.format(formattime(),'6',flage, tmTel))
        db = DbControl()
        print(db.edituser(tmTel))
    elif flage == '限额商品超出购买份额!':
        print('\033[1;33;m [{}] {} {} {} \033[0m'.format(formattime(), '7', flage, tmTel))
        db = DbControl()
        print(db.edituser(tmTel))
    else:
        print('\033[1;33;m [{}] {} {} {} \033[0m'.format(formattime(),'8',flage, tmTel))



if __name__ == '__main__':
    users = loaduser()
    # print(users)
    for user in users:
        print(str(user))
        weikegu = Weikegu(str(user),'242628')

        flag,tmTel = weikegu.login()

        if flag == '商品已售完':
            print('商品已售完',tmTel)
        elif flag == '余额不足':
            print('余额不足',tmTel)
